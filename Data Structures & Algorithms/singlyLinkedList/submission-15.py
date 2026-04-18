class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def get(self, index: int) -> int:
        if index >= self.count or index < 0 or not self.head:
            return -1

        current_node = self.head
        
        for i in range(index):
            current_node = current_node.next
            
        return current_node.val

    def insertHead(self, val: int) -> None:
        new_head = Node(val)

        if self.head:
            self.head.prev = new_head
            new_head.next = self.head
            self.head = new_head
        else:
            self.head = new_head
            self.tail = new_head    

        self.count += 1

    def insertTail(self, val: int) -> None:
        new_tail = Node(val)

        if self.tail:
            self.tail.next = new_tail
            new_tail.prev = self.tail
            self.tail = new_tail
        else:
            self.head = new_tail
            self.tail = new_tail

        self.count +=1

    def remove(self, index: int) -> bool:
        if index >= self.count or index < 0:
            return False

        if self.head:
            current_node = self.head
        else:
            return None

        for i in range(index):
            current_node = current_node.next

        if current_node.next and current_node.prev:
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
        elif not current_node.next and current_node.prev:
            current_node.prev.next = None
            self.tail = current_node.prev
        elif not current_node.prev and current_node.next:
            current_node.next.prev = None
            self.head = current_node.next
        else:
            self.head = None
            self.tail = None
            
        self.count -= 1
        return True

    def getValues(self) -> List[int]:
        current_list = []

        if self.head:
            current_node = self.head
        else:
            return current_list

        while current_node:
            current_list.append(current_node.val)
            current_node = current_node.next

        return current_list
        
class Node:
    
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None