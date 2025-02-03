import sys
from PIL import Image

def check_alpha_channel(file_path):
    try:
        with Image.open(file_path) as img:
            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                return f"{file_path}에 투명한 알파 채널이 있습니다."
            else:
                return f"{file_path}에 투명한 알파 채널이 없습니다."
    except Exception as e:
        return f"오류: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python script_name.py <bmp_file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    result = check_alpha_channel(file_path)
    print(result)

