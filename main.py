class PrimeFactors(object):

    def factors_of(self, n):
        factors = []
        divisor = 2
        while  n > 1:
            while  n % divisor  == 0:
                factors.append(divisor)
                n /= divisor
            divisor+= 1
        return factors

