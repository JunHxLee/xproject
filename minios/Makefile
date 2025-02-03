# Makefile to build the bootloader
TARGET = boot.bin
CC = i686-elf-gcc
LD = i686-elf-ld
AS = nasm
OBJCOPY = objcopy

CFLAGS = -ffreestanding -m32 -nostdlib
LDFLAGS = -Ttext 0x7C00 --oformat binary

all: $(TARGET)

boot.o: boot.c
	$(CC) $(CFLAGS) -c boot.c -o boot.o

$(TARGET): boot.o
	$(LD) $(LDFLAGS) boot.o -o $(TARGET)
	dd if=/dev/zero bs=1 count=$$((512 - $$(stat --format=%s $(TARGET)))) >> $(TARGET)

clean:
	rm -f *.o $(TARGET)
