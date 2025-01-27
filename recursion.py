def tri_recursion(k):
    if (k>0):
        result = k+tri_recursion(k-1)
        #print(result)
    else:
        result = k
    return result

print(tri_recursion(6))
