package cn.kis2.LoopAdvanced;

import java.util.Random;
import java.util.Scanner;

//需求：程序自动生成一个1-100之间的随机数字，使用程序实现猜出这个数字是多少？
//扩展小需求：加一个保底机制，3次猜不中，直接提示猜中了。
//注意: int number = r.nextInt(100) + 1;不能写作循环里面否则每次都会生成一个新的随机数
public class test7 {
    public static void main(String[] args) {
        int count = 0;
        Random r = new Random();
        int number = r.nextInt(100) + 1;
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("请输入你要猜的数字");
            int guessNumber = sc.nextInt();
            count++;
            if (count == 3) {
                System.out.println("猜对了");
                break;
            }
            if (guessNumber > number) {
                System.out.println("猜大了");
            } else if (guessNumber < number) {
                System.out.println("猜小了");
            } else {
                System.out.println("猜中了");
                break;
            }
        }

    }
}
