package cn.kis2.RelationalOperators;

import java.util.Scanner;

public class test1 {
    /* 需求：
 您和您的约会对象正试图在餐厅获得一张桌子。
 键盘录入两个整数，表示你和你约会对象衣服的时髦度。（手动录入0~10之间的整数，不能录其他）
 如果你的时髦程度大于你对象的时髦程度，相亲就成功，输出true。
 否则输出false。*/
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入我们自己的衣服的时髦度");
        int myFashion = sc.nextInt();
        System.out.println("请输入相亲对象的衣服的时髦度");
        int girlFashion = sc.nextInt();
        //对比时髦度
        boolean result = myFashion > girlFashion;
        //打印结果
        System.out.println(result);
    }
}
