package com.Coding;


public class RhymingWords {
    public static void main(String[] args) {
        String[] arr=new String[]{"puzzle","thunder","powder","under","blender"};
        String check="thunder";
        int clen=check.length();
        int n=5;
        String result="";
        for(int i=0;i<n;i++)
        {
            int maxCount=0;
            String temp=arr[i];
            int tlen=temp.length();
	            if(temp!=check) 
	            {
	                for (int j = clen-1; j > 0; j--) {
	                    int count=0;
	                    for (int k = tlen-1; k > 0; k--) {
	                        if (temp.charAt(k) != check.charAt(j)) {
//	                            count++;
//	                            System.out.println(temp);
//	                            System.out.println(count);
	                        	break;
	                        }
	                        else {
	                        	count ++;
	                        }
	                        if(maxCount<count){
	                            maxCount=count;
	                            System.out.println("Max count word:"+maxCount);
	                            result=temp;
	                        }
	                    }
	                }
	            }
            }
        System.out.println(result);
        }


    }
