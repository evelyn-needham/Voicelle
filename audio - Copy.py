
# importing librarys

import speech_recognition as sr
from speech_recognition import AudioData
import subprocess
import ffmpeg
import wave
import contextlib

check = False
audio = ""
r = sr.Recognizer()
r.energy_threshold = 2000
r.pause_threshold = 1
mic = sr.Microphone(device_index=0)
# Configuring the record function as well as a barrier for the mic to read(energy threshold)
# Pause threshold will govern the length of silence needed to begin another line
# ( Device index line governs the microphone that is used 0 is default

with mic as source:
    print("file or mic? say which you want")
    response = r.listen(mic)
    # mic as source intiilises the microphone and audio detects speech from mic

    print(response)
if response.lower == "mike\n":
    # if said mic begin microphone program
    while response == response:
        response = "yes"
        while response.lower() == "yes":
            print("begin when ready, if you stop speaking for 1 second, the block will end")

        audio = r.listen(mic) + "\n"
        response = input(audio + " line 1" + "\nRecord second line?")


else:

    file = input("file name")
    stream = ffmpeg.input(file)
    audioia = stream.audio
    out = ffmpeg.output(audioia, 'BIGFILEENERGY.flac')

    # noinspection PyBroadException
    try:

        # attempt to mount and read file
        file2 = r.record(out)
        BIG_MEME = (r.recognize_google(file2))
        print(BIG_MEME)
    except:
        print("U did a bad.")

    with contextlib.closing(wave.open(out, 'r')) as f:
        # prototype rip audio from file
        frames = file2.getnframes()
        rate = file2.getframerate()
        duration = frames / float(rate)
        x = 0
        check = False
        text = ""
        text_hold = ""

    while x < duration and check == True:
        y = 1

        text_temp = (r.recognize_google(file2, x, y))
        text = text + " " + text_temp
        text_hold = text_hold + (text_temp + " second " + x)
        x = x + y
        # this code ticks up a second counter to read each x seconds of a file and compile and compare to the entire
        # file then the code will if not correct check every 2 seconds of a file and so on and so forth
        if text == r.recognize_google(audio):
            check = True
        elif x >= duration:
            y = y + 1
            x = 0
