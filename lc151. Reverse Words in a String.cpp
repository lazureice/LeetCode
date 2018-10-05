class Solution {
public:
    
    void reverseWords(string &s) {
        int i=0,j;
        
        while(i<s.size()){
            while(i<s.size()&&!isalpha(s[i])){
                i++;
            }
            j=i;
            while(j!=s.size()&&isalpha(s[j])){
                j++;
            }
            reverse(s.begin()+i,s.begin()+j);
            
            i=j;
        }
        reverse(s.begin(),s.end());
    }
};