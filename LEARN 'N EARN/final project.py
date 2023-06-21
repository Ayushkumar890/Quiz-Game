class color:
      black = '\033[30m'
      red = '\033[31m'
      green = '\033[32m'
      orange = '\033[33m'
      blue = '\033[34m'
      purple = '\033[35m'
      cyan = '\033[36m'
      lightgrey = '\033[37m'
      darkgrey = '\033[90m'
      lightred = '\033[91m'
      lightgreen = '\033[92m'
      yellow = '\033[93m'
      lightblue = '\033[94m'
      pink = '\033[95m'
      lightcyan = '\033[96m'
      end = '\033[0m'
import time
import random as rd

print(color.red+"WELCOME SWEETIES"+color.end)
#time.sleep(2)
print(color.red+"Let's LEARN while having FUN"+color.end,"\U0001F60A")
playing = input(color.pink+"do you want to play? (then type 'play') : -"+color.end)
e = playing.upper()
if e != "PLAY":
    quit()
#time.sleep(2)
x = "RULES"
print(x.center(40))
print("------------------------------------------")
#time.sleep(2)
print(color.blue+"1) There are three Levels in this game having 5 questions each."+color.end)
#time.sleep(2)
print(color.blue+"2) For every correct answer you will be awarded with a smiley."+color.end, "\U0001F60A")
#time.sleep(2)
print(color.blue+"3) For every incorrect answer you will be awarded nothing but applause."+color.end, "\U0001F60A")
print()
#time.sleep(2)
k1="Here It Goes"
print(k1.center(40))
k2="All The Best"
print(k2.center(40))

print()
print(color.purple+"------------------------------------------"+color.end)
#time.sleep(2)

count = 0
cor = 0
icor = 0
n = (input("choose your subject (Maths,Science,GK) : "))
if n.upper() == "MATHS" :
#question 1
    f=rd.randint(10,99)
    g=rd.randint(10,99)
    ans=f+g
    print(color.red+'''    *********************************
    *                               *
    *         !! LEVEL 1 !!         *
    *                               *
    *********************************'''+color.end)
    print("Q1)",f,"+",g,"= ?")
    a = int(input("ans : "))
    if a == ans:
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer= ",ans)
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)

#question 2
    f=rd.randint(10,50)
    g=rd.randint(50,100)
    print("Q2) Which is greater",f,"or",g,"?")
    b = int(input("ans : "))
    if b == g:
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer=",g)
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)

#question 3
    print("Q3) Which number means we have nothing?")
    print()
    c = int(input("ans : "))
    if c == 0:
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer= 0")
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)

#question 4
    lisp=["Apple","Orange","Globe","Earth","Planets","Sun","Moon"]
    lisq=["Brick","Book","Box","Matchbox","Fish Tank","Radio","Deck of Cards","Lunch Box"]
    licy=["Gas Cylinder","Pipe","Beaker","Candle","Test Tube","Soda Can","Marker Pen"]
    j=rd.choice(lisp)
    k=rd.choice(lisq)
    l=rd.choice(licy)
    print("Q4) Which of them has a shape similar to your Device ?")
    print("(",j,",",k,",",l,")")
    c = input("ans : ")
    if c.upper() == k.upper():
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer= ", k)
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)

#question 5
    a=rd.randint(100,999)
    print("Q5) Which number follows ",a)
    d = int(input("ans : ",))
    if d == a+1:
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer= ",a+1)
        icor += 1

    print()
    print(color.purple+"------------------------------------------"+color.end)


#question 6
    time.sleep(1)
    print(color.red+'''    *********************************
    *                               *
    *         !! LEVEL 2 !!         *
    *                               *
    *********************************'''+color.end)
    time.sleep(1)
    a=rd.randint(100,500)
    b=rd.randint(500,1000)
    print("Q6) which number is lesser ",a,"or",b,"? ")
    c = int(input("ans : "))
    if c == a:
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer= ",a)
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)

