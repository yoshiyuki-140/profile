
main:main.c lifeGame.o
	gcc -O2 -o $@ $^
lifeGame.o:lifeGame.c
	gcc -O2 -c $^
run:
	./main
cmpRun:
	make && make run
clean:
	rm main lifeGame.o
