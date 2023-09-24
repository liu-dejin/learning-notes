package cn.kis2.BranchStructure;

import java.util.Scanner;

public class ifDemo1 {
    public static void main(String[] args) {
        //键盘录入女婿酒量如果大于2斤,老丈人给出回应反之不回应

        //if格式
        //if(关系表达式){
        //语句体
        // }
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入女婿的酒量");
        int wine = sc.nextInt();
        if (wine > 2) {
            System.out.println("小伙子不错哦");
        }
        /*
    if(关系表达式){
    语句体;
     }
     1,大括号可以另起一行但是不推荐
     2.只有语句代码大括号可以省略,不建议这样做
     3.如果对布尔类型的变量进行判断,不要用== 直接把变量写到小括号即可
     */

//        int number =10 ;
//        if (number>=10){
//            System.out.println("number大于等于10");
//        }
        boolean flag = true;
//        这里是赋值
        if (flag = true) {
            System.out.println("flag的值是true");
        }
    }
}
