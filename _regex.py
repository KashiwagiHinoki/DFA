class _Regex:
    def __init__(self, s: str):
        self.s = s

    def __eq__(self, x):
        if self.s == None and x.s == None:
            return True
        if self.s == None:
            return False
        if x.s == None:
            return False
        return self.s == x.s

    def __add__(self, x):
        if x == empty_set:
            return self
        if self == empty_set:
            return x
        return self.__class__("(" + self.s + "+" + x.s + ")")

    def __radd__(self, x):
        if x == empty_set:
            return self
        if self == empty_set:
            return x
        return self.__class__("(" + x.s + "+" + self.s + ")")
    
    def __mul__(self, x):
        if x == empty_set or self == empty_set:
            return empty_set
        return self.__class__("(" + self.s + x.s + ")")

    def __rmul__self(self, x):
        if x == empty_set or self == empty_set:
            return empty_set
        return self.__class__("(" + self.s + x.s + ")")
    
    def __str__(self):
        if self.s == None:
            return "empty_set"
        return self.s
    
    def rep(self):
        if self.s == None:
            return None
        return self.__class__("("+self.s+")*")
            
empty_set = _Regex(None)
