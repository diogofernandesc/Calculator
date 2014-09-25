# Diogo Fernandes - "Could a calculator do your Maths A Level for you?"
#***Finalized version

import math

#-----CLEAR CONSOLE--------------------------------------------------------------------------------
def wipe():
    print("\n"*50,'''
        
 ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗      ██████╗ ███╗   ██╗
██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗    ██╔═══██╗████╗  ██║
██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝    ██║   ██║██╔██╗ ██║
██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗    ██║   ██║██║╚██╗██║
╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║    ╚██████╔╝██║ ╚████║
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═══╝                                                                                        
''')
#-----USER GUIDANCE--------------------------------------------------------------------------------

def guidance():
    wipe()
    choice = input("What module would you like to access? \n 1. C1 \n 2. C2 \n 3. D1 \n Please input:").lower()
    if choice in ["c1","1"]:
        wipe()
        C1_menu()

    elif choice in ["c2","2"]:
        wipe()
        C2_menu()

    elif choice in ["d1","3"]:
        wipe()
        D1_menu()

    else:
        print("Your choice is invalid, try again")
        wipe()
        guidance()
        
#---------------------------------------------------------------------------------------------------

def C1_menu():
    choice = input("What do you want to do? \n \n 1. Rationalise denominator \n \n 2. Find the discriminant and know what your graph will look like \n \n 3. Find the gradient of a line \n \n 4. Find the equation of a line \n \n 5. Find the common difference of a sequence \n \n 6. Find the sum of a series \n \n 7. Find the nth term of a sequence \n \n Please input:").lower()

    if choice in ["1","rationalise","rationalise denominator"]:
        wipe()
        rationalise_denominator()
        other_options()

    elif choice in ["2","discriminant","find discriminant"]:
        wipe()
        discriminant()
        other_options()

    elif choice in ["3","gradient","find the gradient","find gradient"]:
        wipe()
        gradient()
        other_options()

    elif choice in ["4" or "equation of line","equation line","equation"]:
        wipe()
        equation_line()
        other_options()

    elif choice in ["5","common difference","find the common difference","find the common difference of a sequence"]:
        wipe()
        common_difference()
        other_options()

    elif choice in ["6","sum of series","sum series","find the sum of a series"]:
        wipe()
        sum_series()
        other_options()

    elif choice in ["7","nth term","nth term sequence","nth term of a sequence"]:
        wipe()
        nth_term()
        other_options()

    else:
        print("Your choice is invalid, try again")
        wipe()
        C1_menu()

# First navigation menu - Multiple input possibilities - Where the condition is met; so user inputs one of the options; the procedure/function is executed;
# If input is incorrect, user will be told it is incorrect and recursion will incur so the user can try again;
# Other_options() used after to allow the user to choose whether they want to carry out another calculation or exit the program;


#-----------------------------------------------------------------------------------------------------------------------------

