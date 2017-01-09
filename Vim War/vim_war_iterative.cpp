#include<iostream>
#include<stack>
#include<map>
#include<string>
#include<list>
typedef list<int>::iterator position;

using namespace std;
int main()
{
	stack< pair<position, int> > my_stack;
	map<pair<position, int>, int > my_map;
	ma<pair<position, int>, int >::iterator map_iter;
	position stack_iter;
	list<int> S;
	position S_iter;
	int mod_value = 10**9 + 7;
	int N, M, R;
	cin >> N >> M;
	string temp;
	int i;
	for(i=0;i<N; i++)
	{
		cin >> temp;
		S.push_back(stoi(temp, nullptr, 2));
	}
	cin >> temp;
	R = stoi(temp, nullptr, 2);
	for(S_iter = S.begin();S_iter != S.end(); S_iter ++)
	{
		if(*S_iter)
	}
	return 0;
}

R = int(raw_input(), 2)
S = filter(lambda x: x & (~R) == 0, S)
N = len(S)
if N == 0: #if there are no soldiers left then there can be no possible solutions at all
	print 0
else:
	count_memoized = {}
	stack = []
	stack.append((0,0))
	count = 0 
	while(len(stack)!=0):
		print stack
		current_soldier, current_skills = stack.pop()
		if current_skills == R:
			temp = count_memoized[(current_soldier, current_skills)] = pow(2,N-current_soldier, mod_value)
			count = mod_add(count, temp)
		elif current_soldier == N:
			continue
		elif (current_soldier, current_skills) in count_memoized:
			count = mod_add(count,count_memoized[(current_soldier,current_skills)])
		else:
			new_data = (current_soldier + 1, current_skills | S[current_soldier] )
			if new_data in count_memoized:
				count = mod_add(count, count_memoized[new_data])
			else:
				stack.append(new_data)
			new_data = (current_soldier + 1, current_skills )
			if new_data in count_memoized:
				count = mod_add(count, count_memoized[new_data])
			else:
				stack.append(new_data)
	print count