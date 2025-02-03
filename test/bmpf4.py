import argparse
import struct

def get_bmp_bit_depth(file_path):
    with open(file_path, 'rb') as f:
        # BMP 헤더에서 비트 깊이는 28번째 바이트부터 2바이트에 저장
        f.seek(28)  # 28번째 위치로 이동
        bit_depth = struct.unpack('<H', f.read(2))[0]  # 2바이트 읽어서 해석
    return bit_depth

def main():
    # 명령줄 인자 파서 설정
    parser = argparse.ArgumentParser(description="BMP 파일의 비트 깊이를 확인합니다.")
    parser.add_argument("file_path", help="비트 깊이를 확인할 BMP 파일 경로")
    args = parser.parse_args()

    # 비트 깊이 확인
    bit_depth = get_bmp_bit_depth(args.file_path)
    print(f"BMP 파일의 비트 깊이: {bit_depth} bit")

if __name__ == "__main__":
    main()
