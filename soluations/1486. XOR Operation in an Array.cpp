class Solution{
    public:{

            int xorOperations(int n , int start){

                int result = 0;

                for (int i = 0; i < n; ++i){
                    result ^= start + 2 * i;
                }

                return result;

            }


    }


}