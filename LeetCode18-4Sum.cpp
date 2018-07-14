class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> ans;
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size();i++){
        // 这就是在前面判断，在3sum中，一个java代码就是这样做的。
        // 在4sum中，我不加辨别就直接套用了，但是没能通过`[0,0,0,0],target=0`。
        // 其实，我觉得即使是3sum，也通不过啊。尽管那个代码加了i<nums.length-2
        // if(i!=0&&nums[i]==nums[i-1]){continue;}
            int tgt3=target-nums[i];
            for(int j=i+1;j<nums.size();j++){
            // if(j!=0&&nums[j]==nums[j-1]){continue;}
                int tgt2=tgt3-nums[j];
                
                int left=j+1;
                int right=nums.size()-1;
                
                while(left<right){
                    if(nums[left]+nums[right]<tgt2){
                        left++;
                    }
                    else if(nums[left]+nums[right]>tgt2){
                        right--;
                    }
                    else{
                        vector<int> tem={nums[i],nums[j],nums[left],nums[right]};
                        ans.push_back(tem);
                        // 左指针右移，如果相等，继续
                        while (++left < right && nums[left] == nums[left - 1]) ;
                        while (--right > left && nums[right] == nums[right + 1]) ;
                    }
                }
                // 不能是`!=0`,因为是在后面判断，所以应该判断下一个，而不是前一个。
                while(j+1!=nums.size()&&nums[j]==nums[j+1]){j++;}
            }
            while(i+1!=nums.size()&&nums[i]==nums[i+1]){i++;}
        }
        return ans;
    }
    
};
