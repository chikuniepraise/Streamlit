# pip install SpeechRecognition
# pip install pipwin, pipwin install pyaudio, 
#mac: pip install pyaudio

import streamlit as st
import speech_recognition as sr

def transcribe_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Speak now...")
        audio_text = r.listen(source)
        st.info("Transcribing...")

        try:
            text = r.recognize_google(audio_text)
            return text
        except:
            return "Sorry, I did not get that."
        
        
def main():
    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")

    if st.button("Start Recording"):
        text = transcribe_speech()
        st.write("Transcription: ", text)
if __name__ == "__main__":
    main()