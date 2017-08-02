#object-select
##About
A quickly made tool for selecting objects in an image, and writing the information about their 2d position in the image using the KITTI dataset label format.
Uses a flask application to send each image to the user when requested, javascript to allow the selection of objects, and then the data is sent back into the flask application to be written to disk.
##Usage
Start the script, passing the path to the root directory of the file structure used by NVIDIA DIGITS for detectnet (Must already contain images to be used, existing labels will be overwritten). Directory is passed as the first non-optional argument.
Host, port and the debug mode for the flask application can each be set using the arguments --host [HOST], --port [PORT] and --debug [True/False] respectively.
