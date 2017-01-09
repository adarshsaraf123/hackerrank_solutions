#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

unsigned long min_cost_position(int roses_low, int *P, int sprinkler_index, int e, int *local_positions, int *local_positions_count, int N, int M, int S)
{
	if(roses_low > N) //implies all the roses have been watered
		return 0;
	if(sprinkler_index == M) // no more sprinklers available to water the roses
		return -1;
	if( (P[sprinkler_index] - roses_low) > e ) //some of the roses will remain dry if this condition holds
		return -1;
	included = min_cost_position(P[0] + e + 1, P[1:], e, N, M, S)
	excluded = min_cost_position(roses_low, P[1:], e, N, M, S)
	if excluded != None:
		if included != None:
			if (S+included[0]) < excluded[0]:
				return (S+included[0], [P[0]] + included[1])
			else:
				return excluded
		else:
			return excluded
	elif included != None:
		return (S+included[0], [P[0]] + included[1])
	else:
		return None
}		
int main()
{
	int T, N, M;
	int S, Q;
	int E_min, E_max, optimal_E, e;
	unsigned long optimal_cost, local_cost;
	int *optimal_positions, local_positions;
	int optimal_positions_count, local_positions_count;
	int *P;
	int i, temp;
	scanf("%u", &T);
	while(T--)
	{
		scanf("%u %u %u %u", &N, &M, &S, &Q);
		P = (int *)malloc(M*sizeof(int));
		
		//setting up E_min
		E_min = P[0] - 1;
		for(i=0; i<M-1; i++)
		{
			temp = (P[i+1]-P[i]) / 2;
			if (temp > E_min)
				E_min = temp
		}
		temp = N - P[M-1];
		if(temp > E_min)
			E_min = temp;
		
		// setting up E_max
		E_max = P[M-1] -1;
		temp = N - P[0];
		if(temp > E_max)
			E_max = temp
		
		//initialization of the optimal parameters
		optimal_cost = ULONG_MAX;
		optimal_positions = (int *)calloc(M *sizeof(int));
		optimal_E = -1;
		optimal_positions_count = 0;
		
		local_positions_count = 0;
		local_positions = (int *)calloc(M * sizeof(int));
		
		for(e = E_min; e <= E_max; e ++)
		{
			local_cost = min_cost_position(1, P, 0, e, local_positions, &local_positions_count, N, M, S);
			if(local_cost != -1 && (local_cost = local_cost + e*Q) < optimal_cost)
			{
				optimal_cost = local_cost;
				for(i=0; i<M; i++)
					optimal_positions[i] = local_positions[i];
				optimal_E = e;
				optimal_positions_count = local_positions_count;
			}
			for(i=0; i<M; i++)
				local_positions[i] = 0;
			local_positions_count = 0;
		}
		printf("%d %d\n", optimal_positions_count, optimal_E);
		for(i=0;i<M;i++)
			if(optimal_positions[i])
				printf("%d ", P[i]);
		printf("\n");
		free(P);
		free(optimal_positions);
	}
	return 0;
}