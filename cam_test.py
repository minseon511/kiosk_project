#cam_test.py

import cv2
from ultralytics import YOLO

# 모델 로드
model = YOLO("C:/Users/bacde/Desktop/yolov8s_augmented_v4/weights/best.pt")

# 웹캠 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

print("웹캠이 열렸습니다. ESC 키를 눌러 종료하세요.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("프레임을 읽을 수 없습니다.")
            break

        # YOLOv8 추론
        results = model(frame)

        # 결과 시각화
        annotated_frame = results[0].plot()

        # 출력
        cv2.imshow("YOLOv8 Real-Time Detection", annotated_frame)

        # ESC 키로 종료
        if cv2.waitKey(1) & 0xFF == 27:
            print("종료합니다.")
            break

finally:
    cap.release()
    cv2.destroyAllWindows()