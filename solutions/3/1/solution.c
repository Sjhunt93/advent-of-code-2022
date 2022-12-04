#include <stdio.h>
#include <string.h>


// Its been 8 or more years since writing plain old C... Wow its hard haha

/*
Thoughts

We are comparing two sets of fixed values 
ASCII a-z and ASCII A-Z

We could make a bit mask of values..

lessons learnt
types matter way more than I thought
1 is not the same as 1LL

*/

static const int lowA = 'a';
static const int lowZ = 'z';
static const int upA = 'A';
static const int upZ = 'Z';


int64_t to_bit_mask(char * string, int len) 
{
    int64_t values = 0;
    for (size_t i = 0; i < len; i++) {
        char c = string[i];
        // lower case letters bits 0-25
        if (c >= lowA && c <= lowZ) {
            int bit = c - lowA;
            //printf("setting bit %i %c \n", bit, c);
            values |= 1LL << bit;
        }
        // upper case letters bits 26-51
        else if (c >= upA && c <= upZ) {
            int bit = (c - upA) + 26;
            //printf("setting bit %i %c \n", bit, c);
            values |= 1LL << bit;
        }
    }
    return values;

}

int getPrioForPattern(int64_t num)
{
    for (size_t i = 0; i < 26*2; i++) {
        if (num & 1LL << i) {
            return i+1;
            //printf("bit %i set -> %c \n", i, i >=26 ? i-26+upA : i+lowA);
        }
    }
}

void printHelper(int64_t num) 
{
    for (size_t i = 0; i < 26*2; i++) {
        if (num & 1LL << i) {
            printf("bit %i set -> %c \n", i, i >=26 ? i-26+upA : i+lowA);
        }
    }
    
}

int main() 
{
    FILE *fptr;
    fptr = fopen("full.txt","r");

    char line[256] = {0};
    char pack1[128] = {0};
    char pack2[128] = {0};

    
    size_t len = 0;
    int read = 0;

    int score = 0;
    if (fptr) {
        int64_t patterns_for_3[3] = {0ll};
        int counter = 0;
        while (fgets(line, sizeof(line), fptr) != NULL) {
            const int len = strlen(line);

            memcpy(pack1, line, len/2);
            pack1[len/2 + 1] = '\0';
            memcpy(pack2, line+(len/2), len/2);
            pack2[len/2 + 1] = '\0';

            int64_t pack1Pattern = to_bit_mask(pack1, len/2);
            int64_t pack2Pattern = to_bit_mask(pack2, len/2);
        
            // solution A
            int64_t duplicates = pack1Pattern & pack2Pattern;
            // printf("%u %u %u %i\n", pack1Pattern, pack2Pattern, duplicates, sizeof(pack1Pattern));
            // printHelper(duplicates);
            score += getPrioForPattern(duplicates);
        }   
    }
    else {
        printf("ERROR\n");
    }
    fclose(fptr);

    printf("Output = %i\n", score);

    return 0;
}