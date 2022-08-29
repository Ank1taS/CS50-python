# # implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

def main():
    monthList = [   "January",
                    "February",
                    "March",
                    "April",
                    "May",
                    "June",
                    "July",
                    "August",
                    "September",
                    "October",
                    "November",
                    "December" ]


    
    while True:
        inputDate = input("Date: ")
        try:
            try:
                month, date, year = inputDate.split("/")

            except ValueError:
                month, date, year = inputDate.split(" ")

            # month
            if month.isalpha():
                mon = monthList.index(month) + 1
                if "," not in date:
                    continue
                date = date.replace(",", "")
            else:
                mon = int(month)

            if mon < 1 or mon > 12:
                continue

            # date
            dt = int(date)

            if dt < 1 or dt > 31:
                continue

            # year
            if " " in year:
                year = year.strip()

        except ValueError: # for both list item check ie index() and int conversion
            pass

        else:
            print(f"{year:4}-{mon:02}-{dt:02}")
            break





if __name__ == "__main__":
    main()




# def main():
#     monthList = [   "January",
#                     "February",
#                     "March",
#                     "April",
#                     "May",
#                     "June",
#                     "July",
#                     "August",
#                     "September",
#                     "October",
#                     "November",
#                     "December" ]

    
#     while True:
#         inputDate = input("Date: ")
#         try:
#             try:
#                 month, date, year = inputDate.split("/")
#             except ValueError:
#                 month, date, year = inputDate.split(" ")
#                 # if "," in date:
#                 date = date.replace(",", "")
                           
#             dt = int(date)
            
#             if dt < 1 or dt > 31:
#                 continue

#             if month.isalpha():
#                 mon = monthList.index(month) + 1
#             else:
#                 mon = int(month)

#             if mon < 1 or mon > 12:
#                 continue

#             # try:
#             #     mon = int(month)
#             #     if mon < 1 or mon > 12:
#             #         continue
#             # except ValueError:
#             #     mon = monthList.index(month) + 1
            
#             # remove unnecesary space after inputed date(if any)
#             if " " in year:
#                 year = year.strip()

#         except ValueError: # for both list item check ie index() and int conversion
#             pass
    
#         else:
#             print(f"{year}-{mon:02}-{dt:02}")
#             break

        


# if __name__ == "__main__":
#     main()

