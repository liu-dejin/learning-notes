package cn.kis2.Arithmeticoperator;

public class TypeConversionDemo1 {
    public static void main(String[] args) {
        byte b1=10;
        byte b2 =20;
        //我们要强转的b1+b2的结果
        byte result = (byte) (b1+b2);
        System.out.println(result); //结果发生错误,因为要转的数据过大
    }
}
