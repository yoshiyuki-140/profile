
import java.util.Scanner;

class LifeGame {
    boolean[][] world;
    boolean[][] tmpworld;
    int[] world_size;
    int Dimension;

    LifeGame() {
        // default value of dimension.
        this.Dimension = 10;
        this.world_size = new int[2];
        this.world_size[0] = Dimension;
        this.world_size[1] = Dimension;
        // """ ここほかに移したほうがいいかも
        // """
        world = new boolean[world_size[1]][world_size[0]];
        tmpworld = new boolean[world_size[1]][world_size[0]];
        this.worldInit(world);
        this.worldInit(tmpworld);
    }

    LifeGame(int world_size[]) {
        // default value of dimension.
        this.Dimension = 10;
        // ここの処理はif 分で引数world_size
        this.world_size = new int[2];
        this.world_size[0] = world_size[0];
        this.world_size[1] = world_size[1];
        // """ ここほかに移したほうがいいかも
        // """
        world = new boolean[world_size[1]][world_size[0]];
        tmpworld = new boolean[world_size[1]][world_size[0]];
        this.worldInit(world);
        this.worldInit(tmpworld);
    }

    LifeGame(int width,int height) {
        // default value of dimension.
        this.world_size = new int[2];
        this.world_size[0] = width;
        this.world_size[1] = height;
        // """ ここほかに移したほうがいいかも
        // """
        world = new boolean[world_size[1]][world_size[0]];
        tmpworld = new boolean[world_size[1]][world_size[0]];
        this.worldInit(world);
        this.worldInit(tmpworld);
    }

    void worldInit(boolean world[][]) {
        for (int yi = 0; yi < world_size[1]; yi++) {
            for (int xi = 0; xi < world_size[0]; xi++) {
                world[yi][xi] = false;
            }
        }
    }

    void setWorldSize(int world_size[]) {
        this.world_size[0] = world_size[0];
        this.world_size[1] = world_size[1];
    }

    int howManyAliveCells(int x, int y) {
        int counter = 0;
        int fx = x;
        int fy = y;

        // x%y==(x+n*y)%y
        // の性質を利用するためにwhileを使用
        while (fx < world_size[0]) {
            fx += world_size[0];
        }
        while (fy < world_size[1]) {
            fy += world_size[1];
        }

        for (int yi = fy - 1; yi <= fy + 1; yi++) {
            for (int xi = fx - 1; xi <= fx + 1; xi++) {
                if (world[(yi) % this.world_size[1]][(xi) % this.world_size[0]]) {
                    if ((fx == xi) && (fy == yi)) {
                        continue;
                    }
                    counter++;
                }
            }
        }
        return counter;
    }

    boolean isAliveCell(int x, int y) {
        int count = howManyAliveCells(x, y);
        if (world[y][x]) {
            if (count == 2 || count == 3) {
                return true;
            }
            return false;
        } else {
            if (count == 3) {
                return true;
            }
            return false;
        }
    }

    void copyWorld(boolean from[][], boolean to[][]) {
        for (int yi = 0; yi < world_size[1]; yi++) {
            for (int xi = 0; xi < world_size[0]; xi++) {
                to[yi][xi] = from[yi][xi];
            }
        }
    }

    void printWorld() {
        for (int yi = 0; yi < world_size[1]; yi++) {
            for (int xi = 0; xi < world_size[0]; xi++) {
                if (world[yi][xi]) {
                    System.out.print("x");
                } else {
                    System.out.print(".");
                }
            }
            // 改行
            System.out.println();
        }
    }

    void createGrider(int x, int y) {
        // arg x : x >= 1
        // arg y : y >= 1

        // x.x
        // .xx
        // .x.

        world[y - 1][x - 1] = true;
        world[y - 1][x] = false;
        world[y - 1][x + 1] = true;

        world[y][x - 1] = false;
        world[y][x] = true;
        world[y][x + 1] = true;

        world[y + 1][x - 1] = false;
        world[y + 1][x] = true;
        world[y + 1][x + 1] = false;
    }

    void update() {
        // this.copyWorld(world, tmpworld);

        for (int yi = 0; yi < world_size[1]; yi++) {
            for (int xi = 0; xi < world_size[0]; xi++) {
                tmpworld[yi][xi] = isAliveCell(xi, yi);
            }
        }
        copyWorld(tmpworld, world);
    }
}
