#!/usr/bin/python3

def get_zodiac_sign(month, day):
    if (month == 'March' and day >= 21) or (month == 'April' and day <= 19):
        return "You are an Aries!"
    elif (month == 'April' and day >= 20) or (month == 'May' and day <= 20):
        return "You are a Taurus!"
    elif (month == 'May' and day >= 21) or (month == 'June' and day <= 20):
        return "You are a Gemini!"
    elif (month == 'June' and day >= 21) or (month == 'July' and day <= 22):
        return "You are a Cancer!"
    elif (month == 'July' and day >= 23) or (month == 'August' and day <= 22):
        return "You are a Leo!"
    elif (month == 'August' and day >= 23) or (month == 'September' and day <= 22):
        return "You are a Virgo!"
    elif (month == 'September' and day >= 23) or (month == 'October' and day <= 22):
        return "You are a Libra!"
    elif (month == 'October' and day >= 23) or (month == 'November' and day <= 21):
        return "You are a Scorpio!"
    elif (month == 'November' and day >= 22) or (month == 'December' and day <= 21):
        return "You are a Sagittarius!"
    elif (month == 'December' and day >= 22) or (month == 'January' and day <= 19):
        return "You are a Capricorn!"
    elif (month == 'January' and day >= 20) or (month == 'February' and day <= 18):
        return "You are an Aquarius!"
    elif (month == 'February' and day >= 19) or (month == 'March' and day <= 20):
        return "You are a Pisces!"
    else:
        return "Wrong Entry! Please try again!"


def main():    
    while True:
        month = input("Enter the month of your birthday  or 'exit' to quit: ")
        if month.lower() == 'exit':            
            print("Goodbye!") 
            break
        try:            
            day = int(input("Enter the day of your birthday: ")) 
        except:
            print("Invalid day! Please enter a valid number.")
            continue

        result = get_zodiac_sign(month, day)
        print(result)

main()
