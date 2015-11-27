def sieve(n): # 4
	ps = [] 
	sieve = [True] * (n+1) # highest index 4
	for p in range(2, n+1): 
		if sieve[p]: # sieve[4]
			ps.append(p)
			for i in range(p*p, n+1, p): # range(4, 7, 2)   
				print "outer loop", p
				print "inner loop", i
				sieve[i] = False
	
	return ps

print "Sieve of Erastosthenes, O(n log log n)"
print sieve(6)

