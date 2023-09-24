package cn.kis2.BranchStructure;

public class test2 {
    public static void main(String[] args) {
        boolean isLightGreen = false;
        boolean isLightYellow = false;
        boolean isLightRed = true;
//红绿灯
//        if (isLightGreen){
//            System.out.println("dododo");
//        }
//
//        if (isLightYellow){
//            System.out.println("slow!!!");
//        }
//
//        if (isLightRed){
//            System.out.println("stop!!!");
//        }
        if (isLightGreen) {
            System.out.println("dododo");
        } else if (isLightYellow) {
            System.out.println("slow!!!");
        } else if (isLightRed) {
            System.out.println("stop!!!");
        }

    }
}
