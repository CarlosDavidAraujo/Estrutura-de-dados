from abc import ABC, abstractmethod


class TreeADT(ABC):

    @abstractmethod
    def insert(self, value):
        """Método de inserção de informação na árvore"""
        pass

    @abstractmethod
    def empty(self):
        """Método que retorna True, caso a árvore esteja vazia, False caso contrário"""
        pass

    @abstractmethod
    def root(self):
        """Método que retorna o nó raiz da árvore. Se a árvore estiver vazia, None deve ser retornado"""
        pass


class Node:

    def __init__(self, data=None, parent=None, left=None, right=None):
        self._data = data
        self._parent = parent
        self._left = left
        self._right = right

    def empty(self):
        return not self._data

    def __str__(self):
        return self._data.__str__()


class BinaryTree(TreeADT):

    def __init__(self, data=None):
        self._root = Node(data)

    def insert(self, data, parent = None):
      if not parent: 
        parent = self._root
      leaf = Node(data, parent) 
      if self.empty(): 
        self._root = Node(data)  
      elif data < parent._data: 
        if parent._left: 
          self.insert(data, parent._left)
        else: 
          parent._left = leaf
      else: 
        if parent._right:
          self.insert(data, parent._right)       
        else:
          parent._right = leaf

    def remove(self, data):
      node = self.search(data) #busca se o elemento esta na arvore e retorna o nó correspodente
      if node: # se o nó existir, apaga o ponteiro que aponta para ele
        if node == self._root: # caso do nó ser a raiz
          self._root = None
        elif node._parent._left == node: # caso de ser filho esq
          node._parent._left = None
        else: # caso de ser filho dir
          node._parent._right = None 
        
    def recursive_search(self, data, node):
      if not node or node._data == data:
        return node
      elif node._data > data:
        return self.recursive_search(data, node._left)
      else:
        return self.recursive_search(data, node._right)

    def search(self, data):
      node = self._root
      while node and node._data != data:
        if data > node._data:
          node = node._right
        else:
          node = node._left
      return node
        
    def traversal(self, in_order=True, pre_order=False, post_order=False):
        list = [[],[],[]]
        if in_order: 
          list[0] = self.__in_order(self._root, [])
        if pre_order:
          list[1] = self.__pre_order(self._root, [])
        if post_order:
          list[2] = self.__post_order(self._root, [])
        return list
                     
    def __in_order(self, node, list):
      if node._left:
        self.__in_order(node._left, list)
      list.append(node._data)
      if node._right:
        self.__in_order(node._right, list)
      return list

    def __pre_order(self, node, list):
      list.append(node._data)
      if node._left:
        self.__pre_order(node._left, list)
      if node._right:
        self.__pre_order(node._right, list)
      return list

    def __post_order(self, node, list):
      if node._left:
        self.__post_order(node._left, list)
      if node._right:
        self.__post_order(node._right, list)
      list.append(node._data)
      return list

    def empty(self):
        return not self._root._data
    
    def root(self):
        return self._root._data

    def print_2d_tree(self, node, space=""):
      space += "        "
      if node._left:
        self.print_2d_tree(node._left, space)
      print(space + str(node._data))
      if node._right:
        self.print_2d_tree(node._right, space)
      


def menu():
    print('1 - adicionar folha')
    print('2 - imprimir arvore em ordem')
    print('3 - imprimir arvore em pré-ordem')
    print('4 - imprimir arvore em pós-ordem')
    print('5 - remover nó')
    print('6 - imprimir arvore em 2d')
    opcao = int(input())
    return opcao
    
if __name__ == '__main__':
    bt = BinaryTree()
    bt.insert(21)
    bt.insert(14)
    bt.insert(28)
    bt.insert(11)
    bt.insert(18)
    bt.insert(25)
    bt.insert(32)
    print(bt.empty())
    print(bt.root())
    opt = menu()
    while opt < 7:
      if opt == 1:
        leaf = int(input("Digite o valor da folha: "))
        bt.insert(leaf)
      elif opt == 2:    
        print(bt.traversal()) 
      elif opt == 3:     
        print(bt.traversal(False, True)) 
      elif opt == 4:      
        print(bt.traversal(False, False, True))
      elif opt == 5:
        data = int(input("Digite o valor do nó que deseja remover: "))
        bt.remove(data)
        print(bt.traversal())
      elif opt == 6:
        bt.print_2d_tree(bt._root)
      opt = menu()
