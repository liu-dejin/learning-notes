package cn.kis2.LogicalConnective;

public class LogicalConnectiveDemo1 {
    public static void main(String[] args) {
        // &  //两边都是真，结果才是真。
        System.out.println(true & true);//true
        System.out.println(false & false);//false
        System.out.println(true & false);//false
        System.out.println(false & true);//false

        System.out.println("===================================");

// | 或  //两边都是假，结果才是假，如果有一个为真，那么结果就是真。
        System.out.println(true | true);//true
        System.out.println(false | false);//false
        System.out.println(true | false);//true
        System.out.println(false | true);//true
    }
}
