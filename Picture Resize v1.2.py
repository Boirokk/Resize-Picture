# Duplicate picture and resize image saving it with a 'small' prefix to a separate folder named 'small'
# Written by Chad C. 2016-05-08 v1.0
from PIL import Image
import os, subprocess
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.pdfbase import pdfdoc

root_dir = os.getcwd()

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
11: Brad Melink
12: Chad C.
13: Jeff Scott


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
if name == str(13):
    project_manager = "P:\Yacht Department\Picture Transfer file\\xJeff"


    

new_folder = project_manager + os.sep + folder

def resize(project_manager):
    '''Create the destination folders for the original and resized small pictures'''
    try:
        os.mkdir(new_folder)
        os.mkdir(new_folder + os.sep + 'small')
        # Scan through the root folder and look for pictures larger than 800 wide to resize
        for roots, dirs, files in os.walk(root_dir):

            for file in files:
                file_name = roots + os.sep + file
                
                if file.endswith('.png') or file.endswith('.PNG') or file.endswith('.jpg') or file.endswith('.JPG')\
                   or file.endswith('.jpeg') or file.endswith('.JPEG') or file.endswith('.gif') or file.endswith('.GIF'):
                    
                    # Open the image and save picture object
                    pic = Image.open(file_name)
                    # Get image size
                    width, height = pic.size
                    # Save ratio to make 800 pixels into a variable
                    ratio = 800 / width
                    # If picture larger than 800 wide. resize to 800 with appropriate height ratio
                    if width > 800:
                        pic.save(new_folder + os.sep + file + ".jpg")
                        print('Resizing', file, 'to', int(width * ratio), 'X', int(height * ratio))
                        smallpic = pic.resize((int(width * ratio), int(height * ratio)))
                        # Save resized photo to this location
                        smallpic.save(new_folder + os.sep + "small" + os.sep + "small_" + file + ".jpg")
                        os.remove(file_name)
                    # I picture smaller than 800 wide. Move and delete the photos to destination folder.
                    else:
                        print('Moving', file_name)
                        pic.save(new_folder + os.sep + file + ".jpg")
                        os.remove(file_name)
                        # Remove empty folder
                        try:
                            os.rmdir(new_folder + os.sep + 'small')
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
    pdf_image = []
    count = 0
    pdfname = new_folder + '\\' + folder  +  '.pdf'
    pdfdoc.PDFCatalog.OpenAction = '<</S/JavaScript/JS(this.print\({bUI:true,bSilent:false,bShrinkToFit:true}\);)>>'
    c = canvas.Canvas(pdfname, pagesize=landscape(letter))
    for file_name in os.listdir(new_folder):
        if file_name.endswith('.png') or file_name.endswith('.PNG') or file_name.endswith('.jpg')\
                or file_name.endswith('.JPG') or file_name.endswith('.jpeg')\
                or file_name.endswith('.JPEG') or file_name.endswith('.gif')or file_name.endswith('.GIF'):
            count += 1
            pdf_image.append(new_folder + os.sep + file_name)

    if count <= 4:
        # Left images
        try:
            c.drawImage(pdf_image[0], 45, 60, width=340, height=215)
        except:
            pass
        try:
            c.drawImage(pdf_image[1], 45, 335, width=340, height=215)
        except:
            pass
        # Right images
        try:
            c.drawImage(pdf_image[2], 410, 60, width=340, height=215)
        except:
            pass
        try:
            c.drawImage(pdf_image[3], 410, 335, width=340, height=215)
        except:
            pass
   
        
    

        c.showPage()

        c.save()
    else:
        for i in range(count // 9):
            try:

                # Left images
                c.drawImage(pdf_image[0], 45, 50, width=235, height=160)
                c.drawImage(pdf_image[1], 45, 225, width=235, height=160)
                c.drawImage(pdf_image[2], 45, 400, width=235, height=160)

                # Middle images
                c.drawImage(pdf_image[3], 282, 50, width=235, height=160)
                c.drawImage(pdf_image[4], 282, 225, width=235, height=160)
                c.drawImage(pdf_image[5], 282, 400, width=235, height=160)

                # Right images
                c.drawImage(pdf_image[6], 519, 50, width=235, height=160)
                c.drawImage(pdf_image[7], 519, 225, width=235, height=160)
                c.drawImage(pdf_image[8], 519, 400, width=235, height=160)

                # Remove elements
                try:
                    del pdf_image[0]
                    del pdf_image[1]
                    del pdf_image[2]
                    del pdf_image[3]
                    del pdf_image[4]
                    del pdf_image[5]
                    del pdf_image[6]
                    del pdf_image[7]
                    del pdf_image[8]
                except:
                    continue
            except:
                break

            c.showPage()
        try:
            c.showPage()
            # Print any left over pictures not divisible by 9
            # Left images
            c.drawImage(pdf_image[0], 45, 50, width=235, height=160)
        except:
            pass
        try:
            c.drawImage(pdf_image[1], 282, 50, width=235, height=160)
        except:
            pass
        try:
            c.drawImage(pdf_image[2], 519, 50, width=235, height=160)
        except:
            pass
        try:
            c.drawImage(pdf_image[3], 45, 225, width=235, height=160)
        except:
            pass
        try:
            c.drawImage(pdf_image[4], 282, 225, width=235, height=160)
        except:
            pass
        try:
            c.drawImage(pdf_image[5], 519, 225, width=235, height=160)
        except:
            pass
        try:
            c.drawImage(pdf_image[6], 45, 400, width=235, height=160)
        except:
            pass
        try:
            c.drawImage(pdf_image[7], 282, 400, width=235, height=160)
        except:
            pass
        try:
            c.drawImage(pdf_image[8], 519, 400, width=235, height=160)
        except:
            pass




        c.save()

    os.startfile(pdfname)
    input('Done... Press enter to exit')

# Call main
main()

