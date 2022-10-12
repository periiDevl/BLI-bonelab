#importing the os library
from operator import mod
import os
#importing zipfile library
from zipfile import ZipFile 
import subprocess
#importing shutil library
import shutil
#importing sys library
import sys

#getting the windows PC username
USER_NAME = os.getenv('USER', os.getenv('USERNAME', 'user'))


# The path to the drop mods folder
path = "drop_mods"

# store mods in a list
mods_list = []
def findFiles():
   
    # add all zip files to the mods_list variable
    for (root, dirs, file) in os.walk(path):
        for f in file:
            #detect if the file is a .zip file
            if '.zip' in f:
                #add the .zip to the mods list
                mods_list.append(f)
            #adding dummy so windows compress can join the empty directory
            if '.dummy' in f:
                    #removing the dummy
                    os.remove(path + "/" + f)


def extractall():
    
    #extracting all the zip files in the mod folder
    for mod in mods_list:

        
            
        #move the .zip files to the stress level zero bonelab mods folder
        shutil.move(path + "/" + mod, "C:/Users/" + USER_NAME + "/AppData/LocalLow/Stress Level Zero/BONELAB/Mods/")
        #extracting the file in the mods location
        with ZipFile("C:/Users/" + USER_NAME + "/AppData/LocalLow/Stress Level Zero/BONELAB/Mods/" + mod, 'r') as zip: 
            zip.extractall("C:/Users/" + USER_NAME + "/AppData/LocalLow/Stress Level Zero/BONELAB/Mods/") 
        #delete all left zip files for a cleaner mods folder
        for (root, dirs, file)  in os.walk("C:/Users/" + USER_NAME + "/AppData/LocalLow/Stress Level Zero/BONELAB/Mods/"):
            for f in file:
                if '.zip' in f:
                    #remove all the zip files from bonelab folder
                    os.remove("C:/Users/" + USER_NAME + "/AppData/LocalLow/Stress Level Zero/BONELAB/Mods/" + "/" + f)
                    #save all the zip files from bonelab folder
                    #shutil.move(directory + "/" + f, path + "/" + mod)
                
    update()

        

def openmodsfolder():
    #opening the drop mods folder location
    subprocess.Popen(r'explorer /select, "drop_mods"')

def update():
    #reopening the folder so it will be able to refresh
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 