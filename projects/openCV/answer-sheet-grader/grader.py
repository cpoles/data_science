# import the necessary packages
from imutils.perspective import four_point_transform
from imutils import contours
from modules import helpers as hp
import numpy as np
import cv2
import os

# define the answer key which maps the question number
# to the correct answer
ANSWER_KEY = {0: 0, 1: 3, 2: 2, 3: 1, 4: 3}


if __name__ == '__main__':
    curr_dir = os.getcwd()
    img_path = hp.validate_args(curr_dir)
    img_name = os.path.basename(img_path)
    img_name = os.path.splitext(img_name)[0]

    if not img_path:
        print("Image not captured.")
        raise SystemExit(0)
    else:
        # load image
        image = cv2.imread(img_path)
        # make a copy
        orig = image.copy()
        # convert to grayscale
        gray = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)

        # -- EDGE DETECTION -- #
        print('STEP 1: Edge Detection')
        edged, ratio = hp.detect_edges(image)
        # -- FIND CONTOURS -- #
        print("STEP 2: Find document contours")
        sheet_contours = hp.find_contours(edged)
        # -- APPLY PERSPECTIVE TRANSFORM -- #
        print('STEP 3: Apply perspective transform')
        document = four_point_transform(orig, sheet_contours.reshape(4, 2) * ratio)
        warped = hp.apply_perspective_transform(orig, sheet_contours, ratio)
        # display document and its grayscale version
        # cv2.imshow('Paper Transformed', document)
        # cv2.imshow('Gray Transformed', warped)
        # cv2.waitKey(0)
        # -- EXTRACT ANSWER CONTOURS -- #
        print('STEP 4: Extract answer contours')
        question_contours, thresh = hp.extract_answer_contours(document, warped)
        questions = document.copy()
        # cv2.drawContours(questions, question_contours, -1, (0, 0, 255), 2)
        # cv2.imshow('Questions', questions)
        # cv2.waitKey(0)
        # -- GRADING -- #
        print('STEP 5: Grading')
        # -- GRADING -- #
        # sort the question_contours top-to-bottom,
        # then initialize the total number of correct answers
        question_contours = contours.sort_contours(question_contours, method='top-to-bottom')[0]
        correct_answers = 0

        # each question has 5 possible answers
        # each question is represented as a slice of size 5 in question_contours
        N_QUESTIONS = 5

        # each question has 5 possible answers, to loop over the
        # question in batches of 5
        for q, i in enumerate(np.arange(0, len(question_contours), N_QUESTIONS)):
            # sort the contours for the current question from
            # left to right, then initialize the index of the
            # bubbled answer
            cnts = contours.sort_contours(question_contours[i:i + N_QUESTIONS])[0]
            bubbled = None
            # loop over the sorted contours
            for idx, contour in enumerate(cnts):
                # construct a mask that reveals only the current
                # "bubble" for the question
                mask = np.zeros(thresh.shape, dtype="uint8")
                cv2.drawContours(mask, [contour], -1, 255, -1)
                # apply the mask to the thresholded image, then
                # count the number of non-zero pixels in the
                # bubble area
                mask = cv2.bitwise_and(thresh, thresh, mask=mask)
                total = cv2.countNonZero(mask)
                # if the current total has a larger number of total
                # non-zero pixels, then we are examining the currently
                # bubbled-in answer
                if bubbled is None or total > bubbled[0]:
                    bubbled = (total, idx)

            # initialize the contour color and the index of the
            # *correct* answer
            color = (0, 0, 255)
            k = ANSWER_KEY[q]
            # check to see if the bubbled answer is correct
            if k == bubbled[1]:
                color = (0, 255, 0)
                correct_answers += 1
            # draw the outline of the correct answer on the test
            cv2.drawContours(document, [cnts[k]], -1, color, 3)


        # grab the test taker
        score = (correct_answers / 5.0) * 100
        print(f"[INFO] Total: {score:.2f}")
        cv2.putText(document, f"Correct: {score}%", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        cv2.putText(document, f"Incorrect: {100 - score}%", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        hp.write_to_disk(document, img_name + '_graded.png', 'graded')
        cv2.imshow("Original", image)
        cv2.imshow("Exam", document)
        cv2.waitKey(0)



