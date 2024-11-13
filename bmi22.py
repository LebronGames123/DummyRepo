print("This is my dummy code for the lab test")


def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/height**2
    format_bmi="{:.2f}".format(bmi)

    print("Your BMI is = "+ str(format_bmi))

    if bmi<18.5:
        classification = "Under Weight"
        if bmi>=18.5 and bmi<=25.0:
            classification = "Normal Weight"
    else:
        classification = "Over Weight"
    
    print("Your BMI classification is= "+ classification)

calculate_bmi(height=1.73,weight=53)