set -v
nasm -f bin boot.asm -o boot.bin
#nasm -f elf32 kernel_entry.asm -o kernel_entry.o
#nasm -f elf32 boot.asm -o boot.o
#nasm -f elf32 kernel_entry.asm -o kernel_entry.o
#nasm -f elf32 gdt.asm -o gdt.o
#nasm -f elf32 idt.asm -o idt.o
#i686-linux-gnu-gcc -ffreestanding -fno-pic -c kernel.c -o kernel.o
#i686-linux-gnu-gcc -ffreestanding -m32 -c kernel.c -o kernel.o
#i686-linux-gnu-ld -m elf_i386 -Ttext 0x1000 kernel_entry.o kernel.o --entry=_start --n
#i686-linux-gnu-ld -m elf_i386 -Ttext 0x1000 kernel_entry.o kernel.o gdt.o idt.o --entry=_start -o kernel.bin
#cat boot.bin kernel.bin > os-image.bin
#qemu-system-i386 -drive format=raw,file=os-image.bin -nographic
qemu-system-i386 -drive format=raw,file=boot.bin,if=floppy -boot order=a -nographic
