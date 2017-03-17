from itertools import combinations
from keyword import kwlist

for combo in combinations(kwlist, 2):
    print(*combo)
