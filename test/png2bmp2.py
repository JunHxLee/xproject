import argparse
from PIL import Image
import os
import glob

def convert_png_to_32bit_bmp(input_png_path, output_bmp_path):
    # PNG 이미지 열기
    with Image.open(input_png_path) as img:
        # RGBA 모드 확인 또는 변환
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # 32비트 BMP로 저장
        img.save(output_bmp_path, format='BMP')
        print(f"이미지가 32비트 BMP로 저장되었습니다: {output_bmp_path}")

def main():
    # 명령줄 인자 파서 설정
    parser = argparse.ArgumentParser(description="PNG 이미지를 32비트 BMP로 일괄 변환합니다.")
    parser.add_argument("input_pattern", help="입력 PNG 파일 경로 패턴 (예: 'input_dir/*.png')")
    parser.add_argument("output_directory", help="출력 BMP 파일을 저장할 디렉토리")
    
    # 인자 파싱
    args = parser.parse_args()

    # glob를 사용해 파일 패턴에 맞는 파일 리스트 가져오기
    input_files = glob.glob(args.input_pattern, recursive=True)
    if not input_files:
        print(f"지정된 패턴에 맞는 파일이 없습니다: {args.input_pattern}")
        return

    # 출력 디렉토리 확인 및 생성
    output_dir = args.output_directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 각 파일 변환
    for input_file in input_files:
        # 출력 파일 이름 생성
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = os.path.join(output_dir, f"{base_name}.bmp")
        
        # 변환 실행
        convert_png_to_32bit_bmp(input_file, output_file)

if __name__ == "__main__":
    main()
