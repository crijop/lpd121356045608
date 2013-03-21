all: file.o file_wrap.c _file.so

file.o: file.c
	gcc -c -fPIC file.c
	
file_wrap.c: file.i
	swig -python file.i
	
file_wrap.o: file_wrap.c
	gcc -c -fPIC file_wrap.c -I/usr/include/python2.7
	
_file.so: file.o file_wrap.o
	gcc -shared file_wrap.o file.o -o _file.so -I/usr/include/python2.7



clean:
	rm *.o
	
	