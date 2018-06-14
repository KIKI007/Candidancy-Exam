import math
import copy
import numpy
import json
import io
import os

N =  33
M =  33
V= [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0]

Normal = [ [ 0,0,1 ], [ 0,0.682318250360011,0.731055268242869 ], [ 0,-0.682318250360011,0.731055268242869 ], [ 0.682318250360011,0,0.731055268242869 ], [ 0.563618777559932,-0.563618777559932,0.603877261671356 ], [ 0.563618777559932,0.563618777559932,0.603877261671356 ], [ 0.319042273070035,0.319042273070034,0.892425938657439 ], [ 0.335637291070351,-0.335637291070351,0.880167721338333 ], [ -0.759256602365297,0,0.650791373455969 ], [ -0.447224262713539,0.808111795173499,0.383335082325891 ], [ -0.449725818928381,-0.806404916699167,0.384002341285318 ], [ 0,0,1 ], [ 0,0.90286051882393,0.429933580392348 ], [ -2.56608393221976E-16,-0.90286051882393,0.429933580392347 ], [ 0,-0.739940073395944,-0.672672793996313 ], [ 4.31286715821677E-18,0.739940073395943,-0.672672793996313 ], [ 0.850265146687862,0,0.526354614616296 ], [ 0.570431076996155,0.741560400095001,0.353124000045239 ], [ 0.570431076996155,-0.741560400095001,0.353124000045238 ], [ 0.877895572914384,0,-0.478852130680574 ], [ 0.578554853539199,-0.752121309600958,-0.315575374657744 ], [ 0.578554853539199,0.752121309600958,-0.315575374657745 ], [ 0,1,0 ], [ 0,-1,0 ], [ -0.563618777559932,-0.563618777559932,0.603877261671356 ], [ -0.682318250360011,0,0.731055268242869 ], [ -0.563618777559932,0.563618777559932,0.603877261671356 ], [ -0.343054657946701,-0.343054657946701,0.874429530220786 ], [ -0.343414797579955,0.343414797579955,0.874146757476247 ], [ 0,0,1 ], [ -0.132074532234037,-0.991239788313181,0 ], [ -0.133412012141539,0.991060661622863,0 ], [ 0,0,-1 ], ]

nojoint =  [[0, 4], [4, 0], [0, 5], [5, 0], [0, 24], [24, 0], [0, 26], [26, 0], [1, 3], [3, 1], [1, 6], [6, 1], [1, 25], [25, 1], [1, 28], [28, 1], [2, 3], [3, 2], [2, 7], [7, 2], [2, 25], [25, 2], [2, 27], [27, 2], [3, 6], [6, 3], [3, 7], [7, 3], [3, 9], [9, 3], [3, 10], [10, 3], [4, 8], [8, 4], [4, 10], [10, 4], [4, 23], [23, 4], [5, 8], [8, 5], [5, 9], [9, 5], [5, 22], [22, 5], [6, 8], [8, 6], [6, 9], [9, 6], [6, 22], [22, 6], [7, 8], [8, 7], [7, 10], [10, 7], [7, 23], [23, 7], [8, 12], [12, 8], [8, 13], [13, 8], [9, 11], [11, 9], [9, 15], [15, 9], [10, 11], [11, 10], [10, 14], [14, 10], [11, 17], [17, 11], [11, 18], [18, 11], [12, 16], [16, 12], [12, 21], [21, 12], [13, 16], [16, 13], [13, 20], [20, 13], [14, 18], [18, 14], [14, 19], [19, 14], [15, 17], [17, 15], [15, 19], [19, 15], [16, 20], [20, 16], [16, 21], [21, 16], [17, 19], [19, 17], [18, 19], [19, 18], [20, 32], [32, 20], [21, 32], [32, 21], [22, 26], [26, 22], [22, 28], [28, 22], [23, 24], [24, 23], [23, 27], [27, 23], [24, 29], [29, 24], [24, 30], [30, 24], [25, 27], [27, 25], [25, 28], [28, 25], [25, 30], [30, 25], [25, 31], [31, 25], [26, 29], [29, 26], [26, 31], [31, 26], [27, 29], [29, 27], [27, 30], [30, 27], [28, 29], [29, 28], [28, 31], [31, 28], [30, 31], [31, 30]]
center = [ [ -54,-7.5,25 ], [ -54,7.5,18 ], [ -54,-22.5,18 ], [ -20.5,-7.5,18 ], [ -22.9900800746889,-20.009919925311,15.6481494727527 ], [ -22.990080074689,5.00991992531105,15.6481494727527 ], [ -14.3461538461538,16.7307692307692,5.5 ], [ -14.3461538461539,-30.7692307692308,5.5 ], [ -3.99615301009751,-7.50962011745074,21.5044881548862 ], [ -1.02464339755337,3.22890570915065,18.164367063744 ], [ -1.02467600876244,-18.2675292380239,18.1631353514261 ], [ 17.5,-7.53846153846153,32 ], [ 17.5,4.96153846153847,21.5 ], [ 17.5,-20.0384615384615,21.5 ], [ 21,-20.0384615384615,5.50000000000001 ], [ 21,4.96153846153847,5.50000000000001 ], [ 36.5,-7.53846153846153,21.5 ], [ 34.265474237795,3.20204973130141,18.3045448724444 ], [ 34.265474237795,-18.2789728082245,18.3045448724444 ], [ 40,-7.53846153846154,5.50000000000001 ], [ 36.5486030092033,-18.4894537548372,7.39730363256798 ], [ 36.5486030092033,3.41253067791408,7.39730363256799 ], [ -54,15,5.5 ], [ -54,-30,5.5 ], [ -85.009919925311,-20.0099199253111,15.6481494727527 ], [ -87.5,-7.5,18 ], [ -85.0099199253111,5.00991992531104,15.6481494727527 ], [ -94,-30.0192307692308,5.50000000000001 ], [ -94,15,5.5 ], [ -115.860342400589,-7.51422157395509,11 ], [ -123,-11.2692307692308,5.49999999999999 ], [ -123,-3.76923076923076,5.5 ], [ -50.2619738009012,-7.31078333329507,1.00000000000002 ], ]

