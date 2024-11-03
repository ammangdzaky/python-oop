# method resolution -> terjadi ketika nama method sama

class A:
    def info(self):
        print("show class A")

class B:
    def info(self):
        print("show class B")
        
class C(A,B): #urutan eksekusinya yaitu C -> A -> B (jika nama method sama)
    pass

class D(B,A):
    pass

class E(A,B):
    def info(self):
        print("show class E")

c = C()
d = D()
e = E()

c.info()
d.info()
e.info()

print('\n')
print(help(c))