#question 7
    a7=rd.randrange(10,100)
    print("Q7) If you have ",a7,"rupees, How many Paise do you have ?")
    c = int(input("ans : "))
    if c == (a7*100):
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer= ",a7*100)
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)

#question 8
    a=rd.randint(2000,10000)
    print("Q8) If I walked ",a," metre today, how many kilometre I have walked ?")
    c = (input("ans : "))
    d=a/1000
    if c ==str(d):
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer= ",d)
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)

#question 9
    print("Q9) which number is more 25+30 or 35+5? ")
    c = input("ans : ")
    if c == "25+30":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer= 25+30")
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)

#question 10
    a10=rd.randint(1,11)
    print("Q10) Today I studied for ",a10," hours?, How many minutes did I study")
    c =(input("ans : "))
    d=a10*60
    if c == str(d):
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer = ",d)
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)

#question 11
    print(color.red+'''    *********************************
    *                               *
    *         !! LEVEL 3 !!         *
    *                               *
    *********************************'''+color.end)
    print('''Q11) which number is odd ?
    2,6,10,16,18,82,9,60''')
    c = input("ans : ")
    if c == "9":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer=9")
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)

#question 12
    li=[6,12,18,24,30,36,42,48,54,60]
    a=rd.choice(li)
    b=a+6
    print("Q12) The maximum common number that divide ",a,"and",b, "is " )
    c = input("ans : ")
    if c == "6":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer=6")
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)

#question 13
    print("Q13) how many corner in  there in a slice of PIZZA ?  ","\U0001F355")
    c = input("ans : ")
    if c == "3":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer=3")
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)

#question 14
    a141=rd.randint(5,10)
    a142=rd.randint(1,10)
    print("Q14) If your friend has a bucket with ",a141, "balls and you have ",a142, "friend ,how many balls you have together ?")
    c = int(input("ans : "))
    if c == (a141*a142):
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print(color.green+"Hurray! You got it."+color.end)
        print("Correct Answer= ",(a141*a142))
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)

#question 15
    a151=rd.randint(2,10)
    a152=rd.randint(3,10)
    a5013=rd.randint(2,10)
    print("Q15)? If i have",a151,'''chocolates and mom give''',a152, '''box having ''',a5013,'''chocolates each , how many choclate i have now ?''' )
    c =(input("ans : "))
    d=(a151+a152)*a5013
    if c ==str(d):
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer= ",d)
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)

#print result
    time.sleep(1)
    print("your correct answer is ",cor)
    print("your incorrect answer is ",icor)
    if cor==0:
        print("Sorry! Today was not your day","\U0001F614"*2)
    if cor <=5:
        print("Your Smiley Score:","\U0001F642"*cor)
        print(''''HARD LUCK!! YOU DIDN'T MAKE THIS TIME,
        HERE IS YOUR APPRECIATION COUPON
        ''')
        print(color.blue+'''*********************************
*                               *
*      !! CONGRATULATIONS !!    *
*                               *
*                               *
*         *APPRECIATION*        *
*            *COUPON*           *
*                               *
*                               *
*********************************'''+color.end)
        print("Collect 5 of them to win a MINI CHOCO-COUPON")
    elif cor>5>=10:
        print("Your Smiley Score: ","\U0001F60A"*cor)
        print('''GREAT!! KEEP TRYING FOR A PERFECT SCORE.
        HERE IS YOUR CHOCO-COUPON. ''')
        print(color.red+'''*********************************
*                               *
*      !! CONGRATULATIONS !!    *
*                               *
*         *MINI-COUPON*         *
*      YOU EARNED A CHOCOLATE   *
*          WORTH RUPEES:-       *
*              10-/             *
*                               *
*********************************'''+color.end)
    else:
        print("Your Smiley Score: ","\U0001F604"*cor)
        print("BRAVO!! YOU WERE FIRE TODAY.","\U0001F525")
        print(color.red+'''*********************************
*                               *
*      !! CONGRATULATIONS !!    *
*                               *
*         *GRAND-COUPON*        *
*      YOU EARNED A CHOCOLATE   *
*          WORTH RUPEES:-       *
*              40-/             *
*                               *
*********************************'''+color.end)



