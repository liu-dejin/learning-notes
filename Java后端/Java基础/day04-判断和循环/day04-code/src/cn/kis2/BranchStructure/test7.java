package cn.kis2.BranchStructure;

import java.util.Scanner;

/* 需求：键盘录入星期数，输出工作日、休息日。
(1-5) 工作日，(6-7)休息日。*/
public class test7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("录入一个整数表示星期");
        int week = sc.nextInt();
        switch (week) {
            //case 穿透
            case 1, 2, 3, 4, 5 -> System.out.println("工作日");
            case 6, 7 -> System.out.println("休息日");
            default -> System.out.println("没有这个星期");
        }
    }
}
