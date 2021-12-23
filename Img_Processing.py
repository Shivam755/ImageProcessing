from PIL import Image, ImageEnhance, ImageFilter
from os import mkdir, getcwd
import os.path as op
import numpy as np
from PIL.Image import fromarray

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

global img, ask, path
img = Image.open('birdy.jpg')
path = getcwd()


def WannaSave(p, path1):
    print("Do you want to save this image??\nY / N")
    ask1 = input(">>>> ")
    if ask1.casefold() == "Y".casefold():
        string = input("Enter the name of the file: ")
        if op.isfile(string) == False:
            new = p.save(path1+"\\"+string+'.jpg')
            print("File Saved!")
        else:
            print("Filename already exists. Please try a new filename.")
            WannaSave(p, path1)
    elif ask1.casefold() == "N".casefold():
        pass
    else:
        print("Please enter a valid input!")
        WannaSave(p, path1)


def resizeme(p):
    try:
        d = "Resized Images"
        if op.isdir(path+"\\"+d) == False:
            mkdir(f"{path}\\{d}")
        width = int(input(">>Enter width : "))
        height = int(input(">>Enter height : "))
        new_image = p.resize((width, height))
        new_image.show()
    except Exception as e:
        print(e)
        print("Enter valid input !! ")
        resizeme(p)
    finally:
        WannaSave(new_image, f"{path}\\{d}")


def rotateme(p):
    try:
        d = "Rotated Images"
        if op.isdir(path+"\\"+d) == False:
            mkdir(f"{path}\\{d}")
        deg = int(input(">>Enter degree to rotate : "))
        new_image = p.rotate(deg)
        new_image.show()
    except Exception as e:
        print(e)
        print("Enter valid input !! ")
        rotateme(p)
    finally:
        WannaSave(new_image, f"{path}\\{d}")


def filters(p):
    fil = ["Greyscale", "Enhancement", "Brightness", "Sharpness", "Sepia", "Negative", "Blur"]
    for i in range(len(fil)):
        print(f"{i+1}.  {fil[i]}")
    try:
        d = "Filtered Images"
        if op.isdir(path+"\\"+d) == False:
            mkdir(f"{path}\\{d}")
            for i in range(len(fil)):
                if op.isdir(path+"\\"+d+"\\"+fil[i]) == False:
                    mkdir(f"{path}\\{d}\\{fil[i]}")
        filter = int(input(">>Enter filter : "))
        if filter == 1:
            new_image = p.convert("L")
            new_image.show()
            WannaSave(new_image, f"{path}\\{d}\\{fil[0]}")
        elif filter == 2:
            fact = float(input(">>Enter contrast factor: "))
            contrast = ImageEnhance.Contrast(p)
            c = contrast.enhance(fact)
            c.show()
            WannaSave(c, f"{path}\\{d}\\{fil[1]}")
        elif filter == 3:
            fact = float(input(">>Enter brightness factor: "))
            brightness = ImageEnhance.Brightness(p)
            b = brightness.enhance(fact)
            b.show()
            WannaSave(b, f"{path}\\{d}\\{fil[2]}")
        elif filter == 4:
            fact = float(input(">>Enter sharpness factor: "))
            sharpness = ImageEnhance.Sharpness(p)
            s = sharpness.enhance(fact)
            s.show()
            WannaSave(s, f"{path}\\{d}\\{fil[3]}")
        elif filter == 5:
            sepiaP = sepiaImage(p)
            sepiaP.show()
            WannaSave(sepiaP, f"{path}\\{d}\\{fil[4]}")
        elif filter == 6:
            negativeP = negativeImage(p)
            negativeP.show()
            WannaSave(negativeP,f"{path}\\{d}\\{fil[5]}")
        elif filter == 7:
            print("This is Box Blur. The more the radius(a parameter) the higher the output image will be blurred. ")
            radius = float(input(">>Enter the radius for blur: "))
            blur = p.filter(ImageFilter.BoxBlur(radius))
            blur.show()
            WannaSave(blur,f"{path}\\{d}\\{fil[6]}")
    except Exception as e:
        print(e)
        print("Enter valid input !! ")
        filters(p)


