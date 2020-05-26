Warnings:
    The files must be properly named in order. If they are not named in order, then the program will not sort them correctly. If you are using a digital camera, they have probably already been properly named like "DSC_XXXX" or "IMG_XXXXXXXXX" which is a valid format.
    The files must all be the same dimensions. If the dimensions do not match, the program will throw an error.

Usage:
    python3 merge.py [args]
    "-r"/"--reverse": Reverses the sorted image list. When this is not supplied, then the images will be sorted from least to greatest (DSC_1234 to DSC_9876), however when it is supplied, it will be sorted from greatest to least (DSC_9876 to DSC_1234).
    "-v"/"--vertical":Adds the slices together vertically instead of horizontally.

TODO:
    Fix issues when running the program on over 150 images (opencv sometimes throws a random error when this happens).