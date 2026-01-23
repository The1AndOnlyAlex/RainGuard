import cv2
from ultralytics import YOLO
import time

print("--- STARTING VISION SYSTEM ---")

# 1. Load the AI Brain
print("1. Loading AI Model... (This might take a sec)")
try:
    model = YOLO('yolov8n.pt')
    print("   > Model Loaded Successfully.")
except Exception as e:
    print(f"   > ERROR Loading Model: {e}")
    exit()

# 2. Try to Open the Camera (Trying index 0 first, then 1)
camera_index = 0
print(f"2. Attempting to open Camera Index {camera_index}...")
cap = cv2.VideoCapture(camera_index)

# Mac Specific: Allow warm up time
time.sleep(1.5)

if not cap.isOpened():
    print("   > Failed to open Camera 0. Trying Camera 1...")
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print("   > CRITICAL ERROR: Could not open any camera.")
        print("   > FIX: Check System Settings > Privacy > Camera")
        exit()

print(f"   > Camera Open! Resolution: {cap.get(3)}x{cap.get(4)}")

print("3. Starting Video Loop. Press 'q' to quit.")
frame_count = 0

while True:
    # Read a frame
    success, frame = cap.read()
    
    if not success:
        print("   > Error: Camera is open but sending empty frames.")
        print("   > NOTE: This usually means permissions are blocked.")
        break

    frame_count += 1
    # Print a "heartbeat" every 30 frames so you know it's running
    if frame_count % 30 == 0:
        print(f"   > Processing frame {frame_count}...")

    # AI Processing
    results = model(frame, stream=True)

    # Draw boxes
    for result in results:
        annotated_frame = result.plot()
        cv2.imshow("Mark 1 Vision (Press q to exit)", annotated_frame)

    # Force Mac to update the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("   > Quit signal received.")
        break

cap.release()
cv2.destroyAllWindows()
print("--- END OF PROGRAM ---")
