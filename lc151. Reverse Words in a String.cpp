class Solution {
public:
    
    void reverseWords(string &s) {
        int i=0,j;
        while(i<s.size()&&s[i]==' '){
            i++;
        }
        s.erase(s.begin(),s.begin()+i);
        // 不应用索引，应该用迭代器
        i=0;
        while(i<s.size()){
            
            
            while(i<s.size()&&s[i]==' '){
                i++;
            }
            j=i;
            while(j!=s.size()&&s[j]!=' '){
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