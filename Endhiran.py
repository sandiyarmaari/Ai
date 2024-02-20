import speech_recognition as sr
import pyttsx3
import time
import os
import datetime
import webbrowser
import requests

print("Welcome to World Of Mark Antony - Endhiran")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


speak("Welcome To World of Mark Antony - Endhiran ")


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        print("Good Morning ... ")
        speak("Good Morning...")
    elif 12 <= hour < 18:
        print("Good Afternoon")
        speak("Good Afternoon")
    else:
        print("Good Night")
        speak("Good Night")


wishMe()


def listener():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("How can I Help You...")
        speak("How can i help you")
        print("Tell Boss...")
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source)
            statement = r.recognize_google(audio, language="en-in")
            print(f"User Said: {statement}\n")
            return statement.lower()
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand what you said. Please try again.")
            return "None"
        except sr.RequestError as e:
            speak("Sorry, I'm unable to access the Google API. Please try again later.")
            return "None"


def get_input():
    while True:
        input_choice = input("How would you like to input your command? (keyboard/speech): ").lower()
        if input_choice not in ["keyboard", "speech"]:
            print("Invalid choice. Please choose 'keyboard' or 'speech'.")
            continue
        else:
            return input_choice


def translate_text():
    speak("Welcome to the Translator!")
    print("Welcome to the Translator!")
    speak("Supported Languages:")
    print("Supported Languages:")
    speak("English")
    print("1. English")
    speak("tamil")
    print("2. Tamil")
    speak("spanish")
    print("3. Spanish")
    speak("french")
    print("4. French")
    speak("Malayalam")
    print("5. Malayalam")

    # Mapping of language names to language codes
    language_codes = {"english": "en", "tamil": "ta", "spanish": "es", "french": "fr","malayalam" : "ma"}

    # Get source language from the user
    while True:
        speak("Enter Source Language")
      
        source_language = input("Enter the source language: ").lower()
        if source_language not in language_codes:
            speak("Invalid source language ")
            print("Invalid source language. Please choose from the supported languages.")
        else:
            source_language_code = language_codes[source_language]
            break

    # Get target language from the user
    while True:
        speak("enter target language")
        target_language = input("Enter the target language: ").lower()
        if target_language not in language_codes:
            speak("invalid target language")
            print("Invalid target language. Please choose from the supported languages.")
        else:
            target_language_code = language_codes[target_language]
            break

    # Get text to translate from the user
    text_to_translate = input("Enter the text to translate: ")

    # Translate the text
    translation_url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={source_language_code}&tl={target_language_code}&dt=t&q={text_to_translate}"
    response = requests.get(translation_url)

    # Parse the translation from the response
    translated_text = response.json()[0][0][0]

    # Display the translated text
    speak("Your Text is "+str(translated_text))
    print(f"Translated Text ({source_language.capitalize()} to {target_language.capitalize()}): {translated_text}")


if __name__ == '__main__':
    input_method = get_input()

    while True:
        if input_method == "keyboard":
            statement = input("Please enter your command: ").lower()
        else:
            statement = listener()

        if statement == "none":
            continue
        elif "hi" in statement or "hello" in statement or "how are you" in statement:
            print("Hi boss .. ")
            speak("Hi Boss .. ")
        elif "close" in statement or "bye" in statement or "ok bye" in statement:
            print("Bye Boss... will see you later..")
            speak("Bye Boss... will see you later..")
            break
        elif "translate" in statement or "translator" in statement:
            translate_text()        
        elif "open youtube" in statement or "youtube" in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("YouTube is Opening Now Wait ...")
            time.sleep(5)
        elif "open whatsapp" in statement or "whatsapp" in statement:
            webbrowser.open_new_tab("https://webwhatsapp.com")
            speak("WhatsApp Is Opening Now Please Wait...")
            time.sleep(5)
        elif "open FaceBook" in statement or "FaceBook" in statement:
            webbrowser.open_new_tab("https://facebook.com")
            speak("WhatsApp Is Opening Now Please Wait...")
            time.sleep(5)
        elif "open Instagram" in statement or "Instagram" in statement:
            webbrowser.open_new_tab("https://instagram.com")
            speak("WhatsApp Is Opening Now Please Wait...")
            time.sleep(5)
        elif "news" in statement or "Today News" in statement:
            webbrowser.open_new_tab("https://timesofindia.indiatimes.com/")
            speak("Wait .. Today News Is Updatiing...")
            time.sleep(5)
        elif "Age Calc" in statement or "age finder" in statement:
            speak("Enter Your Year")
            year = int(input("Enter Your Year  =   "))
            age = 2024-year
            speak("Your Age Is "+str(age))
            print("Your Age is " ,age)
        
       
