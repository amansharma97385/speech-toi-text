from flask import Flask, render_template, request
import speech_recognition as sr
import pyttsx3

app = Flask(__name__)

def sptext():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise
        rec.adjust_for_ambient_noise(source)

        print("Recording...")
        audio = rec.listen(source)

        try:
            # Recognize speech using Google's speech recognition
            data = rec.recognize_google(audio)
            print("Recognized: " + data)
            return data
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return "Could not understand the audio"
        except sr.RequestError as e:
            print(f"Error: {e}")
            return f"Error: {e}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize', methods=['POST'])
def recognize_speech():
    text = sptext()  # Call the speech recognition function
    return render_template('index.html', recognized_text=text)

if __name__ == '__main__':
    app.run(debug=True)
