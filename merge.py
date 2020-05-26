#import statements
import cv2, os, numpy, math, sys, shutil

#constants
IMAGE_DIR = './images/'
IMAGE_DIR_TMP = './tmp/'
REVERSE = True if '-r' in sys.argv else False or True if '--reverse' in sys.argv else False
VERTICAL = True if '-v' in sys.argv else False or True if '--vertical' in sys.argv else False
IMAGE_LIST_IN_IMAGES_DIR = sorted(os.listdir(IMAGE_DIR), reverse = REVERSE)

#tell the user what the modes are
print('Running in reverse direction mode' if REVERSE else 'Running in normal direction mode')
print('Running in vertical mode' if VERTICAL else 'Running in horizontal mode')

#create the final image (assume that the first image is the same size as the other images)
firstImage = cv2.imread(IMAGE_DIR + '/' + IMAGE_LIST_IN_IMAGES_DIR[0])
finalImage = numpy.zeros((firstImage.shape[0], firstImage.shape[1], 3), numpy.uint8)

#create the directory for the temporary images
os.mkdir(IMAGE_DIR_TMP)

#calculate the width of the image slices
imageSliceWidth = math.ceil(finalImage.shape[1] / len(IMAGE_LIST_IN_IMAGES_DIR)) if not VERTICAL else math.ceil(finalImage.shape[0] / len(IMAGE_LIST_IN_IMAGES_DIR))

#start cropping the images and placing them in the temporary directory
index = 0
for image in IMAGE_LIST_IN_IMAGES_DIR:
    print('Cropping {} to {}px ({}/{})'.format(image, imageSliceWidth, index + 1, len(IMAGE_LIST_IN_IMAGES_DIR)))
    currentImage = cv2.imread(IMAGE_DIR + '/' + image)
    cropPosition = imageSliceWidth * index
    if (not VERTICAL):
        currentImage = currentImage[0:finalImage.shape[0], cropPosition:cropPosition + imageSliceWidth]
    else:
        currentImage = currentImage[cropPosition:cropPosition + imageSliceWidth, 0:finalImage.shape[1]]
    cv2.imwrite(IMAGE_DIR_TMP + '/' + image.split('.')[0] + '.bmp', currentImage)
    index += 1

#iterate through the cropped images and stitch them together
index = 0
for image in IMAGE_LIST_IN_IMAGES_DIR:
    print('Pasting {} ({}/{})'.format(image, index + 1, len(IMAGE_LIST_IN_IMAGES_DIR)))
    currentImage = cv2.imread(IMAGE_DIR_TMP + '/' + image.split('.')[0] + '.bmp')
    currentPosition = imageSliceWidth * index
    if (not VERTICAL):
        finalImage[
            0:currentImage.shape[0],
            currentPosition:currentPosition + currentImage.shape[1]
        ] = currentImage
    else:
        finalImage[
            currentPosition:currentPosition + currentImage.shape[0],
            0:currentImage.shape[1]
        ] = currentImage
    index += 1

#delete the temporary directory
shutil.rmtree(IMAGE_DIR_TMP)

#write the output image
cv2.imwrite('output.png', finalImage)