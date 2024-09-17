def main():
    user_input = input("Whats time is it ?")
    x = convert(user_input)
    if x >=7 and x<=8:
        print("breakfast time")
    elif x>=12 and x<=13:
        print("lunch time")
    elif x>=18 and x<=19:
        print("dinner time")




def convert(time):

    hours,minutes = time.split(":")

    hours = int(hours)
    minutes = float(minutes)/60
    return hours + minutes


if __name__ == "__main__":
    main()
