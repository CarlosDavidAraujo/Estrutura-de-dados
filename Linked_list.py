from abc import ABC, abstractmethod


class ListADT(ABC):

    @abstractmethod
    def insert(self, indice, elemento):
        """Insere <elemento> na posição <indice>"""
        pass

    @abstractmethod
    def remove(self, elemento):
        """Remove primeira ocorrência de <elemento>"""
        pass

    @abstractmethod
    def count(self, elemento):
        """Conta a quantidade de <elemento> na lista"""
        pass

    @abstractmethod
    def clear(self):
        """Apaga a lista"""
        pass

    @abstractmethod
    def index(self, elemento):
        """Retorna o primeiro índice de <elemento>"""
        pass

    @abstractmethod
    def length(self):
        """Retorna o tamanho da lista"""
        pass

    @abstractmethod
    def remove_all(self, elemento):
      """Remove todas as ocorrências do <elemento>"""
      pass

    @abstractmethod
    def remove_at(self, index):
      """Remove o elemento que se encontra na posição <index> da lista"""
      pass

    @abstractmethod
    def append(self, elemento):
      """Concatena <elemento> na lista"""
      pass

    @abstractmethod
    def replace(self, index, elemento):
      """Substitui na posição <index> o valor existente com <elemento>"""
      pass

class MyList(ListADT):

    def __init__(self):
        self._data = list()
        self._length = 0

    def insert(self, indice, elemento):
        self._data.insert(indice, elemento)
        self._length = self._length + 1

    def remove(self, elemento):
        self._data.remove(elemento)
        self._length -= 1

    def count(self, elemento):
        return self._data.count(elemento)

    def clear(self):
        self._data = list()
        self._length = 0

    def index(self, elemento):
        return self._data.index(elemento)

    def length(self):
        return self._length

    def length2(self):
        return len(self._data)

    def __str__(self):
        return self._data.__str__()

    def remove_all(self, elemento):
        for i in self:
            if self.index(i) == elemento:
                self._data.remove(elemento)

    def __iter__(self):
        return self._data.__iter__()


class Node(object):

    def __init__(self, element=None, next_element=None):
        self._element = element
        self._next = next_element

    def __str__(self):
        if not self._next:
            return '|' + self._element.__str__() + '|'
        else:
            return '|' + self._element.__str__()


