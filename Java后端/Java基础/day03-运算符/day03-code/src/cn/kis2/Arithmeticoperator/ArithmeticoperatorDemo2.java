package cn.kis2.Arithmeticoperator;

public class ArithmeticoperatorDemo2 {
    //结论
    //1.整数参与计算,结果只能是小数
    //2.小数参与计算,结果有可能是不精确的
    public static void main(String[] args) {
        //除数
        System.out.println(10 / 2); //5
        System.out.println(10 / 3); //3
        System.out.println(10.0 / 3); //3.3333333333333335

        //取模,取余,做除法运算,取得余数
        System.out.println(10 % 2); //0
        System.out.println(10 % 3); //1

        //应用场景
        //1.可以用取模来判断，A是否可以被B整除
        //A%B   10%3
        //2.可以判断A是否为偶数
        //A%2
        //3.斗地主发牌
        //拿着序号%3 如果结果为1，就发给第一个玩家
        //如果结果为2，就发给第二个玩家
        //如果结果为3，就发给第三个玩家
    }
}
