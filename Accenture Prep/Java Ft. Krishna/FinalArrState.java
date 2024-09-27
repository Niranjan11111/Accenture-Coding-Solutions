package com.Coding;

import java.util.*;

public class FinalArrState {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter Operations Count: ");
		int k=sc.nextInt();
		System.out.println("Enter Multiplier: ");
		int multi=sc.nextInt();
		System.out.println("Enter Array Elements: ");
		int[] arr=new int[k];
		int mod=1000000007;
		sc.close();
		for(int i=0;i<k;i++) {
			arr[i]=sc.nextInt();
		}
		Arrays.sort(arr);
		for(int i=0;i<k-2;i++) {
			if(arr[i]<arr[i+1]) {
				arr[i]=arr[i]*multi;
			}
			if(arr[i]==arr[i+1]) {
				arr[i]=arr[i]*multi;
				arr[i+1]=arr[i];
			}
			if(arr[0]==arr[1]) {
				arr[0]=arr[0]*multi;
			}
		}
		if(arr.length==2) {
			for(int i=0;i<k-1;i++) {
				if(arr[i]<arr[i+1]) {
					arr[i]=arr[i]*multi;
					continue;
				}
				arr[i+1]=arr[i]-2;
				
			}
		}
		for(int i=0;i<k;i++) {
			arr[i]=arr[i]%mod;
		}
		System.out.println(Arrays.toString(arr));
	}

}
