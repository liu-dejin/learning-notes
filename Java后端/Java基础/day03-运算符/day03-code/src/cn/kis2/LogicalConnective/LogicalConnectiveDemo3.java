package cn.kis2.LogicalConnective;

public class LogicalConnectiveDemo3 {
    public static void main(String[] args) {
        //1.&&短路与
//        运算结果跟&是一模一样的，只不过具有短路效果。
        System.out.println(true && true);//true
        System.out.println(false && false);//false
        System.out.println(true && false);//false
        System.out.println(false && true);//false
        //2.||短路或
//        运算结果跟|是一模一样的。只不过具有短路效果。
        System.out.println(true || true);//true
        System.out.println(false || false);//false
        System.out.println(true || false);//false
        System.out.println(false || true);//false
//  当左边不能确定整个表达式的结果，右边才会执行。
//  当左边能确定整个表达式的结果，那么右边就不会执行了。从而提高了代码的运行效率

        //3.短路逻辑运算符具有短路效果
        //简单理解：当左边的表达式能确定最终的结果，那么右边就不会参与运行了
        int a = 10;
        int b = 10;
        boolean result = ++a < 5 & ++b < 5;
        System.out.println(result);//false
        System.out.println(a);//11
        System.out.println(b);//10
    }
}
