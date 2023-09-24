package cn.kis2.BranchStructure;

public class SwitchDemo1 {
    /*
    switch (表达式) {
	case 1:
		语句体1;
		break;
	case 2:
		语句体2;
		break;
	...
	default:
		语句体n+1;
		break;
}
     */
    public static void main(String[] args) {
        //兰州拉面、武汉热干面、北京炸酱面、陕西油泼面
        String noodles = "兰州拉面";
        switch (noodles) {
            case "兰州拉面":
                System.out.println("吃兰州拉面");
                break;
            case "武汉热干面":
                System.out.println("吃武汉热干面");
                break;
            case "北京炸酱面":
                System.out.println("吃北京炸酱面");
                break;
            case "陕西炸酱面":
                System.out.println("吃陕西炸酱面");
                break;
            default:
                System.out.println("吃方便面");
                break;
        }
    }
}