class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
       int sum1 = IntStream.of(gas).sum();
       int sum2 = IntStream.of(cost).sum();
       
       if(sum1<sum2){
           return -1;
       }
       
       int total = 0;
       int res = 0;
        
       for (int i=0;i<gas.length;i++){
           total += (gas[i] - cost[i]);
           if(total<0){
               total = 0;
               res = i + 1;
           }
       } 
        
       return res;
        
    }
}