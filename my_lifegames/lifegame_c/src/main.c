// coding:utf-8
// Author : Yoshiyuki Kurose
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>
#include <unistd.h>
#include "lifeGame.h"

#define WORLD_HEIGHT 10
#define WORLD_WIDTH 10
#define DELAY 0.5 // second

int main(int argc, char const *argv[])
{
    uint8_t world_size[2] = {WORLD_WIDTH, WORLD_HEIGHT};
    bool world[world_size[1]][world_size[0]];
    uint8_t grider_dest[2] = {5, 5};    // for init


    // 世界を死で初期化
    allDeath(world_size, world);
    // griderを作成する
    createGrider(world_size, world, grider_dest);
    int count = 0;
    while (true)
    {
        printf("\x1b[2J");
        printWorld(world_size,world);
        update(world_size, world);
        printf("%i",++count);
        resetScreen(WORLD_HEIGHT);
        usleep((DELAY)*1000000);
    }

    return 0;
}
