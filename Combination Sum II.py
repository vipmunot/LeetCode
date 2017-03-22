class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        result = []
        candidates.sort()
        
        def dfs(remain, stack):
            if not remain:
                result.append([candidates[i] for i in stack])
        
            if not stack: c = 0
            else: c = stack[-1]+1
        
            for i in xrange(c, len(candidates)):
            
                item = candidates[i]
                if i > c and item == candidates[i-1]: continue
                if item > remain: break
                    
                dfs(remain-item, stack + [i])
            
        dfs(target, [])
        return result    