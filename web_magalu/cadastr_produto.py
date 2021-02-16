class Cadastro:

    def __init__(self, titulo, preco, quanti, codigo_prod, id_vendedor):
        self.titulo = titulo
        self.preco = preco
        self.quanti = quanti
        self.codigo_prod = codigo_prod
        self.id_vendedor = id_vendedor


    def add(self, lista):
        self.lista = lista =[]
        lista.append(super(self.titulo, self.preco, self.quanti, self.codigo_prod, self.id_vendedor))
        return lista

    def consultar(self):
        return self.lista

    def atualizar(self):
        super(Cadastro, self).atualizar(self.lista)


class Produto(Cadastro):


    def produto(self):
        produtos = self.lista
        print(produtos)



    def inativar(self):
        status = False
        self.lista = status

    def deletado(self):
        pass

    def sem_estoque(self):
        pass

