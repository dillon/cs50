# Questions

## What's `stdint.h`?

A header file that defines a set of typedefs that specify exact-width integer types

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

They define the size of the ints you are using

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

BYTE = 1 byte, DWORD = 4 bytes, LONG = 4 bytes, WORD = 2 bytes

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

in ascii: B followed by M

## What's the difference between `bfSize` and `biSize`?

bfSize = The size, in bytes, of the bitmap file
biSize = The number of bytes required by the structure

## What does it mean if `biHeight` is negative?

If biHeight is negative, the bitmap is a top-down DIB and its origin is the upper-left corner.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

Couldn't open the file or couldn't create the file (i.e. if the file is not in folder, and for the second, if there is no more space to save file)

## Why is the third argument to `fread` always `1` in our code?

we're already in forloops so we only need to read 1 element for each forloop

## What value does line 63 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

1

## What does `fseek` do?

it moves the file pointer associated with stream to a new location

## What is `SEEK_CUR`?

sets the offset value relative to the beginning of the file
