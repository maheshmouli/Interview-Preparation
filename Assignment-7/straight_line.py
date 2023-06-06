def straight_line(array):
    n = len(array)
    print(n)
    # if n == 2:
    #     return True
    if n >= 2:
        for i in range(n-2):
            if (array[i+1][1]-array[i][1])*(array[i+2][0]-array[i+1][0]) != (array[i+1][0]-array[i][0])*(array[i+2][1]-array[i+1][1]):
                return False
        return True 
    return False

array = [[1,2], [2,3]]
print(straight_line(array))