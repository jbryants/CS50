# Questions

## What's `stdint.h`?

stdint.h is a header file that lets you declare custom integer sizes.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

You can fill up a specific amount of space for each int. uint8_t is the same as a byte.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

BYTE: 1
DWORD: 4
LONG: 4
WORD: 2

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

0x42 0x4D

## What's the difference between `bfSize` and `biSize`?

bfSize is the size, in bytes, of the bitmap file.
biSize is the number of bytes required by the structure.

## What does it mean if `biHeight` is negative?

The bitmap is a top-down DIB(device independant bitmap) and its origin is the upper-left corner.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

The biBitCount member of the BITMAPINFOHEADER determines the number of bits that defines each pixel.

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

fopen will return NULL if the file cannot be opened. It could be due to lack of memory or if there is no file to be found.

## Why is the third argument to `fread` always `1` in our code?

The third argument tells us how many elements fread will read. We are always reading 1 file.

## What value does line 65 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

3 BYTES

## What does `fseek` do?

fseek() is used to move file pointer associated with a given file to a specific position.

## What is `SEEK_CUR`?

SEEK_CUR specifies that offset is a count of characters from the current file position. This count may be positive or negative.
