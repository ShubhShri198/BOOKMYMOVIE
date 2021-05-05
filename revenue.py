def max_revenue(self):
    if self.total_seats < 60:
        self.total_income = self.total_seats * 10
    elif self.total_seats >= 60:
        p = int(self.row / 2)*int(self.col)*10
        r = (int(self.row)-int(self.row / 2))*int(self.col)*8
        self.total_income = p+r
        return self.total_income


def showStats(self):
    print("Number of Purchased Tickets = ",self.seat_count)
    self.seat_percent = (self.seat_count / self.total_seats)*100
    print("Booking Percentage = ", self.seat_percent)
    print("Income = $", self.current_income)
    rev = self.max_revenue()
    print("Possible Income = $",self.total_income)
    