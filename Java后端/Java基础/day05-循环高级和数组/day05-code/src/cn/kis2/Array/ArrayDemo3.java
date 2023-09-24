package cn.kis2.Array;

public class ArrayDemo3 {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        System.out.println(arr[0]);
        System.out.println(arr[1]);
        System.out.println(arr[2]);
        System.out.println(arr[3]);
        System.out.println(arr[4]);
        //利用循环改进代码
        //开始条件：0
        //结束条件：数组的长度 - 1（最大索引）
/*        for (int i = 0; i < 5; i++) {
            //i: 0 1 2 3 4
            System.out.println(arr[i]);
        }*/
        //数组的长度属性 arr.length
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
        
        //扩展
        //自动生成数组的遍历
        //idea提供的   数组名.fori
        for (int i = 0; i < arr.length; i++) {
            System.out.println(i);
        }
    }
}

