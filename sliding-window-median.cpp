//https://leetcode.com/problems/sliding-window-median/

class Solution {
public:

    void insert(multiset<double,greater<double>> &left, multiset<double> &right, int num)
    {
            if(left.empty() || num < *left.begin())
            {
                left.insert(num);
            }
            else
            {
                right.insert(num);
            }
    }

    void balance(multiset<double,greater<double>> &left, multiset<double> &right)
    {
            if(left.size() + 1 < right.size())
            {
                left.insert(*right.begin());
                right.erase(right.begin());
            }
            else if(right.size() + 1 < left.size())
            {
                right.insert(*left.begin());
                left.erase(left.begin());
            }
    }

    void add_median(multiset<double,greater<double>> &left, multiset<double> &right, vector<double> &median)
    {
        if(right.size() == left.size())
        {
            median.push_back((*left.begin() + *right.begin())/2.0);
        }
        else if(right.size() > left.size())
        {
            median.push_back(*right.begin());
        }
        else
        {
            median.push_back(*left.begin());
        }

    }

    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        multiset<double> right;
        multiset<double,greater<double>> left;

        vector<double> median;

        for(int i = 0; i<k; i++)
        {
            insert(left,right,nums[i]);
            balance(left,right);
        }

        add_median(left,right,median);

        for(int i = k; i<nums.size(); i++)
        {
            auto lcheck = left.find(nums[i-k]);
            auto rcheck = right.find(nums[i-k]);

            if(lcheck != left.end())
            {
                left.erase(lcheck);
            }
            else
            {
                right.erase(rcheck);
            }

            balance(left,right);
            insert(left,right,nums[i]);
            balance(left,right);
            add_median(left,right,median);

        }

        return median;
    }

};