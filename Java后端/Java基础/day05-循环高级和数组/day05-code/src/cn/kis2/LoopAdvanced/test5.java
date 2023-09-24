package cn.kis2.LoopAdvanced;

import java.util.Random;

public class test5 {


    public static void main(String[] args) {
        Random r = new Random();   //小括号写的是随机数的范围,一定是从0开始的 到这个数-1结束
        for (int i = 0; i < 100; i++) {
            int number = r.nextInt(10);
            System.out.println(number);
        }


    }
}
