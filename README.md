# object-select
## About
A tool for selecting objects in images from the dataset structure for training NVIDIA detectnet, and writing the information about their 2d position in the image back to the appropriate place in the filestructure, using the KITTI dataset label format.
Uses a flask application to send each image to the user when requested, javascript to allow the selection of objects, and then the data is sent back into the flask application to be written to disk.
## Usage
Start the script, passing the path to the root directory of the file structure used by NVIDIA DIGITS for detectnet (Must already contain images to be used, existing labels will be overwritten). Directory is passed as the first non-optional argument.
Host, port and the debug mode for the flask application can each be set using the arguments --host [HOST], --port [PORT] and --debug [True/False] respectively.
## Extra information
* This tool is still being developed, and while in theory now ready for use, it appears to have a bug where the display of selection rulers is inconsistantly done on a per-image basis. Once this bug is fixed, the program should be ready for normal use. However, development to improve this may continue if it is worth the time and effort of doing so.
* Objects need to be selected from top-left to bottom-right. If not done this way, the data output to the label in the dataset will be wrong.
* Browser cache may need to be cleared for repeated usage of the tool.
