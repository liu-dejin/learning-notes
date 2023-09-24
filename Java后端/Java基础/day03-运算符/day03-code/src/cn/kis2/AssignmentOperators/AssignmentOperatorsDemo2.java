package cn.kis2.AssignmentOperators;

public class AssignmentOperatorsDemo2 {
    public static void main(String[] args) {
        //扩展赋值运算符
        int a = 10;
        int b = 20;
        a += b;//把左边和右边相加，再把最终的结果赋值给左边，对右边没有任何影响
        // 相当于 a = (int)(a + b);
        System.out.println(a);//30
        System.out.println(b);//20
//        隐层还包含了一个强制转换
    }
}
