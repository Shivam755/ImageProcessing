from PIL import Image,ImageEnhance
# import ImageOps

def printmenu():
    arr = ["Resize","Rotate","Filters","Image Type","Paste Images","Flip","Crop","Exit"]
    for i in range(len(arr)):
        print(f"{i+1}.  {arr[i]}")

print("Welcome to Image Processing Project...")
print("""Our task was to use the Python Imaging Library (PIL) 
to tackle common image processing tasks. We have some algorithms that help us apply filters to images,
 and use PIL to adjust image brightness, contrast, and 
color tone. We also performed basic functionalities along with this.""")

global img,ask
img = Image.open('birdy.jpg')

def WannaSave(p,path):
    print("Do you want to save this image??\nY / N")
    ask1 = input(">>>> ")
    if ask1 == "Y":
        string = input("Enter the name of the file: ")
        new = p.save(path+"\\"+string+'.jpg')
    elif ask1 =="N":
        pass
    else:
        print("Please enter a valid input!")
        WannaSave(p)

def resizeme(p):
    try:
        path= ""
        width=int(input(">>Enter width : "))
        height=int(input(">>Enter height : "))
        new_image = p.resize((width, height))
        new_image.show()
    except:
        print("Enter valid input !! ")
        resizeme(p)
    finally:
        WannaSave(new_image,path)

def rotateme(p):
    try:
        path=""
        deg=int(input(">>Enter degree to rotate : "))
        new_image=p.rotate(deg)
        new_image.show()
        WannaSave(new_image)
    except:
        print("Enter valid input !! ")
        rotateme(p)
    finally:
        WannaSave(new_image,path)

def filters(p):
    fil = ["Color Transform","Enhancement","Brightness","Sharpness"]
    for i in range(len(fil)):
        print(f"{i+1}.  {fil[i]}")
    try:
        path=""
        filter=int(input(">>Enter filter : "))
        if filter==1:
            mode=input(">>Enter mode for transormation (RGB/L/CMYK): ")
            new_image=p.convert(mode)
            new_image.save('img.jpg')
            new_image.show()
        elif filter==2:
            fact=float(input(">>Enter contrast factor : "))
            contrast = ImageEnhance.Contrast(p)
            contrast.save('img.jpg')
            contrast.enhance(fact).show()
        elif filter==3:
            fact=float(input(">>Enter brightness factor : "))
            brightness=ImageEnhance.Brightness(p)
            brightness.save('img.jpg')
            brightness.enhance(fact).show()
        elif filter==4:
            fact=float(input(">>Enter sharpness factor : "))
            sharpness=ImageEnhance.Sharpness(p)
            sharpness.save('img.jpg')
            sharpness.enhance(fact).show()
    except:
        print("Enter valid input !! ")
        filters(p)
    finally:
        WannaSave(new_image,path)

def changemytype(p):
    img_name=input(">>Enter new name of image : ")
    img_type=input(">>Enter extention of image : ")
    p.save(img_name+"."+img_type)

def copypaste(p):
    try:
        path=""
        img2_name=input(">>Enter new name of image : ")
        img2=Image.open(img2_name)
        p_cpy=p.copy()
        dist_left=int(input(">>Enter distance from left : "))
        dist_up=int(input(">>Enter distance from upside : "))
        p_cpy.paste(img2,(dist_left,dist_up))
        p_cpy.show()
    except:
        print("Enter valid input !! ")
        copypaste(p)
    finally:
        WannaSave(p_cpy,path)

def flipme(p):
    try:
        path=""
        flip = ["anti-clockwise flip","clockwise flip","horizontal flip","vertical flip"]
        for i in range(len(flip)):
            print(f"{i+1}.  {flip[i]}")
        opt=int(input(">>Enter flipping option : "))
        if opt==1:
            new_image=p.transpose(Image.TRANSPOSE)
            new_image.show()
            WannaSave(new_image)
        elif opt==2:
            new_image=p.transpose(Image.TRANSVERSE)
            new_image.show()
            WannaSave(new_image)
        elif opt==3:
            # new_img=ImageOps.mirror(p)
            new_img=p.transpose(Image.FLIP_LEFT_RIGHT)
            new_img.save('img.jpg')
            new_img.show()
        elif opt==4:
            new_image=p.transpose(Image.FLIP_TOP_BOTTOM)
            new_image.show()
            WannaSave(new_image)
    except:
        print("Enter valid input !! ")
        flipme(p)
    finally:
        WannaSave(new_image,path)

def cropme(p):
    try:
        path=""
        width,height=p.size
        print(" !! Enter values in range of ",width," , ",height," !!")
        p1=int(input(">>Enter distance from left : "))
        p2=int(input(">>Enter distance from up : "))
        p3=int(input(">>Enter distance from right : "))
        p4=int(input(">>Enter distance from bottom : "))
        if p1<width and p3<width and p1<height and p4<height:
            box=(p1, p2, p3, p4)
            new_img=p.crop(box)
            new_img.show()
        else:
            print("Out Of range !!")
            cropme(p)
    except:
        print("Enter valid input !! ")
        cropme(p)
    finally:
        WannaSave(new_img,path)

while True:
    printmenu()
    print("What do you want?")
    try : 
        ask = int(input(">>>> "))
        if ask==1:
            resizeme(img)
        elif ask==2:
            rotateme(img)
        elif ask==3:
            filters(img)
        elif ask==4:
            changemytype(img)
        elif ask==5:
            copypaste(img)
        elif ask==6:
            flipme(img)
        elif ask==7:
            cropme(img)
        elif ask==8:
            print("Thank You !!")
            break
    except:
        print("Please enter an integer!")
    