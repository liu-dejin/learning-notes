package cn.kis2.LogicalConnective;

import java.util.Scanner;

public class test1 {
    public static void main(String[] args) {
       /*数字6是一个真正伟大的数字，键盘录入两个整数。
        如果其中一个为 6，最终结果输出true。
        如果它们的和为 6的倍数。最终结果输出true。
        其他情况都是false。*/
        //1.定义变量a,b
        //2.a==6||b==6||(a+b)%6==0
        //其中一个满足输出true
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入第一个整数");
        int number1 = sc.nextInt();
        System.out.println("请输入第二个整数");
        int number2 = sc.nextInt();
        boolean result = number1 == 6 || number2 == 6 || (number1 + number2) % 6 == 0;
        System.out.println(result);
    }
}
