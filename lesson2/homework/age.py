def main():
    try:
        while 1:
            age = int(input("What is your age? "))
            if isinstance(age, int) and age > 0:
                print("проверка")

                if age <= 7:
                        print("Pls go to detsad!")
                        break
                elif age < 18:
                    print("Pls go to school!")
                    break
                elif age <= 23:
                    print("Pls go to vuz!")
                    break
                else:
                    print("Pls go to rabota!")
                    break
            else:
                print ("Василий! Введи цифру больше нуля! Давай попытаемся еще разок!")
    except:
        print("Василий! Введи целую цифру больше нуля!")
     

if __name__ == '__main__':
    main()
