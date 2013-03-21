
CC = gcc
CFLAGS = -g -Wall -shared
OBJECTS = file.o file_wrap.o
INCFLAGS = -I/usr/include/python2.7
LDFLAGS = -shared
OBJECTSTOTAL = file.o file_wrap.c _file.so

all: $(OBJECTSTOTAL)

file.o: file.c
	$(CC) -c -fPIC file.c
	
file_wrap.c: file.i
	swig -python file.i
	
file_wrap.o: file_wrap.c
	$(CC) -c -fPIC file_wrap.c $(INCFLAGS)
	
_file.so: $(OBJECTS)
	$(CC) $(LDFLAGS) $(OBJECTS) -o _file.so $(INCFLAGS)


clean:
	rm *.o
	
	