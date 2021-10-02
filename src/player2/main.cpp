#include <stdio.h>
#include <stdint.h>

#include "main.h"

// Compile as shared object with g++

/** 
 * Squaring of small number.
 * Returns the square root of parameter i.
 * 
 * @param i a small number (int)
 * @return n the square root of i
 */
extern "C" int play(void) {
	Board board;
    return board.get_rows();
}
