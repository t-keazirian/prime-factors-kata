class PrimeFactors(object):

    def factors_of(self, n):
        factors = []
        if n > 1:
            while  n % 2  == 0:
                factors.append(2)
                n /= 2
            while  n % 3  == 0:
                factors.append(3)
                n /= 3
        if n > 1:
            factors.append(n)
        return factors

