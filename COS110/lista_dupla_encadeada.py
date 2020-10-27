#    Lista duplamente encadeada
#    Exercício 1POO dos laboratórios de Alg. Prog
#    Outubro de 2020

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class Lista_Dupla_Encadeada:
    def __init__(self):
        self.head = None
        self._size = 0

    def empty(self):
        """ Retorna True se a lista está vazia """
        return self.head == None
    
    def _get_node(self, index):
        """ Retorna o nó do índice index"""
        pointer = self.head
        if (index < 0):
            index = self._size + index 
        for i in range(index):
            if pointer: 
                pointer = pointer.next 
            else:
                raise IndexError ("list index out of range")
        return pointer
    
    def __getitem__(self, index): 
        """ Retorna o elemento de índice index """
        pointer = self._get_node(index)
        if pointer:
            return pointer.data
        raise IndexError ("list index out of range")

    def append(self, data):
        """ Adiciona um elemento ao fim da lista. """
        if self.head:
            tail = self._get_node(-1)
            tail.next = Node(data)
            tail.next.previous = tail 
        else:
            self.head = Node(data)
        self._size +=1

    def __len__(self):
        """ Retorna o tamanho da lista """
        return self._size 

    def pop(self):
        """ Remove o último item adicionado a lista """
        tail = self._get_node(-1)
        data = tail.data
        if self.head.next:
            tail.previous.next = None
        else:
            self.head = None
        self._size-=1
        return data

    def __repr__(self):
        """ Uma representação elegante para um print"""
        r = ""
        pointer = self.head
        while (pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r
    
    def __str__(self):
        return self.__repr__()

from random import randint
lista = Lista_Dupla_Encadeada()
for i in range(10):
    lista.append(randint(0,10))
print(lista)
print(lista.pop())
print(lista)


