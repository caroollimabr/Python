class Fila:
    def __init__(self, fila = None):  # inicializa fila com base na lista fila. Por padrão, ela é vazia
        if fila == None:
            self.fila = []
        else:
            self.fila = fila

    def __eq__(self, outra):  # retorna true se as filas sef e outra tiverem os msms itens na msm ordem
        return self.fila == outra.fila

    def __len__(self):  # retorna número de itens na fila
        return len(self.fila)

    def __repr__(self):  # retorna representação de string canônica da fila
        return 'Fila({})'.format(self.fila)

class Fila2(list):  # classe de fila, subclasse de list
    def esta_vazia(self):  # retorna True se a file estiver vazia
        return (len(self) == 0)

    def remove_mostra_primeiro_item(self):  
        if len(self) == 0:  # se fila vazia
            raise KeyboardInterrupt()
        return self.fila.pop(0)  # remove e retorna item na frente da fila

    def insere_item_final_fila(self, item):
        return self.append(item)