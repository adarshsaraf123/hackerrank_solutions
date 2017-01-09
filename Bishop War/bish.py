# Enter your code here. Read input from STDIN. Print output to STDOUT
debug = False
key_ca = lambda x: len(columns_available[x])
if debug:
	def print_attacked(level, attacked):
		print 
		for row in attacked:
			print level*'\t', row
attacks = [(-1,-1),(-1,1),(1, 1), (1,-1)]
def depth_first_search(posx, posy, attacked, columns_available, bishops_placed):#, location):
    #at each call, the bishop can be placed in the given cell of the board since we check the validity before calling
    attacked = [list(attacked[i]) for i in range(N)]
    columns_available = {x:list( columns_available[x] ) for x in columns_available if x!= posx}
    #del columns_available[posx] #since this row has to no more occur in the rows to be explored
    bishops_placed += 1
    if debug:
		print posx*'\t', posx, posy#, location
		#print_attacked(posx, attacked)
    if bishops_placed == N: #implies this was the last row to be explored and hence represents a valid solution
		if debug:
			print "FOUND:", posx, posy
		return 1
    
    for dx, dy in attacks: #to update the attacked squares upon addition of a bishop at this location
        if debug:
			print "\ndirection:", dx, dy
        x = posx + dx
        y = posy + dy
        while x > -1 and x < N and y > -1 and y < M and unblocked[x][y]:
            attacked[x][y] = True
            if x in columns_available:
				try:
					columns_available[x].remove(y)
				except ValueError:
					pass
            x += dx
            y += dy
        if debug:
			print_attacked(bishops_placed, attacked)
    if debug:
		print posx*'\t', columns_available
    count = 0
    posx = min(columns_available, key = key_ca)
    for posy in columns_available[posx]: #check all the possible cells in the next row to add the bishop 
        if not attacked[posx][posy] and unblocked[posx][posy]: #a bishop can be placed at this cell
			count += depth_first_search(posx, posy, attacked, columns_available, bishops_placed)#, location)
    return count

N, M = map(int, raw_input().split())
unblocked = [map(lambda c: True if c == '.' else False, list(raw_input())) for _ in range(N)]
attacked = [[False for _ in range(M)] for _ in range(N)]
#location = [-1] * N
columns_available = {x:[y for y in range(M) if unblocked[x][y] ] for x in range(N)}
posx = min(columns_available, key = key_ca)
count = 0
for posy in columns_available[posx]:
	if debug:
			print "\n\nRESTART", posx, posy
	if unblocked[posx][posy]: # a bishop can be placed here
		count += depth_first_search(posx, posy, attacked, columns_available, 0)#, location)
print count
