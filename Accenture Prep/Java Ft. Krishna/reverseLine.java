package com.Coding;

import java.util.Scanner;

public class reverseLine {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine();
		String ansStr = "";
		String Space = " ";
		int startIndex = 0;
		for (int i = 0; i <= str.length(); i++) {
			// Check for space or end of string
			if (i == str.length() || str.charAt(i) == ' ') {
//				StringBuilder temp = new StringBuilder(str.substring(startIndex, i));
//				temp.reverse();
				String temp=str.substring(startIndex, i);;
				ansStr += temp;
				if (i != str.length()) {
					ansStr += Space;
				}
				startIndex = i + 1; // Move the start index to the next word
			}
		}
		System.out.println(ansStr);
		sc.close();
	}
}
