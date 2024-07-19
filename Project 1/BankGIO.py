print("Bank GIO")
print("*********************")
#Login and register

if input("Enter whether you need to register or not:") == "No":
    print("Please log in")
    print("*********************")
    Mail = input("Please enter your Mail:")
    Password = input("Please enter your Password:")
else:
    print("Please register:")
    print("*********************")
    Credit_Card = input("Enter your card information:")
    name = input("Enter your name:")
    last_name = input("Enter your lastname:")
    Mail = input("Enter your Mail:")
    Password = input("Set a password:")
#print("*********************") დახმარებით იბეჭდება გამყოფი ხაზი და ტერმინალი ლამაზდება.

#def ნიშნავს განსაზღვრას. განსაზღვრავს ცვლადს, ან ფუნქციას.
#return არის სპეციალური განცხადება, რომელიც შეგიძლიათ გამოიყენოთ ფუნქციის ან მეთოდის შიგნით ფუნქციის შედეგის გასაგზავნად აბონენტისთვის
#F-სტრიქონები სტრიქონების ინტერპოლაციის(განახლება,შეცვლა) პროცესს ინტუიციურ, სწრაფ და ლაკონურს ხდის.
def show_balance(balance):
    print("*********************")
    print(f"Your balance is {balance:.2f}₾")
    print("*********************")


def deposit():
    print("*********************")
    amount = float(input("Enter an amount to be deposited: "))
    print("*********************")
    if amount < 0:
        print("*********************")
        print("That's not a valid amount")
        print("*********************")
        return 0
    else:
        return amount
 #აჩვენებს შეტყობინებას და სთხოვს მომხმარებელს შეიყვანოს შესატანი თანხა.
#ამოწმებს არის თუ არა შეყვანილი თანხა უარყოფითი თუ ასეა ის ბეჭდავს შეცდომის შეტყობინებას და აბრუნებს 0-ს.
#წინააღმდეგ შემთხვევაში ის აბრუნებს შეყვანილ თანხას.

def withdraw(balance):
    print("*********************")
    amount = float(input("Enter amount to be withdrawn: "))
    print("*********************")

    if amount > balance:
        print("*********************")
        print("Insufficient funds")
        print("*********************")
        return 0
    elif amount < 0:
        print("*********************")
        print("Amount must be greater than 0")
        print("*********************")
        return 0
    else:
        return amount
#აჩვენებს შეტყობინებას და სთხოვს მომხმარებელს შეიყვანოს თანხა გამოსატანად.
#ამოწმებს არის თუ არა შეყვანილი თანხა მიმდინარე ბალანსზე მეტი თუ ასეა ის ბეჭდავს შეცდომის შეტყობინებას და აბრუნებს 0-ს.
#ამოწმებს არის თუ არა შეყვანილი თანხა უარყოფითი თუ ასეა ის ბეჭდავს შეცდომის შეტყობინებას და აბრუნებს 0-ს.
#წინააღმდეგ შემთხვევაში ის აბრუნებს შეყვანილ თანხას.

def main():
    balance = 0
    is_running = True
#balance=0 ახდენს ბალანსის ინიციალიზებას 0-მდე.

    while is_running:
        print("*********************")
        print("   Banking Program   ")
        print("*********************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("*********************")
        choice = input("Enter your choice (1-4): ")
#ვიყინებთ while ციკლს მენიუს განმეორებით საჩვენებლად.
#input-ის დახმარებით მომხმარებელი ირჩევს სასურველ ვარიანტს.

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("*********************")
            print("That is not a valid choice")
            print("*********************")
#if elif და else ის დახმარებით თუ არჩევანი არის 1 აჩვენებს ბალანსს.
#2-ის არჩევის შემთხვევაში შეაქვს თანახა.
#3-ის არჩევის შემთვევაში გააქვს თანხა.
#4-ის არჩევის შემთხვევაში While ციკლი ითიშება მომხმარებელი გადის ბანკიდან.

    print("*********************")
    print("Thank you! Have a nice day!")
    print("*********************")


if __name__ == '__main__':
    main()
#ხაზი if __name__ == '__main__': არის პითონის სპეციალური კონსტრუქცია,
#რომელიც ამოწმებს მიმდინარე სკრიპტს უშუალოდ Python-ის ინტერპრეტატორის მიერ აწარმოებს,ან ხდება თუ არა მისი იმპორტი მოდულის სახით სხვა სკრიპტში.
