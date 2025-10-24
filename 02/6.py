def chebyshev_recursive(x):
    if (x == 0):
        return [1]
    elif (x == 1):
        return [1, 0]
    else:
        temp1 = chebyshev_recursive(x - 1)
        temp2 = chebyshev_recursive(x - 2)
        result = list()

        for i in range(len(temp1)):
            result.append(temp1[i] * 2)

        result.append(0)

        offset = len(result) - len(temp2)
        
        for i in range(0, len(temp2)):
            result[i+offset] -= temp2[i]

        return result
    

def chebyshev_memoreccu(x, m_table):
    if (m_table[x] is not None):
        return m_table[x]
    if (x == 0):
        result = [1]
    elif (x == 1):
        result = [1, 0]
    else:
        temp1 = chebyshev_memoreccu(x - 1, m_table)
        temp2 = chebyshev_memoreccu(x - 2, m_table)
        result = list()

        for i in range(len(temp1)):
            result.append(temp1[i] * 2)

        result.append(0)

        offset = len(result) - len(temp2)
        
        for i in range(0, len(temp2)):
            result[i+offset] -= temp2[i]

    m_table[x] = result
    return result

def chebyshev_addoutrec(x):
    def linear_recursive(x, prev_x1, prev_x2):
        if (x == 0):
            return prev_x2
        elif (x == 1):
            return prev_x1
        else:
            result = list()

            for i in range(len(prev_x1)):
                result.append(prev_x1[i] * 2) # T[x] = 2 * T[x-1]

            result.append(0) # T[x] = x * T[x]

            offset = len(result) - len(prev_x2)
            
            for i in range(len(prev_x2)):
                result[i+offset] -= prev_x2[i]  # T[x] = T[x] - T[x-2]

            return linear_recursive(x - 1, result, prev_x1)

    return linear_recursive(x, [1, 0], [1])

def chebyshev_iterative(x):
    prev_n2 = [1]
    prev_n1 = [1, 0]

    memo = [prev_n2, prev_n1]

    if (x <= 1):
        return memo[x]
    else:
        for i in range(2, x + 1):
            temp1 = memo[i-1]
            temp2 = memo[i-2]
            result = list()
            for j in range(len(temp1)):
                result.append(temp1[j] * 2)
            result.append(0)
            offset = len(result) - len(temp2)
            for j in range(0, len(temp2)):
                result[j+offset] -= temp2[j]
            memo.append(result)
        return memo[x]

def main():
    n = int(input())

    for n in range(11):
        print(f"The coefficients of T_{n}(x) in list = {chebyshev_recursive(n)}")

    for n in range(11):
        m_table=[None] * (n+1)
        print(f"The coefficients of T_{n}(x) in list = {chebyshev_memoreccu(n, m_table)}")

    for n in range(11):
        print(f"The coefficients of T_{n}(x) in list = {chebyshev_addoutrec(n)}")

    for n in range(11):
         print(f"The coefficients of T_{n}(x) in list = {chebyshev_iterative(n)}")

main()

"""
The coefficients of T_0(x) in list = [1]
The coefficients of T_1(x) in list = [1, 0]
The coefficients of T_2(x) in list = [2, 0, -1]
The coefficients of T_3(x) in list = [4, 0, -3, 0]
The coefficients of T_4(x) in list = [8, 0, -8, 0, 1]
The coefficients of T_5(x) in list = [16, 0, -20, 0, 5, 0]
The coefficients of T_6(x) in list = [32, 0, -48, 0, 18, 0, -1]
The coefficients of T_7(x) in list = [64, 0, -112, 0, 56, 0, -7, 0]
The coefficients of T_8(x) in list = [128, 0, -256, 0, 160, 0, -32, 0, 1]
The coefficients of T_9(x) in list = [256, 0, -576, 0, 432, 0, -120, 0, 9, 0]
The coefficients of T_10(x) in list = [512, 0, -1280, 0, 1120, 0, -400, 0, 50, 0, -1]
"""