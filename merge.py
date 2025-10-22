#merge.py

import os
import shutil
from glob import glob

# 병합할 데이터셋 폴더들 (각각 YOLO 구조여야 함)
dataset_folders = [
    "C:/Users/User/Desktop/pepper.v1i.yolov8",
    "C:/Users/User/Desktop/soybean paste.v1i.yolov8",
    "C:/Users/User/Desktop/cleanbag.v3i.yolov8",
    "C:/Users/User/Desktop/downy.v1i.yolov8",
    "C:/Users/User/Desktop/homestar.v1i.yolov8"
]

# 병합 대상 최종 경로
merged_root = "C:/Users/User/Desktop/test_merge4m"
splits = ['train', 'valid', 'test']
subfolders = ['images', 'labels']

# 모든 폴더 생성
for split in splits:
    for sub in subfolders:
        os.makedirs(os.path.join(merged_root, split, sub), exist_ok=True)

# 병합 작업
for dataset in dataset_folders:
    for split in splits:
        for sub in subfolders:
            src_dir = os.path.join(dataset, split, sub)
            dst_dir = os.path.join(merged_root, split, sub)

            if not os.path.exists(src_dir):
                continue  # 없는 경우 건너뜀

            for filepath in glob(os.path.join(src_dir, '*')):
                filename = os.path.basename(filepath)

                # 중복 방지를 위해 접두사 붙이기 (폴더 이름 + 원래 파일명)
                prefix = os.path.basename(dataset)
                new_filename = f"{prefix}_{filename}"
                dst_path = os.path.join(dst_dir, new_filename)

                shutil.copy2(filepath, dst_path)