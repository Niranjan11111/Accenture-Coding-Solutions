package com.Coding;

import java.util.Scanner;

public class FindDiagonalForRectangle {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter Number of cases:");
		int NoOfTestCase = sc.nextInt();
		for (int i = 0; i < NoOfTestCase; i++) {
			double l = sc.nextInt();
			double b = sc.nextInt();
			System.out.println(CalculateDiagonal(l, b));
		}
		//System.out.println(Math.pow(2, 3));
		sc.close();

	}

	public static double CalculateDiagonal(double l, double b) {
		double ans = Math.sqrt((Math.pow(l, 2)) + (Math.pow(b, 2)));
		return ans;
	}

}
