'''
responsible for imports and fundamental setup
'''

from tkinter import *       # imports all files from tkinter
from tkinter import ttk     # imports commands for ttk, specifically
import ffmpeg               # imports ffmpeg
import shutil               # allows for the file to be saved into PyGame, briefly, so that the code has access
import os                   # os is used so that the computer knows where paths to files are; removes copies
                                # so that the user's memory is crowded with unnecessary junk
from tkinter.filedialog import askopenfilename      # this specific aspect is used to find the path to the user's file
from PIL import Image, ImageTk

cur_directory = os.getcwd()

'''
this section is responsible for the uploading, conversion, and text of the file
'''


# function that opens a menu bar and allows the use to chose files that have the ending .mp4,
    # .avi, .webm, .mov, and .wav. Saves the value of that file to the originalFile variable
def open_file():
    file = askopenfilename(filetypes = [('mp4 Files', '*.mp4'),
                                                ('avi Files', '*.avi'),
                                                ('webm Files', '*.webm'),
                                                ('mov Files', '*.mov'),
                                                ('wav Files', '*.wav')])

    return file

# this method is responsible for the heavy lifting; when the user choses a file (video) to open, it
    # takes that file, converts it so that it is only audio, then uploads it into the same file that
    # the folder is - for now. Later on, it will be possible to integrate this directly into the
    # conversion algorithm we're working on
    
def run_conversion():
    video = open_file()                         # creates a string 'video' with the location of the video user chose
    if video == '':                             # if the user cancels, '' is returned; catches the error
        return
    global cur_directory                 # creates a string 'cur_directory' with the location of the folder
    path = shutil.copy2(video, cur_directory)   # creates variable of copy that is created in python folder
    
    # takes in the file that the user input; the file, currently, needs to be in the same folder as the code
    stream = ffmpeg.input(video)

    # separates the audio from the video file
    audio = stream.audio

    # creates a new ouput called 'outAudioWebM.wav' with the audio file that was created
    out = ffmpeg.output(audio, 'newSave.wav')

    # runs/(maybe opens, if you are on Windows) the file, just to listen to it and make sure it works
    out.run()

    os.remove(path)

# root is the root window that this program uses. When a button is placed in root, it is placed in the window
root = Tk()                             # creates new window using tkinter
root.geometry('800x600')                # the size of the window
root.title('Transcribing Program')      # the name of the window
root.resizable(False, False)            # prevents the user from resizing the window

canvas = Canvas(width = 900, height = 700)

bck_image = Image.open(str(cur_directory + '/BlurryBackground.jpeg'))   # creates an image file
copy_bck_image = bck_image.copy()           # copies the files, bc original file is deleted after being used
new_bck = bck_image.resize((900,700))
bck_fill = ImageTk.PhotoImage(bck_image)    # turns the image into a format tkinter can use

# places the blurry background image on the canvas to serve as a background
canvas.create_image(400, 300, image = bck_fill, anchor = CENTER)

front_image = Image.open(str(cur_directory + '/button.png'))    #finds the button picture
copy_f_image = front_image.copy()   # creates  a copy of button picture to replace original if
                                        # something gets deleted
new_image = front_image.resize((180,240))   # resizes the image so that it will fit in the canvas
front_fill = ImageTk.PhotoImage(new_image)  # converts the image into a format tkinter can use

canvas.create_image(400, 300, image = front_fill)   # adds a box in front of background to
                                                        # hold program options
canvas.pack(fill = BOTH)    # fills both left and right side of parent widget(root)

# creates a label that will be placed on canvas
option_intro = Label(canvas, bg = '#2A2661', fg = 'pink', font = ('Times New Roman', 16),
                     text = 'Program Options')
option_intro.pack() # places the label on the canvas

# places the option label on the canvas without chaninging the canvas's size
canvas.create_window(400, 200, anchor = CENTER, window = option_intro)

# creates the button that will ask the user for an upload
btn = Button(text ='Upload Files', command = lambda:run_conversion())
btn.pack(pady = 10, side = BOTTOM)
    # moves the button down 10 units and places it on the bottom of the parent widget

# creates a window on canvas and adds the button to it
canvas.create_window(400, 360, anchor = CENTER, window = btn)

# a loop that will run continuously to check if the user clicked a button on the root panel
root.mainloop()
