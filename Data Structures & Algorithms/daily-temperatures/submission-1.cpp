class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {

        vector<int> result(temperatures.size());

        for (int i = 0; i < temperatures.size(); i++) {

            int j = i + 1;

            while(j < temperatures.size() && temperatures[j] <= temperatures[i]) {

                j++;
            }

            if(j < temperatures.size()) {

                result[i] = j - i;
            } else {

                result[i] = 0;
            }

        }

        return result; 
        
    }
};
