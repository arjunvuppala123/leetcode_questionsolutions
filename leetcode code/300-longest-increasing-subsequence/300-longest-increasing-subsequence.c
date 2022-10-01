#define new_max(x,y) (((x) >= (y)) ? (x) : (y))

int max(int num1, int num2)
{
    return (num1 > num2 ) ? num1 : num2;
}

int maximum(int* arr,int arrSize){
    int max = 0;
    
    for (int i=0;i<arrSize;i++){
        if (max<arr[i]){
            max = arr[i];
        }
    }
    
    return max;
}


int lengthOfLIS(int* nums, int numsSize){
    int* res = (int*)malloc(numsSize*sizeof(int));
    for (int i=0;i<numsSize;i++){
        res[i] = 1;
    }
    for (int i=0;i<numsSize;i++){
        for (int j=0;j<i;j++){
            if (nums[i]>nums[j]){
                res[i] = max(res[i],res[j]+1);
            }
        }
    }
    
    return maximum(res,numsSize);
}