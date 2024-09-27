package com.Coding;

import java.util.Scanner;

public class SumOfAsciiValues {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.print("Enter String:");
		String str = sc.nextLine().toLowerCase();
		char[] arr = str.toCharArray();
		float avg, sum = 0;
		for (int i = 0; i < arr.length; i++) {
			float temp = (int) arr[i];
			sum += temp;
		}
		avg = sum / arr.length;
		System.out.println("Average Of Ascii of"+ str+ "is:"+ avg);
		sc.close();
	}

}
