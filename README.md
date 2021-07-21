# Color science NCHU

## HW1

> Input: n, k, m
>
> n decided the domain [0, n)
>
> k decided the length of tuple
>
> m is the m-th cobidic tuple
>
> n = 5, k = 3
>
> ![](./assets/cobidic.png)
> 

## HW2

HW2 is similar to HW1, but return the m-th element tuple

## HW3 - color transfer

HW3 is a program modified from [https://github.com/jrosebr1/color_transfer](https://github.com/jrosebr1/color_transfer)

The most different from our version to original version is the *source* paramater and the *target* paramater. The original version will change the *target* image according to the *source* image. However, we change the *source* image according to the *source* image.

![](./assets/hw3-demo.png)

## HW4
Modify Assignment 3 to produce decimal side
information. The decimal side information is a text file entitled "sideinfodeci.txt". This text file has 12 lines and each line represent a decimal value with four decimal places

+ 1-3: Mean of the *source* image in the RGB (or LAB) channel
+ 4-6: Standard deviation of the *source* image in the RGB (or LAB) channel
+ 7-9: Mean of the *target* image in the RGB (or LAB) channel
+ 10-12: Standard deviation of the *target* image in the RGB (or LAB) channel

## HW5
Write a code to implement the reverse color transfer

+ input: the result image in HW3 and *sideinfodeci.txt* in HW4
    + soruce file: sou1.png
    + target file: tar1.png
    + color transfer file: utl1.png
    + side info: sideinfodeci.txt
+ output: recovered image *yrcsou.png*

## HW6

Proof an equation

![](./assets/hw6-equation.png)

## HW7

**4107056019-07-Bin2Dec**: Transfer float32 binary string to number 

**4107056019-07-Dec2Bin**: Transfer float32 number to binary string

## HW8 - HW13

+ HW8: <a href="./HW8/Assignment 08 update v2-Arnold Transformation.pdf">See assignment</a>
+ HW9: <a href="./HW9/Assignment 09-Logistic map practice.pdf">See assignment</a>
+ HW10: <a href="./HW10/Assignment 10-Determine Secret Keys.pdf">See assignment</a>
+ HW11: <a href="./HW11/Assignment 11-Image Encryption Metrics-1-v02.pdf">See assignment</a>
+ HW12: <a href="./HW12/Assignment 12-Image Encryption Metrics-2.pdf">See assignment</a>
+ HW13: <a href="./HW13/Assignment 13-Image Encryption Metrics-3-v6.pdf">See assignment</a>

## 爭議

+ 5/18 因武漢肺炎疫情加劇，國內進入三級警戒，全國大專院校改以遠距教校。王老師視 HW13 為上課的一種形式

+ HW13 截止日後仍有 6/15, 6/22 兩堂課，王老師沒有補課措施

+ 王老師不公佈成績計算方式就將成績送出，後來寄信去詢問配分方式
    + 65% 13次作業
    + 10% 出席
    + **27% 加分**
    + 4%  全班調分

+ 王老師於課堂強調作業提早繳交將會有「加分」，遲交不計分，但沒有提及所謂的加分是包含在總成績的一個部分。這種說詞跟民進黨說只是「超買」不是「走私」有異曲同工之妙。也就是說如果作業準時繳交沒有提早且答案正確，且遠距上課前都有到課堂點名，你最高能得到：
    + 65 + 10 + 4 = 79 分 (OwO 這成績真棒)

+ @wei-coding 因有一次作業沒算到，寄信向王老師詢問，被告知能加 10 分。作業占 65 分，每次作業也應該只有 5 分，除非每次作業權重不一樣。不禁令人起疑王老師是否是先打分數再編造配分？因為明明有一位A同學比B同學還更常早交作業，且課堂上也有另外加分，但總成績卻比B同學低 6 分

+ 向系主任提出缺課及成績計算爭議

    + 缺課 → 系主任尊重各個教授上課的方式
    + 成績 → 系主任不保證能全班調分成功

+ 幾日後，成績調分完成。系上學期成績名次也因此更動。

![](https://i.imgur.com/pJtuTLq.png)