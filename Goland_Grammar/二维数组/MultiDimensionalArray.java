/*
 * @Author: hakusai
 * @Date: 2023-05-19 16:15:09
 * @LastEditTime: 2023-05-19 16:17:59
 * @Description: 
 */
import java.util.*;
import java.io.*;
import java.math.*;


public class MultiDimensionalArray {

    public static void main(String[] args) {
        case1();
        case2();
        case3();
    }

    /**
     * 二维数组的创建方式
     */
    public static void case1() {
        // 一：先创建再赋值，为赋值的为默认值0
        int[][] tdArray1 = new int[3][3];
        tdArray1[0][0] = 0;
        tdArray1[0][1] = 1;
        tdArray1[0][2] = 2;
        tdArray1[1][0] = 3;
        tdArray1[2][1] = 4;
        // 二：创建并赋值
        var tdArray2 = new int[][]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        System.out.printf("tdArray1：%s   数据类型：%s%n", Arrays.deepToString(tdArray1), tdArray1.getClass().getSimpleName());
        System.out.printf("tdArray2：%s   数据类型：%s%n", Arrays.deepToString(tdArray2), tdArray2.getClass().getSimpleName());
    }

    /**
     * 二维数组双for循环嵌套遍历
     */
    public static void case2() {
        int[][] tdArray = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        for (int i = 0; i < tdArray.length; i++) {
            for (int j = 0; j < tdArray[i].length; j++) {
                System.out.println(tdArray[i][j]);
            }
        }
    }

    /**
     * 二维数组for each遍历
     */
    public static void case3() {
        int[][] tdArray = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        for (int[] arrayOne : tdArray) {
            System.out.println("arrayOne:" + Arrays.toString(arrayOne));
            for (int valueTwo : arrayOne) {
                System.out.println("arrayTwo:" + valueTwo);
            }
        }

        for (var i = 0; i < tdArray.length; i++) {
            System.out.println("i: " + i + " v1: " + Arrays.toString(tdArray[i]));
            for (var j = 0; j < tdArray[i].length; j++) {
                System.out.println("j: " + j + " v2: " + tdArray[i][j]);
            }
        }
    }
}
