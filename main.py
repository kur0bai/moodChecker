import cv2
import cv2.data


class Functions:
    def test_device(self, source):
        """
        Check if the camera is available in device
        """
        capture = cv2.VideoCapture(source)
        if capture is None or not capture.isOpened():
            raise Exception(
                "Warning: Your device can't open the Camera, please check it.")

    def detect_emotion(self, face_img):
        face_path = "face.jpg"
        cv2.INWRITE(face_path, face_img)

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
                    self.detect_emotion(face_img)

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
