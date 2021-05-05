def user_stats(self):
    self.check_row = int(input("Enter the row you booked : \n"))
    self.check_col = int(input("Enter the seat you booked : \n"))
    if self.list1[self.check_row-1][self.check_col-1] == 'B':
        info = self.user_details[(self.check_row,self.check_col)]
        print('Name : ',info[0])
        print('Age : ',info[1])
        print('Gender : ',info[2])
        print('Contact : ',info[3])
    else:
        print("This seat is not booked yet...\n")