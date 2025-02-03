from PIL import Image
import sys
import numpy as np

def print_bmp_info(file_name):
    try:
        # 이미지 파일 열기
        with Image.open(file_name) as img:
            # BMP 여부 확인
            if img.format != 'BMP':
                print(f"{file_name}은 BMP 파일이 아닙니다.")
                return
            
            # 기본 속성 정보 출력
            print(f"파일 이름: {file_name}")
            print(f"이미지 포맷: {img.format}")
            print(f"크기: {img.size[0]}x{img.size[1]}")
            print(f"모드: {img.mode}")

            # 알파 채널 확인
            has_alpha = 'A' in img.mode
            print(f"알파 채널 존재 여부: {'있음' if has_alpha else '없음'}")
            
            if has_alpha:
                # 알파 채널 데이터 추출
                alpha_data = np.array(img.split()[-1])  # 알파 채널 (A)
                transparency_info = {
                    "최소 투명도 값": alpha_data.min(),
                    "최대 투명도 값": alpha_data.max(),
                    "평균 투명도 값": alpha_data.mean(),
                }
                print("알파 채널 투명도 정보:")
                for key, value in transparency_info.items():
                    print(f"  {key}: {value}")

    except FileNotFoundError:
        print(f"{file_name} 파일을 찾을 수 없습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    # 파일명을 입력받아 실행
    if len(sys.argv) != 2:
        print("사용법: python bmp_info.py <파일명>")
    else:
        file_name = sys.argv[1]
        print_bmp_info(file_name)
