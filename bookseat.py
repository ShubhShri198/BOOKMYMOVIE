def buy_seat(self):
    a = int(input("Enter the row number to book your seat : \n"))
    b = int(input("Enter the seat number to book in that row : \n"))
    if self.list1[a-1][b-1] == "B":
        print("Sorry ! This seat is already Taken. Please Choose another one..")
        self.menu()
    elif self.total_seats < 60:
        self.price = 10
        print("Ticket price per person is $10 here, Shall we proceed ? Yes/No")
    elif a < self.row / 2:
        self.price = 10
        print("Ticket price per person is $10 here, Shall we proceed ? Yes/No")
    elif a > self.row / 2:
        self.price = 8
        print("Ticket price person is $8 here, Shall we proceed ? Yes/No\n")
    self.reply = input()

    if self.reply == "Yes" or self.reply == "yes":
        dict1 = {}
        Name = input("Please enter your name :\n")
        Age = int(input("Please enter your age : \n"))
        Gender = input("Enter your Gender (M/F/other) : \n")
        Contact = input("Enter your contact number : \n")
        if len(Contact) == 10:
            self.row1 = a - 1
            self.col1 = b - 1
            self.list1[self.row1][self.col1] = "B"
            self.seat_count = self.seat_count + 1
            self.current_income = self.current_income + self.price
            
            dict1[(self.row1+1),(self.col1+1)] = list((Name,Age,Gender,Contact,self.price))
            self.user_details.update(dict1)
            print("Your Booking is Done Succesfully !! Enjoy Your Movie !\n")
        else:
            print("Invalid input ! Your Booking can't be processed.")
            self.menu()
    else:
        print("Oops !! We think you are not interested to watch a movie right now..\nPlease come back later!\n")
