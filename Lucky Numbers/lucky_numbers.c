#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define N 300000
short* lucky_numbers(n)
{
	short * marked = (short *)malloc(n*sizeof(short));
	if(marked == NULL)
	{
		printf("Too much memory");
		exit(1);
	}
	int i;
	for(i=0;i<n;i++)
		marked[i] = 0;
	int sieve = 3;
	int unmarked = n;
	int k;
	while(sieve < unmarked)
	{
		k = 0;
		// to sieve using this number for sieving
		for(i=0; i < n; i++)
		{
			if(!marked[i])
				k++;
			if(k == sieve)
			{
				marked[i] = 1;
				unmarked -= 1;
				k = 0;
			}
		}
		// to find the next number for sieving
		for(i = (sieve - 1)/2 + 1; i<n; i++)
		{	
			if(!marked[i])
			{
				sieve = i*2 + 1;
				break;
			}
		}
	}
	return marked;
}
int main()
{
	short *marked = lucky_numbers(N);
// 	int i;
// 	for(i=0; i<N; i++)
// 		if(!marked[i])
// 			printf("%d ",i*2 + 1);
	return 0;
}