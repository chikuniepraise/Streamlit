import cv2
import streamlit as st
import os

xml_path = os.path.join(os.getcwd(), 'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(xml_path)

if face_cascade.empty():
    raise IOError("Failed to load haarcascade_frontalface_default.xml file.")

def detect_faces():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        st.error("Could not open webcam")
        return

    stframe = st.empty()
    run_detection = True
    
    while run_detection:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to grab a frame")
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) # BGR green, 2-border thickness
        stframe.image(frame, channels="BGR")

        # Check if the stop button is pressed
        if not st.session_state.detecting_faces:
            run_detection = False
    
    cap.release()
    cv2.destroyAllWindows()

def app():
    st.title("Face Detection using Viola-Jones Algorithm")
    st.write("Press the button below to start detecting faces from your webcam")

    if 'detecting_faces' not in st.session_state:
        st.session_state.detecting_faces = False

    if st.button("Start Detection"):
        st.session_state.detecting_faces = True
        detect_faces()
    if st.button("Stop Detection"):
        st.session_state.detecting_faces = False

if __name__ == "__main__":
    app()
