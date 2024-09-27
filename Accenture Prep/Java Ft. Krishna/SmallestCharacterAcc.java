package com.Coding;

import java.util.Arrays;
import java.util.Scanner;

public class SmallestCharacterAcc {
	public static char SmallestCharacter(String s) {
		char[] arr=s.toCharArray();
		Arrays.sort(arr);
		int num = 97;
		System.out.println(Arrays.toString(arr));
		for(int i=0;i<arr.length;i++) {
			if(arr[i]-num == 0) {
				num++;
			}
		}
		return (char) num;
	}

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.print("Enter String:");
		String str=sc.next().toLowerCase();
		System.out.println("Smallest Missing Character is:"+SmallestCharacter(str));
		sc.close();
	}

}
