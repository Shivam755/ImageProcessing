from PIL import Image,ImageOps,ImageEnhance
# import ImageOps

def printmenu():
    arr = ["Resize","Rotate","Filters","Image Type","Paste Images","Flip","Exit"]
    for i in range(len(arr)):
        print(f"{i+1}.  {arr[i]}")

print("Welcome to Image Processing Project...")
print("""Our task was to use the Python Imaging Library (PIL) 
to tackle common image processing tasks. We have some algorithms that help us apply filters to images,
 and use PIL to adjust image brightness, contrast, and 
color tone. We also performed basic functionalities along with this.""")

global img 
img = Image.open('birdy.jpg')


def resizeme(p):
    width=int(input(">>Enter width : "))
    height=int(input(">>Enter height : "))
    new_image = p.resize((width, height))
    new_image.save('img.jpg')
    new_image.show()
def rotateme(p):
    deg=int(input(">>Enter degree to rotate : "))
    new_image=p.rotate(deg)
    new_image.save('img.jpg')
    new_image.show()
def filters(p):
    fil = ["Color Transform","Enhancement","Brightness","Sharpness"]
    for i in range(len(fil)):
        print(f"{i+1}.  {fil[i]}")
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
def changemytype(p):
    img_name=input(">>Enter new name of image : ")
    img_type=input(">>Enter extention of image : ")
    p.save(img_name+"."+img_type)
def copypaste(p):
    img2_name=input(">>Enter new name of image : ")
    img2=Image.open(img2_name)
    p_cpy=p.copy()
    dist_left=int(input(">>Enter distance from left : "))
    dist_up=int(input(">>Enter distance from upside : "))
    p_cpy.paste(img2,(dist_left,dist_up))
    p_cpy.save('img.jpg')
    p_cpy.show()
def flipme(p):
    flip = ["anti-clockwise flip","clockwise flip","horizontal flip","vertical flip"]
    for i in range(len(flip)):
        print(f"{i+1}.  {flip[i]}")
    opt=int(input(">>Enter flipping option : "))
    if opt==1:
        new_image=p.transpose(Image.TRANSPOSE)
        new_image.save('img.jpg')
        new_image.show()
    elif opt==2:
        new_image=p.transpose(Image.TRANSVERSE)
        new_image.save('img.jpg')
        new_image.show()
    elif opt==3:
        new_img=ImageOps.mirror(p)
        # new_img=p.transpose(Image.FLIP_LEFT_RIGHT)
        new_image.save('img.jpg')
        new_img.show()
    elif opt==4:
        new_image=p.transpose(Image.FLIP_TOP_BOTTOM)
        new_image.save('img.jpg')
        new_image.show()
while True:
    printmenu()
    print("What do you want?")
    try : 
        ask = int(input(">>>> "))
    except:
        print("Please enter an integer!")
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
        print("Thank You !!")
        break