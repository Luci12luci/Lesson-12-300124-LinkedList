class LinkedList:
    def __init__(self):
        self.head = None

    def vloz(self, prvok):
        if self.head is None:
            self.head = prvok
        else:
            aktualny = self.head
            while aktualny.next:
                aktualny = aktualny.next
            aktualny.next = prvok

    def vypis(self):
        aktualny = self.head
        print(aktualny.data)
        while aktualny.next:
            aktualny = aktualny.next
            print(aktualny.data)

    def obsahuje(self, meno):
        aktualny = self.head
        while aktualny.next:
            aktualny = aktualny.next
            if aktualny.data == meno:
                return True
        return False

    def obsahuje(self, meno):
        if aktualny == None:
           return False

class Prvok:
    def __init__(self, data):
        self.data = data
        self.next = None

mojLinked = LinkedList()
# prvok1 = Prvok("Milan")
# mojLinked.vloz(prvok1)
# prvok2 = Prvok("Jozo")
# mojLinked.vloz(prvok2)
# prvok3 = Prvok("Fero")
# mojLinked.vloz(prvok3)
# prvok4 = Prvok("Peter")
# mojLinked.vypis()
# mojLinked.vloz("Peter")
# print(mojLinked obsahuje "Peter")
# print("test")













