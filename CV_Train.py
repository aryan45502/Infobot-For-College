
import sqlite3
import numpy as np
from PIL import Image
import io
import cv2

# Initialize the LBPH face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Path to the SQLite database
db_path = "images.db"

def getImageID(db_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Query to retrieve all images and their associated college IDs
    cursor.execute("SELECT college_id, image FROM images")
    data = cursor.fetchall()
    
    faces = []
    ids = []
    
    for row in data:
        college_id = row[0]
        image_data = row[1]
        
        # Convert binary data to an image
        faceImage = Image.open(io.BytesIO(image_data)).convert('L')
        faceNP = np.array(faceImage)
        
        # Append the face data and ID to the respective lists
        faces.append(faceNP)
        ids.append(college_id)
        
        # Display the image being processed
        cv2.imshow("Training", faceNP)
        cv2.waitKey(1)
    
    conn.close()
    return ids, faces

# Train the recognizer using the images and IDs
try:
    IDs, facedata = getImageID(db_path)
    recognizer.train(facedata, np.array(IDs))
    recognizer.write("Trainer.yml")
    cv2.destroyAllWindows()
    print("Training Completed............")
except Exception as e:
    print(f"Error: {e}")