def changemytype(p):
    print("It will save image automatically, are you sure about that?")
    ask2 = input("Y / N\n>> ")
    if ask2.casefold() == "Y".casefold():
        d = "Type Changed Images"
        if op.isdir(path+"\\"+d) == False:
            mkdir(f"{path}\\{d}")
        img_name = input(">>Enter new name of image : ")
        img_type = input(">>Enter extention of image : ")
        p.save(f"{path}\\{d}\\{img_name}.{img_type}")
    elif ask2.casefold() == "N".casefold():
        print("Okay!")
    else:
        print("Enter valid input!!")


def copypaste(p):
    try:
        d = "Altered Images"
        if op.isdir(path+"\\"+d) == False:
            mkdir(f"{path}\\{d}")
        img2_name = input(">>Enter new name of image : ")
        img2 = Image.open(img2_name)
        p_cpy = p.copy()
        dist_left = int(input(">>Enter distance from the left edge: "))
        dist_up = int(input(">>Enter distance from the top edge: "))
        p_cpy.paste(img2, (dist_left, dist_up))
        p_cpy.show()
    except Exception as e:
        print(e)
        print("Enter valid input !! ")
        copypaste(p)
    finally:
        WannaSave(p_cpy, f"{path}\\{d}")


def flipme(p):
    try:
        d = "Flipped Images"
        flip = ["Anti-Clockwise Flip", "Clockwise Flip",
                "Horizontal Flip", "Vertical Flip"]
        if op.isdir(path+"\\"+d) == False:
            mkdir(f"{path}\\{d}")
            for i in range(len(flip)):
                if op.isdir(path+"\\"+d+"\\"+flip[i]) == False:
                    mkdir(f"{path}\\{d}\\{flip[i]}")
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
            new_image.show()
        elif opt == 4:
            new_image = p.transpose(Image.FLIP_TOP_BOTTOM)
            new_image.show()
    except Exception as e:
        print(e)
        print("Enter valid input !! ")
        flipme(p)
    finally:
        WannaSave(new_image, f"{path}\\{d}")


def cropme(p):
    try:
        d = "Cropped Images"
        if op.isdir(path+"\\"+d) == False:
            mkdir(f"{path}\\{d}")
        width, height = p.size
        print(f"Width and Height of this photo is {width} and {height} respectively.\nPlease enter values with regards to this...")
        p1 = int(input(">>Enter the distance of top of crop-box from the top edge: "))
        p2 = int(input(">>Enter the distance of left of crop-box from the left edge: "))
        p3 = int(input(">>Enter the distance of right of crop-box from the right edge: "))
        p4 = int(input(">>Enter the distance of bottom of crop-box from the bottom edge: "))
        top = p1
        left = p2
        right = width-p3
        bottom = height-p4
        if left<right and top<bottom and left<width and right<width and top<height and bottom<height:
            box = (left,top,right,bottom)
            new_img = p.crop(box)
            new_img.show()
        else:
            print("Values are going out of range!! Please enter valid input!!")
            cropme(p)
    except Exception as e:
        print(e)
        print("Enter valid input !! ")
        cropme(p)
    finally:
        WannaSave(new_img, f"{path}\\{d}")


def negativeImage(p):
    n= np.array(p)
    for i in range(len(n)):
        for j in range(len(n[i])):
            n[i][j][0] = 255 - n[i][j][0]
            n[i][j][1] = 255 - n[i][j][1]
            n[i][j][2] = 255 - n[i][j][2]
    return Image.fromarray(n)

def sepiaImage(p):
    img = np.array(p)
    lmap = np.matrix([[ 0.393, 0.769, 0.189],
                      [ 0.349, 0.686, 0.168],
                      [ 0.272, 0.534, 0.131]                                  
    ])
    filt = np.array([x * lmap.T for x in img] )
    filt[np.where(filt>255)] = 255
    return fromarray(filt.astype('uint8'))


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
        else:
            print("Please enter a number given in the menu!!")
    except Exception as e:
        print(e)
        print("Please enter an integer!")
