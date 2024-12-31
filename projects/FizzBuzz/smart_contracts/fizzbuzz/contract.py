from algopy import ARC4Contract, Bytes, OpUpFeeSource, ensure_budget, subroutine, UInt64, String, urange, arc4

class Fizzbuzz(ARC4Contract):
    @arc4.abimethod()
    def fizzbuzz(self) -> arc4.DynamicArray[arc4.String]:
        result = arc4.DynamicArray[arc4.String]()
        for n in urange(100):
            # Need to do OpUps to get budget for the next iteration of the loop
            # WARNING: using OpUpFeeSource.AppAccount is unsafe for production
            # Instead, use OpUpFeeSource.GroupCredit, which sets innerTxn fees
            # to zero and forces calls to cover innerTxn fees on outerTxns
            ensure_budget(2550, OpUpFeeSource.AppAccount) # FOR DEMO ONLY

            result.append(arc4.String(self.divide(n + 1))) # Start from 1 not 0
        return result
    
    # The core FizzBuzz solution algorithm logic
    @subroutine
    def divide(self, number: UInt64) -> String:
        if number % 3 == 0 and number % 5 == 0:
            return String("FizzBuzz")
        elif number % 3 == 0:
            return String("Fizz")
        elif number % 5 == 0:
            return String("Buzz")
        else:
            return itoa(number)

# Utility to convert integers-->strings so they can be added to the result array
@subroutine
def itoa(int: UInt64) -> String:
    digits = Bytes(b"0123456789")
    radix = digits.length
    if int < radix:
        return String.from_bytes(digits[int])
    return itoa(int // radix) + String.from_bytes(digits[int % radix])

