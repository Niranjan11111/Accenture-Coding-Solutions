package com.Coding;

public class ReplaceCharacterEventManagement {

	public static void main(String[] args) {

		String str = "EAB@EFh8FG";
		int len = str.length();
		while (len > 0) {
			str = str.replace("EF", "");
			str = str.replace("G", "");
			len--;
		}
		System.out.println("ReplaceCharacterEventManagement with '':" + str);
	}

}
