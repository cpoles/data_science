# helpers.py

from typing import DefaultDict
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import preprocess_input as resnetpp
from tensorflow.keras.applications.xception import preprocess_input as xceptionpp
from tensorflow.keras.applications.mobilenet import preprocess_input as mobilenetpp
from tensorflow.keras.preprocessing import image

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

def create_minimal_images_dataset(path_to_images, path_to_metadata):
    df_meta = pd.read_csv(path_to_metadata,
                          index_col='image_id',
                          usecols=['image_id', 'dx']).sort_index()
    
    # dictionary {image_id: path_to_image}
   
    path_dic = {filename.stem: filename.as_posix() \
                        for filename in Path(path_to_images).glob('**/*.jpg')}

    #pixels_dic = {filename.stem: cv.cvtColor(cv.imread(filename), cv.COLOR_BGR2RGB)\
    #                    for filename in Path(path_to_images).glob('**/*.jpg')}

    df_meta['path'] = df_meta.index.map(path_dic)
    

    return df_meta



def set_input_size(nn):
    if nn == 'alexnet':
        return 227, 227
    elif nn == 'resnet':
        return 224, 224
    elif nn == 'xception':
        return 299, 299
    elif nn == 'mobilenet':
        return 224, 224
    raise ValueError('Invalid Neural Network.')


def preprocessing_img(img):
    img = cv.GaussianBlur(img, (7, 7), 0)
    print(img.dtype)
    return (img)



def create_training_validatation_sets(df, batch_size, training_size, nn, data_augmentation=False):
    BATCH_SIZE = batch_size
    IMG_SIZE = set_input_size(nn)

    # split df into train_val and test sets
    train = df.sample(frac=training_size, random_state=42)
    val_test = df.drop(train.index) 
    val = val_test.sample(frac=0.5, random_state=42)
    test = val_test.drop(val.index)

    print(train.dx.value_counts())
    print(val.dx.value_counts())
    print(test.dx.value_counts())

    if nn == 'resnet':
        img_gen = ImageDataGenerator(preprocessing_function=resnetpp)
    elif nn == 'xception':
        img_gen = ImageDataGenerator(preprocessing_function=xceptionpp)
    elif nn == 'mobilenet':
        img_gen = ImageDataGenerator(preprocessing_function=mobilenetpp)
    else:
        img_gen = ImageDataGenerator(rescale=1./255)


                                              
# train data
    train_data = img_gen.flow_from_dataframe(train, 
                                            x_col="path", 
                                            y_col="dx",
                                            class_mode="categorical",
                                            target_size=IMG_SIZE,
                                            batch_size=BATCH_SIZE,
                                            color_mode="rgb",
                                            shuffle=True,
                                            seed=42)

    # val data
    val_data = img_gen.flow_from_dataframe(val, 
                                            x_col="path", 
                                            y_col="dx",
                                            class_mode="categorical",
                                            target_size=IMG_SIZE,
                                            batch_size=BATCH_SIZE,                                            
                                            color_mode="rgb",
                                            shuffle=True,
                                            seed=42)

    # test data - do not shuffle test data
    test_data = img_gen.flow_from_dataframe(test, 
                                            x_col="path", 
                                            y_col="dx",
                                            class_mode="categorical",
                                            target_size=IMG_SIZE,
                                            batch_size=BATCH_SIZE,                                                    
                                            color_mode="rgb",
                                            shuffle=False,
                                            seed=42)
    
    return train_data, val_data, test_data


