import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=1,
    min_detection_confidence=0.3
)

img_path = r"C:\Users\Kanchan Hukare\Downloads\HCI\peace.jpeg"  # change as needed
image = cv2.imread(img_path)

if image is None:
    print("❌ Image not found! Check path:", img_path)
    exit()

image = cv2.resize(image, (640, 480))
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
result = hands.process(img_rgb)

gesture = "No hand detected"

if result.multi_hand_landmarks:
    for handLms in result.multi_hand_landmarks:
        mp_draw.draw_landmarks(image, handLms, mp_hands.HAND_CONNECTIONS)
        lm = handLms.landmark

        # Determine handedness (left/right)
        h, w, _ = image.shape
        cx_thumb = lm[4].x * w
        cx_pinky = lm[20].x * w
        is_right = cx_thumb < cx_pinky  # thumb on left side => right hand

        # Finger states
        finger_tips = [8, 12, 16, 20]
        finger_pips = [6, 10, 14, 18]
        fingers_open = [lm[tip].y < lm[pip].y for tip, pip in zip(finger_tips, finger_pips)]

        # Thumb open logic (depends on hand)
        if is_right:
            thumb_open = lm[4].x < lm[3].x
        else:
            thumb_open = lm[4].x > lm[3].x

        # Gesture classification
        if all(not f for f in fingers_open) and not thumb_open:
            gesture = "Fist ✊"
        elif all(fingers_open) and thumb_open:
            gesture = "Open Palm 🖐️"
        elif thumb_open and not any(fingers_open):
            # Additional check: thumb roughly vertical
            if abs(lm[4].y - lm[3].y) > abs(lm[4].x - lm[3].x):
                gesture = "Thumbs Up 👍"
            else:
                gesture = "Thumbs Side 👈👉"
        elif fingers_open[0] and fingers_open[1] and not any(fingers_open[2:]):
            gesture = "Peace ✌️"
        else:
            gesture = "Unknown / Other 🤔"

        cv2.putText(image, f'Gesture: {gesture}', (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

else:
    cv2.putText(image, gesture, (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

cv2.imshow("Hand Gesture", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
