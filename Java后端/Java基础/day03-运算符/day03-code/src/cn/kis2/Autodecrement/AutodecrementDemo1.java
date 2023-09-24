package cn.kis2.Autodecrement;

public class AutodecrementDemo1 {
    public static void main(String[] args) {
        //++ --
        //无论放变量的前面还是后面，单独写一行结果一样
        //参与计算就有差别了
        int a = 10;
        a++;
        System.out.println(a);  //11
        ++a;
        System.out.println(a);  //12
        a--;
        System.out.println(a);  //11
        --a;
        System.out.println(a);  //10
    }
}
