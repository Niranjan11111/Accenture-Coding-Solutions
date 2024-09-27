package com.Coding;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

public class OddOccurenceAcc {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		HashMap<Integer, Integer> map = new HashMap<>();
		int size = sc.nextInt();
		int[] array = new int[size];
		for (int i = 0; i < size; i++) {
			array[i] = sc.nextInt();
		}
		Arrays.sort(array);
		for (int i = 0; i < array.length; i++) {
			int tempCount = 1;
			for (int j = 0; j < array.length; j++) {
				if (array[i] == array[j]) {
					tempCount = tempCount + 1;
					// System.out.println(tempCount);
				}
				map.put(array[i], tempCount);
			}
		}
		System.out.println(map);
		sc.close();
	}
}