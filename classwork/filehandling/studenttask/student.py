while True:
    print("1: Enter student data")
    print("0: Exit")

    n = int(input("Enter choice (1/0): "))

    if n == 0:
        break

    if n == 1:
        name = input("Enter student name: ")
        marks = int(input("Enter student marks: "))
        city = input("Enter student city: ")

        # dictionary
        student = {
            "name": name,
            "marks": marks,
            "city": city
        }
    #    open student75.txt file if marks is greater than 75
        if marks > 75:
            with open("student75.txt", "a") as f:
                f.write(str(student) + "\n")
         # open the student.txt file to save the <75 marks student data  
        else:
            with open("student.txt", "a") as f:
                f.write(str(student) + "\n")

        print("Data saved successfully!\n")
