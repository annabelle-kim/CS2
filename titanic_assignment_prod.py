import matplotlib

"""
GCDS CS: Titanic Dataset Analysis
Dataset: titanic.csv

SETUP:
------


The titanic.csv dataset contains the following columns:
- PassengerId: Unique ID for each passenger
- Survived: 0 = No, 1 = Yes
- Pclass: Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)
- Name: Passenger name
- Sex: male or female
- Age: Age in years
- SibSp: Number of siblings/spouses aboard
- Parch: Number of parents/children aboard
- Ticket: Ticket number
- Fare: Passenger fare
- Cabin: Cabin number
- Embarked: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)

ASSIGNMENT GOALS:
-----------------

GOAL 1 (Beginner): Load and Display Data
-----------------------------------------
Load the titanic.csv file and display the first 10 rows.
Print the column names and the total number of passengers.

"""
def first_10_rows():
    try:
        with open('titanic.csv', 'r') as file:
            #header = file.readline().strip().split(',')  # Read the header row
            #name_index = header.index('Name')  # Find the index of 'Name' column
        
            for i,line in enumerate(file):
                if i<11:
                    row = line.strip().split(',')
                    print(row)
                    #print(row[name_index])
    except FileNotFoundError:
            print(f"Error: 'titanic.csv' file not found.")
    except Exception as e:
            print(f"An error occurred: {e}")

def total_passengers():
    data_file = open('titanic.csv', 'r')
    rows = data_file.readlines()
    data_file.close()
    print(len(rows)-1) # number of rows, including header
 
"""

GOAL 2 (Beginner): Calculate Survival Rate
-------------------------------------------
Calculate and print the overall survival rate (percentage of passengers who survived).

"""
def survival_percentage():

    with open ('titanic.csv', 'r', newline = '') as file:
        file.seek(0)
        survival = 0
        total = 0
        next(file)
        for line in file:
            row=line.strip().split(',')
            if row[1] == "1":
                survival+=1
                total += 1
            else:
                total += 1
        print (f'Total Survival Rate: {"{:.2f}".format(survival/total*100)}%')

"""

GOAL 3 (Intermediate): Survival by Gender
------------------------------------------
Calculate the survival rate for males and females separately.
Display which gender had a higher survival rate.
"""

def gender_survival():
    with open ('titanic.csv', 'r', newline = '') as file:
        file.seek(0)
        men = 0
        survived_men = 0
        women = 0
        survived_women = 0
        next(file)
        for line in file:
            row=line.strip().split(',')  
            if row[5] == "male":
                men +=1
                if row[1] == "1":
                    survived_men +=1
            else:
                women+=1
                if row [1] == "1":
                    survived_women +=1
        print (f'Male Survival Rate: {"{:.2f}".format(survived_men/men*100)}%')
        print (f'Female Survival Rate: {"{:.2f}".format(survived_women/women*100)}%')

    
"""
GOAL 4 (Intermediate): Age Analysis
------------------------------------
Find and print:
- The average age of all passengers
- The average age of survivors vs non-survivors
- The youngest and oldest passengers
"""

def average_age():
    with open ('titanic.csv', 'r', newline = '') as file:
        file.seek(0)
        age = 0
        total = 0
        allage = 0
        next(file)
        for line in file:
            row=line.strip().split(',')
            total +=1
            if row[6] != '':
                age = float(row[6])
                allage += age
        print (f'Average Age: {"{:.2f}".format(allage/total)}')  

def age_survivor_nonsurvivor():
    with open ('titanic.csv', 'r', newline = '') as file:
        file.seek(0)
        survivors = 0
        survivorage = 0
        dead = 0
        deadage = 0
        next(file)
        for line in file:
            row=line.strip().split(',')
            if row[1] == "1":
                survivors +=1
                if row [6] != '':
                    age1 = float(row[6])
                    survivorage += age1
            else:
                dead+=1
                if row [6] != '':
                    age2 = float(row[6])
                    deadage += age2  
        print (f'Survivor Average Age: {"{:.2f}".format(survivorage/survivors)}')  
        print (f'Non-Survivor Average Age: {"{:.2f}".format(deadage/survivors)}')

def oldestyoungest_passenger():
    with open ('titanic.csv', 'r', newline = '') as file:
        next(file)
        min_age = 200
        max_age = 0
        for line in file:
            row=line.strip().split(',')
            if row[6] != '':
                age = float(row[6])
                if age > max_age:
                    max_age = age
                elif age < min_age:
                    min_age = age
        print (f'The oldest Passenger is {max_age} years old')
        print (f'The youngest Passenger is {max_age} years old')
          

"""

GOAL 5 (Intermediate): Class-Based Analysis
--------------------------------------------
For each passenger class (1st, 2nd, 3rd):
- Calculate the survival rate
- Calculate the average fare paid
Create a summary showing which class had the best survival chances.
"""

