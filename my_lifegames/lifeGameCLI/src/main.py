#coding:utf-8

import gameRule
import time
from outputUtil import printWorld

def main():
    generation = input("何世代まで見たい?\n> ")
    if generation.isdecimal():
        generation = int(generation)
        if generation == 0:
            print("0世代には世界がそもそも存在しないんだよね")
    else:
        print("ちょっと何言ってるかわからないです...")
        print("とりあえず10世代まで見るね")
        generation = 10

    
    world_size = (10, 10)
    delay = 0.5

    gR = gameRule.GameOfLife(world_size)
    gR.createGlider()

    print('\n'*world_size[1])    # 画面の高さ分の改行

    # main
    for _ in range(generation):
        printWorld(gR.world)
        gR.update()
        time.sleep(delay)

if __name__ == "__main__":
    main()
