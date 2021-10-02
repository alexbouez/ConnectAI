target: all
all: player1 player2

player1:
	@ mkdir -p bin
	@ cc -fPIC -shared -o bin/player1.so src/player1/main.c

player2:
	@ mkdir -p bin
	@ g++ -shared -c -fPIC src/player2/main.cpp -o bin/player2.o
	@ g++ -shared -Wl,-soname,bin/player2.so -o bin/player2.so bin/player2.o

.PHONY: clean run
run:
	@ ./src/game.py
clean: 
	@ rm bin/*
	@ rm *.cfg