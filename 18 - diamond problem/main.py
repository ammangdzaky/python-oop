# diamond problem -> sama seperti kasus multiple inheritance, tapi berbentuk diamond


class A:
    def info(self):
        print("info class A")

class B:
    def info(self):
        print("info class B")

class C:
    def info(self):
        print("info class C")
        
class D(B,C): # sama aja urutannya seperti pada multiple inheritance
    pass

d = D()
d.info()
print("\n")
print(help(d))
