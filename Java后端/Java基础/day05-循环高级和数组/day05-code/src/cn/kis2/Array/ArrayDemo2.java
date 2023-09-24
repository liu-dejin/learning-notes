package cn.kis2.Array;

public class ArrayDemo2 {
    public static void main(String[] args) {
        //1.获取元素
        int[] arr = {1, 2, 3, 4, 5};
        int number = arr[0];
        System.out.println(number);
        //获取1索引上的数据并打印
        System.out.println(arr[2]);

        //2.把数据存在数据当中
        //数组名[索引]=具体数值/变量
        //一但覆盖原来的值就不存在了
        arr[0] = 100;
        System.out.println(arr[0]);
    }
}