def C2_menu():
    choice = input("What do you want to do? \n \n 1. Use the sine rule to find an unknown side \n \n 2. Use the cosine rule to find an angle or side \n \n 3. Find the area of a triangle \n \n 4. Find the midpoint of a line \n \n 5. Find the distance between two points/length of a line \n \n 6. Convert degrees to radians \n \n 7. Convert radians to degrees \n \n 8. Find the length of an arc \n \n 9. Find the area of a sector \n \n 10. Find the area of a segment \n \n 11. Find the common ratio of a sequence \n \n 12. Find the sum of a geometric series \n \n 13. Find the sum to infinity of a series \n \n 14. Find the area under a curve with the trapezium rule \n \n Please input:").lower()
    if choice in ["1","sine rule","find a side","find a side with sine rule","sine","side with sine rule","side with sine"]:
        wipe()
        sine_rule()
        other_options()
        
    elif choice in ["2","cosine rule","find an angle","find an angle with cosine rule","cosine","angle"]:
        wipe()
        cosine_rule()
        other_options()

    elif choice in ["3","area triangle","area of a triangle","find area of triangle","find the area of a triangle"]:
        wipe()
        AreaTriangle()
        other_options()

    elif choice in ["4","midpoint","find the midpoint","find midpoint"]:
        wipe()
        midpoint()
        other_options()

    elif choice in ["5","length of line","length","distance between two points","length line"]:
        wipe()
        DistancePoints()
        other_options()

    elif choice in ["6","convert degrees to radians","degrees to radians"]:
        wipe()
        Degree = float(input("Enter your value in degrees:"))
        DegreesToRadians(Degree)
        other_options()

    elif choice in ["7","convert radians to degrees","radians to degrees"]:
        wipe()
        Radian = float(input("Enter your value for radians:"))
        RadiansToDegrees(Radian)
        other_options()

    elif choice in ["8","find length of arc","find length arc","find arc","arc"]:
        wipe()
        length_arc()
        other_options()

    elif choice in ["9","find sector","area sector","area of sector","find area of sector"]:
        wipe()
        area_of_sector()
        other_options()

    elif choice in ["10","segment","area segment","area of segment"]:
        wipe()
        area_of_segment()
        other_options()

    elif choice in ["11","common ratio","common ratio sequence","common ratio of a sequence"]:
        wipe()
        common_ratio()
        other_options()

    elif choice in ["12","sum of series","sum of geometric series","sum geometric","geometric series","geometric"]:
        wipe()
        sum_geometric()
        other_options()

    elif choice in ["13","sum infinity","sum to infinity","infinity series"]:
        wipe()
        sum_infinity()
        other_options()
        
    elif choice in ["14","trapezium","area under curve","area under curve with trapezium rule"]:
        wipe()
        trapezium_rule()
        other_options()

    else:
        print("Your choice is invalid, try again")
        C2_menu()

# Had trouble with if statements but putting input possibilites in a list -> as long the user's input is within that list the condition is met;


#----------------------------------------------------------------------------------------------------------------------------

def D1_menu():
    choice = input("What do you want to do? \n \n 1. Bubble sort in descending order \n \n 2. Bubble sort in ascending order \n \n Please input:").lower()
    if choice in ["1","bubble sort descending","descending"]:
        wipe()
        ask_numbers()
        bubble_sort_descending(number_list)
        print("The ordered list is:",number_list)
        other_options()

    elif choice in ["2","bubble sort ascending".lower(),"ascending".lower()]:
        wipe()
        ask_numbers()
        bubble_sort_ascending(number_list)
        print("The ordered list is:",number_list)
        other_options()


   #elif choice in ["3","quick sort".lower(),"quick".lower()]:
    #    ask_numbers()
     #   quick_sort("The ordered list is:",number_list)
      #  other_options()

    else:
        print("Your choice is invalid, try again")
        D1_menu()


def other_options():
    choice = input("Would you like to carry out any more operations?").lower()
    if choice in ["yes","y"]:
        wipe()
        guidance()
    elif choice in ["no","n"]:
        wipe()
        print("\n"*100,'''
██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗      ██████╗ ███████╗███████╗
██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗    ██╔═══██╗██╔════╝██╔════╝
██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝    ██║   ██║█████╗  █████╗  
██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗    ██║   ██║██╔══╝  ██╔══╝  
╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║    ╚██████╔╝██║     ██║     
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚═╝     ╚═╝
\n Thank you for using the calculator''')

# As mentioned above; user is asked whether they want to carry on - yes calls guidance() - allows user to access the whole program from the start;
# No prints an exiting statement and program exits;


#---------------------------------------C1---------------------------------------------------------
#-----RATIONALISE DENOMINATOR----------------------------------------------------------------------

def rationalise_denominator():
    rationalise_choice = int(input("Please choose the format in which you want to rationalise: \n 1. 1/√x \n 2. 1/(n + √x) \n 3. (√y + √x)/(√y - √x) \n \n *** Please note answers may not be in the most simplified form"))
    if rationalise_choice == 1:
            x = float(input("1/√x: \n What is your x value?"))
            if x > 0:
                wipe()
                print("The rationalised form is:","√",x,"/",x)
            else:
                   print("Your choice is invalid, try again")
                   wipe()
                   rationalise_denominator()
