# object-select
This project is now discontinued, and probably broken. See Extra information for more info.
## About
A tool for selecting objects in images from the dataset structure for training NVIDIA detectnet, and writing the locations to the image label, using the KITTI dataset format.
Uses a flask application to send each image to the user when requested, selections are made in the web page, and received by the flask server to write labels.
## Usage
Start the script, passing the path to the root directory of the file structure used by NVIDIA DIGITS for detectnet (Must already contain images to be used, existing labels will be overwritten). Directory is passed as the first non-optional argument.
Host, port and the debug mode for the flask application can each be set using the arguments --host [HOST], --port [PORT] and --debug [True/False] respectively.
## Extra information
* The tool was in theory ready for basic use, but is untested and will not be developed further.
* Objects need to be selected with the two points in the order that coordinates should appear in the image label.
* It is possible that detectnet uses the same co-ordenate system as javascript, in which case the code that converts the co-ordenate system must be replaced to use the javascript co-ordenates.
* There are performance issues with the selection page canvas when selecting more than ~15 objects.
