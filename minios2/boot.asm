[org 0x7c00]
[bits 16]

; 스택 설정
mov bp, 0x9000
mov sp, bp

; 화면 클리어
mov ax, 0x3
int 0x10

; 부트 메시지 출력
mov si, MSG_REAL_MODE
call print_string

; 커널 로드
call load_kernel

; 보호 모드로 전환
call switch_to_pm

jmp $

%include "print_string.asm"
%include "disk_load.asm"
%include "gdt.asm"
%include "print_string_pm.asm"
%include "switch_to_pm.asm"

[bits 32]
BEGIN_PM:
    mov ebx, MSG_PROT_MODE
    call print_string_pm
    
    ; 커널로 점프
    call KERNEL_OFFSET
    
    jmp $

; 전역 변수
KERNEL_OFFSET equ 0x1000
MSG_REAL_MODE db "Started in 16-bit Real Mode", 0
MSG_PROT_MODE db "Successfully landed in 32-bit Protected Mode", 0

; 부트섹터 패딩
times 510-($-$$) db 0
dw 0xaa55

