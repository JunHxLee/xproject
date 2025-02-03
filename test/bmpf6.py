import sys
from PIL import Image

def get_bmp_info(file_path):
    try:
        with Image.open(file_path) as img:
            info = {
                "파일 경로": file_path,
                "이미지 크기": f"{img.width}x{img.height} 픽셀",
                "이미지 모드": img.mode,
                "포맷": img.format,
                "알파 채널 포함 여부": "있음" if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info) else "없음",
                "팔레트 사용 여부": "있음" if img.mode == 'P' else "없음",
                "DPI": img.info.get('dpi', '정보 없음'),
                "파일 크기": f"{img.tell()} 바이트"
            }
            
            if img.mode == 'P':
                info["팔레트 색상 수"] = len(img.getcolors())
            
            return info
    except Exception as e:
        return {"오류": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python script_name.py <bmp_file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    bmp_info = get_bmp_info(file_path)
    
    print("BMP 파일 정보:")
    for key, value in bmp_info.items():
        print(f"{key}: {value}")

