[BITS 16]
[ORG 0x7C00]

start:
    cli                ; 인터럽트 비활성화
    xor ax, ax         ; 모든 세그먼트를 0으로 초기화
    mov ds, ax
    mov es, ax
    mov fs, ax
    mov gs, ax

    ; DS를 현재 CS와 일치시킴
    mov ax, cs         
    mov ds, ax

    ; "Bootloader Loaded!" 메시지 출력
    mov si, boot_msg
    call print_string

main_loop:
    ; 디버그 메시지 출력
    mov si, debug_loop_msg
    call print_string

    ; 프롬프트 문자 ">" 출력
    mov si, prompt_msg
    call print_string

    ; 사용자 입력 처리
    call read_command

    ; 입력된 명령어가 없는 경우 프롬프트로 돌아감
    mov si, command_buffer
    lodsb
    cmp al, 0
    je main_loop

    ; 명령어 비교 및 처리
    mov si, command_buffer
    call strcmp_sysinfo
    je display_sysinfo   ; 'sysinfo' 입력 시 시스템 정보 출력

    ; 알 수 없는 명령어 처리
    mov si, unknown_cmd_msg
    call print_string

    jmp main_loop       ; 다시 프롬프트로 돌아감

display_sysinfo:
    mov si, sysinfo_msg
    call print_string
    jmp main_loop

;----------------------------------------
; 문자열 출력 (DS:SI에 널 종료 문자열)
print_string:
    pusha
.print_char:
    lodsb              ; DS:SI -> AL
    cmp al, 0
    je .done
    mov ah, 0x0E       ; BIOS teletype 기능
    int 0x10           ; 화면 출력
    jmp .print_char
.done:
    popa
    ret

; 문자열 비교 ('sysinfo'와 비교)
strcmp_sysinfo:
    pusha
    mov di, sysinfo_cmd
.compare_char:
    lodsb              ; DS:SI -> AL
    cmp al, [di]
    jne .not_equal
    cmp al, 0
    je .equal
    inc di
    jmp .compare_char
.not_equal:
    xor al, al         ; 문자열이 다름을 표시
    popa
    ret
.equal:
    mov al, 1          ; 문자열이 동일함을 표시
    popa
    ret

; 키보드로부터 문자열 입력
read_command:
    pusha
    mov di, command_buffer
    xor cx, cx         ; 입력 문자 개수 초기화

.read_char:
    xor ah, ah
    int 0x16           ; BIOS 키보드 입력 (대기)
    cmp al, 0Dh        ; 엔터키 확인
    je .done

    ; 백스페이스 처리
    cmp al, 0x08
    je .handle_backspace

    ; 입력 문자를 버퍼에 저장
    stosb
    inc cx
    ; 화면에 입력된 문자 출력
    mov ah, 0x0E
    int 0x10

    cmp cx, 30         ; 최대 입력 길이 제한 (30자)
    jne .read_char
    jmp .done

.handle_backspace:
    cmp cx, 0
    je .read_char       ; 지울 문자가 없으면 무시
    dec cx
    dec di
    ; 화면에서 문자 삭제
    mov ah, 0x0E
    mov al, 0x08       ; 백스페이스
    int 0x10
    mov al, ' '        ; 공백 출력
    int 0x10
    mov al, 0x08       ; 다시 백스페이스
    int 0x10
    jmp .read_char

.done:
    ; 엔터키 입력 시 줄바꿈 추가
    mov ah, 0x0E
    mov al, 0Dh        ; CR(Carriage Return)
    int 0x10
    mov al, 0Ah        ; LF(Line Feed)
    int 0x10

    mov al, 0          ; 널 종료 문자 추가
    stosb
    popa
    ret

;----------------------------------------
; 데이터 섹션
;----------------------------------------
boot_msg        db "Bootloader Loaded!", 0Dh, 0Ah, 0
prompt_msg      db ">", 0
unknown_cmd_msg db "Unknown command", 0Dh, 0Ah, 0
sysinfo_msg     db "Simple Bootloader v1.0", 0Dh, 0Ah, 0
sysinfo_cmd     db "sysinfo", 0
command_buffer  times 32 db 0
debug_loop_msg  db "[DEBUG] In main loop", 0Dh, 0Ah, 0

; 부트 섹터는 반드시 512바이트여야 하며 마지막은 0xAA55 서명으로 끝나야 함
times 510 - ($ - $$) db 0
dw 0xAA55
