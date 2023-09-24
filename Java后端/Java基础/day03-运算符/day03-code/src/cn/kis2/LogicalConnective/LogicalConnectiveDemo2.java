package cn.kis2.LogicalConnective;

public class LogicalConnectiveDemo2 {
    public static void main(String[] args) {
        //^ 逻辑异或  //左右不相同，结果才是true，左右相同结果就是false
        System.out.println(true ^ true);//false
        System.out.println(false ^ false);//false
        System.out.println(true ^ false);//true
        System.out.println(false ^ true);//true
//      逻辑非  取反
        System.out.println(!false);//true
        System.out.println(!true);//false

        System.out.println(!!false);//注意点：取反最多只用一个。
    }
}
