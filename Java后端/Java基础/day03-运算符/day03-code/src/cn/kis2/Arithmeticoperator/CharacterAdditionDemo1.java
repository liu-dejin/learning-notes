package cn.kis2.Arithmeticoperator;

public class CharacterAdditionDemo1 {
    public static void main(String[] args) {
        //字符参与运算都会转换成ascll字符表
        System.out.println(1 + 'a'); //98
        System.out.println('a' + "abc");  //"aabc"
    }
}
