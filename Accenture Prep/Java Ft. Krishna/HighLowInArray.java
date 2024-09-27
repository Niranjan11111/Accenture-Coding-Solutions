package com.Coding;

import java.util.Arrays;

public class HighLowInArray {

	public static void main(String[] args) {
		int N=3;
		int M=8979;
		int[] a= {909,3347,1211};
		GoodNumbers(N,M,a);
	}
	private static void GoodNumbers(int n,int m,int[] a) {
		String mString=Integer.toString(m);
		char[] mArr=mString.toCharArray();
		Arrays.sort(mArr);
		int check=Integer.parseInt(String.valueOf(mArr[0]));
		int count=0;
		for(int i=0;i<n;i++)  {
			int sum=0;
			String temp=Integer.toString(a[i]);
			char[] dummy=temp.toCharArray();
			for(int j=0;j<dummy.length;j++) {
				int innerDigits=Integer.parseInt(String.valueOf(dummy[j]));
				sum+=innerDigits;
			}
			if(sum>check) {
				count++;
			}	
		}
		System.out.println(count);
		
	}

}
