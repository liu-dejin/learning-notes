package cn.kis2.Array;

public class test7 {
    /*需求：定义一个数组，将数组中0索引和最大索引出的值进行交换*/
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};


        for (int i = 0, j = arr.length - 1; i < j; i++, j--) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
