package com.Coding;

import java.util.Scanner;

public class removeCharacters {
	public static String subString(String str, String str2) {
		int stringOneLength = str.length();
		int stringTwoLength = str2.length();
		String res="";
		if (stringOneLength < stringTwoLength) {
			res=str2.substring(stringOneLength,stringTwoLength);
		}
		else {
			res=str;
		}
		return res;
	}

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter the First Word:");
		String s1 = input.nextLine();
		System.out.println("Enter the Second Word:");
		String s2 = input.next();
		input.close();
		System.out.println("Sub String : " + subString(s1, s2));
	}

}
