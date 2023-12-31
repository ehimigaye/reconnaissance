import cv2
import streamlit as st

face_cascade = cv2.CascadeClassifier('C:/Users/djebb/Downloads/haarcascade_frontalface_default.xml')

def detect_faces():

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('Face Detection using Viola-Jones Algorithm', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    def app():
        st.title("Face Detection using Viola-Jones Algorithm")
        st.write("Press the button below to start detecting faces from your webcam")
        # Add a button to start detecting faces
        if st.button("Detect Faces"):
            # Call the detect_faces function
            detect_faces()
    if __name__ == "__main__":
        app()