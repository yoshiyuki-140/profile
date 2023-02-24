// coding:utf-8
// Author : Yoshiyuki Kurose
// world_size : (width,height) ; 高さと幅の最大値は255でないといけない (-1-) ;
// 8bit int がたの数値の最大値は255 ,2**8==256 これにより(-1-)のような制限がかかる

#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>

// この関数は完成済み
void allDeath(uint8_t world_size[2], bool world[world_size[1]][world_size[0]])
{
    // world_size : [width,height]
    for (uint8_t y = 0; y < world_size[1]; y++)
    {
        for (uint8_t x = 0; x < world_size[0]; x++)
        {
            world[y][x] = false;
        }
    }
}

// この関数は完成済み
void copyWorld(uint8_t world_size[2], bool in[world_size[1]][world_size[0]], bool out[world_size[1]][world_size[0]])
{
    // - worldとtmp_worldは２次元配列のメモリアドレスを格納している
    // - world_sizeはworldとtmp_worldの各次元の配列の長さを格納している長さ2の配列で、
    //   引数として受け取るのはそのメモリアドレス,
    //   この場合,worldの大きさとtmp_worldの大きさは同じでないといけない
    // world_size : [width,height]

    for (uint8_t y = 0; y < world_size[1]; y++)
    {
        for (uint8_t x = 0; x < world_size[0]; x++)
        {
            // tmp_world[y][x] = world[y][x];
            if (in[y][x])
            {
                out[y][x] = true;
            }
            else
            {
                out[y][x] = false;
            }
        }
    }
}

// 完成済み
void printWorld(uint8_t world_size[2], bool world[world_size[1]][world_size[0]])
{
    // world_size : [width,height]
    for (uint8_t y = 0; y < world_size[1]; y++)
    {
        for (uint8_t x = 0; x < world_size[0]; x++)
        {
            if (world[y][x] == true)
            {
                printf("x");
            }
            else
            {
                printf(".");
            }
        }
        printf("\n");
    }
    // カーソルを左上に動かす
}

// この関数は完成済み
void createGrider(uint8_t world_size[2], bool world[world_size[1]][world_size[0]], uint8_t dest[2])
{
    // world_size : [width,height]
    // dest       : [x,y] : (座標はガウス平面っぽく指定してね)
    uint8_t x, y;
    uint8_t width, height;

    width = world_size[0];
    height = world_size[1];

    // ポインタ引数'dest'で指定できる座標は下の文字'a'の位置
    // .......
    // ...x...
    // ...ax..
    // ..xxx..
    // .......

    if (dest != NULL) // ここの判定は改善の余地あり!!
    {
        x = dest[0];
        y = dest[1];
        world[(y - 1) % height][(x - 1) % width] = false;
        world[(y - 1) % height][(x) % width] = true;
        world[(y - 1) % height][(x + 1) % width] = false;
        world[(y) % height][(x - 1) % width] = false;
        world[(y) % height][(x) % width] = false;
        world[(y) % height][(x + 1) % width] = true;
        world[(y + 1) % height][(x - 1) % width] = true;
        world[(y + 1) % height][(x) % width] = true;
        world[(y + 1) % height][(x + 1) % width] = true;
    }
    else
    {
        // c言語にはpythonにあった'デフォルト引数'というシステムがないので
        // else文を使用してデフォルト引数を定めてみる(うまくいくといいなあ
        // ここでは
        // dest : [1,1]
        // とする
        x = 2;
        y = 2;
        world[(y - 1) % height][(x - 1) % width] = false;
        world[(y - 1) % height][(x) % width] = true;
        world[(y - 1) % height][(x + 1) % width] = false;
        world[(y) % height][(x - 1) % width] = false;
        world[(y) % height][(x) % width] = false;
        world[(y) % height][(x + 1) % width] = true;
        world[(y + 1) % height][(x - 1) % width] = true;
        world[(y + 1) % height][(x) % width] = true;
        world[(y + 1) % height][(x + 1) % width] = true;
    }
}

// この関数は完成済み
void resetScreen(uint8_t world_height)
{
    printf("\x1b[%iF", world_height);
}

// この関数は未完成（テストがまだ(コンパイルはできた)
uint8_t countCells(uint8_t world_size[2], bool world[world_size[1]][world_size[0]], uint8_t dest[2])
{
    uint8_t width, height;
    uint8_t x, y;

    uint8_t count = 0;

    width = world_size[0];
    height = world_size[1];
    x = dest[0];
    y = dest[1];

    // x % y == (x + n*y)%y
    // という性質を使用するためにwhileで数を整える

    while (x < width)
    {
        x += width;
    }
    while (y < height)
    {
        y += height;
    }
    
    
    if (world[(y - 1) % height][(x - 1) % width] == true)
    {
        count++;
    }
    if (world[(y - 1) % height][(x) % width] == true)
    {
        count++;
    }
    if (world[(y - 1) % height][(x + 1) % width] == true)
    {
        count++;
    }
    if (world[(y) % height][(x - 1) % width] == true)
    {
        count++;
    }
    if (world[(y) % height][(x + 1) % width] == true)
    {
        count++;
    }
    if (world[(y + 1) % height][(x - 1) % width] == true)
    {
        count++;
    }
    if (world[(y + 1) % height][(x) % width] == true)
    {
        count++;
    }
    if (world[(y + 1) % height][(x + 1) % width] == true)
    {
        count++;
    }
    return count;
}

//  この関数は完成
bool judge(uint8_t world_size[2], bool world[world_size[1]][world_size[0]], uint8_t dest[2])
{
    // この関数はdestで指定指定されたセルが次の時代で生きるか死ぬかを判定する
    // true  : 次の世代で指定されたセルは生きる
    // false : 次の世代で指定されたセルは死ぬ
    // world_size : [width,height]
    uint8_t count = countCells(world_size, world, dest);
    if (world[dest[1]][dest[0]])
    {
        if (count == 2 || count == 3)
        {
            return true;
        }
        return false;
    }
    if (count == 3)
    {
        return true;
    }
    return false;
}

// この関数は未完成(コンパイルはできた)
void update(uint8_t world_size[2], bool world[world_size[1]][world_size[0]])
{
    // world_size : [width,height]
    // この関数はworldの状態の更新を定義する。
    // その時に使用する
    bool tmp_world[world_size[1]][world_size[0]];
    // tmp_worldの初期化
    allDeath(world_size, tmp_world);
    copyWorld(world_size, world, tmp_world); // tmp_worldにworldのコピーを保存

    // 各要素に対して判定を行いそれを適用する、つまり、tmp_worldの中身が変更される
    // worldはその時の判定に使用する
    // worldは最後にtmp_worldに格納された内容をコピーすることで一回のみ変更する
    for (uint8_t y = 0; y < world_size[1]; y++)
    {
        for (uint8_t x = 0; x < world_size[0]; x++)
        {
            uint8_t dest[2] = {x, y}; // セルの生死を決める時にjudge関数を呼び出す。この時に配列で渡さないといけないから、
            if (judge(world_size, world, dest))
            {
                tmp_world[y][x] = true;
            }
            else
            {
                tmp_world[y][x] = false;
            }
        }
    }
    // tmp_worldの内容をworldにコピーする
    // ここにバグあり <-gccコンパイラに'-O2'つまり最適化オプションを加えると、解決した.
    // 配列のコピーで失敗するなんでだろーね
    copyWorld(world_size, tmp_world, world);
}