n = 25

# =============================================recursion ===============================================================
# f(n) = f(n-1) + f(n-2)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

ans =fib(n)
print("recursion ans : ",ans)
# =========================================================================================================================



# =============================================== using DP  ==============================================================
 
dct = {}
def fib_dp(n):
    if n <= 1:
        return n
    
    if dct.get(n):
        return dct[n]
    dct[n] = fib_dp(n-1) + fib_dp(n-2)
    return dct[n]


dp_ans = fib_dp(n)
print("dp ans : ", dp_ans)

# =======================================================================================================================



# ================================================== using bottom up (tabular approch) ====================================
def fib_tab(n):
    dp_dict = {}
    dp_dict[0] = 0
    dp_dict[1] = 1

    for idx in range(2, n+1):
        dp_dict[idx] = dp_dict[idx-1] + dp_dict[idx-2]
    return dp_dict[idx]

tab_ans = fib_tab(n)
print("dp tab ans : ", tab_ans)

# ==========================================================================================================================



# ============================================== using space optimization ===================================================

def fib_tab_space_opt(n):
    previews2 = 0
    previews1 = 1
    
    for idx in range(2, n+1):
        current = previews1 + previews2
        previews2 = previews1
        previews1 = current
    return previews1
space_opt = fib_tab_space_opt(n)
print("spce optimized fibonacci :", space_opt)