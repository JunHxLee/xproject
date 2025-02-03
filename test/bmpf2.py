from PIL import Image

def get_bmp_bit_depth(file_path):
    with Image.open(file_path) as img:
        return img.mode

# 사용 예:
file_path = '/sdcard/Download/navercafe/1.bmp'  # BMP 파일 경로
bit_depth_mode = get_bmp_bit_depth(file_path)

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