#Multiplying a surd by itself removes the square root but the numerator is now the old surd; whole fraction as been multiplied by initial surd;       

    elif rationalise_choice == 2:
            x = float(input("1/(n + √x): \n What is your x value?"))
            n = float(input("1/(n + √x): \n What is your n value?"))
            if x > 0 and n > 0:
                wipe()
                print("The rationalised form is:","(",n,"- √",x,") /",(n**2 - x))
            else:
                   print("Your choice is invalid, try again")
                   wipe()
                   rationalise_denominator()

    elif rationalise_choice == 3:
            x = float(input("(√y + √x)/(√y - √x): \n What is your x value? \n \n ***Please note this version of rationalisation is still in beta and may not produce the right result"))
            y = float(input("(√y + √x)/(√y - √x): \n What is your y value? \n \n ***Please note this version of rationalisation is still in beta and may not produce the right result"))
            if x > 0 and y > 0:
                answer_part1 = (math.sqrt(y) + math.sqrt(x) * (math.sqrt(y) + math.sqrt(x)))
                answer_part2 = ((math.sqrt(y) - math.sqrt(x)) * (math.sqrt(y) + math.sqrt(x)))
                print("The rationalised form is:",(x+y),"+",x,"√",x*y,"/", y - x)

    else:
        print("Your choice is invalid, try again")
        wipe()
        rationalise_denominator()


#-----FINDING THE DISCRIMINANT-------------------------------------------------------------------

def discriminant():
    a = float(input("y = ax² + bx + c  \n What is your a value?"))
    b = float(input("y = ax² + bx + c  \n What is your b value?"))
    c = float(input("y = ax² + bx + c  \n What is your c value?"))
    if b**2 > 4*a*c and a > 0:
        wipe()
        print("The discriminant is", (b**2) - (4*a*c), "and your graph will have two different roots with a positive parabola")
        

    elif b**2 == 4*a*c and a > 0:
        wipe()
        print("The discriminant is", (b**2) - (4*a*c), "and your graph will have two equals roots with a positive parabola")


    elif b**2 < 4*a*c and a > 0:
        wipe()
        print("The discriminant is", (b**2) - (4*a*c), "and your graph will have no real roots with a positive parabola")


    elif b**2 > 4*a*c and a < 0:
        wipe()
        print("The discriminant is", (b**2) - (4*a*c), "and your graph will have two different roots with a negative parabola")


    elif b**2 == 4*a*c and a < 0:
        wipe()
        print("The discriminant is", (b**2) - (4*a*c), "and your graph will have two equal roots with a negative parabola")


    elif b**2 < 4*a*C and a < 0:
        wipe()
        print("The discriminant is", (b**2) - (4*a*c), "and your graph will have no real roots with a negative parabola")


#------GRADIENT------------------------------------------------------------------------------------

def gradient():
    x1 = int(input("What is your first x co-ordinate?"))
    x2 = int(input("What is your second x co-ordinate?"))
    y1 = int(input("What is your first y co-ordinate?"))
    y2 = int(input("What is your second y co-ordinate?"))
    wipe()
    print("The gradient is", (y2 - y1)/(x2 - x1))


#-----EQUATION OF A LINE----------------------------------------------------------------------------

def equation_line():
    m = int(input("What is your gradient?"))
    x = int(input("What is your x co-ordinate?"))
    y = int(input("What is your y co-ordinate?"))
    wipe()
    print("Your equation is: y =",m,"x - ",m*x-y)


#------COMMON DIFFERENCE OF SEQUENCE-----------------------------------------------------------------

def common_difference():
    sequence = []
    first = int(input("What is the first number in the sequence?"))
    sequence.append(first)
    second = int(input("What is the second number in the sequence?"))
    sequence.append(second)
    third = int(input("What is the third number in the sequence?"))
    sequence.append(third)
    wipe()
    print("The common difference is:", sequence[1] - sequence [0])
# I put the variables from the user's inputs in an array/list and then subtracted the second number which is positions [1] in the array away from the intial position [0];
                   
#------NTH TERM----------------------------------------------------------------------------------

def nth_term():
    a = int(input("What is the first number in your sequence?"))
    d = int(input("What is the common difference in your sequence?"))
    wipe()
    print("The nth term is given by:",d,"n -",-d + a)
# Printing an expanded version of Un = a+(n-1)d -> a + dn - d
                   

#-----SUM OF A SERIES-----------------------------------------------------------------------------

