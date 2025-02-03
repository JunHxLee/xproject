from rembg import remove
from PIL import Image
import io

def remove_background(input_image_path, output_image_path):
    """
    이미지에서 배경을 제거하고 인물만 남기는 함수
    
    Args:
        input_image_path (str): 원본 이미지 파일 경로
        output_image_path (str): 배경 제거 후 저장할 PNG 파일 경로
    """
    try:
        # 이미지 열기
        with open(input_image_path, "rb") as input_file:
            input_image = input_file.read()
        
        # 배경 제거
        output_image = remove(input_image)
        
        # PNG 파일로 저장
        with open(output_image_path, "wb") as output_file:
            output_file.write(output_image)
        
        print(f"배경 제거 완료! 결과 파일: {output_image_path}")
    except Exception as e:
        print(f"에러 발생: {e}")

# 사용 예시
input_path = "/sdcard/Download/1.jpg"  # 원본 이미지 경로
output_path = "/sdcard/Download/1.png"  # 결과 이미지 경로
remove_background(input_path, output_path)
