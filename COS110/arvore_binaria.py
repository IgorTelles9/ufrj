#    Uma árvore binária de busca
#    Exercício 2POO dos laboratórios de Alg. Prog
#    Outubro de 2020

class Node:
    def __init__(self, data):
        self.left_branch =  None 
        self.right_branch = None
        self.parent = None
        self.data = data
        self.num_branches = 0

    def add(self,data):
        """ Adiciona um item a árvore """
        if data < self.data:
            if self.left_branch:
                self.left_branch.add(data)
            else:
                self.left_branch = Node(data)
                #print(self, self.left_branch)
                self.left_branch.parent = self
                #print(self.left_branch.parent)
        else:
            if self.right_branch:
                self.right_branch.add(data)
            else:
                self.right_branch = Node(data)
                self.right_branch.parent = self
    
    def search(self, data):
        """ Retorna o nó que contém o parâmetro 'data' na árvore """
        if data == self.data:
            return self
        elif data < self.data and self.left_branch:
            return self.left_branch.search(data)
        elif data >= self.data and self.right_branch:
            return self.right_branch.search(data)
        else:
            return None 
        
    def min(self):
        """ Retorna o menor valor da árvore """
        if self.left_branch:
            return self.left_branch.min()
        return self.data
    
    def max(self):
        """ Retorna o menor valor da árvore """
        if self.right_branch:
            return self.right_branch.max()
        return self.data

    def in_order(self):
        """ Impressão em ordem. """
        if self:
            if self.left_branch:
                self.left_branch.in_order()
            print(str(self.data), end=', ')
            if self.right_branch:
                self.right_branch.in_order()

    def pre_order(self):
        """ Impressão em pré ordem. """
        if self:
            print(str(self.data), end=', ')
            if self.left_branch:
                self.left_branch.pre_order()
            if self.right_branch:
                self.right_branch.pre_order()

    def post_order(self):
        """ Impressão em pós ordem. """
        if self:
            if self.left_branch:
                self.left_branch.post_order()
            if self.right_branch:
                self.right_branch.post_order()
            print(str(self.data), end=', ')

    def set_num_branches(self):
        if self.left_branch:
            self.num_branches +=1
        if self.right_branch:
            self.num_branches +=1 
    
    def min_node(self):
        if self.left_branch:
            return self.left_branch.min_node()
        return self 

    def delete(self):
        self.set_num_branches()

        if self.num_branches == 0:
            if self.parent.left_branch == self:
                self.parent.left_branch = None
            else:
                self.parent.right_branch = None
        #print(self.num_branches)
        #print(self.num_branches == 1)
        
        elif self.num_branches == 1:
            #print('hi')
            # pega o filho 
            if self.left_branch:
                branch = self.left_branch
            else:
                branch = self.right_branch
            
            # substitui o nó que chamou o delete pelo seu filho 
            if self.parent.left_branch == self:
                self.parent.left_branch = branch
            else:
                self.parent.right_branch = branch
            branch.parent = self.parent 

        elif self.num_branches == 2:
            min_branch = self.right_branch.min_node()
            self.data = min_branch.data 
            min_branch.delete()

    
class Tree:
    def __init__(self, root = None):
        if root:
            self.root = Node(root)
        else:
            self.root = None

    def empty(self):
        return self.root == None 
    
    def add(self, data):
        """ Adiciona um item a árvore """
        if self.root:
            self.root.add(data)
        else:
            self.root = Node(data)

    def search(self, data):
        """ Procura o parâmetro data na árvore """
        if self.root:
            return self.root.search(data)
        else:
            return None
        
    def min(self):
        """ Retorna o menor valor da árvore """
        if self.root.left_branch:
            return self.root.min()
        elif self.root:
            return self.root.data
        else:
            return None 
    
    def max(self):
        """ Retorna o maior valor da árvore """
        if self.root.right_branch:
            return self.root.max()
        elif self.root:
            return self.root.data
        else:
            return None 

    def in_order(self):
        """ Impressão em ordem. """
        print("Impressão em ordem: ", end='')
        self.root.in_order()

    def pre_order(self):
        """ Impressão em pré ordem. """
        print("Impressão em pré-ordem: ", end='')
        self.root.pre_order()

    def post_order(self):
        """ Impressão em pós ordem. """
        print("Impressão em pós-ordem: ", end='')
        self.root.post_order()
    
    def delete(self, data):
        try:
            return self.search(data).delete()
        except AttributeError:
            print(str(data) + " não está na árvore.")


def fill_tree(tree, num_elems=10, max_int=15):
    from random import randint
    for i in range(num_elems):
        elem = randint(0, max_int)
        tree.add(elem)
    return tree 


tree = Tree()
tree.add(10)
tree.add(21)
tree.add(15)
tree.add(40)
tree.add(30)
tree.add(50)
tree.add(4)
tree.add(3)
tree.add(2)
#print(tree.search(2))
tree.in_order()
print()
tree.delete(2)
tree.in_order()
print()
tree.delete(4)
tree.in_order()
print()
tree.delete(21)
tree.in_order()
print()
#print(tree.min())
#print(tree.max())
