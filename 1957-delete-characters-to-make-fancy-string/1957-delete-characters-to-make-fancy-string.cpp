#include <string>
using namespace std;

class Solution {
public:
    string makeFancyString(string s) {
        string result;
        
        // Iterate through each character in the string
        for (int i = 0; i < s.size(); i++) {
            int len = result.size();
            
            // Add the character only if the last two characters in `result` are not the same as `s[i]`
            if (len < 2 || !(result[len - 1] == s[i] && result[len - 2] == s[i])) {
                result.push_back(s[i]);
            }
        }
        
        return result;
    }
};
