import argparse
from PIL import Image

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
    parser = argparse.ArgumentParser(description="PNG 이미지를 32비트 BMP로 변환합니다.")
    parser.add_argument("input_png", help="입력 PNG 파일 경로")
    parser.add_argument("output_bmp", help="출력 BMP 파일 경로")
    
    # 인자 파싱
    args = parser.parse_args()
    
    # 변환 함수 호출
    convert_png_to_32bit_bmp(args.input_png, args.output_bmp)

if __name__ == "__main__":
    main()
