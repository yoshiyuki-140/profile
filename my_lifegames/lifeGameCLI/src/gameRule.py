#coding:utf-8
# Author : Yoshiyuki Kurose

from copy import deepcopy

# Game rules


class GameOfLife:
    """
    このライフゲームの要となる法則を定義している。
    """

    def __init__(self, world_size: tuple):
        #世界の大きさdefoultで10
        self.world_size = world_size
        self.allDeath()  # ここでself.worldクラス変数が定義される
        self.tmp_world = deepcopy(self.world)

    def allDeath(self):
        """
        """
        self.world = [[False for _ in range(
            self.world_size[0])] for _ in range(self.world_size[1])]

    def update(self):
        """世代交代
        """
        for y in range(self.world_size[1]):
            for x in range(self.world_size[0]):
                self.tmp_world[y][x] = self.judge(x, y)
        self.world = deepcopy(self.tmp_world)

    def createGlider(self, x=0, y=0):
        """conway's game of life における グライダーを作成する
        x,yはworldの中のy行x列の座標を表す
        x,yはこのメソッドが作成するべきグライダーの左上の座標を示している
        """
        try:
            self.world[y+1][x+1] = True
            self.world[y+1][x+2] = False
            self.world[y+1][x+3] = True
            self.world[y+2][x+1] = False
            self.world[y+2][x+2] = True
            self.world[y+2][x+3] = True
            self.world[y+3][x+1] = False
            self.world[y+3][x+2] = True
            self.world[y+3][x+3] = False
        except:
            raise IndexError("引数に指定された座標に世界は存在しないみたいですYO!")

    def judge(self, x, y):
        """次の時代lifeならTrueを返すdeathならFalseをかえす
        """

        count = self.countCells(x, y)
        # 最後のジャッジ変更した
        if self.world[y][x]:
            if count == 2 or count == 3:
                return True
            return False
        else:
            if count == 3:
                return True
            return False

    def countCells(self, x, y):
        """周辺の状態をカウントする
        """
        count = 0

        for yi in range(-1, 2):
            for xi in range(-1, 2):
                if 0 == xi and 0 == yi:
                    continue
                if self.world[(y+yi) % self.world_size[1]][(x+xi) % self.world_size[0]] == True:
                    count += 1

        return count
