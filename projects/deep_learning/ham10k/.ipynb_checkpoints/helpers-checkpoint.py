# helpers.py

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


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
        axes[0, 0].set_title('Histogram B&W')
        axes[0, 0].plot(hist)
        # BW Equalised
        axes[0, 1].set_title('B&W Equalised')
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
            axes[0, 1].set_title('RGB Equalised')
            
    # Original vs equalised
    axes[1, 0].set_title('Original')
    axes[1, 0].axis('off')
    axes[1, 0].imshow(img, cmap='gray')
    axes[1, 1].set_title('Equalised')
    axes[1, 1].axis('off')
    axes[1, 1].imshow(img_eq, cmap='gray')