def balance_dataset(df_meta):
    # sample equal amount of pictures for each lesion based on the least occurred
    least_occured = df_meta.dx.value_counts().df
    print(least_occured)

    nv_indices = df_meta[df_meta.dx == 'nv'].sample(n=least_occured, random_state=42).index

    mel_indices = df_meta[df_meta.dx == 'mel'].sample(n=least_occured, random_state=42).index

    bkl_indices = df_meta[df_meta.dx == 'bkl'].sample(n=least_occured, random_state=42).index

    bcc_indices = df_meta[df_meta.dx == 'bcc'].sample(n=least_occured, random_state=42).index

    vasc_indices = df_meta[df_meta.dx == 'vasc'].sample(n=least_occured, random_state=42).index

    akiec_indices = df_meta[df_meta.dx == 'akiec'].sample(n=least_occured, random_state=42).index

    df_indices = df_meta[df_meta.dx == 'df'].index

    all_indices = nv_indices.to_list() + mel_indices.to_list() + bkl_indices.to_list() + bcc_indices.to_list() + vasc_indices.to_list() + akiec_indices.to_list() + df_indices.to_list()

    #df_bal = df_meta.drop(index = nv_indices).drop(index=mel_indices).drop(index=bkl_indices).drop(index=bcc_indices).drop(index=vasc_indices).drop(index=akiec_indices)
    df_bal = df_meta.loc[all_indices]

    return df_bal

def plot_samples(img_gen):
    first_batch_images, first_batch_labels = next(img_gen)

    plt.figure(figsize=(16, 16))

    classes = np.array(list(img_gen.class_indices.keys()))

    print(classes)

    for i in range(32):
        ax = plt.subplot(8, 4, i + 1)
        plt.imshow(first_batch_images[i])
        lbl_mask = [not not x for x in first_batch_labels[i]] 
        plt.title(classes[lbl_mask])
        plt.axis("off")


def plot_learning_curves(history, auc=True):
    epochs = np.arange(0, len(history.history['loss']) + 1)

    acc = [0.] + history.history['accuracy']
    val_acc = [0.] + history.history['val_accuracy']

    loss = [0.] + history.history['loss']
    val_loss = [0.] + history.history['val_loss']

    plt.figure(figsize=(12, 12))
    plt.subplot(1, 3, 1)
    plt.legend(loc='lower right')
    plt.ylabel('Accuracy')
    plt.ylim([min(plt.ylim()),1])
    plt.xlabel('epoch')
    plt.title('Training and Validation Accuracy')
    plt.plot(epochs, acc, label='Training Accuracy')
    plt.plot(epochs, val_acc, label='Validation Accuracy')

    # shift the training loss 0.5 epochs to the left 
    plt.subplot(1, 3, 2)
    plt.legend(loc='upper right')
    plt.ylabel('Cross Entropy')
    plt.ylim([0, 1])
    plt.title('Training and Validation Loss')
    plt.xlabel('epoch')
    plt.plot(epochs - 0.5, loss, label='Training Loss')
    plt.plot(epochs, val_loss, label='Validation Loss')

    if auc:
        auc = [0.] + history.history['auc']
        val_auc = [0.] + history.history['val_auc']
        # shift the training loss 0.5 epochs to the left 
        plt.subplot(1, 3, 3)
        plt.plot(epochs, auc, label='Training AUC')
        plt.plot(epochs, val_auc, label='Validation AUC')
        plt.legend(loc='upper right')
        plt.ylabel('Area Under Curve')
        plt.ylim([0, 1])
        plt.xlim([1, 30])
        plt.title('Training and Validation AUC')
        plt.xlabel('epoch')
        plt.show()

    plt.show()


