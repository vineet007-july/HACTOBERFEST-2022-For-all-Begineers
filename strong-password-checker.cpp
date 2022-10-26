//URL for problem: https://leetcode.com/problems/strong-password-checker/

class Solution {
public:
    bool hasLowerCase;
    bool hasUpperCase;
    bool hasDigit;
    int change;
    int basic;
    //
    int repeat;
    std::unordered_map<int, int> uMap; //uMap[last_index] = repeat
    std::unordered_map<int, int>::iterator itu;
    std::unordered_set<int> dSet;
    //
    int extra;
    
    void helperLUD(std::string& password, int& n){
        basic = 0;
        for (int i=0; i<n; i++){
            if (!hasLowerCase && password[i]>='a' && password[i]<='z'){
                hasLowerCase = true;
                basic++;
                continue;
            }
            
            if (!hasUpperCase && password[i]>='A' && password[i]<='Z'){
                hasUpperCase = true;
                basic++;
                continue;
            }
            
            if (!hasDigit && password[i]>='0' && password[i]<='9'){
                hasDigit = true;
                basic++;
            }
        }   
        return;
    }
    
    
    void helperThree(std::string& password, int& n){
        repeat = 1;
        for (int i=1; i<n; i++){
            if (password[i]==password[i-1]){
                repeat++;
            }else{
                if (repeat>=3){
                    uMap[i-1] = repeat;
                }
                repeat = 1;
            }
        }
        if (repeat>=3){
            uMap[n-1] = repeat;
        }
        repeat = 1;
        return;
    }
    
    int strongPasswordChecker(string password) {
        int n = password.size();
        hasLowerCase = false;
        hasUpperCase = false;
        hasDigit = false;
        change = 0;
        int temp = 0;
        bool stopLoop;
        //
        if (n<6){
            helperLUD(password, n);
            basic = std::min(3, basic+(6-n));
            change += 6-n;
            if (basic<3){
                change += (3-basic);
            }
            return change;
        }
        //
        if (n>=6 && n<=20){
            helperLUD(password, n);
            helperThree(password, n);
            for (itu=uMap.begin(); itu!=uMap.end(); itu++){
                temp = (itu->second/3);
                change += temp;
                if (basic<3){
                    basic = std::min(3, basic+temp);
                }
            }
            if (basic<3){
                change += (3-basic);
            }
            return change;
        }
        //
        if (n>20){
            extra = n-20;
            helperLUD(password, n);
            helperThree(password, n);
            
            while (extra>0 && uMap.size()>0){
                stopLoop = true;
                //delete extra elements: "baa(a)b"
                for (itu=uMap.begin(); itu!=uMap.end(); itu++){
                    if (extra>=1 && itu->second>=3 && itu->second%3==0){
                        change++;
                        itu->second--;
                        extra--;
                        if (itu->second<3){
                            dSet.insert(itu->first);
                        }
                        stopLoop = false;
                    }
                }
                
                //delete extra elements: "baa(aa)b"
                for (itu=uMap.begin(); itu!=uMap.end(); itu++){
                    if (extra>=2 && itu->second>3 && itu->second%3==1){
                        change+=2;
                        itu->second-=2;
                        extra-=2;
                        if (itu->second<3){
                            dSet.insert(itu->first);
                        }
                        stopLoop = false;
                    }
                }
                
                //delete extra elements: "baa(aaa)b"
                for (itu=uMap.begin(); itu!=uMap.end(); itu++){
                    if (extra>=3 && itu->second>3 && itu->second%3==2){
                        change+=3;
                        itu->second-=3;
                        extra-=3;
                        if (itu->second<3){
                            dSet.insert(itu->first);
                        }
                        stopLoop = false;
                    }
                }
                
                for (auto it=dSet.begin(); it!=dSet.end(); it++){
                    uMap.erase(*it);
                }
                dSet.clear();
                
                if (stopLoop) break;
            
                //std::cout<<"uMap.size() = "<<uMap.size()<<"\n";
                //std::cout<<"extra = "<<extra<<"\n";
            }//while (extra, uMap)
            
            //replace
            for (itu=uMap.begin(); itu!=uMap.end(); itu++){
                if (itu->second>=3){
                    change += (itu->second)/3;
                    if (basic<3){
                        basic = std::min(3, basic+(itu->second)/3);
                    }
                    itu->second = (itu->second)%3;
                }                
            }
            
                
            change += extra;
            
            if (basic<3){
                change += (3-basic);
            }
            return change;
        }

        return -1;
        
    }
};