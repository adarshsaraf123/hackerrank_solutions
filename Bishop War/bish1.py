# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
attacks = [(-1,-1),(-1,1),(1, 1), (1,-1)]
def depth_first_search(posx, posy, attacked):#, location):
    #at each call, the bishop can be placed in the given cell of the board since we check the validity before calling
    attacked = [list(attacked[i]) for i in range(N)]
    if posx == N-1: #implies this was the last row to be explored and hence represents a valid solution
		return 1
    for dx, dy in attacks: #to update the attacked squares upon addition of a bishop at this location
        x = posx + dx
        y = posy + dy
        while x > -1 and x < N and y > -1 and y < M and unblocked[x][y]:
            attacked[x][y] = True
            x += dx
            y += dy    
    count = 0
    posx += 1
    for y in range(M): #check all the possible cells in the next row to add the bishop 
        if not attacked[posx][y] and unblocked[posx][y]: #a bishop can be placed at this cell
			count += depth_first_search(posx, y, attacked)#, location)
    return count

N, M = map(int, raw_input().split())
unblocked = [map(lambda c: True if c == '.' else False, list(raw_input())) for _ in range(N)]
attacked = [[False for _ in range(M)] for _ in range(N)]
#location = [-1] * N
count = 0
for y in range(M):
    if unblocked[0][y]: # a bishop can be placed here
		count += depth_first_search(0, y, attacked)#, location)
print count