nohalvejoint = [[23, 32], [32, 23],
                [22, 32], [32, 22],
                [31, 32], [32, 31],
                [30, 32], [32, 30],
                [15, 32], [32, 15],
                [14, 32], [32, 14]]
#notenonjoint = [[18, 12], [18, 10], [18, 1], [18, 2]]
notenonjoint = []
order = []
search_list = range(9)
search_list.append(9)
search_list.append(10)
search_list.append(12)
search_list.append(13)
search_list.append(11)
for i in range(14, 24):
    search_list.append(i)
search_list.append(24)
search_list.append(25)
search_list.append(29)
search_list.append(30)
search_list.append(31)
search_list.append(26)
search_list.append(27)
search_list.append(28)
search_list.append(32)
print search_list

forbiden_move_vec = {7 : [0.70710678118654757, 0.70710678118654757, 0.0],
                     8 : [-0.6507913734559686, 3.4346207766550251e-16, -0.75925660236529646],
                     10: [-1.8514998103799575e-15, -0.42993358039234725, -0.90286051882393059],
                     27: [-0.70710678118654746, 0.70710678118654746, -0.0],
                     24: [-0.70710678118654746, 0.70710678118654746, -0.0],
                     26: [-0.70710678118654757, -0.70710678118654757, -0.0],
                     28: [-0.70710678118654757, -0.70710678118654757, -0.0]}


def strongly_connected_components_tree(vertices, edges):
    identified = set()
    stack = []
    index = {}
    lowlink = {}

    def dfs(v):
        index[v] = len(stack)
        stack.append(v)
        lowlink[v] = index[v]

        for w in edges[v]:
            if w not in index:
                # For Python >= 3.3, replace with "yield from dfs(w)"
                for scc in dfs(w):
                    yield scc
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif w not in identified:
                lowlink[v] = min(lowlink[v], lowlink[w])

        if lowlink[v] == index[v]:
            scc = set(stack[index[v]:])
            del stack[index[v]:]
            identified.update(scc)
            yield scc

    for v in vertices:
        if v not in index:
            # For Python >= 3.3, replace with "yield from dfs(v)"
            for scc in dfs(v):
                yield scc


def has_joint(u, v):
    if u == v:
        return False
    return bool(V[u * M + v])


def get_order(visited, id):
    if visited.get(id) != None:
        return visited[id]
    else:
        return len(visited)


def print_graph(joint_graph, visited, vec, num_vertices, dot_file, png_file):
    vertices = range(num_vertices + 1)
    edges = {}

    for id in range(num_vertices + 1):
        edges[id] = []

    for id in range(N):
        u = get_order(visited, id)
        for jd, edgevec in joint_graph[id].items():
            edgevec = VectorUnitize(edgevec)
            if VectorDotProduct(edgevec, vec) > -0.99:
                v = get_order(visited, jd)
                if v not in edges[u]:
                    edges[u].append(v)
    print_str = "digraph {\n"
    print_str += "label = \"["+ str(vec[0]) + ", " + str(vec[1]) + ", " + str(vec[2]) + "]\""
    for i in range(num_vertices + 1):
        for j in range(num_vertices + 1):
            if j in edges[i]:
                print_str += str(i) + " -> " + str(j) + "\n"
    print_str += "}"
    with open(dot_file, "w") as data_file:
        data_file.write(print_str)
    command = "dot -Tpng " + dot_file + " -o " + png_file;
    os.system(command)


