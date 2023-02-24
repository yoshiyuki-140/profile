#coding:utf-8
# Author : Yoshiyuki Kurose

def ask_dimension(message=False):
    if message:
        dimension = int(input("How many dimensions? : "))
    else:
        dimension = int(input())
    if dimension < 1:
        raise ValueError("The dimension must be more than 1")
    return dimension


def ask_matix(dimension: int, message=False):
    if message:
        matrix = [[int(x) for x in input(f"Please input {i+1} row >>> ").split()]
                  for i in range(dimension)]
    else:
        matrix = [[int(x) for x in input().split()]
                  for _ in range(dimension)]

    return matrix
