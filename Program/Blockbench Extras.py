'''-------------------------------------------
               BLOCKBENCH EXTRAS
----------------------------------------------
.Json model generator for Minecraft Java

Created by ultimatech
First update: 13/03/2022 17:49
Last update: 15/03/2022 19:30
Version: Beta 0.1.3

                    2022
-------------------------------------------'''


# ------------ Import libraries --------------


import json
from random import *
from math import *
from os import makedirs, path, system
from datetime import date, datetime
from xml.dom.minidom import Element

# Installs eel for HTML GUI
try:
    from eel import *
except ImportError:
    system('python -m pip install eel')
    from eel import *


# ----------- Initialize variables -----------

element_dict = {}
element_current_dict = []

output_folder = "Generated/"

credits = "Made using ultimatech's procedural model generator"


# ------------- Main generator ---------------

# Individual element generator
def generate_element(current_color):

    global element_current_dict, currentXpos, currentYpos, currentZpos, OriginX, OriginY, OriginZ, XCubeSize, YCubeSize, ZCubeSize

    element_current_dict.append({
        "from": [currentXpos+OriginX+0.5, currentYpos+OriginY+0.5, currentZpos+OriginZ+0.5],
        "to": [currentXpos+OriginX+0.5 + XCubeSize, currentYpos+OriginY+0.5 + YCubeSize, currentZpos+OriginZ+0.5 + ZCubeSize],
        "rotation": {"angle": 0, "axis": "y", "Origin": [currentXpos+(XCubeSize)/2, currentYpos+(YCubeSize)/2, currentZpos+(ZCubeSize)/2]},
        "color": current_color,
        "faces": {
            "north": {"uv": [0, 0, XCubeSize, YCubeSize], "texture": "#missing"},
            "east": {"uv": [0, 0, ZCubeSize, YCubeSize], "texture": "#missing"},
            "south": {"uv": [0, 0, XCubeSize, YCubeSize], "texture": "#missing"},
            "west": {"uv": [0, 0, ZCubeSize, YCubeSize], "texture": "#missing"},
            "up": {"uv": [0, 0, XCubeSize, ZCubeSize], "texture": "#missing"},
            "down": {"uv": [0, 0, XCubeSize, ZCubeSize], "texture": "#missing"}
        }
    })


# Color mode selector; Available color modes: (integers from 1 to 9, "Random", "Semi-Hashed", "Hashed")
def color_selector(ColorMode):

    global currentXpos, currentYpos, currentZpos

    ColorDict = [0, 1, 2, 3, 4, 5, 6, 7, 8,
                 9, "Random", "Semi-Hashed", "Hashed"]
    ColorMatch = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, randint(0, 9), ((
        currentXpos+currentYpos) % 2), ((currentXpos+currentYpos) % 2 + (currentYpos-currentZpos) % 2)]
    ColorMode = ColorMatch[ColorDict.index(ColorMode)]

    return ColorMode


# Sphere generator; Available fill modes: ("Fill", "Surface", "Substract", "Hashed", "Surface-Hashed")
def generate_sphere(SphereRadius, FillMode, ColorMode):

    global element_current_dict, currentXpos, currentYpos, currentZpos, OriginX, OriginY, OriginZ, XCubeSize, YCubeSize, ZCubeSize

    XCubeSize, YCubeSize, ZCubeSize = 1, 1, 1
    XSize, YSize, ZSize = SphereRadius*2, SphereRadius*2, SphereRadius*2
    OriginX, OriginY, OriginZ = 7.5-XSize/2, 7.5-YSize/2, 7.5-ZSize/2
    CenterPos = [SphereRadius, SphereRadius, SphereRadius]

    for currentXpos in range(XSize):
        for currentYpos in range(YSize):
            for currentZpos in range(ZSize):

                if FillMode == "Fill" and int(sqrt((currentXpos+(XCubeSize/2) - CenterPos[0])**2 + ((currentYpos+(YCubeSize/2) - CenterPos[1])**2)*0.8 + (currentZpos+(ZCubeSize/2) - CenterPos[2])**2)) <= SphereRadius:

                    generate_element(color_selector(ColorMode))

                elif FillMode == "Surface" and int(sqrt((currentXpos+(XCubeSize/2) - CenterPos[0])**2 + (currentYpos+(YCubeSize/2) - CenterPos[1])**2 + (currentZpos+(ZCubeSize/2) - CenterPos[2])**2)) == SphereRadius-1:

                    generate_element(color_selector(ColorMode))

                elif FillMode == "Substract" and int(sqrt((currentXpos+(XCubeSize/2) - CenterPos[0])**2 + ((currentYpos+(YCubeSize/2) - CenterPos[1])**2)*0.8 + (currentZpos+(ZCubeSize/2) - CenterPos[2])**2)) >= SphereRadius:

                    generate_element(color_selector(ColorMode))

                elif FillMode == "Hashed" and int(sqrt((currentXpos+(XCubeSize/2) - CenterPos[0])**2 + (currentYpos+(YCubeSize/2) - CenterPos[1])**2 + (currentZpos+(ZCubeSize/2) - CenterPos[2])**2)) <= SphereRadius and (currentXpos+currentYpos-currentZpos) % 2 == 0:

                    generate_element(color_selector(ColorMode))

                elif FillMode == "SurfaceHashed" and int(sqrt((currentXpos+(XCubeSize/2) - CenterPos[0])**2 + (currentYpos+(YCubeSize/2) - CenterPos[1])**2 + (currentZpos+(ZCubeSize/2) - CenterPos[2])**2)) == SphereRadius-1 and (currentXpos+currentYpos-currentZpos) % 2 == 0:

                    generate_element(color_selector(ColorMode))

    temp_element_dict = element_current_dict

    return temp_element_dict


