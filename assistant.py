# Requred modules
import sys
import webbrowser
import pyautogui
import speech_recognition as sr
import os
import webbrowser as wb
import datetime
import wikipedia
import pyttsx3
import time
import random

# Required engines
engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
volume = engine.getProperty('volume')
engine.setProperty('rate', 180)
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 0.8)


# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()
    print(text)


# Wishing in the beginning
def wish(text):
    engine.say(text)
    engine.runAndWait()


# Wishing user
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        wish('good morning sir. how are you')
    elif hour >= 12 and hour < 16:
        wish('good afternoon sir. how are you')
    else:
        wish('good evening sir. how are you')


# Taking voice input
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
        r.energy_threshold = 800
        r.dynamic_energy_threshold = True
        r.dynamic_energy_adjustment_damping = 0.2
        try:
            text1 = r.recognize_google(audio)
            text = text1.lower()
            print('You: ' + text)
        except:
            return ""
        return text


def sleep():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
        r.energy_threshold = 500
        try:
            text1 = r.recognize_google(audio)
            text = text1.lower()
            print('You: ' + text)
        except:
            return "none"
        return text


# Logic of the program
text = ''
question = ''
type_sentence = ''
running = True
time.sleep(5)
wishme()

# Operating according to input voice
while running:
    text = takecommand()
    question = text
    query4 = ''
    query3 = ''
    query1 = ''
    query5 = ''
    query2 = ''
    page1 = ''
    page2 = ''
    wakeup_txt = ''
    if 'good evening' in text or 'good morning' in text or 'good afternoon' in text:
        speak('how may i help you sir?')
    if 'search' in text and 'in wikipedia' in text or 'search about' in text and 'in wikipedia' in text or 'wikipedia' in text:
        query1 = text.replace('wikipedia', '')
        query3 = query1.replace('about', '')
        query4 = query3.replace('in', '')
        query5 = query4.replace('for', '')
        query2 = query5.replace('search', '')
        query6 = query2
        speak('do you want me to narrate or open webpage sir?')
        answer = takecommand()
        if 'narrate' in answer or 'direct' in answer:
            results = wikipedia.summary(query6, sentences=1, auto_suggest=False)
            speak('according to wikipedia ' + results)
        elif 'web page' in answer or 'website' in answer or 'webpage' in answer:
            page1 = wikipedia.page(query2, auto_suggest=False)
            print(page1)
            page2 = page1.url
            print(page2)
            speak('redirecting to webpage')
            webbrowser.get().open_new_tab(page2)
            print(page2)
    elif text == '':
        speak('sorry sir. can you say that again?')
    elif 'search' in text and 'in google' in text:
        query1 = text.replace('in google', '')
        query2 = query1.replace('search', '')
        speak('searching ' + query2 + ' in google')
        wb.get().open_new_tab('www.google.com/search?gx&q=' + query2)
    elif 'search' in text and 'in youtube' in text:
        query1 = text.replace('in youtube', '')
        query2 = query1.replace('search for', '')
        speak('searching ' + query2 + ' in youtube')
        wb.get().open_new_tab('https://www.youtube.com/results?search_query=' + query2)
    elif 'search' in text:
        abc1 = text.replace('search', '')
        abc2 = abc1.replace('about', '')
        abc3 = abc2.replace('for', '')
        speak('do you want me to search in google, wikipedia or youtube sir?')
        answer3 = takecommand()
        if 'google' in answer3:
            speak('searching for ' + abc3 + ' in google')
            wb.get().open_new_tab('www.google.com/search?gx&q=' + abc3)

        elif 'wikipedia' in answer3:
            speak('do you want me to narrate or open webpage sir?')
            answer2 = takecommand()
            if 'narrate' in answer2 or 'direct' in answer2:
                results = wikipedia.summary(abc3, sentences=1, auto_suggest=False)
                speak('according to wikipedia ' + results)
            elif 'web page' in answer2 or 'website' in answer2 or 'webpage' in answer2:
                page1 = wikipedia.page(abc3, auto_suggest=False)
                print(page1)
                page2 = page1.url
                print(page2)
                speak('redirecting to webpage')
                webbrowser.get().open_new_tab(page2)
                print(page2)
        elif 'youtube' in answer3:
            speak('searching for ' + abc3 + 'in youtube')
            wb.get().open_new_tab('https://www.youtube.com/results?search_query=' + abc3)

    elif 'your name' in text or text == 'what is the name':
        speak('My name is Sylvie')
    elif text == 'hi' or text == 'hello' or text == 'hai' or text == 'hello hai' or text == 'hello hi':
        speak('Hello sir. how can I help you?')
    elif text == 'i am fine what about you' or text == "i'm fine what about you" or 'how are you' in text or 'what about you' in text:
        speak('I am great. do you need any help sir?')
    elif text == 'i am fine' or text == "i'm fine":
        speak('Great! do you need any help sir?')
    elif 'who created you' in text:
        speak('I was created by Himanshu Chandola')
    elif text == 'introduce yourself' or text == 'who are you' or text == 'tell me something about yourself' or 'introduce yourself' in text:
        speak(
            'I am Panda. You can know me as personal computer and virtual assistant of Himanshu Chandola. I was created by using python. I am 1 day old. currently, I am in development stage.')
    elif text == 'tell me something about mr chandola' or text == 'tell me something about Himanshu Chandola' or text == 'who is himanshu Chandola' or text == 'who is mr chandola' or text == 'who is himanshu':
        speak(
            'Himanshu Chandola is a student from Graphic Era. As a practice and a small project, he created me and I am talking to you.')
    elif 'thank you' in text or 'thanks' in text:
        speak('You are welcome! enything else sir?')
    elif 'roll' in text and 'dice' in text:
        r = random.randint(1, 6)
        dice = str(r)
        speak('you got ' + dice)
    elif 'open instagram' in text:
        speak('ok. opening instagram')
        wb.get().open_new_tab('https://instagram.com')
    elif text == 'quit' or text == 'sylvie bye' or text == 'sylvie quit' or text == 'bye' or 'bye' in text or 'quit' in text:
        speak('bye bye sir. thanks for your time')
        running = False
        sys.exit()
    elif 'open youtube' in text:
        speak('ok. opening youtube')
        wb.get().open_new_tab('https://www.youtube.com')
    elif 'open facebook' in text:
        speak('ok. opening facebook')
        wb.get().open_new_tab('https://www.facebook.com')
    elif text == 'sing a song' or text == 'sing me a song' or 'sing a song' in text:
        speak(
            'I am not a good singer but I hope you will like this. Goin out tonight, changes into something red, Her mother, doesnt like that kind of dress, Everything she never had, she showin off')
    elif 'open chrome' in text or 'open google chrome' in text:
        speak('ok. opening google chrome')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Google Chrome.lnk')
    elif 'yes' in text:
        speak('how can I help you sir?')
    elif 'open spotify' in text:
        speak('ok. opening spotify ')
        os.system('spotify')
    elif 'shut down the computer' in text or 'shutdown the computer' in text or 'shot down the computer' in text:
        speak('ok shutting down the computer')
        os.system('shutdown /s /f')
        running = False
        sys.exit()
    elif 'close opera' in text:
        os.system('TASKKILL /F /IM opera.exe')
        speak('ok. closing opera gx browser')
    elif 'close' in text and 'chrome' in text or text == 'close google chrome' or 'close google chrome' in text:
        speak('ok. closing google chrome')
        os.system('TASKKILL /F /IM chrome.exe')
    elif 'open access' in text or 'open axis' in text or 'open excess' in text:
        speak('ok. opening access')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Access.lnk')
    elif 'open photoshop' in text:
        speak('ok. opening adobe photoshop 2021')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Adobe Photoshop 2021.lnk')
    elif 'open after effects' in text:
        speak('ok. opening Adobe after effects 2021')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Adobe After Effects 2021.lnk')
    elif 'open illustrator' in text:
        speak('ok. opening Adobe illustrator 2021')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Adobe Illustrator 2021.lnk')
    elif 'open media encoder' in text:
        speak('ok. opening Adobe media encoder 2021')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Adobe Media Encoder 2021.lnk')
    elif 'open premiere pro' in text:
        speak('ok. opening adobe premiere pro 2021')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Adobe Premiere Pro 2021.lnk')
    elif 'open bluestacks' in text:
        speak('Ok. opening bluestacks 5')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/BlueStacks 5.lnk')
    elif 'open excel' in text:
        speak('Ok. opening Excel')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Excel.lnk')
    elif 'open free download manager' in text:
        speak('ok. opening free download manager')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Free Download Manager.lnk')
    elif 'open edge' in text:
        speak('ok. opening edge')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Edge.lnk')
    elif 'open screen recorder' in text or 'open recorder' in text:
        speak('ok. opening obs studio')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/OBS Studio (64bit).lnk')
    elif 'open one drive' in text:
        speak('ok. opening one drive')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/OneDrive for Business.lnk')
    elif 'open one note' in text:
        speak('ok. opening one note')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/OneNote.lnk')
    elif 'open outlook' in text:
        speak('ok. opening outlook')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Outlook.lnk')
    elif 'open powerpoint' in text:
        speak('ok. opening powerpoint')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/PowerPoint.lnk')
    elif 'open publisher' in text:
        speak('ok. opening publisher')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Publisher.lnk')
    elif 'open skype' in text:
        speak('ok. opening skype')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Skype for Business.lnk')
    elif 'open visual studio installer' in text:
        speak('ok. opening visual studio installer')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Visual Studio Installer.lnk')
    elif 'open word' in text:
        speak('ok. opening word')
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Word.lnk')
        speak('do you want me to type sir?')
        typin = takecommand()
        if 'yes' in typin:
            pyautogui.press('enter')
            speak('sir you can start. say stop typing if I have to stop')
            while not 'stop typing' in type_sentence:
                type_sentence = takecommand()
                if type_sentence != 'stop typing' and type_sentence != 'press enter':
                    pyautogui.write(type_sentence + '. ')
                elif type_sentence == 'press enter':
                    pyautogui.press('enter')
            speak('stopped typing')
        elif 'no' in typin:
            speak('ok sir')
    elif 'open pycharm' in text:
        speak('ok. opening pycharm')
        os.startfile(
            'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/JetBrains/PyCharm Community Edition 2021.1.3.lnk')
    elif 'stop typing' in text:
        speak('sir I already stopped typing')
    elif 'time' in text:
        h = datetime.datetime.now().strftime("%H,%M,%S")
        speak(f"sir, the time is{h}")
    elif 'open zoom' in text:
        speak('ok. opening zoom')
        os.startfile('C:/Users/nbhel/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Zoom/Zoom.lnk')
    elif 'close access' in text or 'close axis' in text or 'close excess' in text:
        speak('ok. closing access')
        os.system('TASKKILL /F /IM MSACCESS.exe')
    elif 'close after effects' in text:
        speak('ok. closing adobe after effects 2021')
        os.system('TASKKILL /F /IM AfterFX.exe')
    elif 'close illustrator' in text:
        speak('ok. closing adobe illustrator 2021')
        os.system('TASKKILL /F /IM AIRobin.exe')
    elif 'close spotify' in text:
        speak('ok. closing spotify')
        os.system('TASKKILL /F /IM Spotify.exe')
    elif 'close photoshop' in text:
        speak('ok. closing adobe photoshop 2021')
        os.system('TASKKILL /F /IM Photoshop.exe')
    elif 'close pycharm' in text or 'close python' in text:
        speak('ok. closing pycharm')
        os.system('TASKKILL /F /IM pycharm64.exe')
    elif 'close bluestacks' in text:
        speak('ok. closing bluestacks')
        os.system('TASKKILL /F /IM HD-Player.exe')
    elif 'close excel' in text:
        speak('ok. closing excel')
        os.system('TASKKILL /F /IM EXCEL.EXE')
    elif 'close youtube' in text:
        speak('ok. closing youtube')
        pyautogui.hotkey('ctrl', 'w')
    elif 'close facebook' in text:
        speak('ok. closing facebook')
        pyautogui.hotkey('ctrl', 'w')
    elif 'close task manager' in text:
        speak('ok. closing task manager')
        os.system('TASKKILL /F /IM Taskmgr.exe')
    elif 'close free download manager' in text:
        speak('ok. closing free download manager')
        os.system('TASKKILL /F /IM fdm.exe')
    elif 'close edge' in text:
        speak('ok. closing microsoft edge')
        os.system('TASKKILL /F /IM msedge.exe')
    elif 'close recorder' in text:
        speak('ok. closing obs studio')
        os.system('TASKKILL /F /IM obs64.exe')
    elif 'close powerpoint' in text:
        speak('ok. closing powerpoint')
        os.system('TASKKILL /F /IM POWERPNT.EXE')
    elif 'close word' in text:
        speak('ok. closing word')
        os.system('TASKKILL /F /IM winword.exe')
    elif 'repeat' in text:
        speak('ok sir. say stop repeating if i have to stop')
        repeating = ''
        while repeating != 'stop repeating':
            repeating = takecommand()
            if repeating != 'stop repeating':
                speak(repeating)
            elif repeating == 'stop repeating':
                speak('ok sir. repeating stopped.')
    elif 'sleep' in text:
        speak('ok sir goodnight')
        sl_cr = ''
        while not 'wake up' in sl_cr:
            sl_cr = sleep()
            if sl_cr == 'quit':
                speak('bye bye sir. have a great day')
        speak('hello again sir')
    elif 'show' in text and 'mirror' in text or 'open camera' in text:
        speak('ok. opening camera')
        os.system('start microsoft.windows.camera:')
    elif 'close' in text and 'camera' in text:
        speak('ok. closing camera')
        pyautogui.hotkey('alt', 'f4')
    elif 'search' in text and 'in youtube' in text:
        search_text1 = text.replace('search', '')
        search_text2 = search_text1.replace('in youtube', '')
        speak('searching for ' + search_text2 + ' in youtube')
        webbrowser.get().open_new_tab('https://www.youtube.com/results?search_query=' + search_text2)
    elif 'play' in text and 'music' in text or 'playlist' in text:
        speak('ok sir enjoy your music')
        os.system('spotify.exe')
        time.sleep(1)
        pyautogui.click(button='left')
        pyautogui.press('space')
        pyautogui.hotkey('alt', 'f4')
        while not 'wake up' in wakeup_txt:
            wakeup_txt = sleep()
            if wakeup_txt == 'quit':
                speak('bye bye sir. have a great day')
                running = False
                sys.exit()
            elif 'pause' in wakeup_txt or 'play' in wakeup_txt:
                os.system('spotify')
                time.sleep(1)
                pyautogui.press('space')
                pyautogui.hotkey('alt', 'f4')
            elif 'close spotify' in wakeup_txt:
                os.system('TASKKILL /F /IM Spotify.exe')
        speak('hello again sir')
    elif 'open wikipedia' in text:
        speak('ok. opening wikipedia')
        webbrowser.get().open_new_tab('https://www.wikipedia.org')
    else:
        speak('sorry sir that is not assigned. do you want to search for ' + text + '?')
        confirmation = takecommand()
        if 'yes' in confirmation:
            speak('do you want me to search in google, wikipedia or youtube sir?')
            answer4 = takecommand()
            if 'google' in answer4:
                speak('searching for ' + text + ' in google')
                wb.get().open_new_tab('www.google.com/search?gx&q=' + text)

            elif 'wikipedia' in answer4:
                speak('do you want me to narrate or open webpage sir?')
                answer2 = takecommand()
                if 'narrate' in answer2 or 'direct' in answer2:
                    results = wikipedia.summary(text, sentences=1, auto_suggest=False)
                    speak('according to wikipedia ' + results)
                elif 'web page' in answer2 or 'website' in answer2 or 'webpage' in answer2:
                    page1 = wikipedia.page(text, auto_suggest=False)
                    print(page1)
                    page2 = page1.url
                    print(page2)
                    speak('redirecting to webpage')
                    webbrowser.get().open_new_tab(page2)
                    print(page2)
            elif 'youtube' in answer4:
                speak('searching for ' + text + 'in youtube')
                wb.get().open_new_tab('https://www.youtube.com/results?search_query=' + text)
        else:
            speak('ok. anything else sir?')
