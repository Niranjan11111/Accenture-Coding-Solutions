package com.Coding;

import java.util.Scanner;

public class SumOfDigitsInString {
	
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		System.out.println("Enter the Input:");
		int sum=0;
		String str=scan.nextLine();
		char[] arrChar=str.toCharArray();
		for(int i=0;i<arrChar.length;i++) {
			char c=arrChar[i];
			if(Character.isDigit(c)) {
				sum+=c-'0';
			}
		}
		System.out.println(sum);
		scan.close();
	}
}
