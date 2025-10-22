#train_yolov8m.py

from ultralytics import YOLO
import sys

def train_yolov8m():
    # 로그 파일 열기
    log_file = open("train_log.txt", "w", encoding="utf-8")
    sys.stdout = log_file
    sys.stderr = log_file  # 에러 로그도 저장

    # 모델 학습
    model = YOLO("yolov8m.yaml")
    model.train(
        data="C:/Users/User/Desktop/test_merge4m/data.yaml",
        epochs=180,
        imgsz=640,
        patience=20,

        degrees=10,
        translate=0.1,
        scale=0.5,
        shear=2.0,
        mosaic=1.0,
        mixup=0.2,

        name="yolov8m_augmented_v3",
        exist_ok=True
    )

    # 로그 파일 닫기
    log_file.close()

if __name__ == "__main__":
    train_yolov8m()