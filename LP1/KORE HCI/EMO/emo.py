import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # hide TensorFlow warnings

from deepface import DeepFace
import cv2

# Image path
img_path = "C:/Users/Kanchan Hukare/Downloads/HCI/emo/2.jpeg"

if not os.path.exists(img_path):
    print(f"❌ Image not found at: {img_path}")
    exit()

# Analyze emotions
analysis = DeepFace.analyze(
    img_path=img_path,
    actions=['emotion'],
    enforce_detection=False
)

# Extract emotions
emotions = analysis[0]['emotion']

# Find dominant
dominant_emotion = max(emotions, key=emotions.get)
dominant_score = emotions[dominant_emotion]

# Load image
image = cv2.imread(img_path)

# Resize if too large
max_width = 600
height, width = image.shape[:2]
if width > max_width:
    scale = max_width / width
    new_w = int(width * scale)
    new_h = int(height * scale)
    image = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)

# Set starting position for text
x, y0 = 10, 30
dy = 30  # vertical space between lines
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.8
color = (0, 255, 0)  # Green
thickness = 2

# Overlay emotions on image
for i, (emo, score) in enumerate(emotions.items()):
    label = f"{emo.upper()}: {score:.2f}%"
    if emo == dominant_emotion:
        label += " (Dominant)"
        text_color = (0, 0, 255)  # Red for dominant
    else:
        text_color = color
    y = y0 + i * dy
    cv2.putText(image, label, (x, y), font, font_scale, text_color, thickness, cv2.LINE_AA)

# Show image with emotions
cv2.imshow("Emotion Analysis", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Optional: also print result in console
print("\n=== Emotion Analysis Result ===")
for emo, score in emotions.items():
    if emo == dominant_emotion:
        print(f" {emo.upper()} : {score:.2f}%   (Dominant)")
    else:
        print(f"   {emo.capitalize()} : {score:.2f}%")



























# --Ubuntu setup commands for DeepFace emotion detection
# ---------------------------------------------------
# --Update system
# sudo apt update && sudo apt upgrade -y

# --Install Python 3 and pip
# sudo apt install -y python3 python3-pip python3-dev

# --Upgrade pip
# sudo pip3 install --upgrade pip

# --Install required Python packages (NumPy <2, TensorFlow, OpenCV, DeepFace)
# sudo pip3 install "numpy<2" --upgrade
# sudo pip3 install tensorflow==2.14.0
# sudo pip3 install opencv-python
# sudo pip3 install deepface
# sudo pip3 install matplotlib pandas tqdm gdown

# --Install Ubuntu libraries for OpenCV/DeepFace
# sudo apt install -y ffmpeg libsm6 libxext6

# --Verify installations
# python3 -c "import numpy; import tensorflow as tf; from deepface import DeepFace; print('All imports OK')"

# --Run your script
# python3 emotion.py

