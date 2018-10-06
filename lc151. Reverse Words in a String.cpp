class Solution {
public:
    
    void reverseWords(string &s) {
        int i=0,j;
        while(i<s.size()&&s[i]==' '){
            i++;
        }
        s.erase(s.begin(),s.begin()+i);
        while(i<s.size()){
            
            
            while(i<s.size()&&!isalnum(s[i])){
                i++;
            }
            j=i;
            while(j!=s.size()&&isalnum(s[j])){
                j++;
            }
            reverse(s.begin()+i,s.begin()+j);
            
            i=j;
            while(i<s.size()&&s[i]!=' '){
                i++;
            }
            j=i;
            while(j<s.size()&&s[j]==' '){
                j++;
            }
            if(j==s.size()){
                s.erase(s.begin()+i,s.begin()+j);
            }
            else{
                s.erase(s.begin()+i,s.begin()+j-1);
            }
        }
        reverse(s.begin(),s.end());
    }
};