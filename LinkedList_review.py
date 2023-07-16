class Student:
    __slots__ = '_ID','_GPA','_YearOfBirth','_PlaceOfBirth'

    def __init__(self, ID, GPA, YearOfBirth, PlaceOfBirth):
        self._ID = ID
        self._GPA = GPA
        self._YearOfBirth = YearOfBirth
        self._PlaceOfBirth = PlaceOfBirth

    def printinfo(self):
        print("Student", self._ID, self._GPA, self._YearOfBirth, self._PlaceOfBirth)

class LinkedList:
    class Node:
        __slots__ = '_info','_next'

        def __init__(self, info, next):
            self._info = info
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    """Check if a student with the given ID already exists in the list."""
    def check(self, student):
        tmp = self._head
        while tmp is not None:
            if tmp._info._ID == student._ID:
                return False
            tmp = tmp._next
        if (student._GPA <= 0 or student._GPA > 10) or (student._YearOfBirth < 2000 or student._YearOfBirth > 2005):
            return False
        return True

    """Add a student to the end of the list."""
    def add(self,student):
        new_node = self.Node(student,None)
        if self.is_empty():
            self._head = new_node
        else:
            tmp = self._head
            while tmp._next is not None:
                tmp = tmp._next
            tmp._next = new_node
        self._size += 1

    """Print the information of all students in the list."""
    def printall(self):
        tmp = self._head
        while tmp is not None:
            tmp._info.printinfo()
            tmp = tmp._next

    """Add a student at the 4th position in the list."""
    def addfourth(self, student):
        new_node = self.Node(student,None)
        if self._size < 3:
            self.add(student)
        else:
            tmp = self._head
            count = 1
            while count < 3 and tmp._next is not None:
                tmp = tmp._next
                count += 1
            new_node._next = tmp._next
            tmp._next = new_node
            self._size += 1

    """Update the GPA of students born in 2001 to 8.0, then print all students."""
    def update(self):
        tmp = self._head
        while tmp is not None:
            if (tmp._info._YearOfBirth == 2001):
                tmp._info._GPA = 8
            tmp = tmp._next
        self.printall()

    """Print the information of students born in 'TPHCM'."""
    def printcond(self):
        tmp = self._head
        find = False
        while tmp is not None:
            if (tmp._info._PlaceOfBirth == 'TPHCM'):
                tmp._info.printinfo()
                find = True
            tmp = tmp._next
        if not find:
            print('Khong co ai sinh ra o TPHCM')

    """Delete the last two students from the list and print all remaining students."""
    def deletetwo(self):
        if self.is_empty():
            return
        elif self._size < 3:
            return
        else:
            tmp = self._head
            while tmp._next._next._next is not None:
                tmp = tmp._next
            tmp._next = None
        self._size -= 2
        self.printall()

def test():
    lk_l = LinkedList()

    student1 = Student(1001, 9.5, 2001, "TPHCM")
    student2 = Student(1002, 8.7, 2002, "Hanoi")
    student3 = Student(1003, 7.9, 2000, "TPHCM")
    student4 = Student(1004, 8.2, 2003, "TPHCM")
    student5 = Student(1005, 9.1, 2001, "Hanoi")

    lk_l.add(student1)
    lk_l.add(student2)
    lk_l.add(student3)
    lk_l.add(student4)
    lk_l.add(student5)
    print("Student list:")
    lk_l.printall()
    print("Student list after add:")
    student6 = Student(1006, 10, 2003, 'DaNang')
    lk_l.add(student6)
    lk_l.printall()
    print("Student list after add fourth place:")
    student7 = Student(1007, 9.8, 2002, "NhaTrang")
    lk_l.addfourth(student7)
    print("Student list after update:")
    lk_l.update()
    print("Info of students at TPHCM:")
    lk_l.printcond()
    print("Student list after delete two:")
    lk_l.deletetwo()

test()




