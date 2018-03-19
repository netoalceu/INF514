class Funcionario():
    empresa = "XBLUFT Ltda "
    aliq = 0.27

    def __init__(self,n,r,v):
        self.nome = n
        self.registro = r
        self.valorHora= v

    def calc(self,nh):
        return nh * self.valorHora

    def irpf(self,nh):
        return self.calc(nh) *self.aliq

class Vendedor(Funcionario):
    ajCusto = 600.00

    def calc (self,nh):
        return nh * self.valorHora + self.ajCusto








def list(f,h):
    print(f.empresa,f.nome,f.registro,f.calc(h),f.irpf(h))

def test():
    f1 = Funcionario("Joao","001",25.0)
    f2 = Funcionario("Jose","002",25.5)
    v1 = Vendedor("Pedro","003",23.2)
    list(f1,180)
    list(f2,180)
    list(v1,180)

if __name__ == "__main__":
    test()