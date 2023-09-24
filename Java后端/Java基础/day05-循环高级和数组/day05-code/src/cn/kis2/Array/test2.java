package cn.kis2.Array;

public class test2 {
    /*定义一个数组，存储1,2,3,4,5,6,7,8,9,10
遍历数组得到每一个元素，统计数组里面一共有多少个能被3整除的数字*/
    public static void main(String[] args) {
        int count = 0;
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        for (int i = 0; i < arr.length; i++) {
            //i表示每一个索引
            //arr[i]表示每一个元素
            if (arr[i] % 3 == 0) {
//                System.out.println(i);
                count++;
            }
        }
        System.out.println("数组中能被三整除的数字有" + count + "个");
    }
}
