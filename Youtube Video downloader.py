# go to pypi and pytube and copy paste here 

#imported required dependencies
import pytube

from pytube import YouTube

#using python tkinter for GUI
from tkinter import *

root = Tk() #tkinter

root.geometry("300x400") #geometry size for GUI
root.title("Youtube Video Downloader") #Title for our GUI

bkg = PhotoImage(file = r"C:\Users\Ruchi\Downloads\python learning\youtube.png")
#bkg means background we have to call it, path ke baad ye image name.extension add karna pdta hai


# Create a background label for image

l1 = Label(root,image = bkg) #root means gui pe chipkana hai, and image is bkg
l1.place(x=0, y=0, relwidth=1, relheight=1)

#place matlab where to place

# define a function for the downloading task
def youtube():
    a = var.get()   # example link to paste in gui box, get from user
    ytvideo = YouTube(a).streams.filter(progressive=True,file_extension="mp4").order_by('resolution').desc().first()
    ytvideo.download(r"C:\Users\Ruchi\Downloads\python learning")   # folder to save downloaded videos
      #this code we get from pipy
    print("Entry box",a)

def Close(): #we have to close the function or else everything we write here will be added to function
    root.destroy() #we have to destroy root or else the GUI code will overlap with root code


#PyQt5 used other than tkinter for GUI


# Add a text label tothe top of our background image, means heading

my_text = Label(root, text= "Welcome to Downloader", font=("Helvetica",30), fg="Red", bg= '#e1e1e1') #fg font color
#, bg matlab background color matching to the heading bckgrnd
my_text.pack(pady=70) #pady equal spacing from all the sides of our root, and it is pad y matlab y coordinate 

#pad means thickness

# Create a frame to add a text label and user input box
my_frame  = Frame(root, bg= '#e1e1e1')
my_frame.pack(pady=5) #root pe nahi rakh rahe hai, root pe frame and frame pe box


# Create a label for user input, which is on the frame
l2 = Label(my_frame, text="Paste Youtube Video Link in the Box",fg= "black",font=("bold",20), bg= '#e1e1e1')
l2.grid(row=0,column=0, padx=20) #google what is pack and grid

# Add a user's link input box
var = StringVar() # string variable uthana hai var mein
e1 = Entry(my_frame,textvariable=var,width=80)
e1.grid(row=1,column=0, padx=20)


#ab button ke liye frame banaynge, pehle box ke frame banaya

# Create another frame to add multiple buttons in a line
my_frame1  = Frame(root, bg= '#e1e1e1')
my_frame1.pack(pady=200)

# create a download button 
b1 = Button(my_frame1,text="Download",command=youtube,bg="green",width=20,fg="white")
b1.grid(row=0,column=0, padx=50)

# create a exit button to close the GUI
b2 = Button(my_frame1,text="Exit",command=Close,bg="black",width=10,fg="white")
b2.grid(row=0,column=2, padx=50)
         

root.mainloop()