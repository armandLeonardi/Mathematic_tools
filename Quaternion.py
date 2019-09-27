
quaternionRules = {'i':{'i':-1,'j':'k','k':'-j'},'j':{'i':'-k','j':-1,'k':'i'},'k':{'i':'j','j':'-i','k':-1}}
class Quaternion:

    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self,other):
        return Quaternion(self.a + other.a,self.b + other.b,self.c + other.c,self.d + other.d)

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

    def __repr__(self):
        STR = ""
        for k,v in self.__dict__.items():
            STR += "| %s : %s |"%(k,v)
        return STR

    def conj(self):
        self.b = -self.b
        self.c = -self.c
        self.d = -self.d



if __name__ == "__main__":

    q1 = Quaternion(0,3,0,-1)
    q2 = Quaternion(2,0,1,1)
    qp = q1 + q2
    q = q1 * q2

    print(q1)
    print(q2)
    print(qp)
    print(q)
    q.conj()
    print(q)
    