def sum_series():
    n = int(input("To what term do you want the sum of series for?"))
    a = int(input("What is the first number in the series?"))
    d = int(input("What is the common difference in the series?"))
    wipe()
    print("The sum of the series to the",n,"term is",(n/2)*(2*a+(n-1)*d))

#--------------------------------------C2---------------------------------------------------------


#----SINE RULE-----------------------------------------------------------------------------

def sine_rule():


    side = input('''
                         B
                         .
                        . .
                       .   .
                  c   .     .   a
                     .       .
                    .         .
                   .           .
                A ............... C
            
                         b
                     
We will take a triangle ABC, which side do you want to find?''').lower()
       
    if side == "a":
         side1 = float(input("What is the size of side AB or AC?"))
         angle1 = float(input("What is the size of angle A?"))
         angle2 = float(input("What is the size of the angle of the side you chose(AB or AC)?"))
         top = side1*(math.sin(math.radians(angle1)))
         bottom = (math.sin(math.radians(angle2)))
         wipe()
         print("Side a is equal to:",round(top/bottom,2))

    elif side == "b":
        side1 = float(input("What is the size of side AB or BC?"))
        angle1 = float(input("What is the size of angle B?"))
        angle2 = float(input("What is the size of angle of the side you chose(AB or BC)?"))
        top = side1*(math.sin(math.radians(angle1)))
        bottom = (math.sin(math.radians(angle2)))
        wipe()
        print("Side a is equal to:",round(top/bottom,2))

    elif side == "c":
        side1 = float(input("What is the size of side AC or BC?"))
        angle1 = float(input("What is the size of angle C?"))
        angle2 = float(input("What is the size of the angle of the side you chose(AC or BC)?"))
        top = side1*(math.sin(math.radians(angle1)))
        bottom = (math.sin(math.radians(angle2)))
        wipe()
        print("Side a is equal to:",round(top/bottom,2))
        
    else:
        print("Your choice is invalid, try again")
        wipe()
        sine_rule()

#------COSINE RULE------------------------------------------------------------------------
def get_sides():
    global Sa
    global Sb
    global Sc
    Sa = float(input("What is the size of the side a?"))
    Sb = float(input("What is the size of the side b?"))
    Sc = float(input("What is the size of the side c?"))
def cosine_rule():
    global Sa
    global Sb
    global Sc
    choice = input("What do you want to find?: \n The angle or the side?").lower()
    if choice == "angle": #.lower() makes it so that whatever the input UPPERCASE or lowercase the condition will be interpreted with the input in lowercase;
        get_sides()
        if Sa + Sb > Sc and Sa + Sc > Sb and Sc + Sb > Sa:
            angle = input("What angle do you want to find? \n 1. A \n 2. B \n 3. C").lower()
            if angle in ["a","1"]:
                a = (((Sb)**2) + ((Sc)**2) - ((Sa)**2))/(2*Sb*Sc)
                answer = math.acos(a) # variable a above is suppose to CosA - this means that the variable answer now transfers variable a from cos(a) to just the value of a - math.acos = cos^-1(a) [inverse cos];
                answer_degrees = math.degrees(answer)
                wipe()
                print("The angle of A is:", round(answer_degrees, 1),"°")

        elif angle in ["b","2"]:
            b = (((Sa)**2) + ((Sc)**2) - ((Sb)**2))/(2*Sa*Sc)
            answer = math.acos(b)
            answer_degrees = math.degrees(answer)
            wipe()
            print("The angle of B is:", round(answer_degrees, 1),"Ã‚Â°")

        elif angle in ["c","3"]:
            c = (((Sa)**2) + ((Sb)**2) - ((Sc)**2))/(2*Sa*Sb)
            answer = math.acos(c)
            answer_degrees = math.degrees(answer)
            wipe()
            print("The angle of C is:", round(answer_degrees, 1),"Ã‚Â°")

        else:
            print("Your choice is invalid, try again")
            wipe()
            cosine_rule()

    elif choice == "side":
        side = input("What side do you want to find? \n 1. a \n 2. b \n 3. c")
        if side in ["a","1"]:
            AngleA = float(input("What is the size of angle A?"))
            Sb = float(input("What is the size of the side b?"))
            Sc = float(input("What is the size of the side c?"))
            aSquared = (Sb**2) + (Sc**2) - (2*Sb*Sc)*math.cos(math.radians(AngleA))
            wipe()
            print("The size of side a is:", round(math.sqrt(aSquared),2)) # math.radians is responsible for converting from degrees to radians - math.cos(math.radians(AngleA) first converts variable AngleA's value to radians and then cos of that is calculated;
                                                                          # For the print statement I rounded to 2 d.ps [ round("variable",'no of decimal places'], most of the answers for these calculations tend to have a long decimal answer;
        elif side in ["b","2"]:
            AngleB = float(input("What is the size of angle B?"))
            Sa = float(input("What is the size of the side a?"))
            Sc = float(input("What is the size of the side c?"))
            bSquared = (Sa**2) + (Sc**2) - (2*Sa*Sc)*math.cos(math.radians(AngleB))
            wipe()
            print("The size of side b is:", round(math.sqrt(bSquared),2))

        elif side in ["c","3"]:
            AngleC = float(input("What is the size of angle C?"))
            Sa = float(input("What is the size of the side a?"))
            Sb = float(input("What is the size of the side b?"))
            cSquared = (Sb**2) + (Sc**2) - (2*Sb*Sc)*math.cos(math.radians(AngleC))
            wipe()
            print("The size of side c is:", round(math.sqrt(cSquared),2))

        else:
            print("Your choice is invalid, try again")
            wipe()
            cosine_rule()
                   
