class Solution:
    # solution 1
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        teams = n
        while teams != 1:
            if teams % 2 == 0:
                matches += teams/2
                teams = teams/2
            else:
                matches += (teams-1)/2
                teams = (teams-1)/2 + 1
            
        return int(matches)
    
# solution 2
    def numberOfMatches2(self, n: int) -> int: 
        return int(n - 1) 
    # The total number of matches is always one less than the number of teams because 
    # each match eliminates one team until one team remains
    
if __name__ == "__main__": 
    sol = Solution()
    print(sol.numberOfMatches(7))
    print(sol.numberOfMatches(14))
    print(sol.numberOfMatches2(7))
    print(sol.numberOfMatches2(14))