void helper(char* s,int left,int right){
    if (left < right){
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        helper(s,left+1,right-1);
    }
}

void reverseString(char* s, int sSize){
    helper(s,0,sSize-1);
}