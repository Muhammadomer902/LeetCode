class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int i = 0;
        string merged ="";
        while(word1[i]!='\0' && word2[i]!='\0')
        {
            merged = merged+word1[i]+word2[i];
            i++;
        }
        if(word1.length()>word2.length())
        {
            while(word1[i]!='\0')
            {
                merged=merged+word1[i];
                i++;
            }
        }
        else if(word1.length()<word2.length())
        {
            while(word2[i]!='\0')
            {
                merged=merged+word2[i];
                i++;
            }
        }
        return merged;
    }
};