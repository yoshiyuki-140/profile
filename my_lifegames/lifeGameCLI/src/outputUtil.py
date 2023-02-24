#coding:utf-8
# Author : Yoshiyuki Kurose

# - printWorldについて
# worldの内容をCLIに表示する関数
# 引数worldは2次元配列


def printWorld(world:list):
    """
    """
    print(f'\x1b[{len(world)+1}A') #カーソルを元の位置に戻す.ANSIエスケープコードを使用している

    for row in world:
        for b in row:
            # if b == None:
            #     raise ValueError("b must be bool value")
            if b:
                print('x',end='')
            else:
                print('.',end='')
        print() # 改行のため
