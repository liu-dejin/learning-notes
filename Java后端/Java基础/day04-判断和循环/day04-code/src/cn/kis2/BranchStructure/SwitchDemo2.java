package cn.kis2.BranchStructure;

/*
default的位置和省略
1.位置    不一定要写在最底下,习惯性写最底下
2.省略    default可以省略,语法不会有问题,但不建议
 */
public class SwitchDemo2 {
    public static void main(String[] args) {
        int number = 100;
        switch (number) {
            case 1:
                System.out.println("number的值为1");
                break;
            case 10:
                System.out.println("number的值为10");
                break;
            case 20:
                System.out.println("number的值为20");
                break;
            default:
                System.out.println("number的值不是1,10或者20");
                break;
        }
    }
}
