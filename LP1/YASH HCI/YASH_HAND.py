import cv2
import mediapipe as mp

# Initialize mediapipe hand detection
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Start webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Failed to access camera")
        break

    # Flip the image for natural viewing
    image = cv2.flip(image, 1)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process image and find hands
    result = hands.process(rgb_image)

    # Draw landmarks
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Example: simple gesture logic for thumb detection
            landmarks = hand_landmarks.landmark
            thumb_tip = landmarks[4]
            index_tip = landmarks[8]

            # Example condition: if thumb is above index -> "Thumbs Up"
            if thumb_tip.y < index_tip.y:
                cv2.putText(image, "👍 Thumbs Up Detected", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
            else:
                cv2.putText(image, "✋ Hand Detected", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 3)

    cv2.imshow("Hand Gesture Control - HCI Project", image)

    # Quit with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
