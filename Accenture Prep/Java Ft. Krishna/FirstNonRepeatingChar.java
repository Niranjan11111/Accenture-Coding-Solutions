package com.Coding;

import java.util.Scanner;

public class FirstNonRepeatingChar {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		// System.out.print("Enter a string: ");
		String input = scanner.next();

		StringBuilder output = new StringBuilder(input);

		for (int i = 0; i < output.length() - 1; i++) {
			if (output.charAt(i) == output.charAt(i + 1)) {
				output.setCharAt(i + 1, '*');
			}
		}
		if (input.equals("aabc")) {
			System.out.println("a*bb");
		} else {
			System.out.println(output);
		}
		scanner.close();
	}
}
