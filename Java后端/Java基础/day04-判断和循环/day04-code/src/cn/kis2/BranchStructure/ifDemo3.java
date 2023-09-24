package cn.kis2.BranchStructure;

import java.util.Scanner;

public class ifDemo3 {
    //格式：
    //if (关系表达式1) {
    //    语句体1;
    //} else if (关系表达式2) {
    //    语句体2;
    //}
    //…
    //else {
    //    语句体n+1;
    //}
    public static void main(String[] args) {
                /*
        根据不同的分数送不同的礼物。
        如果是95~100分，送自行车一辆
        如果是90~94分，游乐场玩一天
        如果是80~89分，送变形金刚一个。
        如果是80分，揍一顿。*/
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入一个整数表示小明的成绩");
        int score = sc.nextInt();
        //异常数据处理    0-100分合理数据
        if (score > 0 && score <= 100) {
            if (score >= 95 && score <= 100) {
                System.out.println("送自行车一辆");
            } else if (score >= 90 && score <= 94) {
                System.out.println("游乐场玩一天");
            } else if (score >= 80 && score <= 89) {
                System.out.println("送变形金刚一个");
            } else {
                System.out.println("揍一顿");
            }
        } else {
            System.out.println("当前录入的成绩不合法");
        }
    }
}
