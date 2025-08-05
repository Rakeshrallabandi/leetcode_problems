#include <stdio.h>

int numOfUnplacedFruits(int* f, int fruitsSize, int* b, int basketsSize) {
    int c = 0;

    for (int i = 0; i < fruitsSize; i++) {
        for (int j = 0; j < basketsSize; j++) {
            if (f[i] <= b[j]) {
                c++;
                b[j] = -1;  
                break;
            }
        }
    }

    return fruitsSize - c;  
}
