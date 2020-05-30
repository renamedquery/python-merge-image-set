# python-merge-image-set

## Python 3.6 script to stitch together images horizontally or vertically.

### Usage:

`python3 merge.py [args]`

Arguments:

`-r`/`--reverse`: Reverses the list of images that are being added together, so the output will be backwards.

`-v`/`--vertical`: Adds the images from top to bottom instead of left to right (can go from bottom to top if the `-r`/`--reverse` argument is supplied).

### Output examples:

*Horizontal (`python3 merge.py`)*

![](https://i.imgur.com/hNWAoNu.jpg?raw=true =250x)

*Horizontal and reversed (`python3 merge.py -r`)*

![](https://i.imgur.com/mHmozOT.jpg?raw=true  =250x)

*Vertical (`python3 merge.py -v`)*

![](https://i.imgur.com/txEn4oX.jpg?raw=true  =250x)

*Vertical and reversed (`python3 merge.py -r -v`)*

![](https://i.imgur.com/kwpLrmJ.jpg?raw=true  =250x)