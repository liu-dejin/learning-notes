package cn.kis2.LoopAdvanced;

public class LoopAdvancedDemo2 {
    public static void main(String[] args) {
        //1.跳转一次循环
//        for (int i = 1; i < 5; i++) {
//            if (i == 3) {
//                //结束本次循环继续下次循环
//                continue;
//            }
//            System.out.println("小老虎在吃第" + i + "个包子");
//        }

        //2.结束整个循环
        for (int i = 1; i < 5; i++) {
            if (i == 3) {
                //结束整个循环
                break;
            }
            System.out.println("小老虎在吃第" + i + "个包子");
        }
    }
}

