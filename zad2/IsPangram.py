class Pangram:
    def check(self, word):
        x = "abcdefghijklmnopqrstuvwxyz"
        y = ""
        if type(word) is str:
            if len(word) == 0:
                raise Exception("Empty word")
            else:
                for i in range(len(x)):
                    if x[i] in word.lower():
                        y += x[i]
                    else:
                        return False
                return True
        else:
            raise TypeError("Error")