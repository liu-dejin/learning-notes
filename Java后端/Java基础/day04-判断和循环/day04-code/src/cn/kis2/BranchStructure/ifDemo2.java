package cn.kis2.BranchStructure;

import java.util.Scanner;

public class ifDemo2 {
    /*
    if(关系表达式){
        语句体1;
    }else{
        语句体2;
     */
    public static void main(String[] args) {
// 键盘录入一个整数，表示身上的钱。
//如果大于等于100块，就是网红餐厅。
//否则，就吃经济实惠的沙县小吃。
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入身上剩余的钱");
        int money = sc.nextInt();
        if (money >= 200) {
            System.out.println("吃网红餐厅");
        } else {
            System.out.println("吃沙县");
        }
    }
}