def is_interlocking(joint_graph, visited, vec, num_vertices):
    vertices = range(num_vertices + 1)
    edges = {}

    for id in range(num_vertices + 1):
        edges[id] = []

    for id in range(N):
        u = get_order(visited, id)
        for jd, edgevec in joint_graph[id].items():
            edgevec = VectorUnitize(edgevec)
            if VectorDotProduct(edgevec, vec) > -0.999:
                v = get_order(visited, jd)
                if v not in edges[u]:
                    edges[u].append(v)
    for scc in strongly_connected_components_tree(vertices, edges):
        if (0 in scc) and (len(scc) > 1 and len(scc) < num_vertices):
            return False
        if len(scc) == 1 and list(scc)[0] != 0 and num_vertices > 1:
            return False
    return True


def delete_u_from_graph(u, graph):
    graph[u] = []
    for key, value in graph.items():
        if u in value:
            graph[key].remove(u)


def is_graph_connected(graph, num_non_empty_vertices):
    vertices = range(N)
    for scc in strongly_connected_components_tree(vertices, graph):
        if len(scc) == 1:
            if graph[list(scc)[0]] != []:
                return False
        elif len(scc) < num_non_empty_vertices:
            return False
    return True


def is_able_create_joint(visited, joint_graph, u, v):
    if [u, v] in nojoint:
        return False
    return True

def VectorCrossProduct(a, b):
    return numpy.cross(a, b)

def VectorDotProduct(a, b):
    return numpy.dot(a, b)

def VectorScale(a, r):
    b = a.copy()
    b[0] *= r
    b[1] *= r
    b[2] *= r
    return b

def Vector3f(a):
    return numpy.array([a[0], a[1], a[2]])

def VectorUnitize(a):
    len = math.sqrt(a[0] * a[0] + a[1] * a[1]+ a[2]* a[2])
    return VectorScale(a, 1.0 / len)