# science subject questions



elif n.upper() == "SCIENCE":
    print(color.red+'''    *********************************
    *                               *
    *         !! LEVEL 1 !!         *
    *                               *
    *********************************'''+color.end)
    time.sleep(1)
#question 1
    print("Q1) Which planet is farthest to Sun?","\U0001F31E")
    s = input("ans : ")
    se = s.upper()
    if se == "NEPTUNE":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer= Mercury")
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)
#question 2
    print("Q2) What raw food is given by cows?",)
    s = input("ans : ")
    se = s.upper()
    if se == "MILK":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer=Honey")
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)
#question 3
    print("Q3) Which animal is the reason you are wearing a sweater today ?")
    print(color.orange+"HINT :"+color.end,"\U0001F40F")
    s = input("ans : ")
    se = s.upper()
    if se == "SHEEP":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer= Sheep ")
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)
#question 4
    print("Q4) Which star is closest to the earth?","\U0001F30F")
    s = input("ans : ")
    se = s.upper()
    if se == "SUN":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer=Sun")
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)
#question 5
    print("Q5) Which is the  healthiest among them ?")
    print(color.purple+"------------------------------------------"+color.end)
    print("1.","\U0001F354 "
        "2.","\U0001F34E "
        "3.","\U0001F366 "
        "4.","\U0001F35C ")
    print("Give the number of Option.")
    s = (input("ans : "))
    se = s
    if se == 2:
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer=2")
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)
    time.sleep(1)
    print(color.red+'''    *********************************
    *                               *
    *         !! LEVEL 2 !!         *
    *                               *
    *********************************'''+color.end)
    time.sleep(1)
#question 6
    print("Q6) If Legs=Feet then Arm= ?")
    print("1. Ankels"
          " 2. Pelvis"
          " 3. Hands"
          " 4. Skull")
    s = input("ans : ")
    se = s.upper()
    if se == "HANDS":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer=Hands")
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)
#question 7
    print("Q7) Which organ covers the entire body and protects it ?")
    print(" 1. Liver"
          " 2 .Heart"
          " 3. Skin"
          " 4. Brain")
    s = input("ans : ")
    se = s.upper()
    if se == "SKIN":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer=Skin")
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)
#question 8
    print("Q8) Which part of the bird lets it fly high in the sky ?","\U0001F54A")
    print(" 1. Beak"
          " 2. Feet"
          " 3. Wings"
          " 4. Claws")
    s = input("ans : ")
    se = s.upper()
    if se == "WINGS":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer=Wings")
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)
#question 9
    print("Q9) Which nutrient is the reason of your strong muscles. ?")
    print(" 1. Protein"
          " 2. Carbohydrate"
          " 3. Iron"
          " 4. Fats")
    s = input("ans : ")
    se = s.upper()
    if se == "PROTEIN":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer=Protein")
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)
#question 10
    print("Q10) Plants need which gas to prepare their food ?")
    print(" 1. Hydrogen"
          " 2. Carbon monoxide"
          " 3. Carbon dioxide"
          " 4. Oxygen")
    s = input("ans : ")
    se = s.upper()
    if se == "CARBON DIOXIDE":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer= Carbon Dioxide")
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)
    time.sleep(1)
    print(color.red+'''    *********************************
    *                               *
    *         !! LEVEL 3 !!         *
    *                               *
    *********************************'''+color.end)
    time.sleep(1)
