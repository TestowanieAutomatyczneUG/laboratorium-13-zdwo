class FizzBuzz:
    def game(self, x):
        if type(x) is int:
            if x % 15 == 0:
                return "FizzBuzz"
            elif x % 3 == 0:
                return "Fizz"
            elif x % 5 == 0:
                return "Buzz"
            else:
                return x
        else:
            raise TypeError("Error")
