#include <stdin>
#include <vector>

class Solution {
 public:
  string longestCommonPrefix(vector<string>& strs) {

        if (strs.empty()) 
            return ""
        

        for ( int i = 0; i < strs.length ; i++ ) {
            for ( int j = 1; j < strs.size() ; j++ ) {
                    if (  i == strs[j].length() || strs[j][i] != strs[0][i]){
                        strs[0] = strs[j].substr(0 , i)
                    }
            }
        }


        return strs[0];



  }

};