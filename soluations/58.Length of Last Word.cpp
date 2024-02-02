class Solution {
public:
    int lengthOfLastWord(string s) {

        int i = s.length() - 1;

        while( i >=0 && s[i] == '')
            --i;
        

        const int lastIndex = i;

        while( i >=0 && s[i] !=='')
            --i;


            return lastIndex - i;
        
    }
};




// class Solution:
//   def lengthOfLastWord(self, s: str) -> int:
//     i = len(s) - 1

//     while i >= 0 and s[i] == ' ':
//       i -= 1
//     lastIndex = i
//     while i >= 0 and s[i] != ' ':
//       i -= 1

//     return lastIndex - i