import time
def calculate_time(func):
    """
    Calculate execution time of a function.

    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds")
        return result

    return wrapper


n = 40

# =============================================recursion ===============================================================
# f(n) = f(n-1) + f(n-2)
@calculate_time
def recursion():
    def fib(n):
        if n <= 1:
            return n
        return fib(n-1) + fib(n-2)
    return fib(n)

ans =recursion()
print("recursion ans : ",ans)
# =========================================================================================================================



# =============================================== using DP  ==============================================================
 
dct = {}
@calculate_time
def dp():
    def fib_dp(n):
        if n <= 1:
            return n
        
        if dct.get(n):
            return dct[n]
        dct[n] = fib_dp(n-1) + fib_dp(n-2)
        return dct[n]
    return fib_dp(n)


dp_ans = dp()
print("dp : ", dp_ans)

# =======================================================================================================================



# ================================================== using bottom up (tabular approch) ====================================
@calculate_time
def fib_tab(n):
    dp_dict = {}
    dp_dict[0] = 0
    dp_dict[1] = 1

    for idx in range(2, n+1):
        dp_dict[idx] = dp_dict[idx-1] + dp_dict[idx-2]
    return dp_dict[idx]

tab_ans = fib_tab(n)
print("fib_tab ans : ", tab_ans)

# ==========================================================================================================================



# ============================================== using space optimization ===================================================
@calculate_time
def fib_tab_space_opt(n):
    previews2 = 0
    previews1 = 1
    
    for idx in range(2, n+1):
        current = previews1 + previews2
        previews2 = previews1
        previews1 = current
    return previews1
space_opt = fib_tab_space_opt(n)
print("fib_tab_space_opt :", space_opt)




# ========================================= output ====================================================================
"""
recursion took 34.90573787689209 seconds
recursion ans :  102334155
dp took 3.24249267578125e-05 seconds
dp :  102334155
fib_tab took 1.71661376953125e-05 seconds
fib_tab ans :  102334155
fib_tab_space_opt took 2.86102294921875e-06 seconds
fib_tab_space_opt : 102334155

"""