# helpers.py

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def equalize_rgb_channels(rgb_img):
    '''
        Equalises the histogram of each color channel
        and returns an image with all channels equalised
    '''
    rgb_eq_img = np.zeros(rgb_img.shape, dtype=rgb_img.dtype)
    
    # get channels
    channels = rgb_img[:, :, 0], rgb_img[:, :, 1], rgb_img[:, :, 2]
    
    for idx, channel in enumerate(channels):
        # calc equalised histogram
        channel_eq = cv.equalizeHist(channel)
        # add channel
        rgb_eq_img[:, :, idx] = channel_eq
        
    return rgb_eq_img


def compare_hist(img, bw=True):
    '''Compares original and equalised histogram
        
       if bw is True, then image passed must be B&W
    
    '''

    # Histogram original
    hist = cv.calcHist([img], [0], None, [256], [0, 256])
    img_eq = np.nan

    # Plot comparison
    _, axes = plt.subplots(2, 2, figsize=(15,12))
    
    if bw:
        # Histogram equalized as img
        img_eq = cv.equalizeHist(img)

        # Histogram B&W Equalised
        hist_eq = cv.calcHist([img_eq], [0], None, [256], [0, 256])

        # BW original
        axes[0, 0].set_title('Histograma B&W')
        axes[0, 0].plot(hist)
        # BW Equalised
        axes[0, 1].set_title('B&W Equalizado')
        axes[0, 1].plot(hist_eq)
       
    else:
        # equalise channels
        img_eq = equalize_rgb_channels(img)
        
        # print(img_eq.shape == img.shape)
        
        color = ('b', 'r', 'g')
        
        # RGB Original
        for i, col in enumerate(color):
            hist = cv.calcHist([img], [i], None, [256], [0, 256])
            axes[0, 0].plot(hist, color=col)
            axes[0, 0].set_title('RGB Original')
                    
        # RGB Equalised
        for i, col in enumerate(color):
            hist_eq = cv.calcHist([img_eq], [i], None, [256], [0, 256])
            axes[0, 1].plot(hist_eq, color=col)
            axes[0, 1].set_title('RGB Equalizado')
            
    # Original vs equalised
    axes[1, 0].set_title('Original')
    axes[1, 0].axis('off')
    axes[1, 0].imshow(img, cmap='gray')
    axes[1, 1].set_title('Equalizado')
    axes[1, 1].axis('off')
    axes[1, 1].imshow(img_eq, cmap='gray')

    
def create_metadata_df(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, index_col='image_id')
    df.sort_index(inplace=True)
    
    dx_full_desc = {
        'nv': 'melanocytic nevi',
        'akiec': 'Actinic keratoses and intraepithelial carcinoma',
        'bcc': 'basal cell carcinoma',
        'bkl': 'benign keratosis-like lesions',
        'df': 'dermatofibroma',
        'mel': 'melanoma',
        'vasc': 'vascular lesions'
    }
    df['lesion_type'] = df.dx.map(dx_full_desc)
    return df
    

def translate_dataset(df: pd.DataFrame) -> pd.DataFrame:
    '''
        Translates the dataset into Portuguese for plotting
    '''
    dx_pt = {
        'nv': 'nevo melanocítico',
        'akiec': 'queratose actínica e carcinoma intraepitelial',
        'bcc': 'carcinoma basocelular',
        'bkl': 'lesões benignas do tipo queratose',
        'df': 'dermatofibroma',
        'mel': 'melanoma',
        'vasc': 'lesões vasculares'
    }

    localisation_pt = {
        'trunk': 'tronco',
        'lower extremity': 'extr. inferior',
        'chest': 'peito',
        'back': 'costas',
        'abdomen': 'abdômen',
        'foot': 'pé',
        'unknown': 'desconhecido',
        'face': 'rosto',
        'upper extremity': 'extr. superior',
        'neck': 'pescoço',
        'scalp': 'escalpo',
        'genital': 'genital',
        'hand': 'mão',
        'ear': 'orelha',
        'acral': 'acral'
    }

    sex_pt = {
        'male': 'homem',
        'female': 'mulher',
        'unknown': 'desconhecido'
    }
    
    df['localization'] = df.localization.map(localisation_pt)
    df['lesion_type'] = df.dx.map(dx_pt)
    df['sex'] = df.sex.map(sex_pt)
    
    return df


def create_training_validatation_sets(df, batch_size, nn, data_augmentation=False):
    BATCH_SIZE = batch_size
    IMG_SIZE = set_input_size(nn)
    # split df into train_val and test sets
    train_val = df.sample(frac=0.8, random_state=42)
    test = df.drop(train_val.index) 
    # create image data generator for train_val
    train_data_generator = ImageDataGenerator()

    if data_augmentation == True:
        train_data_generator = ImageDataGenerator(validation_split=0.25,
                                                    preprocessing_function=preprocess_input,                                                    
                                                    rescale=1./255,
                                                    rotation_range=20,
                                                    width_shift_range=0.2,
                                                    height_shift_range=0.2,
                                                    horizontal_flip=True,
                                                    dtype=np.uint8
                                                  )
    else:
        train_data_generator = ImageDataGenerator(validation_split=0.25,
                                                  preprocessing_function=preprocess_input,
                                                  rescale=1./255)


    # create image data generator for testing
    test_data_generator = ImageDataGenerator(rescale=1./255)

    # train data
    train_data = train_data_generator.flow_from_dataframe(train_val, 
                                                    x_col="path", 
                                                    y_col="dx",
                                                    class_mode="categorical",
                                                    target_size=IMG_SIZE,
                                                    batch_size=BATCH_SIZE,
                                                    subset="training",
                                                    color_mode="rgb",
                                                    shuffle=True,
                                                    seed=42)

    # val data
    val_data = train_data_generator.flow_from_dataframe(train_val, 
                                                    x_col="path", 
                                                    y_col="dx",
                                                    class_mode="categorical",
                                                    target_size=IMG_SIZE,
                                                    batch_size=BATCH_SIZE,
                                                    subset="validation",
                                                    color_mode="rgb",
                                                    shuffle=True,
                                                    seed=42)

    # test data
    test_data = test_data_generator.flow_from_dataframe(test, 
                                                    x_col="path", 
                                                    y_col="dx",
                                                    class_mode="categorical",
                                                    target_size=IMG_SIZE,
                                                    batch_size=BATCH_SIZE,                                                    
                                                    color_mode="rgb",
                                                    shuffle=True,
                                                    seed=42)
    
    return train_data, val_data, test_data
