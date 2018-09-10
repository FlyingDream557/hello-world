# 以下为通过Python实现双向链表

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkList(object):
    def __init__(self):
        self.head = Node('head')

    def add(self, value):
        p = self.head
        new = Node(value)
        while p.next:
            p = p.next
        p.next = new
        new.prev = p

    def remove(self, value):
        p = self.head
        while p.next:
            if p.value == value:
                temp = p.prev
                xyz = p.next
                temp.next = xyz
                xyz.prev = temp
                break
            else:
                p = p.next

    def find(self, value):
        # 根据制定的值找出位置
        p = self.head
        i = 0
        while p.next:
            if p.value == value:
                return i
            else:
                p = p.next
                i += 1
        raise AttributeError(u'can\'t find this element')

    def index(self, index):
        # 根据指定的位置找出相应的值
        i = 0
        p = self.head
        while p.next:
            if i == index:
                return p.value
            else:
                i += 1
                p = p.next
        raise IndexError(u'index out of range')

    def findprev(self, value):
        """根据指定节点的值找出前面的一个节点的值"""
        p = self.head
        while True:
            if p.value == value:
                return p.prev.value
                break
            else:
                p = p.next
                if not p.next:
                    return p.prev.value
                    break
        raise AttributeError(u"can\'t find this element")

    def findnext(self, value):
        """根据指定节点的值找出后面的一个节点的值"""
        p = self.head
        while 1:
            if p.value == value:
                return p.next.value
            else:
                p = p.next
                if not p.next:
                    return None
        raise AttributeError(u"can\'t' find this element")

    def insert(self, index, value):
        """index必须大于等于1
        """
        i = 0
        p = self.head
        new = Node(value)
        while p.next:
            if i == index:              
                temp = p.prev
                temp.next = new
                new.prev = temp
                new.next = p
                p.prev = new                                
                break
            else:
                p = p.next
                i += 1
        #上面循环自然结束,就直接插入到元素的末尾
        else:
            p.next = new
            new.prev = p

    def length(self):
        p = self.head
        i = 0
        while p.next:       
            p = p.next
            i += 1

        return i

    def output(self):
        p = self.head
        while 1:
            print(p.value)
            p = p.next
            if not p.next:
                print(p.value)
                break

    def reverse(self):
        """反转链表"""
        length = self.length()
        i = 0
        p = self.head.next
        while p.next:
            p = p.next
        else:
            last = p
        first = self.head.next
        while i < length:
            first.value, last.value = last.value, first.value
            first = first.next
            last = last.prev
            i += 1
            length -= 1

LL = LinkList()
LL.add(10)
LL.add(11)
LL.add(12)
LL.add(14)

print('长度为:', LL.length())
LL.output()
print('------------------------------')
LL.reverse()
LL.output()
print('------------------------------')
LL.insert(1, 100)
LL.output()
print('------------------------------')
print(LL.findnext(100))
print('------------------------------')
print(LL.findprev(14))
print('------------------------------')
print(LL.index(0))
print(LL.index(1))
print('------------------------------')
print(LL.find(12))
print('===========================')
LL.remove(12)
LL.output()
