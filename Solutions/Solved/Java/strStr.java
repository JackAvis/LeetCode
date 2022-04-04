class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() == 0){
            return 0;
        }
        if (haystack.length() < needle.length()){
            return -1;
        }
        for (int i = 0; i < haystack.length(); i ++){
            if (haystack.charAt(i) == needle.charAt(0)){
                int checker = i;
                for (int j = 0; j < needle.length(); j ++){
                    if (checker == haystack.length()){
                        return -1;
                    }
                    if (haystack.charAt(checker) == needle.charAt(j)){
                        checker ++;
                    }
                    else{
                        break;
                    }
                    if (j + 1 == needle.length()){
                        System.out.println(j + 1 == needle.length());

                        return i ;
                    }

                }
                
            }
        }
        return -1;
        
    }
}