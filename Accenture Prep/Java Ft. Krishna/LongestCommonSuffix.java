package com.Coding;

public class LongestCommonSuffix {
    public static void main(String[] args) {
        String[] wordsContainer = {"abcd", "bcd", "xbcd"}; //"abcdefgh","poiuygh","ghghgh"
        String[] wordsQuery = {"cd", "bcd", "xyz"}; //"gh","acbfgh","acbfegh"
        int[] result = longest(wordsContainer, wordsQuery);
        for (int index : result) {
            System.out.print(index + " ");
        }
    }

    public static int[] longest(String[] wordsContainer, String[] wordsQuery) {
        int[] result = new int[wordsQuery.length];
        for (int i = 0; i < wordsQuery.length; i++) {
            String query = wordsQuery[i];
            int maxLen = -1;
            int bestIndex = -1;
            for (int j = 0; j < wordsContainer.length; j++) {
                String word = wordsContainer[j];
                int suffixLen = commonSuffixLength(word, query);
                if (suffixLen > maxLen ) {
                    maxLen = suffixLen;
                    bestIndex = j;
                }
            }
            result[i] = bestIndex+1;
        }
        return result;
    }
    

    private static int commonSuffixLength(String s1, String s2) {
        int minLen = Math.min(s1.length(), s2.length());
        for (int i = 1; i <= minLen; i++) {
            if (s1.charAt(s1.length() - i) != s2.charAt(s2.length() - i)) {
                return i - 1;
            }
        }
        return minLen;
    }
}

