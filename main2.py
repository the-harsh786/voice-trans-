from tkinter import *
import speech_recognition as sr
import sounddevice
import pyaudio
from playsound import playsound
from gtts import gTTS
from translate import Translator

def bengali():
    def record_audio():
        with sr.Microphone() as source:
            audio = recognizer.record(source,duration=5)
        recognize_speech(audio)

    def translate_text(text, target_language='en'):
        global translation
        translator = Translator(from_lang="bn",to_lang=target_language)
        translation = translator.translate(text)
        return translation

    def recognize_speech(audio):
        text = recognizer.recognize_google(audio,language="bn")
        l2 = Label(d, text=translate_text(text,target_language='en'), font="TimesNewRoman")
        l2.place(x=250,y=120)
        voice=gTTS(text=translation,lang="en")
        voice.save("voice.mp3")
        playsound("voice.mp3")
        
    recognizer = sr.Recognizer()
    d=Tk()
    d.title("Translate")
    d.geometry("600x300")
    d.eval('tk::PlaceWindow . center')
    d.resizable(0,0)
    l3 = Label(d, text="BENGALI TO ENGLISH", font="TimesNewRoman 20 bold")
    l3.pack()
    btnt=Button(d,text="Click here to speak",command=record_audio)
    btnt.place(x=250,y=200)
    root1.destroy()
    

def hindi():
    def record_audio():
        with sr.Microphone() as source:
            audio = recognizer.record(source,duration=5)
        recognize_speech(audio)

    def translate_text(text, target_language='en'):
        global translation
        try:
            translator = Translator(from_lang="hi",to_lang=target_language)
            translation = translator.translate(text)
            return translation
        except NameError:
            print("Try Again")

    def recognize_speech(audio):
        text = recognizer.recognize_google(audio,language="hi")
        l2 = Label(d, text=translate_text(text,target_language='en'), font="TimesNewRoman")
        l2.place(x=250,y=120)
        voice=gTTS(text=translation,lang="en")
        voice.save("voice.mp3")
        playsound("voice.mp3")
        
    recognizer = sr.Recognizer()
    d=Tk()
    d.title("Translate")
    d.geometry("600x300")


    
    d.eval('tk::PlaceWindow . center')
    d.resizable(0,0)
    l3 = Label(d, text="HINDI TO ENGLISH", font="TimesNewRoman 20 bold")
    l3.pack()
    btnt=Button(d,text="Click here to speak",command=record_audio)
    btnt.place(x=250,y=200)
    root1.destroy()
    
def punjabi():
    def record_audio():
        with sr.Microphone() as source:
            audio = recognizer.record(source,duration=5)
        recognize_speech(audio)

    def translate_text(text, target_language='en'):
        global translation
        translator = Translator(from_lang="pa",to_lang=target_language)
        translation = translator.translate(text)
        return translation

    def recognize_speech(audio):
        text = recognizer.recognize_google(audio,language="pa")
        l2 = Label(d, text=translate_text(text,target_language='en'), font="TimesNewRoman")
        l2.place(x=250,y=120)
        voice=gTTS(text=translation,lang="en")
        voice.save("voice.mp3")
        playsound("voice.mp3")
        
    recognizer = sr.Recognizer()
    d=Tk()
    d.title("Translate")
    d.geometry("600x300")
    d.eval('tk::PlaceWindow . center')
    d.resizable(0,0)
    l3 = Label(d, text="PUNJABI TO ENGLISH", font="TimesNewRoman 20 bold")
    l3.pack()

    btnt=Button(d,text="Click here to speak",command=record_audio)
    btnt.place(x=250,y=200)
    root1.destroy()
    
def urudu():
    def record_audio():
        with sr.Microphone() as source:
            audio = recognizer.record(source,duration=5)
        recognize_speech(audio)

    def translate_text(text, target_language='en'):
        global translation
        translator = Translator(from_lang="ur",to_lang=target_language)
        translation = translator.translate(text)
        return translation

    def recognize_speech(audio):
        text = recognizer.recognize_google(audio,language="ur")
        l2 = Label(d, text=translate_text(text,target_language='en'), font="TimesNewRoman")
        l2.place(x=250,y=120)
        voice=gTTS(text=translation,lang="en")
        voice.save("voice.mp3")
        playsound("voice.mp3")
        
    recognizer = sr.Recognizer()
    d=Tk()
    d.title("Translate")
    d.geometry("600x300")
    d.eval('tk::PlaceWindow . center')
    d.resizable(0,0)
    l3 = Label(d, text="URDU TO ENGLISH", font="TimesNewRoman 20 bold")
    l3.pack()
    btnt=Button(d,text="Click here to speak",command=record_audio)
    btnt.place(x=250,y=200)
    root1.destroy()
    


