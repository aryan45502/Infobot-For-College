import cv2
import os
import sqlite3
import numpy as np

def create_table():
    conn = sqlite3.connect('images.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS images (
            id INTEGER PRIMARY KEY,
            college_id INTEGER,
            name TEXT,
            image BLOB
        )
    ''')
    conn.commit()
    conn.close()

def convert_to_binary(image):
    return cv2.imencode('.jpg', image)[1].tobytes()

def insert_image(college_id, name, image):
    conn = sqlite3.connect('images.db')
    cursor = conn.cursor()
    
    binary_image = convert_to_binary(image)
    cursor.execute('''
        INSERT INTO images (college_id, name, image) VALUES (?, ?, ?)
    ''', (college_id, name, binary_image))
    
    conn.commit()
    conn.close()


def collect_dataset(college_id, name):
    # Ensure the datasets directory exists
    if not os.path.exists('datasets'):
        os.makedirs('datasets')

    video = cv2.VideoCapture(0)
    facedetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    count = 0

    # Check for existing files with the same college ID
    conn = sqlite3.connect('images.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM images WHERE college_id = ?', (college_id,))
    data = cursor.fetchall()
    conn.close()

    if data:
        print("College ID already taken. Please enter a different College ID.")
        return None

    while True:
        ret, frame = video.read()
        if not ret:
            print("Failed to capture frame")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = facedetect.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            face = gray[y:y+h, x:x+w]
            filename = f'{name}_{college_id}_{count}.jpg'
            filepath = f'datasets/{filename}'
            cv2.imwrite(filepath, face)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 2)
            cv2.putText(frame, f'Images Captured: {count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            
            # Insert image into the database
            insert_image(college_id, name, face)

        cv2.imshow("Frame", frame)

        k = cv2.waitKey(1)
        if count >= 200 or k == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
    print("Dataset Collection Done..................")
    return True

if __name__ == "__main__":
    create_table()
    while True:
        try:
            college_id = int(input("Enter Your College ID  "))
            name = input("Enter Your Name: ")
            if collect_dataset(college_id, name) is not None:
                break  # Break the loop if dataset collection was successful
        except ValueError:
            print("Please enter a valid integer for College ID.")

    # Example usage to delete images for a specific college ID
 