# DOCUMENT SCANNER

# USAGE: python3 doc_scan2.py -i <path_to_image>
# USAGE: python3 doc_scan2.py -w True

from modules.helpers import *

if __name__ == '__main__':
    curr_dir = os.getcwd()
    img_path = validate_args(curr_dir)
    print(img_path)

    if not img_path:
        print("Image not captured.")
        raise SystemExit(0)
    else:
        # load image
        image = cv2.imread(img_path)
    
        # -- EDGE DETECTION -- #
        print('STEP 1: Edge Detection')
        edged, ratio = detect_edges(image)
        # -- FIND CONTOURS -- #
        print("STEP 2: Find document contours")
        sheet_contours = find_contours(edged)
        # -- APPLY PERSPECTIVE TRANSFORM -- #
        print('STEP 3: Apply perspective transform')
        warped = apply_perspective_transform(image, sheet_contours, ratio)

        # write scanned image to disk
        write_to_disk(warped, 'scanned.png', 'scanned_images')

        # show original and scanned images
        cv2.imshow('Original', imutils.resize(image, height=650))
        cv2.imshow('Scanned', imutils.resize(warped, height=650))

        cv2.waitKey(0)
        print('Exiting program...')
    
    