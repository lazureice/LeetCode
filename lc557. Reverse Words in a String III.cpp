class Solution {
public:
    string reverseWords(string s) {
        auto i=s.begin(),j=s.begin();
        while(i!=s.end()){
            
            
            while(j!=s.end()&&((*j)!=' ')){
                j++;
            }
            reverse(i,j);
            if(j==s.end()){
                break;
            }
            i=++j;
            
        }
        // reverse(s.begin(),s.end());
        return s;
    }
};