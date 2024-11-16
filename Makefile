.POSIX:
TARGET = k_sha3
CC = gcc
CFLAGS = -Ofast -g -c

# The list of object files.
OBJS = sha3.o

# the list of files to clean
TOCLEAN = k_sha3.dylib $(OBJS)

RM ?= rm -f

all: $(TARGET)
clean:
	$(RM) $(TOCLEAN)

k_sha3: $(OBJS)
	$(CC) $(CFLAGS) *.c
	$(CC) -dynamiclib sha3.o -o $(TARGET).dylib
	rm *.o
	cd Python ; ./Test.py

install:
	cp $(TARGET).dylib /usr/local/lib/