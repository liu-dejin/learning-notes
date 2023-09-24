package cn.kis2.TernaryOperator;

public class test2 {
    //  一座寺庙里住着三个和尚，已知他们的身高分别为150cm、210cm、165cm。
//    请用程序实现获取这三个和尚的最高身高。
    public static void main(String[] args) {
        //1.定义三个变量记录和尚的身高
        int height1 = 150;
        int height2 = 210;
        int height3 = 165;

//2.利用三元运算符求出两个数中的较大值。
        int temp = height1 > height2 ? height1 : height2;

//3.求出最终的结果
        int max = temp > height3 ? temp : height3;

        System.out.println(max);
    }
}
