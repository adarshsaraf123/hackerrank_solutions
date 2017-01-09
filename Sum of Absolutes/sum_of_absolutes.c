#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int N, Q, L, R;
    scanf("%d %d", &N, &Q);
    int *A = (int *)malloc(N * sizeof(int));
    int i, q;
    int odd = 0;
    for(i=0; i< N; i++)
        scanf("%d", A+i);
    for(q=0; q< Q; q++)
    {   
        odd = 0;
        scanf("%d %d", &L, &R);
        for(i = L-1; i < R; i++)
            odd ^= (A[i] & 1);
        printf("%s\n", (odd == 1? "Odd": "Even"));
    }
    return 0;
}
