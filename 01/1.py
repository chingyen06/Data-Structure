# Function to print all tupless present in a list with a given sum
def all_tuples(A, target):
    A = sorted(A)  #先排序

    result = list()

    n = len(A)  #list A 的索引數

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    Sum = A[i] + A[j] + A[k] + A[l]
                    if (Sum == target):
                        result.append((A[i], A[j], A[k], A[l]))

    return result

    
# Driver script
if __name__ == '__main__':
    
    A = [12, 21, 8, 7, 2, 5, 16, 19, 25, 14, 10]
    S = 34
    tuples=all_tuples(A, S)
    print(f"The input list is {A} and tuples summing to {S} are: {tuples}")

    S = 80
    tuples=all_tuples(A, S)
    print(f"The input list is {A} and tuples summing to {S} are: {tuples}")
    
    A = [2, 7, 4, 0, 9, 5, 1, 3]
    S = 20
    tuples=all_tuples(A, S)
    print(f"The input list is {A} and tuples summing to {S} are: {tuples}")