# Cube generator
def generate_cube(XSize, YSize, ZSize, ColorMode):

    global element_current_dict, currentXpos, currentYpos, currentZpos, OriginX, OriginY, OriginZ, XCubeSize, YCubeSize, ZCubeSize

    XCubeSize, YCubeSize, ZCubeSize = 1, 1, 1
    OriginX, OriginY, OriginZ = 7.5-XSize/2, 7.5-YSize/2, 7.5-ZSize/2

    for currentXpos in range(XSize):
        for currentYpos in range(YSize):
            for currentZpos in range(ZSize):

                if (currentXpos+currentYpos-currentZpos) % 2 == 0:

                    element_current_dict.append({
                        "from": [currentXpos+OriginX, currentYpos+OriginY, currentZpos+OriginZ],
                        "to": [currentXpos+OriginX + XCubeSize, currentYpos+OriginY + YCubeSize, currentZpos+OriginZ + ZCubeSize],
                        "rotation": {"angle": 0, "axis": "y", "Origin": [currentXpos+(XCubeSize)/2, currentYpos+(YCubeSize)/2, currentZpos+(ZCubeSize)/2]},
                        "color": color_selector(ColorMode),
                        "faces": {
                            "north": {"uv": [0, 0, XCubeSize, YCubeSize], "texture": "#missing"},
                            "east": {"uv": [0, 0, ZCubeSize, YCubeSize], "texture": "#missing"},
                            "south": {"uv": [0, 0, XCubeSize, YCubeSize], "texture": "#missing"},
                            "west": {"uv": [0, 0, ZCubeSize, YCubeSize], "texture": "#missing"},
                            "up": {"uv": [0, 0, XCubeSize, ZCubeSize], "texture": "#missing"},
                            "down": {"uv": [0, 0, XCubeSize, ZCubeSize], "texture": "#missing"}
                        }
                    })

    temp_element_dict = element_current_dict

    return temp_element_dict


# -------------- Output file ------------------

def generate_file():

    generated_json = {
        "credit": credits,
        "elements": element_dict
    }

    # Creates a folder for generated models if it doesn't already exists
    if not path.exists(output_folder):
        makedirs(output_folder, exist_ok=False)

    # Sets the file name to the current date and time
    output_name = date.today().strftime("%y%m%d") + "-" + \
        datetime.now().strftime("%H%M%S")

    # Generates the .json file(s) in the "Generated" folder
    with open(output_folder + output_name + ".json", 'w') as json_file:
        json.dump(generated_json, json_file, indent=4, sort_keys=False)

    # Creates a copy always named "latest" for easier access
    with open(output_folder + "latest.json", 'w') as json_file:
        json.dump(generated_json, json_file, indent=4, sort_keys=False)

    # Generates - Debug and testing only
    '''with open('TEMP\generated.json', 'w') as json_file:
        json.dump(generated_json, json_file, indent=4, sort_keys=False)'''

    print("\n Generation complete! \n")


# ------------- Required model ----------------

element_dict = generate_cube(20, 45, 20, "Hashed")
#element_dict = generate_sphere(10, "Surface", 9)

generate_file()


# ----------------- Temp ---------------------

'''









'''
