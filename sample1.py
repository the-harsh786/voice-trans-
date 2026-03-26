from tkinter import *
import speech_recognition as sr
import sounddevice
import pyaudio
from playsound import playsound
from gtts import gTTS
from translate import Translator

def bengali():
    def record_audio(code_):
        with sr.Microphone() as source:
            audio = recognizer.record(source,duration=5)
        recognize_speech(audio,code_)

    def translate_text(text, target_language='en'):
        global translation
        translator = Translator(from_lang=a,to_lang=target_language)
        translation = translator.translate(text)
        return translation

    def recognize_speech(audio,code_):
        text = recognizer.recognize_google(audio,language=code_)
        print(translate_text(text,target_language='en'))
        voice=gTTS(text=translation,lang="en")
        voice.save("voice.mp3")
        playsound("voice.mp3")
    global a
    a="bn"
    recognizer = sr.Recognizer()
    record_audio(a)
    root.destroy()
    

def hindi():
    def record_audio(code_):
        with sr.Microphone() as source:
            audio = recognizer.record(source,duration=5)
        recognize_speech(audio,code_)

    def translate_text(text, target_language='en'):
        global translation
        translator = Translator(from_lang=a,to_lang=target_language)
        translation = translator.translate(text)
        return translation

    def recognize_speech(audio,code_):
        text = recognizer.recognize_google(audio,language=code_)
        print(translate_text(text,target_language='en'))
        voice=gTTS(text=translation,lang="en")
        voice.save("voice.mp3")
        playsound("voice.mp3")
    global a
    a="hi"
    recognizer = sr.Recognizer()
    record_audio(a)
    root.destroy()
    
def punjabi():
    def record_audio(code_):
        with sr.Microphone() as source:
            audio = recognizer.record(source,duration=5)
        recognize_speech(audio,code_)

    def translate_text(text, target_language='en'):
        global translation
        translator = Translator(from_lang=a,to_lang=target_language)
        translation = translator.translate(text)
        return translation

    def recognize_speech(audio,code_):
        text = recognizer.recognize_google(audio,language=code_)
        print(translate_text(text,target_language='en'))
        voice=gTTS(text=translation,lang="en")
        voice.save("voice.mp3")
        playsound("voice.mp3")
    global a
    a="pa"
    recognizer = sr.Recognizer()
    record_audio(a)
    root.destroy()
    


def urudu():
    def record_audio(code_):
        with sr.Microphone() as source:
            audio = recognizer.record(source,duration=5)
        recognize_speech(audio,code_)

    def translate_text(text, target_language='en'):
        global translation
        translator = Translator(from_lang=a,to_lang=target_language)
        translation = translator.translate(text)
        return translation

    def recognize_speech(audio,code_):
        text = recognizer.recognize_google(audio,language=code_)
        print(translate_text(text,target_language='en'))
        voice=gTTS(text=translation,lang="en")
        voice.save("voice.mp3")
        playsound("voice.mp3")
    global a
    a="ur"
    recognizer = sr.Recognizer()
    record_audio(a)
    root.destroy()
    


def tamil():
    def record_audio(code_):
        with sr.Microphone() as source:
            audio = recognizer.record(source,duration=5)
        recognize_speech(audio,code_)

    def translate_text(text, target_language='en'):
        global translation
        translator = Translator(from_lang=a,to_lang=target_language)
        translation = translator.translate(text)
        return translation

    def recognize_speech(audio,code_):
        text = recognizer.recognize_google(audio,language=code_)
        print(translate_text(text,target_language='en'))
        voice=gTTS(text=translation,lang="en")
        voice.save("voice.mp3")
        playsound("voice.mp3")
    global a
    a="ta"
    recognizer = sr.Recognizer()
    record_audio(a)
    root.destroy()
    

root = Tk()
root.title("Speech-To-Text")
root.attributes('-fullscreen',True)
root.resizable(0,0)
btn1 = Button(root, text = 'Bengali', bd = '5',width = 55,height = 15, command=bengali) 
btn1.place(x=150, y=200)
btn2 = Button(root, text = 'Hindi', bd = '5',width = 55,height = 15, command=hindi) 
btn2.place(x=600, y=200)
btn3 = Button(root, text = 'Punjabi', bd = '5',width = 55,height = 15,command=punjabi) 
btn3.place(x=1050, y=200)
btn4 = Button(root, text = 'Urudu', bd = '5',width = 55,height = 15,command=urudu) 
btn4.place(x=350, y=500)
btn5 = Button(root, text = 'Tamil', bd = '5',width = 55,height = 15,command=english) 
btn5.place(x=790, y=500)
btn6 = Button(root, text = 'EXIT', bd = '5',width = 25, command=root.destroy) 
btn6.place(x=1300, y=800)
root.mainloop()
