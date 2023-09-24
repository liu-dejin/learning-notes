package cn.kis2.LoopAdvanced;

import java.util.Scanner;

public class test3 {
    //  求质数
    //质数：
    //如果一个整数只能被1和本身整除，那么这个数就是质数。否则这个数叫做合数
    //7 = 1 * 7 质数
    //8 = 1 * 8  2 * 4 合数


    public static void main(String[] args) {
        //定义一个变量,表示标记
//    true是一个整数
        //flase不是一个整数
        boolean flag = true;
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入一个正整数");
        int number = sc.nextInt();

        for (int i = 2; i < number; i++) {
            if (number % i == 0) {
                flag = false;
            }
        }
        if (flag) {
            System.out.println(number + "是一个质数");
        } else {
            System.out.println(number + "不是一个质数");
        }
    }


}
