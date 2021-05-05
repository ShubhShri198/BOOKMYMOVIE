class bookmymovie:
    from seatavailable import show_seats
    from bookseat import buy_seat
    from revenue import showStats
    from revenue import max_revenue
    from userinfo import user_stats
    
    greet = print("\n***BOOKMYMOVIE.COM***\n***We are glad to have you here !***\n")

    def menu(self):
        output = True
        while output:
            print("\nMenu :\n")
            print("1. Show the seats\n2. Book a Ticket\n3. Statistics\n4. Check Your Booking Stats\n0. Exit\n")

            self.inp = input("Please enter your choice from the menu : \n")
            if self.inp.isalpha() == True:
                print("Invalid Choice !! Please enter a number from Menu.\n")
            else:
                self.inp = int(self.inp)
                if self.inp == 1 :
                    self.show_seats()
                elif self.inp == 2 :
                    self.buy_seat()
                elif self.inp == 3 :
                    self.showStats()
                elif self.inp == 4 :
                    self.user_stats()
                elif self.inp == 0 :
                    output = False
                    self.ex()
                else:
                    print("INVALID RESPONSE!!, Try Again !!\n")
    

    def __init__(self):
        self.row = int(input("Enter the number of rows : \n"))
        self.col = int(input("Enter the number of seats in each row : \n"))
        self.total_seats = self.row * self.col
        self.list1 = []
        self.seat_count = 0
        self.current_income = 0
        self.total_income = 0
        self.user_details = {}

        for i in range(self.row):
            list2 = []
            for j in range(self.col):
                list2.append("S")
            self.list1.append(list2)
        print(end=" ")
    
    def ex(self):
        print("\nThankyou for using BookMyMovie..!\nDo visit again..!")

movie_obj = bookmymovie()
movie_obj.menu()