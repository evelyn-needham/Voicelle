import speech_recognition as sr
import subprocess
import ffmpeg
import wave
import contextlib

# importing librarys
from speech_recognition import AudioData
import speech_recognition as sr
import subprocess
import ffmpeg
import wave
import contextlib
import os
from tkinter import *  # imports all files from tkinter
from tkinter import ttk  # imports commands for ttk, specifically
import ffmpeg  # imports ffmpeg
import shutil  # allows for the file to be saved into PyGame, briefly, so that the code has access
import os  # os is used so that the computer knows where paths to files are; removes copies
# so that the user's memory is crowded with unnecessary junk
from tkinter.filedialog import askopenfilename  # this specific aspect is used to find the path to the user's file
from PIL import Image, ImageTk
import platform

check = False
audio = ""
r = sr.Recognizer()
r.energy_threshold = 2000
cur_directory = os.getcwd()
r.pause_threshold = 1
mic = sr.Microphone(device_index=0)


# Configuring the record function as well as a barrier for the mic to read(energy threshold)
# Pause threshold will govern the length of silence needed to begin another line
# ( Device index line governs the microphone that is used 0 is default

def alert_popup(title, message, path):
    """Generate a pop-up window for special messages."""
    root = Tk()
    root.title(title)
    w = 400     # popup window width
    h = 200     # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = message
    m += '\n'
    m += path
    w = Label(root, text=m, width=120, height=10)
    w.pack()
    b = Button(root, text="OK", command=root.destroy, width=10)
    b.pack()

def mic_shtuff():
    response = "yes"
    while response.lower() == "yes":
        print("begin when ready, if you stop speaking for 1 second, the block will end")

        return r.listen(mic) + '\n'


def fileyio(file, l):
    file_big = sr.AudioFile(file)
    with file_big as source:
        r.adjust_for_ambient_noise(source)
        file2 = r.record(source)

        alert_popup("your message good sir or madam", str(r.recognize_google(file2)),"press OK to chosse another WONDERFULL FILE" )
        return r.recognize_google(file2)


    duration = l
    x = 0

    text = ""
    text_hold = ""
    y = 1
    check = True
    x = 0
    y = 1

    #with file_big as source:

        # file_big2 = r.record(source, offset=x, duration=y)
        #file_aaa = r.record(source)

        # with file_big2 as source:

            #    text_temp = r.recognize_google(file_big2)

            #   text = text.strip("\n") + " " + text_temp.strip("\n")
            # text_hold = text_hold + (text_temp.strip("\n") + " second " + str(x) + "\n")
            # x = x + y

        # this code ticks up a second counter to read each x seconds of a file and compile and compare to the entire
        # file then the code will if not correct check every 2 seconds of a file and so on and so forth
        # if text == r.recognize_google(file_aaa):

        #    check = False
        # elif x >= duration:
        #    y = y + 1
        #    x = 0
    # print (text_hold)
    # return text_hold


'''
responsible for imports and fundamental setup
'''

from tkinter import *  # imports all files from tkinter
from tkinter import ttk  # imports commands for ttk, specifically
import ffmpeg  # imports ffmpeg
import shutil  # allows for the file to be saved into PyGame, briefly, so that the code has access
import os  # os is used so that the computer knows where paths to files are; removes copies
# so that the user's memory is crowded with unnecessary junk
from tkinter.filedialog import askopenfilename  # this specific aspect is used to find the path to the user's file
from PIL import Image, ImageTk
import platform

new_text = ''

cur_directory = os.getcwd()
print(cur_directory)

'''
this section is responsible for the uploading, conversion, and text of the file
'''


# function that opens a menu bar and allows the use to chose files that have the ending .mp4,
# .avi, .webm, .mov, and .wav. Saves the value of that file to the originalFile variable
def open_file():
    file = askopenfilename(filetypes=[('wav Files', '*.wav'),
                                      ('avi Files', '*.avi'),
                                      ('AIFF Files', '*.AIFF'),
                                      ('AIFF-c Files', '*.AIFF-C'),
                                      ('FLAC files', '*.FLAC')])
    file = file
    import scipy.io.wavfile as wav
    (sr, ss) = wav.read(file)
    ds = len(ss) / float(sr)
    print(fileyio(file, ds))


