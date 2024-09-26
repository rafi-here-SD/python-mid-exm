class Star_Cinema:
    _hall_list = [] 
    
    def entry_hall(self, hall):
        self._hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, col, hall_no):
        self.rows = rows
        self.col = col
        self.hall_no = hall_no
        self.entry_hall(self)
        self.__show_list = []  
        self.__seats = {}

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        seat_matrix = [[0 for _ in range(self.col)] for _ in range(self.rows)]
        self.__seats[id] = seat_matrix

    def view_available_seats(self, id):
        show_exists = False
        for show in self.__show_list:
            if show[0] == id:
                show_exists = True
                print(f"<-- Available Seats for Show -> {id} -->")
                for row in self.__seats[id]:
                    for seat in row:
                        print("0" if seat == 0 else "1", end=" ")
                    print() 
                break
        if not show_exists:
            print("Show ID not found.")

    def book_seats(self, id, seats_list):
        show_exists = False
        for show in self.__show_list:
            if show[0] == id:
                show_exists = True
                for row, col in seats_list:
                    if row < 1 or row > self.rows or col < 1 or col > self.col:
                        print(f"Invalid seat [{row}, {col}]. Seat is out of range.")
                    elif self.__seats[id][row-1][col-1] == 0:  
                        self.__seats[id][row-1][col-1] = 1  
                        print(f"Seat [{row}, {col}] booked successfully.")
                    else:
                        print(f"Seat [{row}, {col}] is not available.")
                break
        if not show_exists:
            print("Show ID not found.")

    def view_show_list(self):
        print(f'<-- show list for hall-{self.hall_no} -->')
        cnt = 1 
        for show in self.__show_list:
            print(f"\n\t---show-{cnt}---\n Show ID: {show[0]}, Movie Name: {show[1]}, Time: {show[2]}")
            cnt += 1
row, col = map(int, input("Enter Row and Col: ").split())
hall_no = int(input("Enter hall no: "))
hall = Hall(row, col, hall_no)

while True:
    print(
        """
                          CINEMA BOOKING SYSTEM           
                                                           
                    1.Add Show Information              
                    2.View All Shows Today              
                    3.View Available Seats for a Show   
                    4.Book Seat for a Show             
                    5.Exit                              
                                                           
        """
    )
    ch = input(" Enter a number: ")

    if ch == "1":
        h_id = input("Enter the hall id: ")
        movie = input("Enter the movie name: ")
        time = input("Enter the time of movie: ")
        hall.entry_show(h_id, movie, time)
        print("\nAdd Show Information done.\n")

    elif ch == "2":
        print("|          VIEW SHOW DATA           |")
        for show in Star_Cinema._hall_list:
            show.view_show_list()
            
    elif ch == "3":
        print("|        VIEW AVAILABLE SEATS           |")
        show_id = input("Enter the show id: ")
        hall.view_available_seats(show_id)

    elif ch == "4":
        print("BOOK SEAT FOR A SHOW")
        show_id = input("Enter the ID of the show: ")
        num_seat = int(input("Enter the number of seats to book: "))
        seatBook = []
        for _ in range(num_seat):
            r, c = map(int, input("Enter row and col (space-separated): ").split())
            seatBook.append((r, c))
        hall.book_seats(show_id, seatBook)

    elif ch == "5":
        print("Exiting...")
        break

    else:
        print("YOU CHOICE WRONG!!!")
