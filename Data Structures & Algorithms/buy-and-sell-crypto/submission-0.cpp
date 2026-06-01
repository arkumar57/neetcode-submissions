class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buyingprice = 0;
        int sellingprice = 0;
        int profit = 0;

        if(prices.size() >= 0) {

            buyingprice = prices[0];
            sellingprice = prices[0];
        } else {
            return 0;
        }

        for(int i = 1; i < prices.size(); i++) {
            if (buyingprice <= prices[i]) {
                if(sellingprice > prices[i]) {
                    continue;
                } else {
                    sellingprice = prices[i];
                    profit = max(profit, sellingprice - buyingprice);
                    continue;
                }

            } else {
                buyingprice = prices[i];
                sellingprice = prices[i];
                profit = max(profit, sellingprice - buyingprice);
            }
        }

        return profit;
    }
};
