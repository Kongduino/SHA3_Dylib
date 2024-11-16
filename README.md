# SHA3_Dylib

An SHA3 dynamic library for use with Python, Xojo, etc... like my [Chacha20_Dylib](https://github.com/Kongduino/Chacha20_Dylib) and [Blowfish_Dylib](https://github.com/Kongduino/Blowfish_Dylib). It's based on [SHA3IUF](https://github.com/brainhub/SHA3IUF).

```
make
gcc -Ofast -g -c   -c -o sha3.o sha3.c
gcc -Ofast -g -c *.c
gcc -dynamiclib sha3.o -o k_sha3.dylib
rm *.o
cd Python ; ./Test.py
   +------------------------------------------------+ +----------------+
   |.0 .1 .2 .3 .4 .5 .6 .7 .8 .9 .a .b .c .d .e .f | |      ASCII     |
   +------------------------------------------------+ +----------------+
00.|4e 03 65 7a ea 45 a9 4f c7 d4 7b a8 26 c8 d6 67 | |N.ez.E.O..{.&..g|
01.|c0 d1 e6 e3 3a 64 a0 36 ec 44 f5 8f a1 2d 6c 45 | |....:d.6.D...-lE|
   +------------------------------------------------+ +----------------+
b'N\x03ez\xeaE\xa9O\xc7\xd4{\xa8&\xc8\xd6g\xc0\xd1\xe6\xe3:d\xa06\xecD\xf5\x8f\xa1-lE'
SHA3/256 success!

   +------------------------------------------------+ +----------------+
   |.0 .1 .2 .3 .4 .5 .6 .7 .8 .9 .a .b .c .d .e .f | |      ASCII     |
   +------------------------------------------------+ +----------------+
00.|f7 df 11 65 f0 33 33 7b e0 98 e7 d2 88 ad 6a 2f | |...e.33{......j/|
01.|74 40 9d 7a 60 b4 9c 36 64 22 18 de 16 1b 1f 99 | |t@.z`..6d"......|
02.|f8 c6 81 e4 af af 31 a3 4d b2 9f b7 63 e3 c2 8e | |......1.M...c...|
   +------------------------------------------------+ +----------------+
b'\xf7\xdf\x11e\xf033{\xe0\x98\xe7\xd2\x88\xadj/t@\x9dz`\xb4\x9c6d"\x18\xde\x16\x1b\x1f\x99\xf8\xc6\x81\xe4\xaf\xaf1\xa3M\xb2\x9f\xb7c\xe3\xc2\x8e'
SHA3/384 success!

   +------------------------------------------------+ +----------------+
   |.0 .1 .2 .3 .4 .5 .6 .7 .8 .9 .a .b .c .d .e .f | |      ASCII     |
   +------------------------------------------------+ +----------------+
00.|18 58 7d c2 ea 10 6b 9a 15 63 e3 2b 33 12 42 1c | |.X}...k..c.+3.B.|
01.|a1 64 c7 f1 f0 7b c9 22 a9 c8 3d 77 ce a3 a1 e5 | |.d...{."..=w....|
02.|d0 c6 99 10 73 90 25 37 2d c1 4a c9 64 26 29 37 | |....s.%7-.J.d&)7|
03.|95 40 c1 7e 2a 65 b1 9d 77 aa 51 1a 9d 00 bb 96 | |.@.~*e..w.Q.....|
   +------------------------------------------------+ +----------------+
b'\x18X}\xc2\xea\x10k\x9a\x15c\xe3+3\x12B\x1c\xa1d\xc7\xf1\xf0{\xc9"\xa9\xc8=w\xce\xa3\xa1\xe5\xd0\xc6\x99\x10s\x90%7-\xc1J\xc9d&)7\x95@\xc1~*e\xb1\x9dw\xaaQ\x1a\x9d\x00\xbb\x96'
SHA3/512 success!
```
