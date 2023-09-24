package cn.kis2.LoopStructure;

public class test7 {
    /*需求：给你一个整数 x 。
  如果 x 是一个回文整数，打印 true ，否则，返回 false 。
  解释：回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
  例如，121 是回文，而 123 不是。*/
    public static void main(String[] args) {
        int x = 12345;
        //临时变量记录x原来的值,用于最后比较
        int temp = x;
        int num = 0;
        while (x != 0) {
            int ge = x % 10;
            x = x / 10;
            num = num * 10 + ge;
        }
        System.out.println(num);
        System.out.println(temp);
        System.out.println(num == temp);

//        int x = 12345;
//        int ge = x % 10;
//        int shi = x / 10 % 10;
//
//        int rasult =ge *10+shi;
//        System.out.println(rasult);
//
    }
}
