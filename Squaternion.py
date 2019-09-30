

class Squaternion:

    def __init__(self,a,b,c,d,s):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.s = s

    def __add__(self,other):
        return Squaternion(self.a + other.a,self.b + other.b,self.c + other.c,self.d + other.d,other.s)

    def __sub__(self,other):
        return Squaternion(self.a - other.a,self.b - other.b,self.c - other.c,self.d - other.d,self.s)


    def __mul__(self,other):
        a1,a2 = self.a , other.a
        b1,b2 = self.b , other.b
        c1,c2 = self.c , other.c
        d1,d2 = self.d , other.d
        s = self.s * other.s

        a = a1*a2 - b1*b2 - c1*c2 - d1*d2
        b = a1*b2 + c1*d2 - d1*c2 + b1*a2
        c = a1*c2 + c1*a2 + d1*b2 - b1*d2
        d = a1*d2 - c1*b2 + d1*a2 + b1*c2

        return Squaternion(a,b,c,d,s)

    def __truediv__(self,other):
        r = None
        if isinstance(other,Squaternion) == False:

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
        return "< %s | %s i | %s j | %s k | %s s>"%(self.a,self.b,self.c,self.d,self.s)

    def conj(self):
        self.b = -self.b
        self.c = -self.c
        self.d = -self.d

    def norm2(self):
        return self.a **2 + self.b **2 + self.c **2 + self.d **2

    def isEqual(self,other):
        out = False
        if isinstance(other,Squaternion):
            out = self.a == other.a  and self.b == other.b  and self.c == other.c  and self.d == other.d
        return out


    def tostring(self):
        return "< %s | %s i | %s j | %s k | %s s>"%(self.a,self.b,self.c,self.d,self.s)


if __name__ == "__main__":

    q1 = Squaternion(0,3,0,-1,1)
    q2 = Squaternion(2,0,1,1,-1)
    qp = q1 + q2
    q = q1 * q2

    print(q1)
    print(q2)
    print(qp)
    print(q)
    q.conj()
    print(q)
    