#question 11
    print("Q11) If you build your house in Jupiter, then which planet is your neighbour?")
    print(" 1. Mercury"
          " 2. Neptune"
          " 3. Venus"
          " 4. Saturn")
    s = input("ans : ")
    se = s.upper()
    if se == "SATURN":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        print(color.purple+"Saturn is the only planet to have rings around it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer= Saturn")
        print(color.purple+"Saturn is the only planet to have rings around it."+color.end)
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)
#question 12
    print("Q12) What is the reason for your Fluffier Birthday Cakes?","\U0001F382")
    print(" 1. Milk"
          " 2. Sugar"
          " 3. Yeast"
          " 4. Mushroom")
    s = input("ans : ")
    se = s.upper()
    if se == "YEAST":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
        print(color.purple+"Fun Fact: There are about 1,500 different species of yeast."+color.end)
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer= Yeast")
        print("Fun Fact: There are about 1,500 different species of yeast.")
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)

#question 13
    print("Q13) Both Diamond and Coal are made up of ?")
    print(color.orange+"HINT : Decode this:"+color.end, "\U0001F697","+","\U0001F96F")
    s = input("ans : ")
    se = s.upper()
    if se == "CARBON":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer=Carbon")
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)
#question 14
    print("Q14) What part of the body is reason you can kick a football ?")
    print(" 1. Eyes"
          " 2. Lungs"
          " 3. Pancreas"
          " 4. Muscles")
    s = input("ans : ")
    se = s.upper()
    if se == "MUSCLES":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        print("Fun Fact: Human Beings have around 600 muscles")
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer=Muscles")
        print("Fun Fact: Human Beings have around 600 muscles")
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)
#question 15
    print("Q15) If I zoom into your body through a Simple Microscope,What is I am going to see ?")
    print(" 1. Cell"
          " 2. Atoms"
          " 3. Skin"
          " 4. Bones")
    s = input("ans : ")
    se = s.upper()
    if se == "CELL":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print("Sorry! That was Wrong.")
        print("Correct Answer=Cell")
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)

    time.sleep(1)
# print result
    print("your correct answer is ",cor)
    print("your incorrect answer is ",icor)
    if cor==0:
        print("Sorry! Today was not your day","\U0001F614"*2)
    if cor <=5:
        print("Your Smiley Score:","\U0001F642"*cor)
        print(''''HARD LUCK!! YOU DIDN'T MAKE THIS TIME,
        HERE IS YOUR APPRECIATION COUPON
        ''')
        print(color.blue+'''*********************************
*                               *
*      !! CONGRATULATIONS !!    *
*                               *
*                               *
*         *APPRECIATION*        *
*            *COUPON*           *
*                               *
*                               *
*********************************'''+color.end)
        print("Collect 5 of them to win a MINI CHOCO-COUPON")
    elif cor>5>=10:
        print("Your Smiley Score: ","\U0001F60A"*cor)
        print('''GREAT!! KEEP TRYING FOR A PERFECT SCORE.
        HERE IS YOUR CHOCO-COUPON. ''')
        print(color.blue+'''*********************************
*                               *
*      !! CONGRATULATIONS !!    *
*                               *
*         *MINI-COUPON*         *
*      YOU EARNED A CHOCOLATE   *
*          WORTH RUPEES:-       *
*              10-/             *
*                               *
*********************************'''+color.end)
    else:
        print("Your Smiley Score: ","\U0001F604"*cor)
        print(color.red+"BRAVO!! YOU WERE FIRE TODAY."+color.end,"\U0001F525")
        print(color.blue+'''*********************************
*                               *
*      !! CONGRATULATIONS !!    *
*                               *
*         *GRAND-COUPON*        *
*      YOU EARNED A CHOCOLATE   *
*          WORTH RUPEES:-       *
*              40-/             *
*                               *
*********************************'''+color.end)

# gk subject questions


elif n.upper() == "GK":

#question 1
    time.sleep(1)
    print(color.red+'''    *********************************
    *                               *
    *         !! LEVEL 1 !!         *
    *                               *
    *********************************'''+color.end)
    time.sleep(1)
    print("Q1) Where is colour of US President's Residence ?")
    s = input("ans : ")
    se = s.upper()
    if se == "WHITE":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print(color.red+"Sorry! That was Wrong."+color.end)
        print("Correct Answer= White. ")
        icor += 1
    print()
    print(color.purple+"------------------------------------------"+color.end)

