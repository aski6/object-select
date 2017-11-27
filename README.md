# object-select
This project is discontinued. See Extra information for more info.
## About
A tool for selecting objects in images from the dataset structure for training NVIDIA detectnet, and writing the information about their 2d position in the image back to the appropriate place in the filestructure, using the KITTI dataset label format.
Uses a flask application to send each image to the user when requested, javascript to allow the selection of objects, and then the data is sent back into the flask application to be written to disk.
## Usage
Start the script, passing the path to the root directory of the file structure used by NVIDIA DIGITS for detectnet (Must already contain images to be used, existing labels will be overwritten). Directory is passed as the first non-optional argument.
Host, port and the debug mode for the flask application can each be set using the arguments --host [HOST], --port [PORT] and --debug [True/False] respectively.
## Extra information
* The tool is in theory ready for basic use, but is untested and will probably not be developed further. Pull requests with improvements/fixes are welcome.
* Objects need to be selected with the two pounts in the order that you want the co-ordenates to appear.
* It is possible that detectnet uses the same co-ordenate system as javascript, in which case the code that converts the co-ordenate system can be replaced to use the javascript co-ordenates.
* There appear to be performance issues with the selection page javascript when selecting a large number of objects.
