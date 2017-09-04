#!/usr/bin/python3
import sys
import argparse
from shutil import copy2
from os import listdir
from os.path import isdir, isfile, join
from flask import Flask, render_template, redirect, request, url_for

#class and global variable definitions for the script
class Image:
    def __init__(self, name, path, labelpath):
        self.name = name
        self.path = path
        self.labelpath = labelpath

    def __repr__(self):
        return __str__()

    def __str__(self):
        return "<Image name:{0} path:{1} labelpath:{2}>".format(self.name, self.path, self.labelpath)

next_image = 0
total_images = 0
images = []

def parse_args(): #Parse the command arguments, returning them to be used by the program
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="127.0.0.1")
    parser.add_argument("--port", type=int, default=5000)
    parser.add_argument("--debug", type=bool, default=False)
    parser.add_argument("dir", type=str)
    return parser.parse_args()

#functions for dealing with the file structure, handling and output.
def check_file_structure(structure_path, overall_root): #Checks that the file stucture of the specified path matches that of the corresponding part of the detectnet dataset format. overall_root defines if the supplied path is the overall root of the filestructure (True), or if it is one of the subdirectories (False).
    subdirectories = [f for f in listdir(structure_path) if isdir(join(structure_path, f))]
    if(overall_root):
        if ("train" in subdirectories and "val" in subdirectories):
            #return an evaluated boolean (AND) from the results of checking both subdirectories.
            return (check_file_structure(join(structure_path, "train"), False) and check_file_structure(join(structure_path, "val"), False))
    else:
        if ("images" in subdirectories and "labels" in subdirectories):
            return True
    return False

def load_images(dataset_root):# load a list of the images to work on by scanning the appropriate directories, creating a new image object for each file with the file name, path to the file and the path to the corrisponding label file.
    global total_images
    for image_category in ["train", "val"] :
        category_dir = join(dataset_root, image_category)
        image_dir = join(category_dir, "images")
        labels_dir = join(category_dir, "labels")
        for image in listdir(image_dir):
            image_path = join(image_dir, image)
            if isfile(image_path):
                images.append(Image(image, image_path, join(labels_dir, image.split(".")[0] + ".txt")))
                total_images += 1

def get_next_image():
    global next_image
    global total_images
    if (next_image != total_images):
        image = images[next_image]
        copy2(image.path, "static/")
        next_image += 1
        return url_for("static", filename=image.name)
    else:
        return "ERROR: Last Image Already processed."

def write_object_selections(selections_string):
    output_file = open(images[next_image - 1].labelpath, "w")
    for selection in selections_string.split("|"):
        if (selection != ""):
            selection_data = selection.split(",")
            print(selection_data)
            selection_line = "{} 0.0 0 0.0 {} {} {} {} 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n"
            output_file.write(selection_line.format(selection_data[0], selection_data[1], selection_data[4], selection_data[3], selection_data[2]))
    output_file.close()

#flask application functions and setup
app = Flask(__name__)

@app.route("/")
def root():
    image_url = get_next_image()
    if (image_url == "ERROR: Last Image Already processed."):
        return render_template("done.html", stylesheet=url_for("static", filename="style.css"))
    else:
        return render_template("selector.html", image=image_url, scripts=[url_for("static", filename="selector.js")], stylesheet=url_for("static", filename="style.css"))

@app.route("/submit_image/", methods=["GET", "POST"])
def process_submission():
    if (request.method == "POST"):
        write_object_selections(request.form["selectionData"])
    return redirect(url_for("root"))

if(__name__ == "__main__"): #If this is the python file being directly run, perform these actions.
    args = parse_args()
    if (check_file_structure(args.dir, True)):
        print("The target directory matches the required filestructure, loading images and starting web application.")
        load_images(args.dir)
        print("Loaded " + str(total_images) + " images.")
        app.run(host=args.host, port=args.port, debug=args.debug)
    else:
        print("Filestructure check failed on target directory. Please make sure that the target directory matches the required filestructure.")