#-----AREA OF TRIANGLE--------------------------------------------------------------------

def AreaTriangle():
    a = float(input("What is the value of side a?"))
    b = float(input("What is the value of side b?"))
    C = float(input("What is the size of angle C?"))
    sinC = math.sin(math.radians(C))
    area = 0.5 * a * b * sinC
    wipe()
    print("The area of your triangle is:",round(area, 1),"units²")

#------COORDINATES--------------------------------------------------------------------------

def get_coordinates():
    global x1
    global x2
    global y1
    global y2
    x1 = float(input("What is your first x-coordinate?"))
    x2 = float(input("What is your second x-coordinate?"))
    y1 = float(input("What is your first y-coordinate?"))
    y2 = float(input("What is your second y-coordinate?"))

#-----MIDPOINT------------------------------------------------------------------------------

def midpoint():
    get_coordinates()
    midpointX = (x1 + x2)/2
    midpointY = (y1 + y2)/2
    wipe()
    print("Your midpoint is:","(",midpointX,",",midpointY,")")



#-----DISTANCE BETWEEN TWO POINTS-----------------------------------------------------------

def DistancePoints():
    get_coordinates()
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    wipe()
    print("The distance between your points or the length of the line is:",round(d, 2))

#-----CONVERT RADIANS TO DEGREES AND VICE VERSA----------------------------------------------


def DegreesToRadians(Degree):
    answer = Degree * (math.pi/180)
    print(Degree,"° in radians, gives:",round(answer, 2))

def RadiansToDegrees(Radian):
    answer = Radian * (180/math.pi)
    print(Radian,"radians, gives:",round(answer, 2),"°")


#-----INPUT RADIUS AND ANGLE-----------------------------------------------------------------
def inputRA():
    global radius
    global angle
    radius = float(input("What is the radius of the arc?"))
    angle = float(input("What angle does the arc subtend at?"))

#-----LENGTH OF ARC---------------------------------------------------------------------------

def length_arc():
    inputRA()
    print("The length of the arc is:",round(radius*angle,2))

#----AREA OF SECTOR---------------------------------------------------------------------------

def area_of_sector():
    inputRA()
    print("The area of the sector is:",round(0.5*(radius**2)*angle,2),"units²")

#----AREA OF SEGMENT----------------------------------------------------------------------------

def area_of_segment():
    inputRA()
    print("The area of the segment is:",round((0.5*(radius**2)*angle)-(0.5*(radius**2)*math.sin(angle)),2),"units²")

#-----COMMON RATIO---------------------------------------------------------------------------------

def common_ratio():
    n1 = int(input("What is the first term you know from the sequence?"))
    n2 = int(input("What is the second term you know from the sequence?"))
    value1 = int(input("What is the value of {} term?".format(n1)))
    value2 = int(input("What is the value of {} term?".format(n2)))
    answer_1 = value2 / value1
    answer_2 = answer_1 ** (1/((n2 - 1) - (n1-1)))
    wipe()
    print("The common ratio of the sequence is",int(answer_2))

