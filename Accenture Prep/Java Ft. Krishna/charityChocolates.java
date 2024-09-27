package com.Coding;

import java.util.Scanner;

public class charityChocolates {

	public static int totalChocolates(int N) {
		int mod = 1000000007;
		int totalChocolates = 0;
		for (int i = 1; i <= N; i++) {
			int chocolates = i;
			if ((i - 1) % 5 == 0 || (i + 1) % 5 == 0) {
				chocolates += 2;
			}

			totalChocolates = (totalChocolates + chocolates) % mod;
		}

		return totalChocolates;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		System.out.println(totalChocolates(N));
		sc.close();
	}
}
