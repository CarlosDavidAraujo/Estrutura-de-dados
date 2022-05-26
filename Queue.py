from abc import ABC, abstractmethod


class EmptyQueue(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class QueueADT(ABC):

    @abstractmethod
    def enqueue(self, elem):
        """Adiciona <elemento> ao fim da fila"""
        pass

    @abstractmethod
    def dequeue(self):
        """Remove elemento do inicio da fila"""
        pass

    @abstractmethod
    def first(self):
        """Verifica qual é o elemento que se encontra no início da fila, sem removê-lo"""
        pass

    @abstractmethod
    def is_empty(self):
        """Verifica se a fila está vazia"""
        pass


class Queue(QueueADT):
    """Implementação de fila que utiliza uma lista Python para armazenar as informações"""

    def __init__(self):
        """Fila vazia"""
        self._data = []

    def __len__(self):
        """Return the number of elements in the queue."""
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def is_empty(self):
        """Return True if the queue is empty."""
        return len(self._data) == 0

    def enqueue(self, e):
        """Add element to the end of the queue."""
        self._data.append(e)

    def first(self):
        """Return (but do not remove) the element at the beginning of the queue.
        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise EmptyQueue('Queue is empty')
        return self._data[0]  # the first item in the list

    def dequeue(self):
        """Remove and return the element from the beginning of the queue (i.e., FIFO).
       Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise EmptyQueue('Queue is empty')
        return self._data.pop(0)


if __name__ == '__main__':
    Q = Queue()
    Q.enqueue('Manoel')
    Q.enqueue('David')
    Q.enqueue('Paulo')
    Q.enqueue('Jean')
    print(Q)
    try:
        Q.dequeue()
        print(Q)
        print(Q.first())
        print(len(Q))
        Q.dequeue()
        print(Q)
        Q.dequeue()
        print(Q)
        Q.dequeue()
        print(Q)
        Q.dequeue()
        print(Q)
    except EmptyQueue:
        print("Fila vazia: não pode retirar elemento!")
    else:
        print("Execução sem erros")
    finally:
        print("Fim!")

