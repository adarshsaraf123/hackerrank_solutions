#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    int student;
    int ontimers;
    int N, K, T, i;
	int cancel;
    scanf("%d", &T);
    while(T--)
    {
        ontimers = 0;
        scanf("%d %d", &N, &K);
		printf("%d %d\n\n", N, K);
		cancel = 1;
        for(i=0;i<N;i++)
        {
            scanf("%d", &student);
			printf("student = %d", student);
            if(student <= 0) // implies the student has reached on time
            {
				ontimers += 1;
				printf("ontimers = %d", ontimers);
                if(ontimers >= K)
                    cancel = 0;
            }
        }
        if(cancel)
            printf("YES\n");
        else
            printf("NO\n");
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