def create_joint(u, visited, joint_graph, connected_graph, joint, step, move):

    #print visited
    print u, step

    if step == N - 1:
        global input
        global graph
        global order
        global disvec
        visited[u] = step
        input = joint
        graph = joint_graph
        order = range(N)
        for v, index in visited.items():
            order[index] = v
        disvec = move
        print move
        disvec[u] = numpy.array([0,0,0]);
        for id, vec in move.items():
            dot_file = "/Users/ziqwang/Desktop/WorkSpace/planar_lizard/graph_" + str(id) + ".dot"
            png_file = "/Users/ziqwang/Desktop/WorkSpace/planar_lizard/graph_" + str(id) + ".png"
            print_graph(joint_graph, visited, vec , N - 1, dot_file, png_file)
        return True
        ##copy

    c_gh = copy.deepcopy(connected_graph)
    delete_u_from_graph(u, c_gh)
    candidates = []

    ## compute candidates:
    for v in range(N):
        if has_joint(u, v) and visited.get(v) == None and [u, v] not in nojoint:
            cc_gh = copy.deepcopy(c_gh)
            delete_u_from_graph(v, cc_gh)
            if is_graph_connected(cc_gh, N - step - 2):
                candidates.append(v)

    #if candidates == []:
        #return False

    ## add part
    new_visited = copy.deepcopy(visited)
    new_visited[u] = step
    is_all_joint_settled = True

    interlocking_dat = []

    for v in range(N):
        if (is_able_create_joint(visited, joint_graph, u, v) == False):
            continue
        if has_joint(u, v) and visited.get(v) == None:
            for sign in range(3):

                if [u, v] in nohalvejoint and sign != 2:
                    continue

                ## initialization
                is_all_joint_settled = False
                new_jt_gh = copy.deepcopy(joint_graph)
                new_move = copy.deepcopy(move)
                new_jt = copy.deepcopy(joint)
                number_of_joint = 0
                vec = []

                ## find direction halve joint
                vec = VectorCrossProduct(Normal[u], Normal[v])
                if sign == 1:
                    vec = VectorScale(vec, -1)
                elif sign == 2:
                    dot = VectorDotProduct(Normal[u], Normal[v])
                    if math.fabs(dot) > 0.0001:
                        continue
                    vec = numpy.array([Normal[v][0], Normal[v][1], Normal[v][2]])
                vec = VectorUnitize(vec)
                new_move[u] = VectorScale(vec, -1);

                #forbiden moving direction
                if forbiden_move_vec.get(u) != None:
                    forbidvec = forbiden_move_vec[u]
                    dot = VectorDotProduct(new_move[u], forbidvec)
                    if dot > 0.999:
                        continue

                ## create joints
                for w in range(N):
                    if has_joint(u, w):
                        if visited.get(w) == None:
                            if (is_able_create_joint(visited, joint_graph, w, u) == False):
                                new_jt.append([w, u, 2])
                                continue

                            #Tenon Joint
                            if [u, w] not in notenonjoint:
                                sgn = VectorDotProduct(center[w], Normal[w]) - VectorDotProduct(center[u], Normal[w])
                                normalw = numpy.array([Normal[w][0], Normal[w][1], Normal[w][2]])
                                if sgn < 0:
                                    normalw = VectorScale(normalw, -1)

                                if VectorDotProduct(vec, normalw) > 0.1:
                                    new_jt_gh[u][w] = vec
                                    new_jt_gh[w][u] = VectorScale(vec, -1)

                                    new_jt.append([u, w, 1, vec[0], vec[1], vec[2]])
                                    number_of_joint += 1
                                    continue

                            if [u, w] not in nohalvejoint:
                                #Halve Joint
                                edge_dir = VectorCrossProduct(Normal[u], Normal[w])
                                edge_dir = VectorUnitize(edge_dir)
                                edge_angle = VectorDotProduct(edge_dir, vec)
                                if edge_angle > 0.999:
                                    new_jt_gh[u][w] = vec
                                    new_jt_gh[w][u] = VectorScale(vec, -1)
                                    new_jt.append([u, w, 0, True])
                                    number_of_joint += 1
                                    continue
                                elif edge_angle < -0.999:
                                    new_jt_gh[u][w] = vec
                                    new_jt_gh[w][u] = VectorScale(vec, -1)
                                    new_jt.append([u, w, 0, False])
                                    number_of_joint += 1
                                    continue

                            #Non Joint
                            new_jt.append([w, u, 2])

                        elif joint_graph[w].get(u) != None:
                            if (is_able_create_joint(visited, joint_graph, w, u) == False):
                                return False

                ## check interlocking
                if (is_interlocking(new_jt_gh, new_visited, vec, step + 1)):
                    interlocking_dat.append([number_of_joint, new_jt_gh, new_jt, new_move])

    if is_all_joint_settled:
        cand = search_list[step + 1]
        new_jt_gh = copy.deepcopy(joint_graph)
        new_move = copy.deepcopy(move)
        new_jt = copy.deepcopy(joint)
        new_move[u] = numpy.array([Normal[u][0], Normal[u][1], Normal[u][2]]);
        for w in range(N):
            if has_joint(u, w):
                if visited.get(w) == None:
                    if (is_able_create_joint(visited, joint_graph, w, u) == False):
                        new_jt.append([w, u, 2])
        return create_joint(cand, new_visited, new_jt_gh, c_gh, new_jt, step + 1, new_move)
    elif interlocking_dat != []:
        interlocking_dat.sort(key = lambda dat : dat[0], reverse = True)
        cand = search_list[step + 1]
        for dat in interlocking_dat:
            print u, "-> ", dat
            if(create_joint(cand, new_visited, dat[1], c_gh, dat[2], step + 1, dat[3])):
                return True

    return  False


c_gh = {}
jt_gh = {}
visited = {}
jt = []
move = {}

for id in range(N):
    jt_gh[id] = {}

for id in range(N):
    c_gh[id] = []
    for jd in range(N):
        if has_joint(id, jd):
            c_gh[id].append(jd)

for u in [0]:
    if create_joint(u, visited, jt_gh, c_gh, jt, 0, move):
        print 'found'

        ##output input
        with open("/Users/ziqwang/Desktop/WorkSpace/planar_lizard/data.txt", "w") as data_file:
            json.dump(input, data_file)

        #output move
        move = [[] for id in range(33)]
        for u in order:
            v = disvec[u]
            move[u] = [v[0], v[1], v[2]]
        with open("/Users/ziqwang/Desktop/WorkSpace/planar_lizard/move.txt", "w") as data_file:
            json.dump(move, data_file)

        print order
        print move[27]
        print move[28]

        ##output animation
        animation = "Objects " + str(N) + "\n"
        for i in range(N):
            animation += "part_" + str(i) + ".obj "
        animation += "\n\n"
        for u in order:
            vec = disvec[u]
            vec = VectorScale(vec, 2)
            animation += "Begin Action " + str(180) + "\n"
            animation += "Move id " + str(u + 1) + " [" + str(vec[0]) + "," + str(vec[1]) + "," + str(vec[2]) + "]\n"
            animation += "End\n\n"

        with open("/Users/ziqwang/Desktop/WorkSpace/planar_lizard/animation.motion.txt", "w") as animate_file:
            animate_file.write(animation)
        exit()

    else:
        print 'fail'
        input = []