# this method is responsible for the heavy lifting; when the user choses a file (video) to open, it
# takes that file, converts it so that it is only audio, then uploads it into the same file that
# the folder is - for now. Later on, it will be possible to integrate this directly into the
# conversion algorithm we're working on

def run_conversion():
    video = open_file()  # creates a string 'video' with the location of the video user chose
    # if video == '':  # if the user cancels, '' is returned; catches the error
    #   return
    # global cur_directory  # creates a string 'cur_directory' with the location of the folder
    # creates variable of copy that is created in python folder

    # takes in the file that the user input; the file, currently, needs to be in the same folder as the code

    # stream = ffmpeg.input(video)

    # separates the audio from the video file
    # audio = stream.audio

    # creates a new ouput called 'outAudioWebM.wav' with the audio file that was created
    # out = ffmpeg.output(audio, 'newSave.wav')

    # print ("F")
    # out3 = r.record('newSave.wav')
    # print(r.recognize_google(out3))
    # use audioread to find length of given file
    # from mutagen.mp3 import MP3

    # audio_info = out2.info
    # length = int(audio_info.length)

    # runs/(maybe opens, if you are on Windows) the file, just to listen to it and make sure it works
    # print('lol')

    # os.remove(path)
    # print('lol')
    # this spits newSave.wav into the hole where we can look for the thing


# root is the root window that this program uses. When a button is placed in root, it is placed in the window
root = Tk()  # creates new window using tkinter
root.geometry('800x600')  # the size of the window
root.title('Transcribing Program')  # the name of the window
root.resizable(False, False)  # prevents the user from resizing the window
platf = platform.system()
canvas = Canvas(width=900, height=700)
if platf == 'Windows':
    bck_image = Image.open(str(cur_directory + '\BlurryBackground.jpeg.jpg'))  # creates an image file
if platf == 'Darwin':
    bck_image = Image.open(str(cur_directory + '/BlurryBackground.jpeg.jpg'))  # creates an image file
copy_bck_image = bck_image.copy()  # copies the files, bc original file is deleted after being used
new_bck = bck_image.resize((900, 700))
bck_fill = ImageTk.PhotoImage(bck_image)  # turns the image into a format tkinter can use

# places the blurry background image on the canvas to serve as a background
canvas.create_image(400, 300, image=bck_fill, anchor=CENTER)

front_image = Image.open(str(cur_directory + '/button.png'))  # finds the button picture
copy_f_image = front_image.copy()  # creates  a copy of button picture to replace original if
# something gets deleted
new_image = front_image.resize((180, 240))  # resizes the image so that it will fit in the canvas
front_fill = ImageTk.PhotoImage(new_image)  # converts the image into a format tkinter can use

canvas.create_image(400, 300, image=front_fill)  # adds a box in front of background to
# hold program options
canvas.pack(fill=BOTH)  # fills both left and right side of parent widget(root)

# creates a label that will be placed on canvas
option_intro = Label(canvas, bg='#2A2661', fg='pink', font=('Times New Roman', 16),
                     text='Program Options')
option_intro.pack()  # places the label on the canvas

# places the option label on the canvas without chaninging the canvas's size
canvas.create_window(400, 200, anchor=CENTER, window=option_intro)

# creates the button that will ask the user for an upload
btn = Button(text='Upload Files', command=lambda: run_conversion())
btn.pack(pady=10, side=BOTTOM)
option_intro = Label(canvas, bg='#2A2661', fg='pink', font=('Times New Roman', 16),
                     text=new_text)
# moves the button down 10 units and places it on the bottom of the parent widget

# creates a window on canvas and adds the button to it
canvas.create_window(400, 360, anchor=CENTER, window=btn)

# a loop that will run continuously to check if the user clicked a button on the root panel
root.mainloop()