class LinkedList(ListADT):

    def __init__(self, elem=None):
        if elem:
            self._head = Node(elem)     # Atenção ao manipular esta referência
            self._tail = self._head     # Facilita a inserção no fim da lista
            self._length = 1
        else:
            self._head = None   # Atenção ao manipular esta referência
            self._tail = None   # Facilita a inserção no fim da lista
            self._length = 0

    def insert(self, index, elem):
        # a inserção pode acontecer em três locais: início, meio e fim da lista
        # separei em métodos diferentes (privados) para facilitar o entendimento e a legibilidade
        n = Node(elem)  # nó a ser inserido na lista
        if index == 0:  # primeiro local de inserção é no começoo da lista
            self.__insert_at_beginning(n)
        elif index >= self._length: # segundo local de inserçãa é no fim da lista
            self.__insert_at_end(n)  # se o índice passado foi maior que o tamanho da lista, insiro no fim
        else:  # por fim, a inserção no meio da lista
           self.__insert_in_between(index, n)
        self._length += 1  # apóss inserido, o tamanho da lista é modificado

    def __insert_at_beginning(self, n):
        if self.empty():  # caso particular da lista vazia
            self.__empty_list_insertion(n)
        else:  # se houver elemento na lista
            n._next = self._head  # o head atual passa a ser o segundo elemento
            self._head = n  # e o novo nó criado passa a ser o novo head

    def __insert_at_end(self, n):
        if self.empty():  # caso particular da lista vazia
            self.__empty_list_insertion(n)
        else:
            self._tail._next = n  # o último elemento da lista aponta para o nó criado
            self._tail = n  # o nó criado passa a ser o último elemento

    def __empty_list_insertion(self, node):
        # na inserção na lista vazia, head e tail apontam para o nó
        self._head = node
        self._tail = node

    def __insert_in_between(self, index, n):  # 3
        pos = 0  # a partir daqui vamos localizar a posição de inserção
        aux = self._head  # variável auxiliar para nos ajudar na configuração da posição do novo nó
        while pos < index - 1:  # precorre a lista até a posição imediatamente anterior
            aux = aux._next  # A posição onde o elemento será inserido
            pos += 1
        n._next = aux._next  # quando a posição correta tiver sido alcançada, insere o nó
        aux._next = n

    def remove(self, elem):
        if not self.empty():  # Só pode remover se a lista não estiver vazia, não é?!
            aux = self._head
            if aux._element == elem:  # Caso especial: elemento a ser removido está no head
                self._head = aux._next  # head passa a ser o segundo elemento da lista
            else:
                removed = False  # Flag que marca quando a remoção foi feita
                while aux._next and not removed:  # verifico se estamos no fim da lista e não foi removido elemento
                    prev = aux
                    aux = aux._next  # passo para o próximo elemento
                    if aux._element == elem:  # se for o elemento desejado, removo da lista
                        prev._next = aux._next
                        removed = True  # marco que foi removido
            self._length -= 1

    def count(self, elem):
        counter = 0
        if not self.empty():  # Verifica se a lista não está vazia (só faz sentido contar em lists não vazias!)
            aux = self._head  # Se a lista não estiver vazia, percorre a lista contando as ocorrências
            if aux._element is elem:
                counter += 1
            while aux._next:  # precorrendo a lista....
                aux = aux._next
                if aux._element is elem:
                    counter += 1
        return counter

    def clear(self):
        self._head = None  # todos os nós que compunham a lista serão removidos da memória pelo coletor de lixo
        self._tail = None
        self._length = 0

    def index(self, elem):
        result = None
        pos = 0
        aux = self._head
        # Vamos percorrer a lista em busca de elem
        while not result and pos < self._length:  # lembrando que not None é o mesmo que True
            if aux._element is elem:
                result = pos
            aux = aux._next
            pos += 1
        return result  # se o elemento não estiver na lista, retorna None

    def length(self):
        return self._length

    def empty(self):
        return not self._head

    def __len__(self):
        return self._length

    def __str__(self):
        if not self.empty():
            result = ''
            aux = self._head
            result += aux.__str__()
            while aux._next:
                aux = aux._next
                result += aux.__str__()
            return result
        else:
            return '||'

    def remove_all(self, elem):
      if not self.empty():
        aux = self._head
        while aux._element == elem:
          self._head = aux._next
          aux = self._head
          self._length -= 1
          
        while aux._next:
          prev = aux
          aux = aux._next
          if aux._element == elem:
            prev._next = aux._next
            aux = prev
            self._length -= 1
            
        if self._tail._element == elem:
          self._tail = prev
             
    def remove_at(self, index):
      if not self.empty() and index < self._length:
        pos = 0
        aux = self._head
        if index == 0: #se for o primeiro elemento
          self._head = aux._next         
        else: 
          while pos < index:
            prev = aux
            aux = aux._next
            pos += 1
      
          prev._next = aux._next
          if pos == self._length -1: #se for o ultimo elemento 
            self._tail = prev # atualiza o fim da lista para o elemento anterior
         
        self._length -=1
        
    def append(self, elem):
      n = Node(elem)
      self.__insert_at_end(n)
      self._length +=1
      
    def replace(self, index, elem):
      if not self.empty():
        n = Node(elem)
        pos = 0
        aux = self._head
        if index == 0: # se for o primeiro elemento
          self._head = n
          self._head._next = aux._next
        else:
          while pos < index:
            prev = aux
            aux = aux._next
            pos +=1
          prev._next = n
          n._next = aux._next
          if index == self._length -1: # se for o ultimo elemento
            self._tail = n
      
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(0, 4)
    ll.insert(1, 2)
    ll.insert(2, 0)
    ll.insert(3, 2)
    ll.insert(4, 4)
    ll.insert(5, 3)
    ll.insert(6, 4)
    print(ll)
    ll.remove_all(4)
    print(ll)
    ll.remove_at(3)
    print(ll)
    ll.append(6)
    print(ll)
    ll.replace(3,2)
    print(ll)
    print('Lenght: ', ll.length())
    print('Head: ', ll._head)
    print('Tail: ', ll._tail)

  
   