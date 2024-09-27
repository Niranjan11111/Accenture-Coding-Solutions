package com.Coding;

import java.util.Arrays;
import java.util.Scanner;

public class DividendIndex {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int Q = sc.nextInt();
		int Divisor = sc.nextInt();
		int Remainder = sc.nextInt();
		int[] indexArray = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
		System.out.println(CalculateIndex(indexArray, Q, Divisor, Remainder));
		sc.close();
	}

	private static int CalculateIndex(int[] arr, int q, int d, int r) {

		int dividend = d * q + r;
		if (dividend < 10) {
//			for(int i=0;i<arr.length;i++) {
//				if(arr[i]==dividend) {
//					return i;
//				}
//			}
			return Arrays.binarySearch(arr, dividend);
		}
		return -1;
	}
}
