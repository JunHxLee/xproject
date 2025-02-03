import struct

def read_bmp_info(file_name):
    try:
        with open(file_name, 'rb') as f:
            # BMP 파일의 헤더 읽기
            header = f.read(54)  # BMP 헤더는 54바이트

            # BMP 매직 넘버 확인 (BM으로 시작)
            if header[:2] != b'BM':
                print(f"{file_name}은 BMP 파일이 아닙니다.")
                return
            
            # 파일 크기 (바이트)
            file_size = struct.unpack('<I', header[2:6])[0]

            # 이미지 크기 (픽셀)
            width = struct.unpack('<I', header[18:22])[0]
            height = struct.unpack('<I', header[22:26])[0]

            # 비트당 픽셀 (컬러 깊이)
            bits_per_pixel = struct.unpack('<H', header[28:30])[0]

            # 압축 방식
            compression = struct.unpack('<I', header[30:34])[0]

            # 알파 채널 존재 여부 확인
            # BMP에서 32비트 색 깊이를 사용하는 경우 알파 채널이 존재 가능
            has_alpha = bits_per_pixel == 32

            print(f"파일 이름: {file_name}")
            print(f"파일 크기: {file_size} 바이트")
            print(f"이미지 크기: {width}x{height}")
            print(f"컬러 깊이: {bits_per_pixel}비트")
            print(f"압축 방식: {'압축 없음' if compression == 0 else '압축 사용'}")
            print(f"알파 채널 존재 여부: {'있음' if has_alpha else '없음'}")

            if has_alpha:
                # 픽셀 데이터의 시작 위치 (디폴트: 54바이트 이후)
                pixel_data_offset = struct.unpack('<I', header[10:14])[0]
                f.seek(pixel_data_offset)

                # 픽셀 데이터를 읽어서 알파 채널 정보 분석
                pixel_data = f.read()
                alpha_values = pixel_data[3::4]  # 4바이트 중 4번째 바이트는 알파 값

                if alpha_values:
                    alpha_min = min(alpha_values)
                    alpha_max = max(alpha_values)
                    alpha_mean = sum(alpha_values) / len(alpha_values)
                    print("알파 채널 투명도 정보:")
                    print(f"  최소 투명도 값: {alpha_min}")
                    print(f"  최대 투명도 값: {alpha_max}")
                    print(f"  평균 투명도 값: {alpha_mean}")
                else:
                    print("알파 채널 데이터가 없습니다.")
            else:
                print("알파 채널 정보가 없습니다.")

    except FileNotFoundError:
        print(f"{file_name} 파일을 찾을 수 없습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("사용법: python bmp_alpha_info.py <파일명>")
    else:
        read_bmp_info(sys.argv[1])
