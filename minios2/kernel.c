#include <string.h>

// UART 관련 함수 (예시, 실제 하드웨어에 맞게 수정 필요)
#define UART0_DR (*((volatile unsigned int *)0x101f1000))

int strcmp(const char *s1, const char *s2) {
    while (*s1 && (*s1 == *s2)) {
        s1++;
        s2++;
    }
    return *(const unsigned char*)s1 - *(const unsigned char*)s2;
}

void uart_putc(unsigned char c) {
    UART0_DR = c;
}

void print(const char *s) {
    while(*s != '\0') {
        uart_putc(*s);
        s++;
    }
}

void read_command(char *buffer, int max_length) {
    int i = 0;
    char c;
    while(i < max_length - 1) {
        c = UART0_DR;
        if(c == '\r' || c == '\n') {
            uart_putc('\r');
            uart_putc('\n');
            break;
        }
        buffer[i++] = c;
        uart_putc(c);  // Echo the character
    }
    buffer[i] = '\0';
}

void kernel_main() {
    char command[100];

    print("Welcome to MyOS!\r\n");

    while(1) {
        print("MyOS> ");
        read_command(command, sizeof(command));
        
        if(command[0] == '\0') continue;

        // 간단한 명령어 처리
        if(strcmp(command, "hello") == 0) {
            print("Hello, World!\r\n");
        } else if(strcmp(command, "exit") == 0) {
            print("Goodbye!\r\n");
            break;
        } else {
            print("Unknown command: ");
            print(command);
            print("\r\n");
        }
    }
}

