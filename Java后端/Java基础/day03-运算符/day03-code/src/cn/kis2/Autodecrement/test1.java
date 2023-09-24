package cn.kis2.Autodecrement;

public class test1 {
    public static void main(String[] args) {
        //先用后加
        int a = 10;
        int b = a++;
        System.out.println(a);  //11
        System.out.println(b);  //10
        //先加后用
        int c = 10;
        int d = ++c;
        System.out.println(c);  //11
        System.out.println(d);  //11
    }
}
