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

