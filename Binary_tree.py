class Node:
  def __init__(self, data, parent=None, left=None, right=None):
    self._data = data
    self._parent = parent
    self._left = left
    self._right = right

  def __str__(self):
    return self._data.__str__()


class Tree:
  def __init__(self, root = None):
    self._root = None 
    if root:
      self._root = Node(root, None, None, None)

  def insert(self, element, tree = None):
    if not tree: # se não informar a sub-arvore, parte da raiz
      tree = self._root
    leaf = Node(element, tree) # referencia para a folha
    if not self._root: # se a arvore estiver vazia, insere na raiz
      self._root = Node(element)  
    elif element < tree._data: # se o valor for menor que o do nó atual, segue o caminho da esquerda
      if tree._left: #se já existir um filho esquerdo, faz a chamada recursiva partindo desse filho
        self.insert(element, tree._left)
      else: # se não, insere a folha como filho esquerdo
        tree._left = leaf
    else: # se o valor for igual ou maior que o do nó atual, segue o caminho da direita, fazendo o mesmo processo
      if tree._right:
        self.insert(element, tree._right)       
      else:
        tree._right = leaf

  def remove(self, element):
    node = self.search(element) #busca se o elemento esta na arvore e retorna o nó correspodente
    if node: # se o nó existir, apaga o ponteiro que aponta para ele
      if node == self._root: # caso do nó ser a raiz
        self._root = None
      elif node._parent._left == node: # caso de ser filho esq
        node._parent._left = None
      else: # caso de ser filho dir
        node._parent._right = None 
      
  def in_order(self, tree):
    if tree._left:
      self.in_order(tree._left)
    print(tree)
    if tree._right:
      self.in_order(tree._right)

  def print_tree(self, tree, space = ""):
    space += "        "
    if tree._left:
      self.print_tree(tree._left, space)
    print(space + str(tree))
    if tree._right:
      self.print_tree(tree._right, space)
  
  def recursive_search(self, element, node):
    if not node or node._data == element:
      return node
    elif node._data > element:
      return self.recursive_search(element, node._left)
    else:
      return self.recursive_search(element, node._right)

  def search(self, element):
    tree = self._root
    while tree and tree._data != element:
      if element > tree._data:
        tree = tree._right
      else:
        tree = tree._left
    return tree
  
if __name__ == "__main__":
  T = Tree(21)
  T.insert(14)
  T.insert(28)
  T.insert(11)
  T.insert(18)
  T.insert(25)
  T.insert(32)
  T.insert(5)
  T.insert(12)
  T.insert(15)
  T.insert(19)
  T.insert(23)
  T.insert(27)
  T.insert(30)
  T.insert(37)
  T.print_tree(T._root)
  print(T.recursive_search(5, T._root))
  print(T.search(32))
  T.remove(37)
  T.remove(5)
  T.print_tree(T._root)