class A:
    def method_a(self):
        return "ini adalah A"

class B:
    def method_b(self):
        return "ini adalah B"
    
class apalah(A, B): # -> mewarisakan dia class beserta methodnya masing masing
    pass

objek = apalah()
print(objek.method_a())
print(objek.method_b())