#question 2
    print("Q2) Hi,This is my selfie, But what is my name ?","\U0001F434")
    s = input("ans : ")
    se = s.upper()
    if se == "HORSE":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print(color.red+"Sorry! That was Wrong."+color.end)
        print("Correct Answer= Horse. ")
        icor += 1
    print(color.purple+"------------------------------------------"+color.end)

#question 3
    print("Q3) Hi, If you have an emergency you call me first, Who am I?")
    print(color.orange+"HINT: Here is my picture."+color.end,"\U0001F46E")
    s = input("ans : ")
    se = s.upper()
    if se == "POLICEMAN":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    elif se == "POLICE":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print(color.red+"Sorry! That was Wrong."+color.end)
        print("Correct Answer= Police. ")
        icor += 1
    print(color.purple+"------------------------------------------"+color.end)

#question 4
    print("Q4) What is the green pigment in leaf called?")
    s = input("ans : ")
    se = s.upper()
    if se == "CHLOROPHYLL":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print(color.red+"Sorry! That was Wrong."+color.end)
        print("Correct Answer= Chlorophyll. ")
        icor += 1
    print(color.purple+"------------------------------------------"+color.end)

#question 5
    time.sleep(1)
    print(color.red+'''    *********************************
    *                               *
    *         !! LEVEL 2 !!         *
    *                               *
    *********************************'''+color.end)
    time.sleep(1)
    print("Q5) Guess the Festival using this pictures")
    print("\U0001F385")
    print("\U0001F384")
    print("\U0001F381")
    s = input("ans : ")
    se = s.upper()
    if se == "CHRISTMAS":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print(color.red+"Sorry! That was Wrong."+color.end)
        print("Correct Answer= Christmas. ")
        icor += 1
    print(color.purple+"------------------------------------------"+color.end)

#question 6
    print("Q6) The Legendary singer also known as 'Nightingle Of India'?")
    s = input("ans : ")
    se = s.upper()
    if se == "LATA MANGESHKAR":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        print(color.purple+"Fun Fact: Lata Mangeshkar had recorded 50,000 songs in 14 different languages."+color.end)
        cor += 1
    else:
        print(color.red+"Sorry! That was Wrong."+color.end)
        print("Correct Answer= Lata Mangeshkar. ")
        print(color.purple+"Fun Fact: Lata Mangeshkar had recorded 50,000 songs in 14 different languages."+color.end)
        icor += 1
    print(color.purple+"------------------------------------------"+color.end)

#question 7
    print("Q7) I am the most followed person on Instagram, Guess my surname?")
    s = input("ans : ")
    se = s.upper()
    if se == "RONALDO":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print(color.red+"Sorry! That was Wrong."+color.end)
        print("Correct Answer= Ronaldo. ")
        icor += 1
    print(color.purple+"------------------------------------------"+color.end)

#question 8
    print("Q8) Most spoken language in the World")
    s = input("ans : ")
    se = s.upper()
    if se == "ENGLISH":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print(color.red+"Sorry! That was Wrong."+color.end)
        print("Correct Answer= English. ")
        icor += 1
    print(color.purple+"------------------------------------------"+color.end)

#question 9
    print("Q9) The colours of Rainbow are known by which acronym?")
    print(color.orange+"HINT: "+color.end,"\U0001F308")
    s = input("ans : ")
    se = s.upper()
    if se == "VIBGYOR":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print(color.red+"Sorry! That was Wrong."+color.end)
        print("Correct Answer= VIBGYOR. ")
        icor += 1
    print(color.purple+"------------------------------------------"+color.end)

#question 10
    time.sleep(1)
    print(color.red+'''    *********************************
    *                               *
    *         !! LEVEL 3 !!         *
    *                               *
    *********************************'''+color.end)
    time.sleep(1)
    print("Q10) I have three hearts, eight legs, and blue blood, Who am I?")
    s = input("ans : ")
    se = s.upper()
    if se == "OCTOPUS":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print(color.red+"Sorry! That was Wrong."+color.end)
        print("Correct Answer= Octopus. ")
        icor += 1
    print(color.purple+"------------------------------------------"+color.end)

