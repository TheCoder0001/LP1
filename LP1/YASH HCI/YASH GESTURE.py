import cv2
from deepface import DeepFace

# Initialize camera
cap = cv2.VideoCapture(0)
print("Camera started... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Detect emotions using DeepFace
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']

        # Display emotion on the screen
        cv2.putText(frame, f"Emotion: {emotion}", (50, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    except Exception as e:
        cv2.putText(frame, "No face detected", (50, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    # Show the video frame
    cv2.imshow("Emotion Recognition - HCI Project", frame)
    
    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
