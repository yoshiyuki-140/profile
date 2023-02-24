// coding:utf-8
// Author : Yoshiyuki Kurose
// world_size : (width,height) ; 高さと幅の最大値は255 (-1-) ;
// 8bit int がたの数値の最大値は255 ,2**8==256 これにより(-1-)に書いてあることが定まる

#include <stdint.h>
#include <stdbool.h>

// 関数宣言だけを書いておく
void copyWorld(uint8_t world_size[2] ,bool world[world_size[1]][world_size[0]], bool tmp_world[world_size[1]][world_size[0]]);
void allDeath(uint8_t world_size[2],bool world[world_size[1]][world_size[0]]);
void printWorld(uint8_t world_size[2], bool world[world_size[1]][world_size[0]]);
void createGrider(uint8_t world_size[2], bool world[world_size[1]][world_size[0]], uint8_t dest[2]);
void resetScreen(uint8_t world_height);
uint8_t countCells(uint8_t world_size[2], bool world[world_size[1]][world_size[0]], uint8_t dest[2]);
bool judge(uint8_t world_size[2], bool world[world_size[1]][world_size[0]], uint8_t dest[2]);
void update(uint8_t world_size[2], bool world[world_size[1]][world_size[0]]);