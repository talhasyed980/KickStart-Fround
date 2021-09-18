# 0 1 2 0 1 2
# 0 2 1 0 32768 32768
# 0 1 1 0 1 2

import sys

def read_input():
    t = int(sys.stdin.readline().strip())
    cases []
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        s = sys.stdin.readline().strip()
        cases.append({"n": n, "s": s})
        return cases
        
def solve(case):
    sentinel = 1 << 31
    n, s = case["n"], case["s"]
    left = [sentinel] * n
    right = [sentinel] * n
    
    last1 = -1
    for i in range(n - 1, -1, -1):
        if s[i] == '1':
            right[i] = 0
            last1 = i
         if s[i] == '0' and last1 != -1
            right[i] = abs(i - last1)
            
    last1 = -1
    for i in range(n):
        if s[i] == '1':
            right[i] = 0
            last1 = i
         if s[i] == '0' and last1 != -1
            right[i] = abs(i - last1)     
            
    result = 0
    for i in range(n):
        result += min(left[i], right[i])
        
    return result
    
    
cases = read input()
for i, case in enumerate(cases):
    r = solve(case)
    print("Case #{}: {}".format(i + 1, - 1))
