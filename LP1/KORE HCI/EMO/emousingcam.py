import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # hide TensorFlow warnings

from deepface import DeepFace
import cv2

# Initialize webcam (0 = default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Could not open webcam")
    exit()

# Settings for text overlay
x, y0 = 10, 30
dy = 30
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.8
color = (0, 255, 0)  # green
thickness = 2

print("📷 Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    # Resize if too large
    max_width = 600
    height, width = frame.shape[:2]
    if width > max_width:
        scale = max_width / width
        new_w = int(width * scale)
        new_h = int(height * scale)
        frame = cv2.resize(frame, (new_w, new_h), interpolation=cv2.INTER_AREA)

    try:
        # Analyze emotions (enforce_detection=False for faster testing)
        analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        emotions = analysis[0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        dominant_score = emotions[dominant_emotion]

        # Overlay emotions on frame
        for i, (emo, score) in enumerate(emotions.items()):
            label = f"{emo.upper()}: {score:.2f}%"
            if emo == dominant_emotion:
                label += " (Dominant)"
                text_color = (0, 0, 255)  # red for dominant
            else:
                text_color = color
            y = y0 + i * dy
            cv2.putText(frame, label, (x, y), font, font_scale, text_color, thickness, cv2.LINE_AA)

    except Exception as e:
        cv2.putText(frame, "No face detected", (x, y0), font, font_scale, (0,0,255), 2, cv2.LINE_AA)

    # Show webcam frame
    cv2.imshow("Webcam Emotion Detection", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
