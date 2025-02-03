.section .text
.global _start

_start:
    // 스택 포인터 설정
    ldr sp, =0x8000

    // UART 초기화 (예시, 실제 하드웨어에 맞게 수정 필요)
    ldr r0, =0x101f1000
    mov r1, #0
    str r1, [r0]

    // 커널로 점프
    ldr pc, =0x8000

.section .data
    // 필요한 데이터가 있다면 여기에 추가

