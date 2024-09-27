package com.Coding;

import java.util.Arrays;

public class readingBooks {
	public static int maxBooksRead(int[] readingTimes, int totalTime) {
		
		Arrays.sort(readingTimes);
		int totalTimeSpent = 0;
		int maxBooks = 0;

		for (int i=1;i<=readingTimes.length;i++) {
		
			if (totalTimeSpent + i <= totalTime) {
				totalTimeSpent += i;
				maxBooks++;
			} else {
				break; 
			}
		}

		return maxBooks;
	}

	public static void main(String[] args) {
		int[] readingTimes = { 4, 2, 3, 1 };
		int totalTime = 5;
		int maxBooks = maxBooksRead(readingTimes, totalTime);
		System.out.println("Maximum number of books Alex can read: " + maxBooks);
	}
}
