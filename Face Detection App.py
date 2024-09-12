# pip install opencv-python

import cv2 # OpenCV library, used for image processing and computer vision tasks.
import streamlit as st
import os #provides functions to interact with the operating system, such as file path manipulation.

xml_path = os.path.join(os.getcwd(), 'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(xml_path)

if face_cascade.empty():
    raise IOError("Failed to load haarcascade_frontalface_default.xml file.")

def detect_faces():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #  DirectShow backend (multimedia framework and API provided by Microsoft)
    if not cap.isOpened():
        st.error("Could not open webcam")
        return
    stframe = st.empty()  
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to grab a frame")
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) #BGR green, 2-border thickness
        stframe.image(frame, channels="BGR")
    cap.release()
    cv2.destroyAllWindows()


def app():
    st.title("Face Detection using Viola-Jones Algorithm")
    st.write("Press the button below to start detecting faces from your webcam")
    if st.button("Detect Faces"):
        detect_faces()

if __name__ == "__main__":
    app()

