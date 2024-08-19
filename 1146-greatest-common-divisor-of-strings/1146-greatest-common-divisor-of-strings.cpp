class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        int len1 = str1.length();
        int len2 = str2.length();
        int gcdLength = __gcd(len1, len2);
        string possibleGCD = str1.substr(0, gcdLength);
        if (divides(str1, possibleGCD) && divides(str2, possibleGCD)) {
            return possibleGCD;
        }
        
        return "";
    }
    bool divides(const string &s, const string &t) 
    {
        int lenS = s.length(), lenT = t.length();
        if (lenS % lenT != 0) 
            return false;
        string repeatedT = "";
        for (int i = 0; i < lenS / lenT; i++) {
            repeatedT += t;
        }
        return repeatedT == s;
    }
};