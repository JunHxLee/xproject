load_kernel:
    mov bx, KERNEL_OFFSET
    mov dh, 2
    mov dl, [BOOT_DRIVE]
    call disk_load
    ret

disk_load:
    pusha
    push dx
    
    mov ah, 0x02
    mov al, dh
    mov ch, 0x00
    mov dh, 0x00
    mov cl, 0x02
    
    int 0x13
    
    jc disk_error
    
    pop dx
    cmp dh, al
    jne disk_error
    popa
    ret

disk_error:
    mov si, DISK_ERROR_MSG
    call print_string
    jmp $

BOOT_DRIVE: db 0
DISK_ERROR_MSG db "Disk read error!", 0

