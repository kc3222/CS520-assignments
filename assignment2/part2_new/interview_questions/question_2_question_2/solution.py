from typing import List
from collections import Counter
import math

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        if n == 0:
            return 0

        # --- Union-Find (Disjoint Set Union) ---
        parent = list(range(n))
        size = [1]*n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: int, y: int) -> None:
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if size[rx] < size[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            size[rx] += size[ry]

        # --- Sieve primes up to sqrt(maxA) to speed up factoring ---
        maxA = max(A)
        limit = int(math.isqrt(maxA)) + 1
        is_prime = [True]*(limit+1)
        primes = []
        for p in range(2, limit+1):
            if is_prime[p]:
                primes.append(p)
                step = p
                start = p*p
                for m in range(start, limit+1, step):
                    is_prime[m] = False

        # Map: prime factor -> index in A that has this factor (representative)
        factor_rep = {}

        # Factor each number, union with previous indices that share factors
        for i, val in enumerate(A):
            x = val
            # collect distinct prime factors
            factors = []
            for p in primes:
                if p*p > x:
                    break
                if x % p == 0:
                    factors.append(p)
                    while x % p == 0:
                        x //= p
            if x > 1:  # remaining prime factor
                factors.append(x)

            # Union current index with representative of each factor
            for f in factors:
                if f in factor_rep:
                    union(i, factor_rep[f])
                else:
                    factor_rep[f] = i

        # Count component sizes by root representative
        comp_count = Counter(find(i) for i in range(n))
        return max(comp_count.values())
