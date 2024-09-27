package com.Coding;

import java.util.Scanner;

public class FindStartAndEndPosition {

	public static void main(String[] args) {
		Scanner read = new Scanner(System.in);
		System.out.println("Enter array size:");
		int size = read.nextInt();
		int[] arr = new int[size];
		System.out.println("Enter array elements:");
		for (int i = 0; i < size; i++) {
			arr[i] = read.nextInt();
		}
		System.out.println("Enter the target:");
		int target = read.nextInt();
		read.close();
		// FindPos(arr, target);
		FindPos(arr, target);
		System.out.println();
		read.close();

	}

	// Linear Search
//	private static void FindPos(int[] arr, int target) {
//		// TODO Auto-generated method stub
//		ArrayList<Integer> result = new ArrayList<Integer>();
//		for (int i = 0; i < arr.length; i++) {
//			if (target == arr[i]) {
//				result.add(i);
//			}
//		}
//		String res = result.toString();
//		System.out.println("Output for Start and End postion of Targrt Element:" +res);
//	}

	// Binary Search
	private static void FindPos(int[] arr, int t) {
		int start = 0;
		int end = arr.length - 1;
		while (start <= end) {
			int mid = start + (end - start) / 2;
			if (arr[mid] == t) {
				start = mid;
			} else {
				start = -1;
				end = -1;
			}
		}
		System.out.println(start + " " + end);
	}
}
