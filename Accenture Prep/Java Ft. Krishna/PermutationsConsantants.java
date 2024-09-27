package com.Coding;

import java.util.Arrays;

public class PermutationsConsantants {

	public static void main(String[] args) {
		// n!/(n-r)!
		String arr[] = { "hello", "ccbc", "aaeiou" };
		int len = arr.length;
		int[] countArray = new int[len]; // 3,0,0
		for (int i = 0; i < len; i++) {
			String s = arr[i];
			// System.out.println(arr[i]);
			int tempCount = 0;
			for (int j = 0; j < s.length(); j++) {
				Boolean decision = !(isVowel(s.charAt(j)));
				// System.out.println(decision);
				if (decision) {
					// System.out.println(s.charAt(j));
					tempCount++;
				}
			}
			countArray[i] = tempCount;
			// System.out.println(Arrays.toString(countArray));

		}
		System.out.println(Arrays.toString(countArray));
		for (int i = 0; i < len; i++) {
			System.out.println("Permutation:" + calculatePermutation(countArray[i], arr[i].length()));
		}

	}

	public static boolean isVowel(char letter) {
		letter = Character.toLowerCase(letter);
		char[] Vowels = { 'a', 'e', 'i', 'o', 'u' };
		for (char c : Vowels) {
			// System.out.println(c);
			if (c == letter) {
				return true; // Return true if the letter matches a vowel
			}
		}
		return false;
	}

	private static int calculatePermutation(int n,int len) {
		// TODO Auto-generated method stub
		int fact = 1;
		int fact2=1;
		int r=len-n;
		for (int i = 1; i <= r; i++) {
			fact2*=i;
		}
		while(len>0) {
			fact=len*fact;
			len--;
		}
		// n!/(n-r)!
		int ans=fact/fact2;
		return ans;
	}

}
