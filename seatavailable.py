def show_seats(self):
    print("\n Cinema :\n")
    a = 0
    b = 0
    print(end=" ")
    for j in range(1, self.col + 1):
        b = b + 1
        print(b, end = " ")
    print()
    for i in self.list1:
        a = a + 1
        print(a, end = " ")
        print(" ".join(i),sep=",")