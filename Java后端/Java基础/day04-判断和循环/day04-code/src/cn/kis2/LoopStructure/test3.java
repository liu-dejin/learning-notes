package cn.kis2.LoopStructure;

public class test3 {
    /*  需求：在实际开发中，如果要获取一个范围中的每一个数据时，也会用到循环。
  比如：求1-5之间的和*/
    public static void main(String[] args) {
//        扩展:
        //1.求和的变量不能定义再循环的里面,因为变量只在所属大括号中有效
        //2.如果我们把变量定义到循环里面,那么当前变量只能在本次循环中有效
        //当本次循环结束之后就会在内存中消失
        //第二次循环开始的时候,又会重新定义一个新的变量
        //结论:写累加求和的变量,将变量定义在循环的外面
        int sum = 0;
        for (int i = 1; i <= 100; i++) {
//            System.out.println(i);
            sum = sum + i;  //sum+=i
        }

        //当循环结束后,已经把1-5累加赋值给了sum
        System.out.println(sum);
    }
}
