from genericpath import isfile
from PIL import Image, ImageEnhance
from os import mkdir, getcwd
import os.path as op


def printmenu():
    arr = ["Resize", "Rotate", "Filters", "Image Type",
           "Paste Images", "Flip", "Crop", "Exit"]
    for i in range(len(arr)):
        print(f"{i+1}.  {arr[i]}")


print("Welcome to Image Processing Project...")
print("""Our task was to use the Python Imaging Library (PIL) 
to tackle common image processing tasks. We have some algorithms
that help us apply filters to images, and use PIL to adjust image 
brightness, contrast, and color tone. We also performed basic
functionalities along with this.""")

global img, ask
img = Image.open('birdy.jpg')


def WannaSave(p, path):
    print("Do you want to save this image??\nY / N")
    ask1 = input(">>>> ")
    if ask1.casefold() == "Y".casefold():
        string = input("Enter the name of the file: ")
        if op.isfile(string) == False:
            new = p.save(path+"\\"+string+'.jpg')
            print("File Saved!")
        else:
            print("Filename already exists. Please try a new filename.")
            WannaSave(p, path)
    elif ask1.casefold() == "N".casefold():
        pass
    else:
        print("Please enter a valid input!")
        WannaSave(p, path)


def resizeme(p):
    try:
        path = getcwd()
        d = "Resized Images"
        if op.isdir(path+"\\"+d) == False:
            mkdir(f"{path}\\{d}")
        width = int(input(">>Enter width : "))
        height = int(input(">>Enter height : "))
        new_image = p.resize((width, height))
        new_image.show()
    except Exception as e:
        print("Enter valid input !! ")
        print(e)
        # resizeme(p)
    finally:
        WannaSave(new_image, f"{path}\\{d}")


def rotateme(p):
    try:
        path = getcwd()
        d = "Rotated Images"
        if op.isdir(path+"\\"+d) == False:
            mkdir(f"{path}\\{d}")
        deg = int(input(">>Enter degree to rotate : "))
        new_image = p.rotate(deg)
        new_image.show()
    except:
        print("Enter valid input !! ")
        rotateme(p)
    finally:
        WannaSave(new_image, f"{path}\\{d}")


def filters(p):
    fil = ["Color Transform", "Enhancement", "Brightness", "Sharpness"]
    for i in range(len(fil)):
        print(f"{i+1}.  {fil[i]}")
    try:
        path = getcwd()
        d = "Filtered Images"
        if op.isdir(path+"\\"+d) == False:
            mkdir(f"{path}\\{d}")
        filter = int(input(">>Enter filter : "))
        if filter == 1:
            mode = input(">>Enter mode for transormation (RGB/L/CMYK): ")
            new_image = p.convert(mode)
            new_image.save('img.jpg')
            new_image.show()
            WannaSave(new_image, f"{path}\\{d}")
        elif filter == 2:
            fact = float(input(">>Enter contrast factor : "))
            contrast = ImageEnhance.Contrast(p)
            contrast.enhance(fact).show()
            WannaSave(contrast, path)
        elif filter == 3:
            fact = float(input(">>Enter brightness factor : "))
            brightness = ImageEnhance.Brightness(p)
            brightness.enhance(fact).show()
            WannaSave(brightness, path)
        elif filter == 4:
            fact = float(input(">>Enter sharpness factor : "))
            sharpness = ImageEnhance.Sharpness(p)
            sharpness.enhance(fact).show()
            WannaSave(sharpness, path)
    except:
        print("Enter valid input !! ")
        filters(p)


def changemytype(p):
    img_name = input(">>Enter new name of image : ")
    img_type = input(">>Enter extention of image : ")
    p.save(img_name+"."+img_type)


def copypaste(p):
    try:
        path = getcwd()
        d = "Altered Images"
        if op.isdir(path+"\\"+d) == False:
            mkdir(f"{path}\\{d}")
        img2_name = input(">>Enter new name of image : ")
        img2 = Image.open(img2_name)
        p_cpy = p.copy()
        dist_left = int(input(">>Enter distance from left : "))
        dist_up = int(input(">>Enter distance from upside : "))
        p_cpy.paste(img2, (dist_left, dist_up))
        p_cpy.show()
    except:
        print("Enter valid input !! ")
        copypaste(p)
    finally:
        WannaSave(p_cpy, path)


def flipme(p):
    try:
        path = getcwd()
        d = "Flipped Images"
        if op.isdir(path+"\\"+d) == False:
            mkdir(f"{path}\\{d}")
        flip = ["Anti-Clockwise Flip", "Clockwise Flip",
                "Horizontal Flip", "Vertical Flip"]
        for i in range(len(flip)):
            print(f"{i+1}.  {flip[i]}")
        opt = int(input(">>Enter flipping option : "))
        if opt == 1:
            new_image = p.transpose(Image.TRANSPOSE)
            new_image.show()
        elif opt == 2:
            new_image = p.transpose(Image.TRANSVERSE)
            new_image.show()
        elif opt == 3:
            new_image = p.transpose(Image.FLIP_LEFT_RIGHT)
            new_image.save('img.jpg')
            new_image.show()
        elif opt == 4:
            new_image = p.transpose(Image.FLIP_TOP_BOTTOM)
            new_image.show()
    except:
        print("Enter valid input !! ")
        flipme(p)
    finally:
        WannaSave(new_image, path)


def cropme(p):
    try:
        path = getcwd()
        d = "Cropped Images"
        if op.isdir(path+"\\"+d) == False:
            mkdir(f"{path}\\{d}")
        width, height = p.size
        print(" !! Enter values in range of :\nWidth: 0",
              width, "\nHeight: 0 ", height, " !!")
        p1 = int(input(">>Enter distance from left : "))
        p2 = int(input(">>Enter distance from up : "))
        p3 = int(input(">>Enter distance from right : "))
        p4 = int(input(">>Enter distance from bottom : "))
        if p1 < width and p3 < width and p1 < height and p4 < height:
            box = (p1, p2, p3, p4)
            new_img = p.crop(box)
            new_img.show()
        else:
            print("Out Of range !!")
            cropme(p)
    except:
        print("Enter valid input !! ")
        cropme(p)
    finally:
        WannaSave(new_img, path)


while True:
    printmenu()
    print("What do you want?")
    try:
        ask = int(input(">>>> "))
        if ask == 1:
            resizeme(img)
        elif ask == 2:
            rotateme(img)
        elif ask == 3:
            filters(img)
        elif ask == 4:
            changemytype(img)
        elif ask == 5:
            copypaste(img)
        elif ask == 6:
            flipme(img)
        elif ask == 7:
            cropme(img)
        elif ask == 8:
            print("Thank You !!")
            break
    except:
        print("Please enter an integer!")
