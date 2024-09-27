package com.Coding;

import java.util.Scanner;

public class TimeConversion {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		System.out.print("Enter Hour:");
		int H=sc.nextInt();
		System.out.print("Enter Minutes:");
		int M=sc.nextInt();
		int TotalTimeInMinutes=H*60+M;
		int TotalTimeLeft=(24*60)-TotalTimeInMinutes;
		sc.close();
		System.out.println("Total Hours & Minutes: " + TotalTimeLeft/60 +"Hrs" + TotalTimeLeft%60+"Mins");
	}

}
