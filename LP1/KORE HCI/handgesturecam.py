import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.6, min_tracking_confidence=0.6)

def classify_gesture(lm):
    # Finger tips and pip joints
    tips = [4, 8, 12, 16, 20]

    fingers = []

    # ----- Thumb -----
    # Detect left/right hand automatically
    thumb_is_open = lm[4].x < lm[3].x if lm[17].x < lm[5].x else lm[4].x > lm[3].x
    fingers.append(thumb_is_open)

    # ----- 4 Fingers -----
    for tip, base in zip([8, 12, 16, 20], [6, 10, 14, 18]):
        fingers.append(lm[tip].y < lm[base].y)

    # Pattern list
    f = fingers  # [Thumb, Index, Middle, Ring, Pinky]

    # ----- Gesture Classification -----
    if f == [True, False, False, False, False]:
        return "Thumbs Up 👍"

    elif f == [False, False, False, False, False]:
        return "Fist ✊"

    elif f == [True, True, True, True, True]:
        return "Open Palm 🖐️"

    elif f == [False, True, True, False, False]:
        return "Peace ✌️"

    elif f == [False, True, False, False, False]:
        return "One Finger ☝️"

    elif f == [False, True, False, False, True]:
        return "Pointing 👉"

    return "Unknown 🤔"

# ----- CAMERA LOOP -----
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    gesture_text = "Detecting..."

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        lm = hand.landmark

        # Draw landmarks
        mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

        # Classify gesture
        gesture_text = classify_gesture(lm)

    # Display text
    cv2.putText(frame, f"Gesture: {gesture_text}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 255, 0), 3)

    cv2.imshow("Hand Gesture Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
