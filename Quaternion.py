
class Quaternion:

    def __init__(self,a,b,c,d):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)

    def __add__(self,other):
        return Quaternion(self.a + other.a,self.b + other.b,self.c + other.c,self.d + other.d)

    def __sub__(self,other):
        return Quaternion(self.a - other.a,self.b - other.b,self.c - other.c,self.d - other.d)


    def __mul__(self,other):
        a1,a2 = self.a , other.a
        b1,b2 = self.b , other.b
        c1,c2 = self.c , other.c
        d1,d2 = self.d , other.d

        a = a1*a2 - b1*b2 - c1*c2 - d1*d2
        b = a1*b2 + c1*d2 - d1*c2 + b1*a2
        c = a1*c2 + c1*a2 + d1*b2 - b1*d2
        d = a1*d2 - c1*b2 + d1*a2 + b1*c2

        return Quaternion(a,b,c,d)

    def __truediv__(self,other):
        """
        a1,a2 = self.a , other.a
        b1,b2 = self.b , other.b
        c1,c2 = self.c , other.c
        d1,d2 = self.d , other.d
    
        a = (a1*a2 + b1*b2 + c1*c2 + d1*d2) / n
        b = (b1*a2 + d1*c2 - a1*b2 - c1*d2) / n
        c = (b1*d2 + c1*a2 - d1*b2 -a1*c2) / n
        d = (d1*a2 - a1*d2 - b1*c2 - c1*b2) / n
        """
        r = None
        if isinstance(other,Quaternion) == False:

            self.a = self.a / other
            self.b = self.b / other
            self.c = self.c / other
            self.d = self.d / other

            r = self

        else:
            n = other.norm2()
            r = (other.conj() * self) / n 
    
        return r
        

    def __repr__(self):
        return "< %s | %s i | %s j | %s k >"%(self.a,self.b,self.c,self.d)

    def _maxSign(self):
        d = list(self.__dict__.values())
        return sum([2**i if d[i] != 0 else 0 for i in range(len(d))])

    def conj(self):
        b = -self.b
        c = -self.c
        d = -self.d
        return Quaternion(self.a,b,c,d)

    def norm2(self):
        return self.a **2 + self.b **2 + self.c **2 + self.d **2

    def __eq__(self,other):
        out = False
        if isinstance(other,Quaternion):
            out = self.a == other.a  and self.b == other.b  and self.c == other.c  and self.d == other.d
        return out

    def __ne__(self,other):
        return False if self == other else True

    def __gt__(self,other):
        #out = False
        #out = True if self.a > other.a else False
        #out = True if self.b > other.b else False
        #out = True if self.c > other.c else False
        #out = True if self.d > other.d else False

        out = None
        if self._maxSign() > other._maxSign():
            out = True
        elif self._maxSign() < other._maxSign():
            out = False
        else:
            out = False
            for c1,c2 in zip(list(self.__dict__.values()),list(other.__dict__.values())):
                if c1 > c2:
                    out = True
                    break
        return out


    def __ge__(self,other):
        out = False
        out = True if self.a >= other.a else False
        out = True if self.b >= other.b else False
        out = True if self.c >= other.c else False
        out = True if self.d >= other.d else False

        return out

    def __lt__(self,other):
        return False if self > other else True

    def __le__(self,other):
        return False if self >= other else True


if __name__ == "__main__":

    q1 = Quaternion(0,3,0,-1)
    q2 = Quaternion(2,0,1,1)
    qp = q1 + q2
    q = q1 * q2

    q22 = q / q1

    print(q1)
    print(q2)
    print(qp)
    print(q)
    qc= q.conj()
    print(qc)
    
    print(q22)

    print(q2 == q22)

    print(q1 > q)
    print(q < q)
    print(q == q1)
    print(q1 != q2)