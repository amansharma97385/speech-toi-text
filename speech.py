import pyttsx3
import speech_recognition as sr
import pyfiglet

def sptext():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Haa bhai, sun raha hoon...")
        
        # Remove noise
        rec.adjust_for_ambient_noise(source)
        
        print("Sun le raha hoon kya bola tu...")
        audio = rec.listen(source)
        
        try:
            # Recognize speech using Google's speech recognition
            data = rec.recognize_google(audio)
            print("Sun liya: " + data)
            show_large_text(data)
        except sr.UnknownValueError:
            print("Kuch samajh nahi aaya")
            show_large_text("Error: Kuch samajh nahi aaya")
        except sr.RequestError as e:
            print(f"Error: {e}")
            show_large_text(f"Error: {e}")

def show_large_text(text):
    # Create large ASCII art text
    large_text = pyfiglet.figlet_format(text)
    print(large_text)

sptext()
