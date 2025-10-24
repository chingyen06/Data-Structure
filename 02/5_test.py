def product_rec(n, m):
    if (m == 1):
        return n
    else:
        return n + product_rec(n, m-1)
    
def product_ite(n, m):
    result = 0

    for i in range(m):
        result += n

    return result

#---------------------------------------------------------timeit
import timeit as ti

#---------------------------------------------------------Method 1
print("Running time comparison (Timer Method 1):")
tstart = ti.default_timer() #timer start 計時器開啟
for i in range(10000):
    product_rec(80, 700)
tend = ti.default_timer() #timer end計時器關閉
t_rec=tend - tstart#開始與結束的差值

tstart = ti.default_timer() #timer start 計時器開啟
for i in range(10000):
    product_ite(80, 700)
tend = ti.default_timer() #timer end計時器關閉
t_ite=tend - tstart#開始與結束的差值
print("Recursion 80*700=", product_rec(80, 700),"Iteration 80*700=", product_ite(80, 700))
print("Recursive approach:", t_rec)
print("iterative approach:", t_ite)

#---------------------------------------------------------Method 2
print("Running time comparison (Timer Method 2):")
t_rec = ti.timeit("product_rec(80, 700)", setup="from __main__ import product_rec", number = 10000)#timeit(函數名稱,執行次數)
t_ite = ti.timeit("product_ite(80, 700)", setup="from __main__ import product_ite", number = 10000)

print("Recursion 80*700=", product_rec(80, 700),"Iteration 80*700=", product_ite(80, 700))
print("Recursive approach:", t_rec)
print("Iterative approach:", t_ite)