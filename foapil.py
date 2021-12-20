from PIL import Image

def printmenu():
    arr = ["Resize","Rotate","Filters","Image Type","Paste Images","Flip"]
    for i in range(len(arr)):
        print(f"{i+1}.  {arr[i]}")

print("Welcome to Image Processing Project...")
print("""Our task was to use the Python Imaging Library (PIL) 
to tackle common image processing tasks. We have some algorithms that help us apply filters to images,
 and use PIL to adjust image brightness, contrast, and 
color tone. We also performed basic functionalities along with this.""")

global img 
img = Image.open('example.jpg')

def resizeme(p):
    pass
def rotateme(p):
    pass
def filters(p):
    fil = ["Color Transform","Enhancement","Brightness","Sharpness"]
    for i in range(len(fil)):
        print(f"{i+1}.  {fil[i]}")
def changemytype(p):
    pass
def copypaste(p):
    pass
def flipme(p):
    pass

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

