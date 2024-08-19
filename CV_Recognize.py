# import cv2
# import os
# import pyttsx3
# import sqlite3
# import sys
# import subprocess

# # Initialize video capture
# video = cv2.VideoCapture(0)

# # Define paths
# haar_cascade_path = "haarcascade_frontalface_default.xml"
# trainer_path = "Trainer.yml"
# db_path = "images.db"

# # Check if Haar cascade file exists
# if not os.path.exists(haar_cascade_path):
#     raise FileNotFoundError(f"Haar cascade file not found: {haar_cascade_path}")

# # Check if Trainer file exists
# if not os.path.exists(trainer_path):
#     raise FileNotFoundError(f"Trainer file not found: {trainer_path}")

# # Load Haar cascade for face detection
# facedetect = cv2.CascadeClassifier(haar_cascade_path)

# # Load LBPH face recognizer and trained model
# recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer.read(trainer_path)

# # Initialize text-to-speech engine
# engine = pyttsx3.init()

# # Function to create a mapping from IDs to names based on database entries
# def load_names_from_database(db_path):
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
#     cursor.execute("SELECT college_id, name FROM images")
#     rows = cursor.fetchall()
#     conn.close()

#     names = {}
#     for row in rows:
#         college_id, name = row
#         names[college_id] = name
#     return names

# # Load names from database
# names = load_names_from_database(db_path)

# # To keep track of already greeted people
# greeted = set()

# while True:
#     ret, frame = video.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = facedetect.detectMultiScale(gray, 1.3, 5, minSize=(30, 30))

#     for (x, y, w, h) in faces:
#         serial, conf = recognizer.predict(gray[y:y+h, x:x+w])
#         if conf < 50:  # Lower confidence means better match
#             name = names.get(serial, "Unknown")
#             color = (0, 255, 0) if name != "Unknown" else (255, 0, 0)
            
#             if name != "Unknown":
#                 # Greet the recognized person
#                 greeting_text = f"Hello, {name}, how are you?"
#                 print(greeting_text)
#                 engine.say(greeting_text)
#                 engine.runAndWait()

#                 # Terminate the face recognition program
#                 video.release()
#                 cv2.destroyAllWindows()

#                 # Run the AI Assistant program
#                 subprocess.Popen(['python', 'final1.py'])  # Adjust the path as needed

#                 # Exit the current program
#                 sys.exit()
            
#         else:
#             name = "Unknown"
#             color = (255, 0, 0)  # Ensure the color is red for unknown faces
#             greeting_text = "Hi, how can I help you?"
#             print(greeting_text)
#             engine.say(greeting_text)
#             engine.runAndWait()

#         cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
#         cv2.rectangle(frame, (x, y - 40), (x + w, y), color, -1)
#         cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

#     cv2.imshow("Frame", frame)

#     k = cv2.waitKey(1)
#     if k == ord("q"):
#         break

# video.release()
# cv2.destroyAllWindows()
# print("Program Ended")


import cv2
import os
import pyttsx3
import sqlite3
import sys
import subprocess

# Initialize video capture
video = cv2.VideoCapture(0)

# Define paths
haar_cascade_path = "haarcascade_frontalface_default.xml"
trainer_path = "Trainer.yml"
db_path = "images.db"

# Check if Haar cascade file exists
if not os.path.exists(haar_cascade_path):
    raise FileNotFoundError(f"Haar cascade file not found: {haar_cascade_path}")

# Check if Trainer file exists
if not os.path.exists(trainer_path):
    raise FileNotFoundError(f"Trainer file not found: {trainer_path}")

# Load Haar cascade for face detection
facedetect = cv2.CascadeClassifier(haar_cascade_path)

# Load LBPH face recognizer and trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(trainer_path)

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to create a mapping from IDs to names based on database entries
def load_names_from_database(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT college_id, name FROM images")
    rows = cursor.fetchall()
    conn.close()

    names = {}
    for row in rows:
        college_id, name = row
        names[college_id] = name
    return names

# Load names from database
names = load_names_from_database(db_path)

# To keep track of already greeted people
greeted = set()

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        serial, conf = recognizer.predict(gray[y:y+h, x:x+w])
        if conf < 50:  # Lower confidence means better match
            name = names.get(serial, "Unknown")
            color = (0, 255, 0) if name != "Unknown" else (255, 0, 0)
            
            if name != "Unknown":
                # Greet the recognized person
                greeting_text = f"Hello, {name}, I hope you are having a good time?"
                print(greeting_text)
                engine.say(greeting_text)
                engine.runAndWait()

                # Terminate the face recognition program
                video.release()
                cv2.destroyAllWindows()

                # Run the AI Assistant program
                subprocess.Popen(['python', 'app.py'])  # Adjust the path as needed

                # Exit the current program
                sys.exit()
            
        else:
            name = "Unknown"
            color = (255, 0, 0)  # Ensure the color is red for unknown faces
            greeting_text = "Hi, how can I help you?"
            print(greeting_text)
            engine.say(greeting_text)
            engine.runAndWait()

        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.rectangle(frame, (x, y - 40), (x + w, y), color, -1)
        cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow("Frame", frame)

    k = cv2.waitKey(1)
    if k == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
print("Program Ended")

















