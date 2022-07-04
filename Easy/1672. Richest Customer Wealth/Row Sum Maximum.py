class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for account in accounts:
            curr_wealth = sum(account)
            richest = max(richest, curr_wealth)
            
        return richest
