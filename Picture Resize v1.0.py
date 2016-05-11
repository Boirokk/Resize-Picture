# Duplicate picture and resize image saving it with a 'small' prefix to a separate folder named 'small'
# Written by Chad C. 2016-05-08 v1.0
from PIL import Image
import os
import subprocess



print('Who are these pictures for?')
print('Enter the number of the corresponding person.')
print('''
1:  Mike Pratt
2:  Tom Moen
3:  Chuck Dimarco
4:  Peter Wormwood
5:  Mike Rogers
6:  Alan Brosilow
7:  Dave Nelson
8:  Todd Sharp
9:  Mike Baker
10: James Donghia
11: Brad
12: Chad C.

''')
name = input()

folder = input('Please name your destination folder.')

if name == str(1):
    project_manager = "P:\Yacht Department\Picture Transfer file\Mike P"
if name == str(2):
    project_manager = "P:\Yacht Department\Picture Transfer file\Tom M"
if name == str(3):
    project_manager = "P:\Yacht Department\Picture Transfer file\Chuck"
if name == str(4):
    project_manager = "P:\Yacht Department\Picture Transfer file\Peter"
if name == str(5):
    project_manager = "P:\Yacht Department\Picture Transfer file\Mike R"
if name == str(6):
    project_manager = "P:\Yacht Department\Picture Transfer file\Alan"
if name == str(7):
    project_manager = "P:\Yacht Department\Picture Transfer file\\xDave N"
if name == str(8):
    project_manager = "P:\Yacht Department\Picture Transfer file\Todd"
if name == str(9):
    project_manager = "P:\Yacht Department\Picture Transfer file\\xMike B"
if name == str(10):
    project_manager = "P:\Yacht Department\Picture Transfer file\\xJimmy"
if name == str(11):
    project_manager = "P:\Yacht Department\Picture Transfer file\Brad"
if name == str(12):
    project_manager = "P:\Yacht Department\Picture Transfer file\\xChad C"

    

new_folder = project_manager + '\\' + folder

def resize(project_manager):
    '''Create the destination folders for the original and resized small pictures'''
    try:
        os.mkdir(new_folder)
        os.mkdir(new_folder + '\\' + 'small')
        # Scan through the root folder and look for pictures larger than 800 wide to resize
        for roots, dirs, files in os.walk(r"C:\Users\cczilli\Desktop\Pics to resize"):
            

            for file in files:
                file_name = roots + '\\' + file
                
                if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.JPG')\
                   or file.endswith('.jpeg') or file.endswith('.gif'):
                    
                    # Open the image and save picture object
                    pic = Image.open(file_name)
                    # Get image size
                    width, height = pic.size
                    # Save ratio to make 800 pixels into a variable
                    ratio = 800 / width
                    # If picture larger than 800 wide. resize to 800 with appropriate height ratio
                    if width > 800:
                        pic.save(new_folder + "\\" + file + ".jpg")
                        print('Resizing', file_name, 'to', int(width * ratio), 'X', int(height * ratio))
                        smallpic = pic.resize((int(width * ratio), int(height * ratio)))
                        # Save resized photo to this location
                        smallpic.save(new_folder + "\\" + "small" + "\\" + "small_" + file + ".jpg")
                        os.remove(file_name)
                    # I picture smaller than 800 wide. Move and delete the photos to destination folder.
                    else:
                        print('Moving', file_name)
                        pic.save(new_folder + "\\" + file + ".jpg")
                        os.remove(file_name)
                        # Remove empty folder
                        try:
                            os.rmdir(new_folder + '\\' + 'small')
                        # If exception from folder with files continue
                        except:
                             continue

                   
    except PermissionError as err:
        print(err)
    except FileExistsError as err:
        print(err)
    except FileNotFoundError as err:
        print(err)

    
# main
def main():
    resize(project_manager)
    file_open = ['explorer', new_folder]
    subprocess.Popen(file_open)
    input('Done... Press enter to exit')

# Call main
main()

