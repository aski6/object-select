#!/usr/bin/python3
import sys
import argparse
from shutil import copy2
from os import listdir
from os.path import isdir, join
from flask import Flask, render_template, redirect, request, url_for

def parse_args(): #Parse the command arguments, returning them to be used by the program
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="127.0.0.1")
    parser.add_argument("--port", type=int, default=5000)
    parser.add_argument("--debug", type=bool, default=False)
    parser.add_argument("dir", type=str)
    return parser.parse_args()

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

def load_images(dataset_root):
    
    print("TODO load images")

next_image = 0
total_images
images = []

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("selector.html", image=get_next_image() scripts=[url_for("static", filename="selector.js")])

@app.route("/submit_image/")
def process_submission():
    #TODO add code to process the submitted images
    return redirect(url_for(root))

if(__name__ == "__main__"): #If this is the python file being directly run, perform these actions.
    args = parse_args()
    if(check_file_structure(args.dir, True)):
        print("The target directory matches the required filestructure,")
        app.run(host=args.host, port=args.port, debug=args.debug)

class Image:
    def __init__(self, name, path, labelpath):
        self.name = name
        self.path = path
        self.labelpath = labelpath
