package com.Coding;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class MidPointAscendDescend {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int size = sc.nextInt();
		int midPoint = size / 2;
		int[] array = new int[size];
		for (int i = 0; i < size; i++) {
			array[i] = sc.nextInt();
		}
		ArrayList<Integer> part1 = new ArrayList<Integer>();
		ArrayList<Integer> part2 = new ArrayList<Integer>();
		for (int i = 0; i < midPoint; i++) {
			part1.add(array[i]);
		}
		for (int i = midPoint; i < size; i++) {
			part2.add(array[i]);
		}
		Collections.sort(part1);
		Collections.sort(part2, Collections.reverseOrder());
		part1.addAll(part2);
		System.out.println(part1);
		sc.close();
	}

}
