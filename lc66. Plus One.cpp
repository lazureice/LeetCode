class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int length=digits.size();
        for(int i=length;i!=0;i--){
            if(digits[i-1]!=9) {
                digits[i-1]++;
                break;
            }
            else{
                digits[i-1]=0;
                if(i==1){
                    
                    digits.insert(digits.begin(),1);
                }
                
                
            }
            
        }
        return digits;
    }
};
