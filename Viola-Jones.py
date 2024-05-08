import cv2 # OpenCV
import tkinter as tk 
from tkinter import messagebox # Pop-up Window
import os # For dynamic path handling 

# VideoCapture class to handle webcam capture
class VideoCapture:
    def __init__(self):
        # Initialize the webcam capture
        self.cap = cv2.VideoCapture(1) # 0 -> Default camera 1
        if not self.cap.isOpened():
            raise Exception("\033[1;91mError: Could not access the webcam.\033[0m") # Error Message -> Webcam (access)
    
    def read_frame(self):
        # Read a frame from the webcam
        ret, frame = self.cap.read()
        if not ret:
            raise Exception("\033[1;91mError: Issue while capturing the video feed.\033[0m") # Error Message -> Webcam (whilst on)
        return frame

    def release(self):
        # Release the webcam when done
        self.cap.release()

# FaceDetector class (face, eye, and mouth detection)
class FaceDetector:
    def __init__(self, cascade_paths):
        # Initialize cascade classifiers for face, eyes, and mouth
        self.face_cascade, self.eye_cascade, self.mouth_cascade = [cv2.CascadeClassifier(path) for path in cascade_paths]

    def detect_faces_eyes_mouths(self, frame):
        # Convert the frame to grayscale for detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale image
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=25, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Red bounding boxes for FACES
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            # Adjust parameters for eye detection
            eyes = self.eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=37, minSize=(20, 20))

            for (ex, ey, ew, eh) in eyes:
                # Green bounding boxes for EYES
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            # Adjust parameters for mouth detection
            mouths = self.mouth_cascade.detectMultiScale(roi_gray, scaleFactor=1.3, minNeighbors=30, minSize=(40, 20))
            for (mx, my, mw, mh) in mouths:
                # Blue bounding boxes for MOUTHS
                cv2.rectangle(roi_color, (mx, my), (mx + mw, my + mh), (255, 0, 0), 2)
        return frame


# GUI class to manage the tkinter window (pop-up)
class GUI:
    def __init__(self, icon_path):
        # Initialize the tkinter window
        self.root = tk.Tk()
        self.root.withdraw()
        self.set_window_icon(icon_path)
        self.exit_confirmation_shown = False

    def set_window_icon(self, icon_path):
        try:
            # Create a PhotoImage object from the icon file
            icon_image = tk.PhotoImage(file=icon_path)
            # Set the window icon using the created PhotoImage object
            self.root.iconphoto(True, icon_image)
        except tk.TclError:
            print("\033[1;93mWarning: Icon image could not be set.\033[0m")



    def show_exit_confirmation(self):
        if not self.exit_confirmation_shown:
            # Display an exit confirmation dialog
            confirm_exit = messagebox.askquestion("Confirmation", "Are you sure you want to close the application?")
            if confirm_exit == "yes":
                self.exit_confirmation_shown = True
                self.root.destroy()

    def run(self):
        # Start the tkinter main loop
        self.root.mainloop()

# Main function to run the program
def main():
    # Dynamic path 
    current_directory = os.path.dirname(os.path.abspath(__file__)) 

    # CASCADES
    cascade_paths = [
        os.path.join(current_directory, 'haarcascade_frontalface_default.xml'),
        os.path.join(current_directory, 'haarcascade_eye.xml'),
        os.path.join(current_directory, 'haarcascade_mcs_mouth.xml')
    ]

    # ICON
    icon_path = os.path.join(current_directory, 'Icon.png')
    print(icon_path)
    video_capture = VideoCapture()
    face_detector = FaceDetector(cascade_paths)
    gui = GUI(icon_path)

    try:
        while True:
            frame = video_capture.read_frame()
            frame = face_detector.detect_faces_eyes_mouths(frame)
            cv2.imshow('VJ Detection', frame) # Title Window

            key = cv2.waitKey(1)
            # Exit Keybinds
            if key == 27 or key == ord('q') or key == ord('Q'):
                gui.show_exit_confirmation()
                if gui.exit_confirmation_shown:
                    break

    except Exception as e:
        print(f"\033[1;91mError: {e}\033[0m")

    finally:
        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()