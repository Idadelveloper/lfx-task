def returnIntegers(arr):
    if len(arr)%10 != 0:
        msg = 'The length of the array' + '(' + str(arr) + ')' + ' is not a multiple of 10'
        raise Exception(msg)
    res = []
    for i in range(len(arr)):
        if i%2 != 0 and i % 3 != 0:
            res.append(int(arr[i]))
    return res


