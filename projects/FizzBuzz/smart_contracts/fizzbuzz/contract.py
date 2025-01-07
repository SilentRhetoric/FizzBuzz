from algopy import ARC4Contract, Bytes, OpUpFeeSource, ensure_budget, subroutine, UInt64, String, urange, arc4

class Fizzbuzz(ARC4Contract):
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
        
    @arc4.abimethod()
    def fizzbuzz(self) -> arc4.DynamicArray[arc4.String]:
        # Instantiate an empty but dynamic-length array of strings to return
        result = arc4.DynamicArray[arc4.String]() # Note this is an array only of strings
        for n in urange(100):
            # Need to do OpUps to get OpCode budget for the next iteration of the loop
            ensure_budget(2550, OpUpFeeSource.GroupCredit) 

            result.append(arc4.String(self.divide(n + 1))) # Start from 1 not 0
        return result


# Utility to convert integers-->strings so they can be added to the result array
@subroutine
def itoa(int: UInt64) -> String:
    digits = Bytes(b"0123456789")
    radix = digits.length
    if int < radix:
        return String.from_bytes(digits[int])
    return itoa(int // radix) + String.from_bytes(digits[int % radix])

