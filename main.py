import logging


logger = logging.getLogger("errorLogger")
logger.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def returnIntegers(arr):
    if len(arr) == 0:
        return arr
    if len(arr)%10 != 0:
        logger.error('Error: The length of this array is not a multiple of 10')
    res = []
    for i in range(len(arr)):
        if type(arr[i]) != int:
            return []
        if i%2 != 0 and i % 3 != 0:
            res.append(arr[i])
    return res

test1 = [2, 5, 20, 10]
test2 = [10, 2, 9, 3, 0, 1, 19, 8, 0]
print(returnIntegers([10, 2, 9, 3, 0, 1, 19, 8, 0, 67, 12, 15]))
# [2, 1, 8]
# assert returnIntegers([2, 5, 20, 10]) == []




