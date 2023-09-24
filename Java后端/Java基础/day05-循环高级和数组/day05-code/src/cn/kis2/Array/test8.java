package cn.kis2.Array;

import java.util.Random;

public class test8 {
    public static void main(String[] args) {
        //需求：定义一个数组，存入1~5。要求打乱数组中所有数据的顺序。
        //难点：
        //如何获取数组中的随机索引
       /* int[] arr = {1,2,3,4,5};
        //索引范围：0 1 2 3 4
        Random r = new Random();
        int randomIndex = r.nextInt(arr.length);
        System.out.println(randomIndex);*/
        int[] arr = {1, 2, 3, 4, 5};
        Random r = new Random();

        for (int i = 0; i < arr.length; i++) {
            int randomindex = r.nextInt(arr.length);
            int temp = arr[i];
            arr[i] = arr[randomindex];
            arr[randomindex] = temp;
        }
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
