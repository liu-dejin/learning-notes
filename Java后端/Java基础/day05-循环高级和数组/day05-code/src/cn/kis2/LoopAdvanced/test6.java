package cn.kis2.LoopAdvanced;

import java.util.Random;

public class test6 {
    public static void main(String[] args) {
//        生成1-100随机数
        Random r = new Random();
        int number = r.nextInt(100) + 1;
        System.out.println(number);

        //秘诀    生成任意数到任意数的随机数  7-15
        //1.让这个范围头尾都减去一个值,让这个范围从0开始     -7 0-8
        //2.尾巴+1
        //3.最终的结果,再加上第一步减去的值
/*        Random r = new Random();
        int number = r.nextInt(9)+7;
        System.out.println(number);*/


    }
}
