import cv2
from ultralytics import YOLO
import math

# Load the Pose Estimation Model
# Note: The first time you run this, it will download 'yolov8n-pose.pt'
model = YOLO('yolov8n-pose.pt')

# --- TEST MODE ---
# Option A: Use live Webcam (0)
# source = 0 
# Option B: Use a video file (Replace with your file name)
source = 'test_walk.mp4' 

cap = cv2.VideoCapture(source)

# Drone Settings
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
CENTER_X = FRAME_WIDTH // 2
DEADZONE = 50  # Pixels

print("--- POSE TRACKING SYSTEM ENGAGED ---")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("End of video or camera error.")
        break

    # Resize for consistency
    frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))

    # Run YOLO Pose
    # stream=True makes it faster
    results = model(frame, stream=True, verbose=False)

    # Draw the "Drone Center" crosshair
    cv2.circle(frame, (CENTER_X, FRAME_HEIGHT//2), 5, (0, 0, 0), -1)
    cv2.line(frame, (CENTER_X, 0), (CENTER_X, FRAME_HEIGHT), (0, 0, 0), 1)

    for result in results:
        # Check if any keypoints were detected
        if result.keypoints is not None:
            # Get the keypoints (x, y) for all detected people
            # confs is the confidence score
            keypoints = result.keypoints.xy.cpu().numpy()
            
            for person_idx, person_kpts in enumerate(keypoints):
                # YOLO Pose Keypoint Map:
                # 0: Nose, 1-2: Eyes, 3-4: Ears, 5: Left Shoulder, 6: Right Shoulder
                
                # We want the SHOULDERS (Indices 5 and 6)
                left_shoulder = person_kpts[5]
                right_shoulder = person_kpts[6]
                
                # Check if both shoulders were detected (coordinates not [0,0])
                if left_shoulder[0] > 0 and right_shoulder[0] > 0:
                    
                    # Calculate the MIDPOINT between shoulders
                    target_x = int((left_shoulder[0] + right_shoulder[0]) / 2)
                    target_y = int((left_shoulder[1] + right_shoulder[1]) / 2)

                    # Draw the "Skeleton" Target
                    cv2.line(frame, (int(left_shoulder[0]), int(left_shoulder[1])), 
                                  (int(right_shoulder[0]), int(right_shoulder[1])), (0, 255, 0), 3)
                    cv2.circle(frame, (target_x, target_y), 8, (0, 0, 255), -1)
                    
                    # --- FLIGHT CONTROL LOGIC ---
                    error_x = target_x - CENTER_X
                    
                    cmd = "HOLD"
                    color = (0, 255, 0)
                    
                    if error_x > DEADZONE:
                        cmd = ">> YAW RIGHT >>"
                        color = (0, 0, 255)
                    elif error_x < -DEADZONE:
                        cmd = "<< YAW LEFT <<"
                        color = (0, 0, 255)
                        
                    # Display Info
                    cv2.putText(frame, f"TARGET: {cmd}", (target_x - 50, target_y - 20), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
                    cv2.putText(frame, f"ERR: {error_x}", (10, 30), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

    cv2.imshow("Mark 1 - Pose Tracking", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()