mod_value = 10**9 + 7
count_memoized = {}
def count_possibilities(current_soldier, current_skills):
	if current_skills == R:
		temp = count_memoized[(current_soldier, current_skills)] = pow(2,N-current_soldier, mod_value)
		return temp
	if current_soldier == N:
		return 0
	if (current_soldier, current_skills) in count_memoized:
		return count_memoized[(current_soldier,current_skills)]
	count = 0
	if S[current_soldier] & (~R) == 0:
		count += count_possibilities(current_soldier + 1, current_skills | S[current_soldier])
	count = ( count + count_possibilities(current_soldier + 1, current_skills) ) % mod_value
	print current_soldier, current_skills, count
	count_memoized[(current_soldier, current_skills)] = count
	return count
N, M = map(int, raw_input().split())
S = []
for n in xrange(N):
	S.append( int(raw_input(), 2) )
R = int(raw_input(), 2)
S = filter(lambda x: x & (~R) == 0, S)
N = len(S)
print count_possibilities(0,0)

#include<iostream>
#include<map>
#include<vector>
#include<limits>
#include<deque>

// use vector for positions
// use map for the memoization
// use deque for the list of sprinkler positions
using namespace std;
typedef pair<int, int> map_key;
typedef deque<int> list_created, map_value;

vector<int> P;
typedef map<map_key, unsigned int> my_map;
my_map cost_memoized;

list_created min_cost_position(int roses_low, int sprinkler_low, int e, int N, int M, int first = 0)
{
	list_created included, excluded;
	my_map::iterator it;
	if(roses_low > N) //implies all the roses have been watered
		return included;
	if( (sprinkler_low == M) || ( (P[sprinkler_low] - roses_low) > e ) ) // no more sprinklers available to water the roses or not possible to water all the roses
	{
		included.push_front(-1);
		return included;
	}
	
	if (first)
		cost_memoized.clear();
	
	it = cost_memoized.find(make_pair(roses_low, sprinkler_low));
	if(it != cost_memoized.end())
		return it -> second;
		
	included = min_cost_position(P[sprinkler_low] + e + 1, sprinkler_low + 1, e, N, M);
	
	excluded = min_cost_position(roses_low, sprinkler_low + 1, e, N, M);
	
	if(included[0] != -1)
	{
		included.push_front(P[sprinkler_low]);
		if(excluded[0] != -1 && (included.size() > excluded.size()) )
		{
			cost_memoized[make_pair(roses_low, sprinkler_low)] = excluded;
			return excluded;
		}

		cost_memoized[make_pair(roses_low, sprinkler_low)] = included;
		//cout << cost_memoized << endl;
		return included;
	}
	cost_memoized[make_pair(roses_low, sprinkler_low)] = excluded;
	//cout << cost_memoized << endl;
	return excluded;
}

int main()
{
	int T, N, M;
	int S, Q;
	int E_min, E_max, optimal_E, e;
	unsigned long optimal_cost, local_cost;
	list_created optimal_positions, local_positions;
	int i, temp, input;
	list_created::iterator it;
	int first;
	for n in xrange(N):
	S.append( int(raw_input(), 2) )
	R = int(raw_input(), 2)
	S = filter(lambda x: x & (~R) == 0, S)
	N = len(S)
	print count_possibilities(0,0)
	cin >> T;
	//cout << T << "\n\n\n";
	while(T--)
	{
		cin >> N >> M >> S >> Q;
		//cout << N << " " << M << " "<< S << " "<< Q << endl;
		P.clear();
		P.reserve(M);
		
		//taking input for P and setting up E_min
		cin >> input;
		//cout << input << " ";
		P.push_back(input);
		//cout << P[0] << endl;
		E_min = P[0] - 1;
		for(i=1; i < M; i++)
		{
			cin >> input;
			P.push_back(input);
			//cout << P[i] << endl;
			temp = (P[i]-P[i - 1]) / 2;
			if (temp > E_min)
				E_min = temp;
		}
		temp = N - P[M-1];
		if(temp > E_min)
			E_min = temp;
		
		// setting up E_max
		E_max = P[M-1] -1;
		temp = N - P[0];
		if(temp > E_max)
			E_max = temp;
		
		//initialization of the optimal parameters
		optimal_cost = numeric_limits<unsigned long>::max();
		optimal_positions.clear();
		optimal_E = -1;
		
		for(e = E_min; e <= E_max; e++)
		{
			local_positions = min_cost_position(1, 0, e, N, M, first = 1);
			local_cost = local_positions.size()*S + e*Q;
			if(local_cost < optimal_cost)
			{
				optimal_cost = local_cost;
				optimal_positions = local_positions;
				optimal_E = e;
			}
		}
		cout << optimal_positions.size() << " " << optimal_E << endl;
		for(it = optimal_positions.begin(); it != optimal_positions.end(); it ++)
			cout << *it << " ";
		cout << endl;
	}
	return 0;
}