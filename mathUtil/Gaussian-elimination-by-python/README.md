# Gaussian elimination

- やってみたこと

行列の掃き出し法をpythonで実装してみました。大学で掃き出し法を習ったときに先生が「コンピュータはもっとごり押しで計算するけどね」とおっしゃってたことがきっかけです。
- 実行例

linuxでの実行例です、windowsでもpowershellでは同じような感じです。
```sh
 $ python3 main.py
How many dimensions? : 3
Please input 1 row of the matrix >> 1 1 -1
Please input 2 row of the matrix >> 1 -1 1
Please input 3 row of the matrix >> -1 1 1
[0.5, 0.5, 0.0]
[0.5, 0.0, 0.5]
[0.0, 0.5, 0.5]
```

3x3の行列の逆行列を求めます。
最初の行で何x何の行列かを聞いてきますので求めたい行列の行の数を入力してください。
ここでは
```
1 1 -1
1 -1 1
-1 1 1
```
の行列の逆行列を計算しています。

- モジュール使え！(大声)

楽しくない！(同じ音量で)
