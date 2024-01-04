'''
Queue Data Structure
-------------------------------------------------------------
'''

class Queue:
    def __init__(self) -> None:
        self.items = []

    def __repr__(self) -> str:
        return f'Queue object: data={self.items}'
    
    def is_empty(self):
        return not self.items
    
    def enqueue(self, item):
        self.items.append(item)

    def size(self):
       return len(self.items)

    def dequeue(self):
        return self.items.pop(0)
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
    
if __name__ == '__main__':
    q = Queue()
    print(q.is_empty())
    q.enqueue('First')
    q.enqueue('Second')
    print(q)
    print(q.dequeue())
    print(q)
    print(q.size())
    print(q.peek())
    


    