#define VIDEO_MEMORY 0xB8000
#define VGA_WIDTH 80
#define VGA_HEIGHT 25

void clear_screen() {
    char *video = (char *)VIDEO_MEMORY;
    for (int i = 0; i < VGA_WIDTH * VGA_HEIGHT * 2; i += 2) {
        video[i] = ' ';
        video[i + 1] = 0x07;  // 흰색 글자, 검은 배경
    }
}

void print(const char *str) {
    static int row = 0, col = 0;
    char *video = (char *)VIDEO_MEMORY;

    while (*str) {
        if (*str == '\n') {
            row++;
            col = 0;
        } else {
            int offset = (row * VGA_WIDTH + col) * 2;
            video[offset] = *str;
            video[offset + 1] = 0x07;
            col++;
            if (col >= VGA_WIDTH) {
                col = 0;
                row++;
            }
        }

        if (row >= VGA_HEIGHT) {
            row = 0;  // 화면이 가득 차면 다시 첫 줄로
        }

        str++;
    }
}

char get_key() {
    char key;
    asm volatile (
        "int $0x16"    // BIOS 키보드 서비스 호출
        : "=al" (key)  // AL 레지스터에 키 값 반환
        : "ah" (0x00)  // AH에 기능 코드 0x00 (키 대기)
    );
    return key;
}

void main() {
    clear_screen();
    print("Simple Bootloader v1.0\n");

    while (1) {
        print("> ");
        char cmd = get_key();

        if (cmd == 'h') {
            print("\nHello from Bootloader!\n");
        } else if (cmd == 'r') {
            print("\nRebooting...\n");
            asm volatile ("jmp 0xFFFF:0x0000");  // 시스템 재부팅 명령
        } else {
            print("\nUnknown command\n");
        }
    }
}