def class_survival_rate():
    with open ('titanic.csv', 'r', newline = '') as file:
        next(file)
        survival1 = 0
        total1 = 0
        survival2 = 0
        total2 = 0
        survival3 = 0
        total3 = 0
        for line in file:
            row=line.strip().split(',')
            if row[2] == "1":
                if row[1] == "1":
                    survival1 += 1
                    total1 += 1
                else:
                    total1 += 1
            if row[2] == "2":
                if row[1] == "1":
                    survival2 += 1
                    total2 += 1
                else:
                    total2 += 1
            if row[2] == "3":
                if row[1] == "1":
                    survival3 += 1
                    total3 += 1
                else:
                    total3 += 1
        print (f'1st Class Survival Rate: {"{:.2f}".format(survival1/total1*100)}%')
        print (f'2nd Class Survival Rate: {"{:.2f}".format(survival2/total2*100)}%')
        print (f'3rd Class Survival Rate: {"{:.2f}".format(survival3/total3*100)}%')

def avg_fare_paid():
    with open ('titanic.csv', 'r', newline = '') as file:
        next(file)
        total_fairs = 0
        total_payers = 0
        for line in file:
            row=line.strip().split(',')
            number = float(row[10])
            total_fairs += number
            total_payers += 1
        print (f'Average Fairs Paid ${"{:.2f}".format(total_fairs/total_payers)}')



"""
GOAL 6 (Advanced): Family Survival Patterns
--------------------------------------------
Create a new column called 'FamilySize' (SibSp + Parch + 1).
Analyze survival rates based on family size.
Determine if traveling alone or with family improved survival chances.
"""

def family():
    with open ('titanic.csv', 'r', newline = '') as file:
        file.seek(1) 
        next(file)
        file.seek(0)
        family_size = []
        survived = 0
        survivedfam = 0
        dead = 0
        deadfam = 0

        next(file)

        for line in file:
            row = line.strip().split(',')
            nextnum = float(row[7]) + float(row[8])+1
            workbetter = str(nextnum)
            family_size.append(workbetter)
            if row[1]=="1":
                survived+=1
                survivedfam = survivedfam + nextnum
            else:
                dead+=1
                deadfam= deadfam+ nextnum
        deadfam_ave = "{:.2f}".format(deadfam/dead)
        survivedfam_ave = "{:.2f}".format(survivedfam/survived)
        if (float(deadfam_ave)+2) < float(survivedfam_ave):
            print ("the average family size for people that survived is larger than the amount of people that died")
        elif (float(survivedfam_ave)+2) < float(deadfam_ave):
            print ("the average family size for people that died is larger than the amount of people that survived't")
        else:
            print("there is little difference from the family size of the people who survived and died")

        print(f"the average family size for dead people is: {deadfam_ave}")
        print(f"the average family size for people who survived is: {survivedfam_ave}")
        return family_size, deadfam_ave, survivedfam_ave
    

def add_family_column(family_size):
    new_header_name = "family size"
    with open('titanic.csv', 'r') as infile, open('titanic.family.csv', 'w') as outfile:
        lines = infile.readlines()
        if lines:
            original_header = lines[0].strip()
            new_header_row = f"{original_header}, {new_header_name}\n"
            outfile.write(new_header_row)
        for i in range(1, len(lines)):
            original_line = lines[i].strip()
            new_value = family_size[i-1]
            modified_line = f"{original_line}, {new_value}\n"
            outfile.write(modified_line)



"""
GOAL 7 (Advanced): Data Visualization
--------------------------------------
Create at least 3 different charts:
1. Bar chart comparing survival rates by gender
2. Histogram showing age distribution
3. Bar chart showing survival rates by passenger class
(You'll need matplotlib: pip install matplotlib)

GOAL 8 (Challenge): Comprehensive Report
-----------------------------------------
Write a function that generates a complete survival analysis report including:
- Overall statistics (total passengers, survivors, survival rate)
- Breakdown by gender, class, and age group (child <18, adult 18-60, senior >60)
- Identify the profile of passengers most likely to survive (combination of features)
- Handle missing data appropriately
- Save the report to a text file

STARTER CODE TEMPLATE:
"""

#1. open your titanic.csv file and read the data
#2. do a simple statistic, like total males/females
#3. write the output to a csv
#4. move that code to a function

"""
BONUS CHALLENGES:
-----------------
- Find the most common first names among survivors
- Analyze survival rates by port of embarkation
- Investigate if cabin location affected survival
- Predict survival for a hypothetical passenger based on their attributes
"""

def main():
    first_10_rows()
    total_passengers()
    survival_percentage()
    gender_survival()
    average_age()
    age_survivor_nonsurvivor()
    oldestyoungest_passenger()
    class_survival_rate()
    avg_fare_paid()
    family_size, deadfam_ave, survivedfam_ave = family()
    add_family_column(family_size)

main()
