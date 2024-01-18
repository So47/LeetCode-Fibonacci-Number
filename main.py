
# solved by dynamic programming 'Bottom-Up Approach (Tabulation)'

class Solution:
    def fib(self, n: int) -> int:

        if n <= 1:
            return n


        dp = [0] * (n+1)

        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]        



# a recursive approach enhanced with memoization 'Top-Down Approach (Memoization)'

# with helper 'memoize_fib'
class Solution:
    def fib(self, n: int) -> int:
        # create a helper method that does the actual computation with memoization,
        def memoize_fib(n, memo): 
            if memo is None:
                return {}

            # Base cases
            if n <= 1:
                return n

            # Check if the result is already computed
            if n not in memo:
                memo[n] = memoize_fib(n-1, memo) + memoize_fib(n-2, memo)


            return memo[n]

        return memoize_fib(n, {})


# Use a Class Attribute

class Solution:
    def __init__(self):
        # Base cases
        self.memo = {0:0,1:1}

    def fib(self, n: int) -> int:
       
        # Check if the result is already computed
        if n in self.memo:
            return self.memo[n]
           
        self.memo[n] = self.fib(n-1) + self.fib(n-2)

        return self.memo[n]



# less efficient with straightforward recursive 

class Solution:

    def fib(self, n: int) -> int:
       
        if n <= 1:
          return n

        return self.fib(n-1) + self.fib(n-2)

             
        


