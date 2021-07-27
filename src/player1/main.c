#include <stdio.h>
#include <stdint.h>
#include <stdio.h>

// Compile with cc -fPIC -shared -o bin/main.so src/player1/main.c 

/** 
 * Squaring of small number.
 * Returns the square root of parameter i.
 * 
 * @param i a small number (int)
 * @return n the square root of i
 */
int square(int i) {
	return i * i;
}