def make_confusion_matrix(cf,
                          group_names=None,
                          categories='auto',
                          count=True,
                          percent=True,
                          cbar=True,
                          xyticks=True,
                          xyplotlabels=True,
                          sum_stats=True,
                          figsize=None,
                          cmap='Blues',
                          title=None):
    '''
    This function will make a pretty plot of an sklearn Confusion Matrix cm using a Seaborn heatmap visualization.
    Arguments
    ---------
    cf:            confusion matrix to be passed in
    group_names:   List of strings that represent the labels row by row to be shown in each square.
    categories:    List of strings containing the categories to be displayed on the x,y axis. Default is 'auto'
    count:         If True, show the raw number in the confusion matrix. Default is True.
    normalize:     If True, show the proportions for each category. Default is True.
    cbar:          If True, show the color bar. The cbar values are based off the values in the confusion matrix.
                   Default is True.
    xyticks:       If True, show x and y ticks. Default is True.
    xyplotlabels:  If True, show 'True Label' and 'Predicted Label' on the figure. Default is True.
    sum_stats:     If True, display summary statistics below the figure. Default is True.
    figsize:       Tuple representing the figure size. Default will be the matplotlib rcParams value.
    cmap:          Colormap of the values displayed from matplotlib.pyplot.cm. Default is 'Blues'
                   See http://matplotlib.org/examples/color/colormaps_reference.html
                   
    title:         Title for the heatmap. Default is None.
    '''


    # CODE TO GENERATE TEXT INSIDE EACH SQUARE
    blanks = ['' for i in range(cf.size)]

    if group_names and len(group_names)==cf.size:
        group_labels = ["{}\n".format(value) for value in group_names]
    else:
        group_labels = blanks

    if count:
        group_counts = ["{0:0.0f}\n".format(value) for value in cf.flatten()]
    else:
        group_counts = blanks

    if percent:
        group_percentages = ["{0:.2%}".format(value) for value in cf.flatten()/np.sum(cf)]
    else:
        group_percentages = blanks

    box_labels = [f"{v1}{v2}{v3}".strip() for v1, v2, v3 in zip(group_labels,group_counts,group_percentages)]
    box_labels = np.asarray(box_labels).reshape(cf.shape[0],cf.shape[1])


    # CODE TO GENERATE SUMMARY STATISTICS & TEXT FOR SUMMARY STATS
    if sum_stats:
        #Accuracy is sum of diagonal divided by total observations
        accuracy  = np.trace(cf) / float(np.sum(cf))

        #if it is a binary confusion matrix, show some more stats
        if len(cf)==2:
            #Metrics for Binary Confusion Matrices
            precision = cf[1,1] / sum(cf[:,1])
            recall    = cf[1,1] / sum(cf[1,:])
            f1_score  = 2*precision*recall / (precision + recall)
            stats_text = "\n\nAccuracy={:0.3f}\nPrecision={:0.3f}\nRecall={:0.3f}\nF1 Score={:0.3f}".format(
                accuracy,precision,recall,f1_score)
        else:
            #Metrics for Multiclassification Confusion Matrices
            precision = np.diagonal(cf) / np.sum(cf, axis=0)
            recall = np.diagonal(cf) / np.sum(cf, axis=1)
            f1_score = (2*precision*recall) / (precision + recall)
            # Generate strings with metrics
            pr_str, rc_str, f1_str = [], [], []
            for idx, (pr, rc, f1) in enumerate(zip(precision, recall, f1_score)):                
                pr_str.append(f'Precision: {precision[idx]:.4f}      ')
                rc_str.append(f'Recall:    {recall[idx]:.4f}         ')
                f1_str.append(f'F1 Score:  {f1_score[idx]:.4f}       ')
            stats_text = ''.join(pr_str) + '\n' + ''.join(rc_str) + '\n' + ''.join(f1_str)
    else:
        stats_text = ""


    # SET FIGURE PARAMETERS ACCORDING TO OTHER ARGUMENTS
    if figsize==None:
        #Get default figure size if not set
        figsize = plt.rcParams.get('figure.figsize')

    if xyticks==False:
        #Do not show categories if xyticks is False
        categories=False


    # MAKE THE HEATMAP VISUALIZATION
    plt.figure(figsize=figsize)
    sns.heatmap(cf,annot=box_labels,fmt="",cmap=cmap,cbar=cbar,xticklabels=categories,yticklabels=categories)

    if xyplotlabels:
        plt.ylabel('True label')
        if len(cf)>2:
            plt.xlabel('Predicted label' + '\n\n' + stats_text)
        else:
            plt.xlabel('Predicted label' + stats_text)
    else:
        plt.xlabel(stats_text)
    
    if title:
        plt.title(title)









