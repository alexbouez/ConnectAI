target: all
all: 
	@ cc -fPIC -shared -o bin/player1.so src/player1/main.c

.PHONY: clean run
run:
	@ ./src/game.py
clean: 
	@ rm bin/*