#-------SUM OF GEOMETRIC SERIES---------------------------------------------------------------------
          
def sum_geometric():
    a = int(input("What is the first term of your sequence?"))
    r = float(input("What is the common ratio of your sequence?"))
    n = int(input("To what term do you want the sum of the squence for?"))
    SUM = (a*((r**n) - 1))/(r - 1)
    wipe()
    print("The sum of the series is:", SUM)  # Have realised python doesn't accept negative numbers as input naturally **

#-----SUM TO INFINITY-----------------------------------------------------------------------------

def sum_infinity():
    a = int(input("What is the first term of your sequence?"))
    r = float(input("What is the common ratio of your sequence?"))
    SUM = a / (1-r)
    wipe()
    print("The sum to infinity of your series is:",SUM)


#----TRAPEZIUM RULE------------------------------------------------------------------------------
    
def trapezium_rule():
    nStrip = int(input("How many strips does the area have?"))
    wStrip = float(input("What is the width of the strips?"))
    y1 = float(input("What is the first value of y?"))
    y2 = float(input("What is the second value of y?"))
    y3 = float(input("What is the third value of y?"))
    y4 = float(input("What is the fourth value of y?"))
    y5 = float(input("What is the fifth value of y?"))
    area = 0.5*wStrip*((y1 + 2*(y2 + y3 + y4) + y5))
    wipe()
    print("The area of the trapezium is", area)
            
#------------------------------------------D1-----------------------------------------------------

#------BUBBLE SORT--------------------------------------------------------------------------------
def ask_numbers():
    global number_list
    global choice
    number_list = []
    choice = int(input("How many numbers do you want to put in order?"))
    i = 0
    for i in range(0,choice):
        number = int(input("Enter your number:"))
        number_list.append(number)
        i = i + 1

# A simple loop to get the user to choose the size of their list, the numbers in the list and these are then used in any of the sorting algorithms because they each take the parameter of number_list;
# I initialise variable i has the control variable of the loop as 0;
# so from the point i = 0 to whatever it becomes from the input of choice - the program will continuous ask for numbers to input into the list and then append these to the list number_list;        
        
def bubble_sort_descending(wrong_list):
    length = len(wrong_list) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(length):
            if wrong_list[i] < wrong_list[i + 1]: # This condition is responsible for determining whether bubble sort is sorting in descending or ascending order;
                sorted = False
                wrong_list[i], wrong_list[i + 1] = wrong_list[i + 1], wrong_list[i]
                                                  # The loop will run for as long as i is in the range of the variable length which is the length of the list - 1;
                                                  # The last statement basically carries out the change; so say you have 5,7 where number_list[i] = 5 and number_list[i + 1] = 7 , this statement will make number_list[i] = 7 and number_List[i + 1] = 5;


def bubble_sort_ascending(wrong_list):
    length = len(wrong_list) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(length):
            if wrong_list[i] > wrong_list[i + 1]:
                sorted = False
                wrong_list[i], wrong_list[i + 1] = wrong_list[i + 1], wrong_list[i]

#------QUICK SORT--------------------------------------------------------------------------------------------

#def quick_sort_ascending(number_list):
 #   less = []
  #  equal = []
   # greater = []
    #if len(number_list) > 1:
     #   pivot = number_list[0]
      #  for i in number_list:
       #     if i < pivot:
        #        less.append(i)
         #   elif i == pivot:
          #      equal.append(i)
           # elif i > pivot:
            #    greater.append(i)
        # return quick_sort(less) + equal + quick_sort(greater)

# Three lists which values are appended to based on whether they are smaller, the same or bigger than the pivot at that point;
# The initial condition that has to be met before quick sort can be carried out is whether or not the length of number_list is bigger than 1, if it is not then there is nothing to put in order since there will only be either 1 or zero values
# For numbers less than the pivot they append to list less[] , equal to list equal[] and greater than to list greater[]
# The last print statement basically prints out the contents of each list now organised
# Still can't get it to work

#------------------------------------------------------------------------------------------------------------------
        
guidance()
