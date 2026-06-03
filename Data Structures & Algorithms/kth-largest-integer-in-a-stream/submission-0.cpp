#include <queue>
class KthLargest {
public:

    int kk;

    priority_queue<int, vector<int>, greater<int>> pq;

    KthLargest(int k, vector<int>& nums) {
        
        kk = k;

        for(int n:nums) {
            pq.push(n);
        }

        while(pq.size() > kk) {

            pq.pop();
        }
    }
    
    int add(int val) {
        
        pq.push(val);

        while(pq.size() > kk) {

            pq.pop();
        }

        return pq.top();


    }
};
