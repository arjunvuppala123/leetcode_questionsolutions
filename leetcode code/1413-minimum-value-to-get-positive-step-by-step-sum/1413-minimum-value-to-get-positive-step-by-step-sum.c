int minimum(int a,int b){
    if (a>b){
        return b;
    }
    else{
        return a;
    }
}

int minStartValue(int* nums, int numsSize){
    int minVal = 0;
    int val = 0;
    
    for (int i=0;i<numsSize;i++){
        val += nums[i];
        minVal = minimum(minVal,val);
    }
    
    return -minVal+1;
}