# helpers.py
import argparse
import os
import cv2
import imutils
import numpy as np
from skimage.filters import threshold_local
from imutils.perspective import four_point_transform
from imutils import contours  # for sorting contours


def validate_args(curr_dir):
    """Validates arguments and return path to image"""
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--image', required=False, help='Path to the image to be scanned')
    ap.add_argument('-w', '--webcam', required=False, help='Capture image via webcam')
    args = vars(ap.parse_args())

    webcam = args['webcam']
    img_path = args['image']

    if img_path is None and webcam is None:
        print('USAGE for image: python3 grader.py -i <path_to_image>')
        print('USAGE for webcam: python3 grader.py -w True')
        raise SystemExit(0)

    # validate webcam arg
    if webcam is not None:
        assert webcam in ['True', 'False'], 'Only True or False are accepted values for Webcam'
        webcam = False if webcam == 'False' else True
    else:
        webcam = False

    # if no webcam selected, must pass a path to an image
    if not webcam:
        # check if image was passed
        img_path = args['image']
        if img_path is None:
            print("You must enter a path to an image if the webcam is off")
            raise SystemExit(0)
        else:
            img_path = os.path.join(curr_dir, img_path)
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
                # write img to disk
                img_name = f'my_shot_{shot_count}.png'
                img_path = write_to_disk(frame, img_name, 'images')

        cam.release()
        del cam
        cv2.destroyAllWindows()

    return img_path


def write_to_disk(image, image_name, directory):
    cwd = os.getcwd()
    save_dir = os.path.join(cwd, directory)

    if not os.path.exists(save_dir):
        try:
            os.mkdir(save_dir)
            print(f'{save_dir} directory created.')
        except IOError:
            print('Error creating directory.')

    img_name = os.path.join(save_dir, image_name)
    try:
        cv2.imwrite(img_name, image)
    except IOError:
        print('Error writing to disk.')

    print(f'{image_name} successfully saved.')
    return img_name


def detect_edges(image):
    # get image dimensions
    OLD_HEIGHT, OLD_WIDTH, _ = image.shape
    NEW_HEIGHT = 500
    # get the ratio of the original image height and the new height
    ratio = OLD_HEIGHT / NEW_HEIGHT

    # resize image for processing purposes
    image = imutils.resize(image, height=NEW_HEIGHT)

    # convert img to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # blurr gray img
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    # apply Canny edge detector
    edged = cv2.Canny(gray, 75, 200)

    return edged, ratio


def find_contours(edged):
    # find the contours
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # grab contours
    cnts = imutils.grab_contours(cnts)
    # keep the top five largest based on contour area
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

    sheet_contour = np.array([])
    # loop over the contours
    for contour in cnts:
        # approximate the contour
        peri = cv2.arcLength(contour, True)  # calculates the perimeter - If True, suppose the contour to be closed
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)  # epsilon 1 - 5% of perimeter

        # if our approximated contour has four points,
        # then we can assume we found the rectangle of the document sheet
        if len(approx) == 4:
            sheet_contour = approx
            break

    if sheet_contour.size > 0:
        return sheet_contour
    else:
        print("ERROR: A Fully Closed Contour was not detected.")
        print("Exiting...")
        raise SystemExit(0)


def apply_perspective_transform(orig, sheet_contours, ratio):
    warped = four_point_transform(orig, sheet_contours.reshape(4, 2) * ratio)

    # convert warped image to grayscale, then threshold it
    # to give it a B&W paper effect
    warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    T = threshold_local(warped, 11, offset=10, method='gaussian')
    warped = (warped > T).astype('uint8') * 255

    return warped


def extract_answer_contours(document, warped):
    # apply Otsu threshold
    ret, thresh = cv2.threshold(warped, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    # find contours in the thresholded image, then initialise
    # the list of contours that correspond to the questions
    cts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cts = imutils.grab_contours(cts)
    question_contours = []

    # loop over the contours
    for contour in cts:
        # compute the bounding box of the contour, then use the bounding box
        # to derive the aspect ratio
        x, y, w, h = cv2.boundingRect(contour)
        ar = w / float(h)
        # in order to label the contour as a question
        # region should be sufficiently wide, sufficiently tall, and have an aspect ratio
        # approximately equal to 1
        if w >= 25 and h >= 25 and 0.9 <= ar <= 1.1:
            question_contours.append(contour)

    question_contours = np.array(question_contours)
    return question_contours, thresh


