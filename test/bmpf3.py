import argparse
from PIL import Image

def get_bmp_bit_depth(file_path):
    with Image.open(file_path) as img:
        return img.mode

def main():
    # 명령줄 인자 파서 설정
    parser = argparse.ArgumentParser(description="BMP 파일의 비트 깊이를 확인합니다.")
    parser.add_argument("file_path", help="비트 깊이를 확인할 BMP 파일 경로")
    args = parser.parse_args()

    # 비트 깊이 확인
    bit_depth_mode = get_bmp_bit_depth(args.file_path)

    # 비트 깊이 변환
    mode_to_bit_depth = {
        "1": 1,  # 흑백
        "L": 8,  # 그레이스케일
        "P": 8,  # 팔레트
        "RGB": 24,  # 컬러 (8비트 채널 * 3)
        "RGBA": 32,  # 컬러 + 알파 (8비트 채널 * 4)
    }
    bit_depth = mode_to_bit_depth.get(bit_depth_mode, "알 수 없음")
    print(f"BMP 파일의 비트 깊이: {bit_depth} bit")

if __name__ == "__main__":
    main()
