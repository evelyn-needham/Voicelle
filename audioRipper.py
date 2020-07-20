import speech_recognition as sr
import subprocess
import ffmpeg
import wave
import contextlib
r = sr.Recognizer()
r.energy_threshold=2000
r.pause_threshold=1
mic = sr.Microphone(device_index=0)

with mic as source:
    print("file or mic? say which you want")
    audio = r.listen(mic)

    try:
        response = (r.recognize_google(audio))
    except:
        file = input("file name")
        try:
            print(r.recognize_google(file))
        except:
            command = "ffmpeg -i " + file + " -ab 160k -ac 2 -ar 44100 -vn audio.wav"
            print(r.recognize_google(audio.wav))
    print (response)
if response.lower == "mike\n":
    while response == response:

        print("begin when ready, if you stop speaking for 1 second, the block will end")
        while response == "yes":

            audio = r.listen(mic) + "\n"
            response = input(audio +" line 1" +"\nRecord second line?")


else:


    file = input("file name")
    try:
        print(r.recognize_google(file))
    except:
       command = "ffmpeg -i "+file+ " -ab 160k -ac 2 -ar 44100 -vn audio.wav"
       audio2 = r.record('audio.wav')
       print(r.recognize_google(audio2))

    with contextlib.closing(wave.open(audio,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames/float(rate)
        x=0
        check == False
    while x < duration and check == True:
        y=1

        text_temp = (r.recognize_google(audio,offset=x, duration=y))
        text = text + " " + text_temp
        print (text_temp + " second 1")
        x=x+y
        if text== r.recognize_google(audio):
            check = True
        elif x >= duration:
            y = y+1
            x=0
