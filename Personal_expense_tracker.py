import datetime
print("===== EXPENSE TRACKER =====")

print( "1. Add expense \n2. View all expenses \n3. Show total spending \n 4. Show highest expense \n5. Search expenses by category \n6. Exit")


lis=[]

while True:
    choice=int(input("Enter your choice: "))
    highest=0
    spending=0

    if choice==1:
        try:
            amount=int(input("Enter amount:"))
            break
        except:
            print(ValueError())

        category=input("Enter Category:")
        amount=input("Enter amount")
        description=input("Enter description:")
        date=datetime.date.today()

        print("Expense added!")

        expenses={"Amount":amount, "Category":category, "Description":description, "date":date}
        lis.append(expenses)

    elif choice==2:
        for items in lis:
            print(items)

    elif choice==3:
          for items in lis:
                spending=spending+items["Amount"]
          print(spending)

    elif choice==4:
        for items in lis:
            if items["Amount"]>highest:
                highest = items["Amount"]
                highest_expense = items
        print(highest_expense)

    elif choice==5:
        cat=input("Enter category you want to see expense of:")
        for items in lis:
            if items["Category"]==cat:
                print(items)

    elif choice==6:
        break
        
    else:
        print("invalid choice")
    


