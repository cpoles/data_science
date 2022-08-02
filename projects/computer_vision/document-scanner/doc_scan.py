# DOCUMENT SCANNER

# USAGE: python3 doc_scan.py -i <path_to_image>
# USAGE: python3 doc_scan.py -w True

import cv2
import os
import argparse
import imutils
import numpy as np
from modules.transform import four_point_transform
from skimage.filters import threshold_local

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=False, help='Path to the image to be scanned')
ap.add_argument('-w', '--webcam', required=False, help='Capture image via webcam')
args = vars(ap.parse_args())

# ---- ARGUMENT VALIDATION ---- #
webcam = args['webcam']
image = args['image']

if image is None and webcam is None:
    print('USAGE for image: python3 doc_scan.py -i <path_to_image>')
    print('USAGE for webcam: python3 doc_scan.py -w True')
    raise SystemExit(0)

# validate webcam arg
if webcam is not None:
    assert webcam in ['True', 'False'], 'Only True or False are accepted values for Webcam'
    webcam = False if webcam == 'False' else True
else:
    webcam = False

img_path = ''
# if no webcam selected, must pass a path to an image
if not webcam:
    # check if image was passed
    img_path = args['image']
    if img_path is None:
        print("You must enter a path to an image if the webcam is off")
        raise SystemExit(0)
    else:
        img_path = args['image']
        image = cv2.imread(img_path)
        if image is None:
            print("File Not Found")
            raise SystemExit(0)

# if webcam was selected
if webcam:
    # create webcam object
    cam = cv2.VideoCapture(0)
    cv2.namedWindow('Webcam')

    shot_count = 0

    while True:
        ret, frame = cam.read()
        if ret:
            cv2.imshow('Webcam', frame)
        else:
            print("Failed to capture frame.")
            break

        key = cv2.waitKey(1)
        if key % 256 == 27:  # ESC key
            print("Exiting...")
            break
        elif key % 256 == 32:  # SPACEBAR
            # --- GET DIRECTORY FOR SAVING --- #
            shot_count += 1
            cwd = os.getcwd()
            save_dir = os.path.join(cwd, 'images')
            img_path = os.path.join(save_dir, f'my_shot_{shot_count}.png')

            print(img_path)
            # write img to disk
            cv2.imwrite(img_path, frame)
            print(f"Image Saved to {img_path} \n successfully.")

    cam.release()
    del cam
    cv2.destroyAllWindows()


# ----- EDGE DETECTION ------ #
image = cv2.imread(img_path)

# get image dimensions
OLD_HEIGHT, OLD_WIDTH, _ = image.shape
NEW_HEIGHT = 500
# get the ratio of the original image height and the new height
ratio = OLD_HEIGHT / NEW_HEIGHT
# make a copy of the original image
orig = image.copy()
# resize image for processing purposes
image = imutils.resize(image, height=NEW_HEIGHT)

# convert img to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blurr gray img
gray = cv2.GaussianBlur(gray, (3, 3), 0)
cv2.imshow('Gray', gray)
# apply Canny edge detector
edged = cv2.Canny(gray, 75, 200)

# show the original and the edge detected images
print('STEP 1: Edge Detection')
cv2.imshow('Image', image)
cv2.imshow('Edged', edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---- FINDING  CONTOURS ---- #
# find the contours
contours = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# grab contours
contours = imutils.grab_contours(contours)
# keep the top five largest based on contour area
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

sheet_contour = np.array([])
# loop over the contours
for contour in contours:
    # approximate the contour
    peri = cv2.arcLength(contour, True)  # calculates the perimeter - If True, suppose the contour to be closed
    approx = cv2.approxPolyDP(contour, 0.02 * peri, True)  # epsilon 1 - 5% of perimeter

    # if our approximated contour has four points,
    # then we can assume we found the rectangle of the document sheet
    if len(approx) == 4:
        sheet_contour = approx
        break

if sheet_contour.size > 0:
    # show the contour (outline) of the document
    print("STEP 2: Find document contours")
    cv2.drawContours(image, [sheet_contour], -1, (0, 255, 0), 2)
    cv2.imshow('Outline', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("A Fully Closed Contour was not detected.")
    print("Exiting...")
    raise SystemExit(0)
# ---- Apply Perspective Transform & Threshold ---- #
# apply four point transform to obtain a top-down view of the original image
# an error here means that no closed contours were found
print('STEP 3: Apply perspective transform')
warped = four_point_transform(orig, sheet_contour.reshape(4, 2) * ratio)

# convert warped image to grayscale, then threshold it
# to give it a B&W paper effect
warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
T = threshold_local(warped, 11, offset=10, method='gaussian')
warped = (warped > T).astype('uint8') * 255

# show original and scanned images
cv2.imshow('Original', imutils.resize(orig, height=650))
cv2.imshow('Scanned', imutils.resize(warped, height=650))
cv2.waitKey(0)