def tamil():
    def record_audio():
        with sr.Microphone() as source:
            audio = recognizer.record(source,duration=5)
        recognize_speech(audio)

    def translate_text(text, target_language='en'):
        global translation
        translator = Translator(from_lang="ta",to_lang=target_language)
        translation = translator.translate(text)
        return translation

    def recognize_speech(audio):
        text = recognizer.recognize_google(audio,language="ta")
        l2 = Label(d, text=translate_text(text,target_language='en'), font="TimesNewRoman")
        l2.place(x=100,y=100)
        voice=gTTS(text=translation,lang="en")
        voice.save("voice.mp3")
        playsound("voice.mp3")
        
    recognizer = sr.Recognizer()
    d=Tk()
    d.eval('tk::PlaceWindow . center')
    d.title("Translate")
    d.geometry("600x300")
    d.resizable(0,0)
    l3 = Label(d, text="TAMIL TO ENGLISH", font="TimesNewRoman 20 bold")
    l3.pack()
    btnt=Button(d,text="Click here to speak",command=record_audio,)
    btnt.place(x=240,y=200)
    root1.destroy()
    

def main():
    root = Toplevel(root1)
    root.title("Speech to text")
    root.attributes('-fullscreen', True)
    root.resizable(0,0)
    bg = PhotoImage( file =r"C:\Users\NARAIN KARTHIGEYAN\OneDrive\Desktop\Hackathon#1\13328.png") 
    label1 = Label(root, image = bg) 
    label1.pack()
    frame1 = Frame(root, bg = "#88cffa") 
    frame1.pack(pady = 20) 
    l1 = Label(root, text="Regional Language To English Translator")
    l1.configure(font=('Courier new',25))
    l1.pack()
    photo1 = PhotoImage(file = r"C:\Users\NARAIN KARTHIGEYAN\OneDrive\Desktop\Hackathon#1\BENGLI1.png") 
    photoimage = photo1.subsample(3,3)
    btn1 = Button(root, text = 'Bengali', bd = '5',command=bengali, image=photoimage) 
    btn1.place(x=200, y=130)
    photo2 = PhotoImage(file = r"C:\Users\NARAIN KARTHIGEYAN\OneDrive\Desktop\Hackathon#1\hindi1.png") 
    photoimage2 = photo2.subsample(3,3)
    btn2 = Button(root, text = 'Hindi', bd = '5',command=hindi, bg="light blue", image=photoimage2) 
    btn2.place(x=600, y=130)
    photo3 = PhotoImage(file = r"C:\Users\NARAIN KARTHIGEYAN\OneDrive\Desktop\Hackathon#1\PUNJABI.png") 
    photoimage3 = photo3.subsample(3,3)
    btn3 = Button(root, text = 'Punjabi', bd = '5',command=punjabi, bg="grey",image=photoimage3) 
    btn3.place(x=1000, y=130)
    photo4 = PhotoImage(file = r"C:\Users\NARAIN KARTHIGEYAN\OneDrive\Desktop\Hackathon#1\urdu.png") 
    photoimage4 = photo4.subsample(3,3)
    btn4 = Button(root, text = 'Urudu', bd = '5',command=urudu, bg="white",image=photoimage4) 
    btn4.place(x=400, y=410)
    photo5 = PhotoImage(file = r"C:\Users\NARAIN KARTHIGEYAN\OneDrive\Desktop\Hackathon#1\tamil.png") 
    photoimage5 = photo5.subsample(3,3)
    btn5 = Button(root, text = 'Tamil', bd = '5',command=tamil, bg="white",image=photoimage5) 
    btn5.place(x=800, y=410)
    photo6 = PhotoImage(file = r"C:\Users\NARAIN KARTHIGEYAN\OneDrive\Desktop\Hackathon#1\exit.png") 
    photoimage6 = photo6.subsample(3,3)
    btn6 = Button(root, text = 'EXIT', bd = '5',command=root.destroy,image=photoimage6) 
    btn6.place(x=650, y=650)
    root.mainloop()

root1 = Tk()
root1.title("Insructions")
root1.attributes('-fullscreen',True)
root1.resizable(0,0)
bg = PhotoImage( file = r"C:\Users\NARAIN KARTHIGEYAN\OneDrive\Desktop\Hackathon#1\intructions.png") 
label1 = Label(root1, image = bg) 
label1.pack(expand=True) 
frame1 = Frame(root1, bg = "#88cffa") 
frame1.pack(pady = 20)
btn1 = Button(root1, text = 'Next', bd = '5',command=main, bg="white", width=20, height=2) 
btn1.place(x=1000, y=800)
btn2 = Button(root1, text = 'Back', bd = '5',command=root1.destroy, bg="white", width=10, height=2) 
btn2.place(x=1250,y=800)
