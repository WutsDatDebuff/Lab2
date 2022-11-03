def cal_bmi(h,w):
    print("Height = "+ str(h))
    print("Weight = "+ str(w))

    bmi = float(w)/ (float(h)* float(h))

    if bmi <18.5:
        print("Under Weight")
    elif bmi >= 18.5 or bmi <= 25.0:
        print("Normal Weight")
    else:
        print("Over Weight")

    print("Bmi is " + str(bmi))

cal_bmi(w=57, h=1.73)
