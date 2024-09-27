package com.Coding;

import java.util.Scanner;

class OddNumOfDigits {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int count = 0;
		System.out.println("Enter the Number:");
		int n = sc.nextInt();
		for (int i = 1; i <= n; i++) {
			String str = Integer.toString(i);
			if (str.length() % 2 != 0) {
				count++;
			}
		}
		sc.close();
		System.out.println("Total Number OddNumOfDigits:\n"+count);
	}
}
