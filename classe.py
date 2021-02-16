"""
func_1 = Funcionario()

func_1.nome = "Leia"
func_1.sobrenome = "Organa"
func_1.email = "leia@rebeliao.com"
func_1.salario = 1_000_000

print(func_1.email)
print(func_1.nome)

#Forma manual de criar
print(func1.email)
print(func2.email)

#print(f"{func1.nome} {func1.sobrenome}")

print(func1.nomeCompleto())
func2.aumento()
print(func2.salario)
func1.valor = 1.10 #acresenta mais uma chave e valor ao dict e não um novo valor, já que ele só esta na classe

print(func1.salario)
print(func1.__dict__)

print(func3.lingProg)

print(Funcionario.num_func)

#print(func4.listar())
#func4.add(func1)

print(isinstance(func1, Funcionario))
print(issubclass(Funcionario, Dev))
#print(isinstance(func4, Gerente))

"""
import datetime

class Funcionario:

    num_func = 0
    valor = 1.05

    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario
        self.email = nome + "." + sobrenome + "@gmail.com"

        Funcionario.num_func += 1

    def nomeCompleto(self):
        return f"{self.nome} {self.sobrenome}"

    def aumento(self):
        self.salario = self.salario * self.valor

    @classmethod
    def string(cls, func_str):
        nome, sobrenome, salario = func_str.split("-")
        return cls(nome, sobrenome, salario)

    @staticmethod
    def diaSemana(dia):
        if dia.weekday() == 5 or dia.weekday() == 6:
            return False
        return True


class Dev(Funcionario):

    def __init__(self, nome, sobrenome, salario, lingProg):
        super().__init__(nome, sobrenome, salario)
        self.lingProg = lingProg

class Gerente(Funcionario):

    def __init__(self, nome, sobrenome, salario, funcionarios=None):
        super().__init__(self, nome, sobrenome, salario)
        self.funcionarios = funcionarios

        if funcionarios is None:
            self.funcionarios = []
        else:
            self.funcionarios = funcionarios

    def add(self, func):
        if self.func not in self.funcionarios:
            self.funcionarios.append(func)

    def remover(self, func):
        if func in self.funcionarios:
            self.funcionarios.remove(func)

    def listar(self):
        for func in self.funcionarios:
            print(f"---> Nome: {func.nomeCompleto()}")



func1 = Funcionario("Leia", "Organa", 1_000)
func2 = Funcionario("Luke", "Skywalker", 800)
func3 = Dev("Yoda", "Mestre", 15_000, "Python")
#func4 = Gerente("Lando", "calrissian", 2500, [])

func_str1 = "Viuva-Negra-12000"
func_str2 = "Peter-Park-3000"


func4 = Funcionario.string(func_str1)
print(func4.nomeCompleto())

minhaData = datetime.date(2020, 11, 11)
print(Funcionario.diaSemana(minhaData))




