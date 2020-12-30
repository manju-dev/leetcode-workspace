# Problem 122: Best Time to Buy and Sell Stock II
class Solution(object):
    # Approach 1: Brute Force
    def maxProfit1(self, prices) -> int:
        return self.calculate(prices, 0)

    def calculate(self, prices, init):
        if(init >= len(prices)):
            return 0
        profitFinal = 0
        for i in range(init, len(prices)):
            profitInter = 0
            for j in range(i+1, len(prices)):
                if(prices[i] < prices[j]):
                    profit = self.calculate(prices, j+1) + prices[j] - prices[i]
                    if(profit > profitInter):
                        profitInter = profit
            if (profitInter > profitFinal):
                profitFinal = profitInter
        return profitFinal

    # Approach 2: Peak Valley Approach
    def maxProfit2(self, prices) -> int:
        i = 0
        valley = prices[0]
        peak = prices[0]
        profit = 0
        while(i < len(prices) - 1):
            while(i < len(prices) - 1 and prices[i] >= prices[i+1]):
                i += 1
            valley = prices[i]
            while(i < len(prices) - 1 and prices[i] <= prices[i+1]):
                i += 1
            peak = prices[i]
            profit += peak - valley
        return profit

    # Approach 3: Simple One Pass
    def maxProfit(self, prices) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if(prices[i] > prices[i-1]):
                profit += prices[i] - prices[i-1]
        return profit

# Test
solution = Solution()
# should be 7
print(solution.maxProfit([7,1,5,3,6,4]))
# should be 4
print(solution.maxProfit([1,2,3,4,5]))
# should be 0
print(solution.maxProfit([7,6,4,3,1]))
# should be 12
print(solution.maxProfit([1, 7, 2, 3, 6, 7, 6, 7]))