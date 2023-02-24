#coding:utf-8
# Author : Yoshiyuki Kurose

import doctest
from copy import deepcopy


def findCofactor(dimension: int, matrix: list, k: int):
    """
    # k >= 1
    >>> CalculationUtil().findCofactor(3,[[1,2,3],[1,2,3],[1,3,4]],2)
    {'head': -2, 'matrix': [[1, 3], [1, 4]]}
    >>> CalculationUtil().findCofactor(3,[[1,2,3],[1,2,3],[1,3,4]],1)
    {'head': 1, 'matrix': [[2, 3], [3, 4]]}
    """

    result = {
        'head': pow(-1, k+1)*matrix[0][k-1],
        'matrix': None}
    tmpMatrix = deepcopy(matrix)
    # 1行目を削除
    del tmpMatrix[0]
    # k列目を削除
    for i in range(dimension-1):
        del tmpMatrix[i][k-1]
    result['matrix'] = tmpMatrix

    return result


def calcDeterminant(dimension: int, matrix: list):
    result = []
    if dimension == 1:
        result = matrix
    elif dimension == 2:
        # when dimension is two
        result = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        for i in range(1, dimension+1):
            cofactor = findCofactor(dimension, matrix, i)
            result.append(
                cofactor['head']*calcDeterminant(dimension-1, cofactor['matrix']))
        result = sum(result)

    return result


if __name__ == '__main__':
    doctest.testmod()
