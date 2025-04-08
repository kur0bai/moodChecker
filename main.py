import os
import cv2
import cv2.data
from deepface import DeepFace


class dimensions:
    x = 0,
    y = 0,
    h = 0,
    w = 0


class Functions:
    def test_device(self, source):
        """
        Check if the camera is available in device
        """
        capture = cv2.VideoCapture(source)
        if capture is None or not capture.isOpened():
            raise Exception(
                "Warning: Your device can't open the Camera, please check it.")

    def detect_emotion(self, face_img, frame, dimensions):
        try:
            face_path = "face.jpg"
            cv2.imwrite(face_path, face_img)

            # analyze
            analysis = DeepFace.analyze(img_path=face_path, actions=[
                                        'emotion'], enforce_detection=False)
            emotion = analysis[0]['dominant_emotion']

            name = 'Subject'
            label = f"{name} is {emotion}" if name != "Unknown" else f"{emotion}"
            cv2.rectangle(frame, (dimensions["x"], dimensions["y"]), (dimensions["x"] +
                                                                      dimensions["w"], dimensions["y"] + dimensions["h"]), (0, 255, 0), 2)

            cv2.putText(frame, label, (dimensions["x"], dimensions["y"] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

            # recon
            """ name = "Unknown"
            db_path = "faces"
            if os.path.exists(db_path):
                result = DeepFace.find(
                    img_path=face_path, db_path=db_path, enforce_detection=False)
                if len(result) > 0 and not result[0].empty:
                    matched_path = result[0].iloc[0]['identity']
                    name = os.path.basename(
                        os.path.dirname(matched_path))

                    # Mostrar info en pantalla
                    label = f"{name} - {emotion}" if name != "Unknown" else f"{emotion}"
                    cv2.rectangle(frame, (dimensions["x"], dimensions["y"]), (dimensions["x"] +
                                dimensions["width"], dimensions["y"] + dimensions["height"]), (0, 255, 0), 2)
                    cv2.putText(frame, label, (dimensions["x"], dimensions["y"] - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2) """

        except Exception as ex:
            print(f'Something went wrong: {ex}')

    def start_capturing(self):
        """
        Start to capturing the faces with the camera
        """
        try:
            face_cascade = cv2.CascadeClassifier(
                cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            self.test_device(0)

            # Start capturing
            capture = cv2.VideoCapture(0)

            while True:
                ret, frame = capture.read()
                if not ret:
                    break

                gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(
                    gray_scale, scaleFactor=1.3, minSize=(30, 30), minNeighbors=5)

                # Draw circles around the finded faces xd
                for (x, y, width, height) in faces:
                    face_img = frame[y:y+height, x:x + width]
                    self.detect_emotion(
                        face_img, frame, {"x": x, "y": y, "h": height, "w": width})

                    cv2.rectangle(frame, (x, y), (x + width,
                                  y + height), (0, 255, 0), 2)

                cv2.imshow('Face Detector', frame)

                # Wait for quit word to leave
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            capture.release()
            cv2.destroyAllWindows()
        except Exception as ex:
            print(f'Ups, something went wrong: {ex}')


if __name__ == '__main__':
    functions = Functions()
    functions.start_capturing()
