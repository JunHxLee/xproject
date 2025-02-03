import struct

def get_bmp_bit_depth(file_path):
    with open(file_path, 'rb') as f:
        f.seek(28)  # BMP 헤더에서 비트 깊이는 28번째 바이트에 저장
        bit_depth = struct.unpack('<H', f.read(2))[0]  # 2바이트 읽어서 언패킹
    return bit_depth

# 사용 예:
file_path = '/sdcard/Download/navercafe/1.bmp'  # BMP 파일 경로
bit_depth = get_bmp_bit_depth(file_path)
print(f"BMP 파일의 비트 깊이: {bit_depth} bit")