#question 11
    print("Q11) First Asian athlete to win an Olympic gold medal in Men's Javelin throw?")
    s = input("ans : ")
    se = s.upper()
    if se == "NEERAJ CHOPRA":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print(color.red+"Sorry! That was Wrong."+color.end)
        print("Correct Answer= Neeraj Chopra ")
        icor += 1
    print(color.purple+"------------------------------------------"+color.end)

#question 12
    print("Q12) The strongest part in your body is ?")
    print("Tooth, Bone, Nails, Hair")
    s = input("ans : ")
    se = s.upper()
    if se == "TOOTH":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print(color.red+"Sorry! That was Wrong."+color.end)
        print("Correct Answer= Tooth ")
        icor += 1
    print(color.purple+"------------------------------------------"+color.end)

#question 13
    print("Q13) Who was mother of Lord Krishna ?")
    s = input("ans : ")
    se = s.upper()
    if se == "DEVKI":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print(color.red+"Sorry! That was Wrong."+color.end)
        print("Correct Answer= Devki")
        icor += 1
    print(color.purple+"------------------------------------------"+color.end)

#question 14
    print("Q14) Name of a country and also name of a bird?")
    print(color.orange+"HINT :"+color.end,"\U0001F1F9\U0001F1F7")
    s = input("ans : ")
    se = s.upper()
    if se == "TURKEY":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print(color.red+"Sorry! That was Wrong."+color.end)
        print("Correct Answer= Turkey")
        icor += 1
    print(color.purple+"------------------------------------------"+color.end)

#question 15
    print('''Q15)I am the only creature that has venom like Replite, Beak like Birds,
    feeds our young one with milk like Mammles, Guess my name ?''')
    s = input("ans : ")
    se = s.upper()
    if se == "PLATYPUS":
        time.sleep(1)
        print(color.green+"Hurray! You got it."+color.end)
        cor += 1
    else:
        print(color.red+"Sorry! That was Wrong."+color.end)
        print("Correct Answer= Platypus")
        icor += 1
#print result
    print("your correct answer is ",cor)
    print("your incorrect answer is ",icor)
    time.sleep(1)
    if cor==0:
        print("Sorry! Today was not your day","\U0001F614"*2)
    if cor <=5:
        print("Your Smiley Score:","\U0001F642"*cor)
        print(''''HARD LUCK!! YOU DIDN'T MAKE THIS TIME,
        HERE IS YOUR APPRECIATION COUPON
        ''')
        print(color.blue+'''*********************************
*                               *
*      !! CONGRATULATIONS !!    *
*                               *
*                               *
*         *APPRECIATION*        *
*            *COUPON*           *
*                               *
*                               *
*********************************'''+color.end)
        print("Collect 5 of them to win a MINI CHOCO-COUPON")
    elif 5<cor>=10:
        print("Your Smiley Score: ","\U0001F60A"*cor)
        print('''GREAT!! KEEP TRYING FOR A PERFECT SCORE.
        HERE IS YOUR CHOCO-COUPON. ''')
        print(color.blue+'''*********************************
*                               *
*      !! CONGRATULATIONS !!    *
*                               *
*         *MINI-COUPON*         *
*      YOU EARNED A CHOCOLATE   *
*          WORTH RUPEES:-       *
*              10-/             *
*                               *
*********************************'''+color.end)
    else:
        print("Your Smiley Score: ","\U0001F604"*cor)
        print("BRAVO!! YOU WERE FIRE TODAY.","\U0001F525")
        print(color.blue+'''*********************************
*                               *
*      !! CONGRATULATIONS !!    *
*                               *
*         *GRAND-COUPON*        *
*      YOU EARNED A CHOCOLATE   *
*          WORTH RUPEES:-       *
*              40-/             *
*                               *
*********************************'''+color.end)
else:
    exit()