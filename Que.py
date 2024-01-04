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