class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        
        
		#Pointers to keep track of which token to play face up and face down
        up, down = 0, len(tokens) - 1
		
        maxScore, curScore = 0, 0
        tokens.sort()
        
        while up <= down:
            if power>=tokens[up]:
                power -= tokens[up]
                curScore += 1
                up += 1
                maxScore = max(maxScore, curScore)
            elif curScore > 0:
                power += tokens[down]
                curScore -= 1
                down -= 1
            
            else:
                break
        
        return maxScore
        