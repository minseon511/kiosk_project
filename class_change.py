#class_change.py

#homestar의 train labels의 클래스 아이디를 4로 변경하는 코드
#파일 디렉토리와 클래스 아이디 숫자를 변경
import os

label_dir = "C:/Users/User/Desktop/homestar.v1i.yolov8/train/labels"

for filename in os.listdir(label_dir):
    if filename.endswith(".txt"):
        file_path = os.path.join(label_dir, filename)

        # 라벨 수정: class ID를 무조건 '4'로 변경
        with open(file_path, 'r') as f:
            lines = f.readlines()

        updated_lines = []
        for line in lines:
            parts = line.strip().split()
            if len(parts) >= 5:
                parts[0] = '4'  # 클래스 ID를 무조건 4로 설정
                updated_lines.append(" ".join(parts) + "\n")

        with open(file_path, 'w') as f:
            f.writelines(updated_lines)

print("모든 라벨의 클래스 ID를 4로 변경 완료!")