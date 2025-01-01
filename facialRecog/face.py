import threading
import cv2
import os
from deepface import DeepFace

# Initialize webcam
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

count = 0
isMatch = False
matched_person = None

people_dir = "people"

reference_images = []
reference_names = []

for file_name in os.listdir(people_dir):
    file_path = os.path.join(people_dir, file_name)
    if os.path.isfile(file_path):
        name = os.path.splitext(file_name)[0].replace("_", " ")
        reference_images.append(cv2.imread(file_path))
        reference_names.append(name)

def check_face(frame):

    global isMatch, matched_person
    try:
        for ref_img, name in zip(reference_images, reference_names):
            if DeepFace.verify(frame, ref_img.copy())['verified']:
                isMatch = True
                matched_person = name
                return

        isMatch = False
        matched_person = None
    except Exception as e:
        print(f"Error during face verification: {e}")
        isMatch = False
        matched_person = None

while True:
    ret, frame = capture.read()

    if ret:
        if count % 1000 == 0:  # Check every 1000 frames
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except Exception as e:
                print(f"Error starting thread: {e}")
        count += 1

        if isMatch:
            match_text = f"Matched: {matched_person}"
            cv2.putText(frame, match_text, (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "No Match Found", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()
