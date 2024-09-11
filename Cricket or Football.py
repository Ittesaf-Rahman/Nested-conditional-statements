print("WHat are you choosed a game press 1 or 2")
print("1. Cricket")
print("2. Football")
choose = int(input("press 1 or 2 = "))
if choose == 1:
    print("What is your favourite cricket team = ")
    print("1. England")
    print("2. Australia")
    choose2 = int(input("press 1 or 2 ="))
    if choose2 == 1:
        print("What is your favourite cricket player = ")
        print("1. Joe Root")
        print("2. Hary Broke")
        choose8 = int(input("press 1 or 2 ="))
        if choose8 == 1:
            print("Joseph Edward Root, MBE is an English international cricketer,\n who plays for the English cricket team and formerly captained the Test team.\n He also represents Yorkshire in English domestic cricket.")
        else:
            print("Harry Cherrington Brook is an English cricketer who plays international cricket for England and domestic cricket for Yorkshire.\n Primarily a right-handed batsman, he also bowls right-arm medium pace.\n He made his international debut for England in January 2022.")
    else:
        print("What is your favourite cricket player = ")
        print("1. David Warnner")
        print("2. Stiven Smith")
        choose7 = int(input("press 1 or 2 ="))
        if choose7 == 1:
            print("David Andrew Warner is a former Australian international cricketer and a former Test vice-captain.\n A left-handed opening batsman, Warner was the first Australian cricketer in 132 years to be \nselected for the national team in any format without experience in first-class cricket.")
        else:
            print("Steven Peter Devereux Smith is an Australian international cricketer and former captain of the Australian national team\n in all three formats of the game. He is widely regarded as one of the greatest Test batsmen since Don Bradman.")
elif choose == 2:
    print("What is your favourite football team = ")
    print("1. Argentina")
    print("2. Brazil")
    choose3 = int(input("press 1 or 2 ="))
    if choose3 == 1:
        print("What is your favourite football player = ")
        print("1. Lionel Messi")
        print("2. Paoulo Dibala")
        choose4 = int(input("press 1 or 2 ="))
        if choose4 == 1:
            print("Lionel Andrés Messi is an Argentine professional footballer who plays as a forward for and captains both \nMajor League Soccer club Inter Miami and the Argentina national team.")
        else:
            print("Paulo Exequiel Dybala is an Argentine professional footballer who plays as an attacking midfielder \nor winger for Serie A club Roma and the Argentina national team. Nicknamed, he is noted for his dribbling, creativity, and goal-scoring ability.")
    else:
        print("What is your favourite football player = ")
        print("1. Neymer")
        print("2. Pele")
        choose5 = int(input("press 1 or 2 ="))
else:
    print("Please choose cricket or football")