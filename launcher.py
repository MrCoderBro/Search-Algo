# This function loads the titanic dataset
def load_titanic(filename):

    global passenger_class
    global survival_status
    global names
    global gender
    global age
    global embarkation_loc
    global boat

#IMPORTANT

    passenger_class = []
    survival_status = []
    names = []
    gender = []
    age = []
    embarkation_loc = []
    boat = []

    record = 0

    print('The Titanic dataset is a simplified version of the dataset found from open source')
    print('Loading the titanic dataset...')

    with open(filename) as file:
        print(f'Opening {filename}. Make sure the file is in the same folder if you run into an error')
        lines = file.read().splitlines()

        first_line_skipped = False

        for line in lines:
            if not first_line_skipped:
                first_line_skipped = True
            else: 
                print(f'Loading record number {record}', end='\r')
                fields = line.split(',')
                
                passenger_class.append(fields[0])
                survival_status.append(fields[1])
                names.append(fields[2])
                gender.append(fields[3])
                age.append(fields[4])
                embarkation_loc.append(fields[5])
                boat.append(fields[6])

                record += 1

        print(f'Loading complete. {record} records loaded')

#############################
# Write your functions here #
#############################
# TODO: To add on new functionalities

# This is a sample function that displays the names of all first class passengers
# Feel free to delete this function

def survival_rate(no_of_people_survive, total_no_of_people):
    survival_rate = no_of_people_survive / total_no_of_people * 100
    return survival_rate

def split_list_into_smaller_lists(original_list):
    list = []
    for i in range(0, len(original_list)):
        #Splicing the original list and adding it to the list above
        list.append(original_list[i:i+1])
    return list

def find_index(firstname_input, lastname_input, list):
    index = 0
    for i in range(0, len(list)):
        x = names[index]
        if firstname_input in x and lastname_input in x:
            return index
        index += 1

def index_list(list1, user_input):
    index_list = []
    index = 0
    for i in list1:
        if user_input == list1[index]:
            index_list.append(index)
        index += 1
    return index_list


def index_list_v2(userslist, user_input):
    index_list_v2 = []
    index = 0
    for i in userslist:
        if user_input == '1':
            if userslist[index] == 'N.A':
                None
            elif float(userslist[index]) < 13:
                    index_list_v2.append(index)
        if user_input == '2':
            if userslist[index] == 'N.A':
                None
            elif float(userslist[index]) >= 13 and float(userslist[index]) < 35:
                    index_list_v2.append(index)
        if user_input == '3':
            if userslist[index] == 'N.A':
                None
            elif float(userslist[index]) >= 35:
                    index_list_v2.append(index)
        index += 1
    return index_list_v2


def put_into_married_list(list1):
    list = []
    index = 0
    for i in list1:
        x = names[index]
        if 'Mrs' in x:
            list.append(list1[index])
        index += 1
    return list

def put_into_notmarried_list(userslist):
    list = []
    index = 0
    for i in userslist:
        x = names[index]
        if 'Miss' in x :
            list.append(userslist[index])
        index += 1
    return list

def put_into_married_survived_list(list3):
    list = []
    index = 0
    for i in list3:
        x = names[index]
        if survival_status[index] == '1' :
            list.append(list3[index])
        index += 1
    return list

def put_into_notmarried_survived_list(list4):
    list = []
    index = 0 
    for i in list4:
        x = names[index]
        if survival_status[index] == '1' :
            list.append(list4[index])
        index += 1
    return list


def display_first_class():
    print('Displaying names of first-class passengers')
    print('==========================================')
    count = 0
    for index in range(0, len(passenger_class)):
        if passenger_class[index] == '1':
            print(names[index])
            
    print('=== End of list ===')
    print()

def display_port_table():
    #PORT S
    no_of_s_port_people_firstclass = 0
    no_of_s_port_people_secondclass = 0
    no_of_s_port_people_thirdclass = 0

    #PORT C
    no_of_c_port_people_firstclass = 0
    no_of_c_port_people_secondclass = 0
    no_of_c_port_people_thirdclass = 0

    #PORT Q
    no_of_q_port_people_firstclass = 0
    no_of_q_port_people_secondclass = 0
    no_of_q_port_people_thirdclass = 0


    # print('Displaying Table')
    # print('=========================================')

    for i in range(0, len(passenger_class)):
        #PORT S
        if embarkation_loc[i] == 'S' and passenger_class[i] == '1':
            no_of_s_port_people_firstclass += 1
        elif embarkation_loc[i] == 'S' and passenger_class[i] == '2':
            no_of_s_port_people_secondclass += 1
        elif embarkation_loc[i] == 'S' and passenger_class[i] == '3':
            no_of_s_port_people_thirdclass += 1

        #PORT C
        elif embarkation_loc[i] == 'C' and passenger_class[i] == '1':
            no_of_c_port_people_firstclass += 1
        elif embarkation_loc[i] == 'C' and passenger_class[i] == '2':
            no_of_c_port_people_secondclass += 1
        elif embarkation_loc[i] == 'C' and passenger_class[i] == '3':
            no_of_c_port_people_thirdclass += 1
        

        #PORT Q
        elif embarkation_loc[i] == 'Q' and passenger_class[i] == '1':
            no_of_q_port_people_firstclass += 1
        elif embarkation_loc[i] == 'Q' and passenger_class[i] == '2':
            no_of_q_port_people_secondclass += 1
        elif embarkation_loc[i] == 'Q' and passenger_class[i] == '3':
            no_of_q_port_people_thirdclass += 1
        
    no_of_s_port_people = no_of_s_port_people_firstclass + no_of_s_port_people_secondclass + no_of_s_port_people_thirdclass
    no_of_c_port_people = no_of_c_port_people_firstclass + no_of_c_port_people_secondclass + no_of_c_port_people_thirdclass
    no_of_q_port_people = no_of_q_port_people_firstclass + no_of_q_port_people_secondclass + no_of_q_port_people_thirdclass

    print(f"no_of_s_port_people_firstclass: {no_of_s_port_people_firstclass}")
    print(f"no_of_s_port_people_secondclass: {no_of_s_port_people_secondclass}")
    print(f"no_of_s_port_people_thirdclass: {no_of_s_port_people_thirdclass}")

    print(f"no_of_c_port_people_firstclass: {no_of_c_port_people_firstclass}")
    print(f"no_of_c_port_people_secondclass: {no_of_c_port_people_secondclass}")
    print(f"no_of_c_port_people_thirdclass: {no_of_c_port_people_thirdclass}")

    print(f"no_of_q_port_people_firstclass: {no_of_q_port_people_firstclass}")
    print(f"no_of_q_port_people_secondclass: {no_of_q_port_people_secondclass}")
    print(f"no_of_q_port_people_thirdclass: {no_of_q_port_people_thirdclass}")

    print(f"no_of_s_port_people: {no_of_s_port_people}")
    print(f"no_of_c_port_people: {no_of_c_port_people}")
    print(f"no_of_q_port_people: {no_of_q_port_people}")

def find_person_details():
    #Purpose: Helps the user to find the details of someone who they want to know the details of without looking through the entire excel spreadsheet. Saving time
    firstname_input = input("What is the person's first name?")
    lastname_input = input("What is the person's last name?")
    list = split_list_into_smaller_lists(names)
    index = find_index(firstname_input, lastname_input, list)
    print("--Generating Details--")
    print(f"Full name: {names[index]}, \n" )
    print(f"Passenger Class: {passenger_class[index]}, \n")
    print(f"Gender: {gender[index]}, \n")
    print(f"Age: {age[index]}, \n")
    print(f"Embarkation location: {embarkation_loc[index]}, \n")
    print(f"Survival Status(1- Survived, 0- Did not survive): {survival_status[index]} \n")

def option_5():
    split_list = split_list_into_smaller_lists(names)
    married_woman_list = put_into_married_list(split_list)
    not_married_woman_list = put_into_notmarried_list(split_list)
    married_woman_survived_list = put_into_married_survived_list(married_woman_list)
    notmarried_woman_survived_list = put_into_notmarried_survived_list(not_married_woman_list)

    number_of_married_woman_total = len(married_woman_list)
    number_of_notmarried_woman_total = len(not_married_woman_list)
    number_of_married_woman_survived = len(married_woman_survived_list)
    number_of_notmarried_woman_survived = len(notmarried_woman_survived_list)
    
    survival_rate_married_woman = survival_rate(number_of_married_woman_survived, number_of_married_woman_total)
    survival_rate_notmarried_woman = survival_rate(number_of_notmarried_woman_survived, number_of_notmarried_woman_total)

    print(f"Survival rate of married woman = {survival_rate_married_woman}%")
    print(f"Survival rate of not married woman = {survival_rate_notmarried_woman}%")
    print("")
    print("We can conclude that if a woman is married, they have a higher chance to survive")
    print("")


##Jovan's code below

def mortality_rate(passenger,surv):
    mort = passenger - surv
    rate = mort / passenger * 100
    return rate

def first_class_survival_age():
    survage13 = 0
    survage35 = 0
    survagem35 = 0
    # for i in range(len(age)):
    #     if len(age[i]) == 0:
    #         print("N.A")
    #     else:
    #         print(float(age[i]))
    ages = []
    ages_final = []
    for i in range (len(age)):
        if len(age[i]) == 0:
            ages.append(age[i])
        else:
            ages.append(age[i])
    for i in range (0,len(ages)):
        if ages[i] != "":
            ages_final.append(ages[i])
    # print(ages_final)
    for i in range (0,len(ages_final)):
        compare = ages_final[i]
        if float(compare) <= 13:
            survage13 += 1
        if float(compare) > 13 and float(compare) <= 35:
            survage35 += 1
        if float(compare) > 35:
            survagem35 += 1
    # for i in range (0,len(age)):
    #     if len(age[i]) > 0 :
    #         for i in range (0,len(passenger_class)):
    #             if survival_status[i] == '1' and float(age[i]) <= 13 and passenger_class[i] == '1':
    #                 survage13 += 1
    #         for i in range (0,len(passenger_class)):
    #             if survival_status[i] == '1' and float(age[i]) > 13 and age <= 35 and passenger_class[i] == '1':
    #                 survage35 += 1
    #         for i in range (0,len(passenger_class)):
    #             if survival_status[i] == '1' and float(age[i]) > 35 and passenger_class[i] == '1':
    #                 survagem35 += 1
    print(f'Survivors Below 13 {survage13}')
    print(f'Survivors Above 13 and Below 35 {survage35}')
    print(f'Survivors Above 35 {survagem35}')

def first_class_survival_boat():
    print(f'Displaying survival status and boat of first-class passengers')
    print('==============================================================')
    for i in range(0, len(passenger_class)):
        if survival_status[i] == '1' and passenger_class[i] == '1':
            print(names[i] + ' ' + survival_status[i]+ ',' + boat[i])
    fcount = 0
    scount = 0
    tcount = 0
    for i in range (0,len(passenger_class)):
        if survival_status[i] == '1' and passenger_class[i] == '1':
            fcount += 1
    for i in range (0,len(passenger_class)):
        if survival_status[i] == '1' and passenger_class[i] == '2':
            scount += 1
    for i in range (0,len(passenger_class)):
        if survival_status[i] == '1' and passenger_class[i] == '3':
            tcount += 1
    print(f'Total survivors in first-class {fcount} vs second-class {scount} vs third-class {tcount}')
    fpass = 0
    spass = 0
    tpass = 0
    for i in range (0,len(passenger_class)):
        if passenger_class[i] == '1':
            fpass += 1
    for i in range (0,len(passenger_class)):
        if passenger_class[i] == '2':
            spass += 1
    for i in range (0,len(passenger_class)):
        if passenger_class[i] == '3':
            tpass += 1
    fmort = mortality_rate(fpass,fcount)
    smort = mortality_rate(spass,scount)
    tmort = mortality_rate(tpass,tcount)
    print(f'Mortality Rates between classes first-class {fmort:.2f}%, second-class {smort:.2f}%, third-class {tmort:.2f}%')




## Most of the functions below is used in the search algo
## Jayden Part
def search_passengerclass():
    index_passenger_class_list = []
    passlist = []
    surstatlist = []
    namelist = []
    genderlist = []
    agelist = []
    emblist = []
    boatlist = []

    #While loop to make sure that the user keys in the correct value
    user_input = ''
    while user_input != '1' or '2' or '3':
        user_input = input(f'To classify by class, please input the class number(1, 2, or 3): ')
        user_input.lower()
        if user_input == '1':
            print(f'Displaying info of all first class passengers')
            break
        elif user_input == '2':
            print(f'Displaying info of all second class passengers')
            break
        elif user_input == '3':
            print(f'Displaying info of all third class passengers')
            break
        else:
            print(f'Invalid gender')

    index_passenger_class_list  =  index_list(passenger_class, user_input)
    print(" ")

    #Appending all the values into the list
    for i in index_passenger_class_list:
        passlist.append(passenger_class[i])
        surstatlist.append(survival_status[i])
        namelist.append(names[i])
        genderlist.append(gender[i])
        agelist.append(age[i])
        emblist.append(embarkation_loc[i])
        boatlist.append(boat[i])
    
    #Display All Of The Details
    print("Passenger Class  Survival Status( 1-Survived  0-Didn't Survive )  Name  Gender  Age  EmbarkationLocation  Boat")
    print(" ")

    index = 0
    for i in index_passenger_class_list:
        print(f"{passlist[index]}  {surstatlist[index]}  {namelist[index]}  {genderlist[index]}  {agelist[index]}  {embarkation_loc[index]}  {boatlist[index]}")
        index += 1

    return index_passenger_class_list


#Jayden
def search_surname():
    surname_list = []
    surname_list_final = []
    index_list = []
    passlist = []
    surstatlist = []
    namelist = []
    genderlist = []
    agelist = []
    emblist = []
    boatlist = []


    user_input = input("Please type in the surname that you would like to search for(You can also put in a letter to find the surname that all starts with that letter): ")

    # CUT THE NAME INTO SURNAMES AND NAMES
    for i in names:
        list1 = []
        for j in i.split(" - "):
            list1.append(j)
        surname_list.append(list1)
    
    # CUT AWAY THE NAME
    for i in surname_list:
        surname_list_final.append(i[:1])
    
    # GET THE INDEXES
    index = 0
    for i in surname_list_final:
        x = surname_list_final[index]
        if user_input in x[0]:
            index_list.append(index)
        index += 1
    
    #Appending all the values into the list
    for i in index_list:
        passlist.append(passenger_class[i])
        surstatlist.append(survival_status[i])
        namelist.append(names[i])
        genderlist.append(gender[i])
        agelist.append(age[i])
        emblist.append(embarkation_loc[i])
        boatlist.append(boat[i])

    
    #Display All Of The Details
    print("Passenger Class  Survival Status( 1-Survived  0-Didn't Survive )  Name  Gender  Age  EmbarkationLocation  Boat")
    print(" ")

    index = 0
    for i in index_list:
        print(f"{passlist[index]}  {surstatlist[index]}  {namelist[index]}  {genderlist[index]}  {agelist[index]}  {embarkation_loc[index]}  {boatlist[index]}")
        index += 1

    return index_list


## JOVANS PART
def search_gender():
    gender_search = ''
    while gender_search != 'male' or 'female':
        gender_search = input(f'Please Input the gender you are searching for (female/male): ')
        gender_search.lower()
        if gender_search == 'male':
            print(f'Displaying info of all male passengers')
            break
        elif gender_search == 'female':
            print(f'Displaying info of all female passengers')
            break
        else:
            print(f'Invalid gender')
    class_info_gender = []
    survival_info_gender = []
    names_info_gender = []
    gender_info = []
    ages_info_gender = []
    embark_info_gender = []
    boat_info_gender = []
    # for i in range(0, len(passenger_class)):
    #     if gender[i] == gender_search:
    #         class_info_gender.append(passenger_class[i])
    #         survival_info_gender.append(survival_status[i])
    #         names_info_gender.append(names[i])
    #         gender_info.append(gender[i])
    #         ages_info_gender.append(age[i])
    #         embark_info_gender.append(embarkation_loc[i])
    #         boat_info_gender.append(boat[i])
    x = index_list(gender, gender_search)
    for i in x:
            class_info_gender.append(passenger_class[i])
            survival_info_gender.append(survival_status[i])
            names_info_gender.append(names[i])
            gender_info.append(gender[i])
            ages_info_gender.append(age[i])
            embark_info_gender.append(embarkation_loc[i])
            boat_info_gender.append(boat[i])
    print(x)
    print('')
    print('Passenger Class  Survival Status  Names  Ages  Gender  Embarked Location  Boat')
    print('')
    index = 0
    for i in x:
        print(f'{class_info_gender[index]}  {survival_info_gender[index]}  {names_info_gender[index]}  {gender_info[index]}  {ages_info_gender[index]}  {embark_info_gender[index]}  {boat_info_gender[index]}')
        index += 1    
    
    return x

#JOVAN

def search_age():
        ages = []
        for i in range (0, len(passenger_class)):
            if len(age[i]) == 0:
                ages.append('N.A')
            else:
                ages.append(age[i])
        class_info_age = []
        survival_info_age = []
        names_info_age = []
        gender_info_age = []
        ages_info = []
        embark_info_age = []
        boat_info_age = []
        age_search = ''
        while age_search != '1' or '2' or '3':
            print('(1) Below 13')
            print('(2) Above 13 but Below 35')
            print('(3) Above 35')
            age_search = input(f'Please select the age group: ')
            if age_search == '1':
                print('Displaying all passengers under the age of 13')
                break
            if age_search == '2':
                print('Displaying all passengers above the age 13 but below the age of 35')
                break
            if age_search == '3':
                print('Displaying all passengers above the age of 35')
                break
            else:
                print(f'Invalid Option')
        x = index_list_v2(ages, age_search)
        print(x)
        for i in x:
            class_info_age.append(passenger_class[i])
            survival_info_age.append(survival_status[i])
            names_info_age.append(names[i])
            gender_info_age.append(gender[i])
            ages_info.append(age[i])
            embark_info_age.append(embarkation_loc[i])
            boat_info_age.append(boat[i])
        # print(x)
        print("")
        print('Passenger Class  Survival Status  Names  Ages  Gender  Embarked Location  Boat')
        print("")
        index = 0
        for i in x:
            print(f'{class_info_age[index]}  {survival_info_age[index]}  {names_info_age[index]}  {gender_info_age[index]}  {ages_info[index]}  {embark_info_age[index]}  {boat_info_age[index]}')
            index += 1

        return x
            # if age_search == '1':
            #     if ages[i] == 'N.A':
            #         None
            #     else:
            #         if float(ages[i]) < 13:
            #             print(f'{class_info_age[i]}  {survival_info_age[i]}  {names_info_age[i]}  {gender_info_age[i]}  {ages_info[i]}  {embark_info_age[i]}  {boat_info_age[i]}')
            # elif age_search == '2':
            #     if ages[i] == 'N.A':
            #         None
            #     else:
            #         if float(ages[i]) >= 13 and float(ages[i]) < 35:
            #             print(f'{class_info_age[i]}  {survival_info_age[i]}  {names_info_age[i]}  {gender_info_age[i]}  {ages_info[i]}  {embark_info_age[i]}  {boat_info_age[i]}')
            # else: 
            #     if ages[i] == 'N.A':
            #         None
            #     else:
            #         if float(ages[i]) >= 35:
            #             print(f'{class_info_age[i]}  {survival_info_age[i]}  {names_info_age[i]}  {gender_info_age[i]}  {ages_info[i]}  {embark_info_age[i]}  {boat_info_age[i]}')

#Jayden
def search_survivalstat():
    index_survivalstat_list = []
    passlist = []
    surstatlist = []
    namelist = []
    genderlist = []
    agelist = []
    emblist = []
    boatlist = []

    #While loop to make sure user keys in correctly
    user_input = ''
    while user_input != '1' or '0':
        user_input = input(f'To classify by survival status, please input the survival status number(1-Survived, 0-Did not survive): ')
        user_input.lower()
        if user_input == '1':
            print(f'Displaying info of all survived passengers')
            break
        elif user_input == '0':
            print(f'Displaying info of all dead passengers')
            break
        else:
            print(f'Invalid option')
    

    index_survivalstat_list  =  index_list(survival_status, user_input)
    print(" ")

    #Appending all the values into the list
    for i in index_survivalstat_list:
        passlist.append(passenger_class[i])
        surstatlist.append(survival_status[i])
        namelist.append(names[i])
        genderlist.append(gender[i])
        agelist.append(age[i])
        emblist.append(embarkation_loc[i])
        boatlist.append(boat[i])
    
    #Display All Of The Details
    print("Passenger Class  Survival Status( 1-Survived  0-Didn't Survive )  Name  Gender  Age  EmbarkationLocation  Boat")
    print(" ")

    index = 0
    for i in index_survivalstat_list:
        print(f"{passlist[index]}  {surstatlist[index]}  {namelist[index]}  {genderlist[index]}  {agelist[index]}  {embarkation_loc[index]}  {boatlist[index]}")
        index += 1
    
    return index_survivalstat_list

#Jayden
def search_embarklocation():
    index_embarkloc_list = []
    passlist = []
    surstatlist = []
    namelist = []
    genderlist = []
    agelist = []
    emblist = []
    boatlist = []

    #While loop to make sure user keys in correctly
    user_input = ''
    while user_input != 'C' or 'Q' or 'S':
        user_input = input(f'To classify by embarkation location, please input the assigned letters(C: Cherbourg, Q: Queenstown, S: Southampton): ')
        if user_input == 'C':
            print(f'Displaying info of all passengers who embarked at Cherbourg')
            break
        elif user_input == 'Q':
            print(f'Displaying info of all passengers who embarked at Queenstown')
            break
        elif user_input == 'S':
            print(f'Displaying info of all passengers who embarked at Southampton')
        else:
            print(f'Invalid option')
    

    index_embarkloc_list  =  index_list(embarkation_loc, user_input)
    print(" ")

    #Appending all the values into the list
    for i in index_embarkloc_list:
        passlist.append(passenger_class[i])
        surstatlist.append(survival_status[i])
        namelist.append(names[i])
        genderlist.append(gender[i])
        agelist.append(age[i])
        emblist.append(embarkation_loc[i])
        boatlist.append(boat[i])
    
    #Display All Of The Details
    print("Passenger Class  Survival Status( 1-Survived  0-Didn't Survive )  Name  Gender  Age  EmbarkationLocation  Boat")
    print(" ")

    index = 0
    for i in index_embarkloc_list:
        print(f"{passlist[index]}  {surstatlist[index]}  {namelist[index]}  {genderlist[index]}  {agelist[index]}  {emblist[index]}  {boatlist[index]}")
        index += 1
    
    return index_embarkloc_list


def search_boat():
        boat_info = []
        # for i in range (0, len(passenger_class)):
        #     if len(boat[i]) == 0:
        #         boat.append('N.A')
        #     elif len(boat[i]) == 'A':
        #         boat.append('A')
        #     elif len(boat[i]) == 'B':
        #         boat.append('B')
        #     elif len(boat[i]) == 'C':
        #         boat.append('C')
        #     elif len(boat[i]) == 'D':
        #         boat.append('D')
        #     else:
        #         boat.append(boat[i])
        class_info_boat = []
        survival_info_boat = []
        names_info_boat = []
        gender_info_boat = []
        ages_info_boat = []
        embark_info_boat = []
        boat_info = []
        boat_whom = '1'
        user_input = ''
        while user_input != 'digits' or user_input != 'letters':     
            user_input = input('Would you like to search by digits or letters: ')
            if user_input == 'digits':
                while int(boat_whom) > 0 or int(boat_whom) < 16:
                    boat_whom = input(f'Please input the identity of the boat (1-16): ')
                    break
                else:
                    print('Invalid Boat ID')
            elif user_input == 'letters':
                while boat_whom != 'A' or boat_whom != 'B' or boat_whom != 'C' or boat_whom != 'D':
                    boat_whom = input(f'Please input the identity of the boat (A/B/C/D): ')
                    break
                else:
                    print('Invalid Boat ID')
            else:
                print('Invalid Search')
            break
        x = index_list(boat, boat_whom)
        print(x)
        print(passenger_class[11])
        for i in x:
            class_info_boat.append(passenger_class[i])
            survival_info_boat.append(survival_status[i])
            names_info_boat.append(names[i])
            gender_info_boat.append(gender[i])
            ages_info_boat.append(age[i])
            embark_info_boat.append(embarkation_loc[i])
            boat_info.append(boat[i])
        print("")
        print('Passenger Class  Survival Status  Names  Ages  Gender  Embarked Location  Boat')
        print("")
        index = 0
        for i in x:
            print(f'{class_info_boat[index]}  {survival_info_boat[index]}  {names_info_boat[index]}  {gender_info_boat[index]}  {ages_info_boat[index]}  {embark_info_boat[index]}  {boat_info[index]}')
            index += 1

        return x
        #     if boat_info == 'A':
        #         if boat_info == 'N.A':
        #             None
        #         elif boat_whom == 'A':
        #             print(f'{class_info_boat[i]}  {survival_info_boat[i]}  {names_info_boat[i]}  {gender_info_boat[i]}  {ages_info_boat[i]}  {embark_info_boat[i]}  {boat_info[i]}')
        #     elif boat_info == 'B':
        #         if boat_info == 'N.A':
        #             None
        #         elif boat_whom == 'B':
        #             print(f'{class_info_boat[i]}  {survival_info_boat[i]}  {names_info_boat[i]}  {gender_info_boat[i]}  {ages_info_boat[i]}  {embark_info_boat[i]}  {boat_info[i]}')
        #     elif boat_info == 'C':
        #         if boat_info == 'N.A':
        #             None
        #         elif boat_whom == 'C':
        #             print(f'{class_info_boat[i]}  {survival_info_boat[i]}  {names_info_boat[i]}  {gender_info_boat[i]}  {ages_info_boat[i]}  {embark_info_boat[i]}  {boat_info[i]}')
        #     elif boat_info == 'D':
        #         if boat_info == 'N.A':
        #             None
        #         elif boat_whom == 'D': 
        #             print(f'{class_info_boat[i]}  {survival_info_boat[i]}  {names_info_boat[i]}  {gender_info_boat[i]}  {ages_info_boat[i]}  {embark_info_boat[i]}  {boat_info[i]}')
        #     elif boat_whom == boat[i]:
        #         if boat_info == 'N.A':
        #             None
        #         else: 
        #             print(f'{class_info_boat[i]}  {survival_info_boat[i]}  {names_info_boat[i]}  {gender_info_boat[i]}  {ages_info_boat[i]}  {embark_info_boat[i]}  {boat_info[i]}')
        # search_algo()


## Functions used to further classify the data after the first classification
def index_list_passenger_filtered(userslist, user_input):
    passenger_classes_filtered_list = []
    index_passenger_class_list = []
    for i in userslist:
        passenger_classes_filtered_list.append(passenger_class[i])

    #appends the indexes in the userslist into the final index_passenger_class_list
    index = 0
    for j in passenger_classes_filtered_list:
        if j == user_input:
            index_passenger_class_list.append(userslist[index])
        index += 1

    return index_passenger_class_list


def search_passenger_class_filtered(userslist):

    index_passenger_class_list = []
    passlist = []
    surstatlist = []
    namelist = []
    genderlist = []
    agelist = []
    emblist = []
    boatlist = []

    #While loop to make sure that the user keys in the correct value
    user_input = ''
    while user_input != '1' or '2' or '3':
        user_input = input(f'To classify by class, please input the class number(1, 2, or 3): ')
        user_input.lower()
        if user_input == '1':
            print(f'Displaying info of all first class passengers')
            break
        elif user_input == '2':
            print(f'Displaying info of all second class passengers')
            break
        elif user_input == '3':
            print(f'Displaying info of all third class passengers')
            break
        else:
            print(f'Invalid option')

    index_passenger_class_list  =  index_list_passenger_filtered(userslist, user_input)
    print(index_passenger_class_list)
    print(" ")

    #Appending all the values into the list
    for i in index_passenger_class_list:
        passlist.append(passenger_class[i])
        surstatlist.append(survival_status[i])
        namelist.append(names[i])
        genderlist.append(gender[i])
        agelist.append(age[i])
        emblist.append(embarkation_loc[i])
        boatlist.append(boat[i])
    
    #Display All Of The Details
    print("Passenger Class  Survival Status( 1-Survived  0-Didn't Survive )  Name  Gender  Age  EmbarkationLocation  Boat")
    print(" ")

    index = 0
    for i in index_passenger_class_list:
        print(f"{passlist[index]}  {surstatlist[index]}  {namelist[index]}  {genderlist[index]}  {agelist[index]}  {embarkation_loc[index]}  {boatlist[index]}")
        index += 1


def index_list_gender_filtered(userslist, user_input):
    gender_classes_filtered_list = []
    index_gender_class_list = []
    for i in userslist:
        gender_classes_filtered_list.append(gender[i])

    #appends the indexes in the userslist into the final index_passenger_class_list
    index = 0
    for j in gender_classes_filtered_list:
        if j == user_input:
            index_gender_class_list.append(userslist[index])
        index += 1

    return index_gender_class_list


def search_gender_filtered(userslist):
    gender_search = ''
    while gender_search != 'male' or 'female':
        gender_search = input(f'Please Input the gender you are searching for (female/male): ')
        gender_search.lower()
        if gender_search == 'male':
            print(f'Displaying info of all male passengers')
            break
        elif gender_search == 'female':
            print(f'Displaying info of all female passengers')
            break
        else:
            print(f'Invalid gender')
    class_info_gender = []
    survival_info_gender = []
    names_info_gender = []
    gender_info = []
    ages_info_gender = []
    embark_info_gender = []
    boat_info_gender = []
    # for i in range(0, len(passenger_class)):
    #     if gender[i] == gender_search:
    #         class_info_gender.append(passenger_class[i])
    #         survival_info_gender.append(survival_status[i])
    #         names_info_gender.append(names[i])
    #         gender_info.append(gender[i])
    #         ages_info_gender.append(age[i])
    #         embark_info_gender.append(embarkation_loc[i])
    #         boat_info_gender.append(boat[i])
    x = index_list_gender_filtered(userslist, gender_search)
    for i in x:
            class_info_gender.append(passenger_class[i])
            survival_info_gender.append(survival_status[i])
            names_info_gender.append(names[i])
            gender_info.append(gender[i])
            ages_info_gender.append(age[i])
            embark_info_gender.append(embarkation_loc[i])
            boat_info_gender.append(boat[i])
    print(x)
    print('')
    print('Passenger Class  Survival Status  Names  Ages  Gender  Embarked Location  Boat')
    print('')
    index = 0
    for i in x:
        print(f'{class_info_gender[index]}  {survival_info_gender[index]}  {names_info_gender[index]}  {gender_info[index]}  {ages_info_gender[index]}  {embark_info_gender[index]}  {boat_info_gender[index]}')
        index += 1    
    
    return x


def index_list_survstat_filtered(userslist, user_input):
    survstat_classes_filtered_list = []
    index_survstat_class_list = []
    for i in userslist:
        survstat_classes_filtered_list.append(survival_status[i])

    #appends the indexes in the userslist into the final index_passenger_class_list
    index = 0
    for j in survstat_classes_filtered_list:
        if j == user_input:
            index_survstat_class_list.append(userslist[index])
        index += 1

    return index_survstat_class_list


def search_survstat_filtered(userslist):
    index_survivalstat_list = []
    passlist = []
    surstatlist = []
    namelist = []
    genderlist = []
    agelist = []
    emblist = []
    boatlist = []

    #While loop to make sure user keys in correctly
    user_input = ''
    while user_input != '1' or '0':
        user_input = input(f'To classify by survival status, please input the survival status number(1-Survived, 0-Did not survive): ')
        user_input.lower()
        if user_input == '1':
            print(f'Displaying info of all survived passengers')
            break
        elif user_input == '0':
            print(f'Displaying info of all dead passengers')
            break
        else:
            print(f'Invalid option')
    

    index_survivalstat_list  =  index_list_survstat_filtered(userslist, user_input)
    print(" ")

    #Appending all the values into the list
    for i in index_survivalstat_list:
        passlist.append(passenger_class[i])
        surstatlist.append(survival_status[i])
        namelist.append(names[i])
        genderlist.append(gender[i])
        agelist.append(age[i])
        emblist.append(embarkation_loc[i])
        boatlist.append(boat[i])
    
    #Display All Of The Details
    print("Passenger Class  Survival Status( 1-Survived  0-Didn't Survive )  Name  Gender  Age  EmbarkationLocation  Boat")
    print(" ")

    index = 0
    for i in index_survivalstat_list:
        print(f"{passlist[index]}  {surstatlist[index]}  {namelist[index]}  {genderlist[index]}  {agelist[index]}  {embarkation_loc[index]}  {boatlist[index]}")
        index += 1
    
    return index_survivalstat_list


def index_list_boat_filtered(userslist,user_input):
    boat_filtered_list = []
    index_boat_list = []
    for i in userslist:
        boat_filtered_list.append(boat[i])

    #appends the indexes in the userslist into the final index_passenger_class_list
    index = 0
    for j in boat_filtered_list:
        if j == user_input:
            index_boat_list.append(userslist[index])
        index += 1

    return index_boat_list


def search_boat_filtered(userslist):
        boat_info = []
        # for i in range (0, len(passenger_class)):
        #     if len(boat[i]) == 0:
        #         boat.append('N.A')
        #     elif len(boat[i]) == 'A':
        #         boat.append('A')
        #     elif len(boat[i]) == 'B':
        #         boat.append('B')
        #     elif len(boat[i]) == 'C':
        #         boat.append('C')
        #     elif len(boat[i]) == 'D':
        #         boat.append('D')
        #     else:
        #         boat.append(boat[i])
        class_info_boat = []
        survival_info_boat = []
        names_info_boat = []
        gender_info_boat = []
        ages_info_boat = []
        embark_info_boat = []
        boat_info = []
        boat_whom = '1'
        user_input = ''
        while user_input != 'digits' or user_input != 'letters':     
            user_input = input('Would you like to search by digits or letters: ')
            if user_input == 'digits':
                while int(boat_whom) > 0 or int(boat_whom) < 16:
                    boat_whom = input(f'Please input the identity of the boat (1-16): ')
                    break
                else:
                    print('Invalid Boat ID')
            elif user_input == 'letters':
                while boat_whom != 'A' or boat_whom != 'B' or boat_whom != 'C' or boat_whom != 'D':
                    boat_whom = input(f'Please input the identity of the boat (A/B/C/D): ')
                    break
                else:
                    print('Invalid Boat ID')
            else:
                print('Invalid Search')
            break
        x = index_list_boat_filtered(userslist, boat_whom)
        print(x)
        print(passenger_class[11])
        for i in x:
            class_info_boat.append(passenger_class[i])
            survival_info_boat.append(survival_status[i])
            names_info_boat.append(names[i])
            gender_info_boat.append(gender[i])
            ages_info_boat.append(age[i])
            embark_info_boat.append(embarkation_loc[i])
            boat_info.append(boat[i])
        print("")
        print('Passenger Class  Survival Status  Names  Ages  Gender  Embarked Location  Boat')
        print("")
        index = 0
        for i in x:
            print(f'{class_info_boat[index]}  {survival_info_boat[index]}  {names_info_boat[index]}  {gender_info_boat[index]}  {ages_info_boat[index]}  {embark_info_boat[index]}  {boat_info[index]}')
            index += 1

        return x


def index_list_surname_filtered(userslist, user_input):
    surname_filtered_list = []
    index_surname_list = []
    for i in userslist:
        surname_filtered_list.append(names[i])
    index = 0
    for j in surname_filtered_list:
        if j == user_input:
            index_surname_list.append(userslist[index])
        index += 1

    return index_surname_list


def search_surname_filtered(userslist):
    surname_list = []
    surname_list_final = []
    index_list = []
    passlist = []
    surstatlist = []
    namelist = []
    genderlist = []
    agelist = []
    emblist = []
    boatlist = []


    user_input = input("Please type in the surname that you would like to search for(You can also put in a letter to find the surname that all starts with that letter): ")

    # CUT THE NAME INTO SURNAMES AND NAMES
    for i in userslist:
        list1 = []
        for j in names[i].split(" - "):
            list1.append(j)
        surname_list.append(list1)
    
    # CUT AWAY THE NAME
    for i in surname_list:
        surname_list_final.append(i[:1])
    
    # GET THE INDEXES
    index = 0
    for i in surname_list_final:
        if user_input in i[0]:
            index_list.append(index)
        index += 1

    #Appending all the values into the list
    for i in index_list:
        passlist.append(passenger_class[i])
        surstatlist.append(survival_status[i])
        namelist.append(names[i])
        genderlist.append(gender[i])
        agelist.append(age[i])
        emblist.append(embarkation_loc[i])
        boatlist.append(boat[i])

    
    #Display All Of The Details
    print("Passenger Class  Survival Status( 1-Survived  0-Didn't Survive )  Name  Gender  Age  EmbarkationLocation  Boat")
    print(" ")

    index = 0
    for i in index_list:
        print(f"{passenger_class[i]}  {survival_status[i]}  {names[i]}  {gender[i]}  {age[i]}  {embarkation_loc[i]}  {boat[i]}")
        index += 1

    return index_list

def index_list_age_filtered(userslist, user_input):
    
    ageuserslist = []
    for i in range(0, len(userslist)):
        if age[userslist[i]] == '':
            ageuserslist.append('N.A')
        else:
            ageuserslist.append(age[userslist[i]])

    index_age_list = []


    index = 0

    for i in userslist:
        if user_input == '1':
            if ageuserslist[index] == 'N.A':
                None
            elif float(ageuserslist[index]) < 13:
                    index_age_list.append(userslist[index])
        if user_input == '2':
            if ageuserslist[index] == 'N.A':
                None
            elif float(ageuserslist[index]) >= 13 and float(ageuserslist[index]) < 35:
                    index_age_list.append(userslist[index])
        if user_input == '3':
            if ageuserslist[index] == 'N.A':
                None
            elif float(ageuserslist[index]) >= 35:
                    index_age_list.append(userslist[index])
        index += 1

    return index_age_list


def search_age_filtered(userslist):
        ages = []
        for i in range (0, len(passenger_class)):
            if len(age[i]) == 0:
                ages.append('N.A')
            else:
                ages.append(age[i])
        class_info_age = []
        survival_info_age = []
        names_info_age = []
        gender_info_age = []
        ages_info = []
        embark_info_age = []
        boat_info_age = []
        age_search = ''
        while age_search != '1' or '2' or '3':
            print('(1) Below 13')
            print('(2) Above 13 but Below 35')
            print('(3) Above 35')
            age_search = input(f'Please select the age group: ')
            if age_search == '1':
                print('Displaying all passengers under the age of 13')
                break
            if age_search == '2':
                print('Displaying all passengers above the age 13 but below the age of 35')
                break
            if age_search == '3':
                print('Displaying all passengers above the age of 35')
                break
            else:
                print(f'Invalid Option')
        x = index_list_age_filtered(userslist, age_search)
        for i in x:
            class_info_age.append(passenger_class[i])
            survival_info_age.append(survival_status[i])
            names_info_age.append(names[i])
            gender_info_age.append(gender[i])
            ages_info.append(age[i])
            embark_info_age.append(embarkation_loc[i])
            boat_info_age.append(boat[i])
        # print(x)
        print("")
        print('Passenger Class  Survival Status  Names  Ages  Gender  Embarked Location  Boat')
        print("")
        index = 0
        for i in x:
            print(f'{class_info_age[index]}  {survival_info_age[index]}  {names_info_age[index]}  {gender_info_age[index]}  {ages_info[index]}  {embark_info_age[index]}  {boat_info_age[index]}')
            index += 1

        return x


def index_list_embark_loc_filtered(userslist, userinput):
    #userslist = index list
    embark_loc_filtered_list = []
    index_embark_loc_list = []
    for i in userslist:
        embark_loc_filtered_list.append(embarkation_loc[i])

    index = 0

    for i in embark_loc_filtered_list:
        if i == userinput:
            index_embark_loc_list.append(userslist[index])
        index += 1

    return index_embark_loc_list


def search_embarklocation_filtered(userslist):
    index_embarkloc_list = []
    passlist = []
    surstatlist = []
    namelist = []
    genderlist = []
    agelist = []
    emblist = []
    boatlist = []

    #While loop to make sure user keys in correctly
    user_input = ''
    while user_input != 'C' or 'Q' or 'S':
        user_input = input(f'To classify by embarkation location, please input the assigned letters(C: Cherbourg, Q: Queenstown, S: Southampton): ')
        if user_input == 'C':
            print(f'Displaying info of all passengers who embarked at Cherbourg')
            break
        elif user_input == 'Q':
            print(f'Displaying info of all passengers who embarked at Queenstown')
            break
        elif user_input == 'S':
            print(f'Displaying info of all passengers who embarked at Southampton')
        else:
            print(f'Invalid option')
    

    index_embarkloc_list  =  index_list_embark_loc_filtered(userslist, user_input)
    print(" ")

    #Appending all the values into the list
    for i in index_embarkloc_list:
        passlist.append(passenger_class[i])
        surstatlist.append(survival_status[i])
        namelist.append(names[i])
        genderlist.append(gender[i])
        agelist.append(age[i])
        emblist.append(embarkation_loc[i])
        boatlist.append(boat[i])
    
    #Display All Of The Details
    print("Passenger Class  Survival Status( 1-Survived  0-Didn't Survive )  Name  Gender  Age  EmbarkationLocation  Boat")
    print(" ")

    index = 0
    for i in index_embarkloc_list:
        print(f"{passlist[index]}  {surstatlist[index]}  {namelist[index]}  {genderlist[index]}  {agelist[index]}  {emblist[index]}  {boatlist[index]}")
        index += 1
    
    return index_embarkloc_list



def search_algo_filter(a,user_input):
    print("----------------------------------------------------------")
    check = input('1. [Use filter function] or Q. [Go back to the start]: ')
    if check == '1':
        None
    elif check == 'q' or check == 'Q':
        search_algo()
    list_of_options = ['1','2','3','4','5','6','7','q','Q']
    if check == "1":
        # a = search_passengerclass()
        while check != 'q' or check == '1':
            print('(1. [Passenger Class] 2. [Surname] 3. [Gender] 4. [Age] 5. [Survival Status] 6. [Embarkation Location] 7.[Boat they used to get off] OR [Q] to quit)')
            check = input('Which other category would you like to search: ')
            if check not in list_of_options:
                print("You did not enter a valid option! Please try again.")
            elif check in list_of_options:
                if check == user_input:
                    print("You entered the same category, please try again")
                elif check == '1':
                    a = search_passenger_class_filtered(a)
                    check = input("Would you like to continue? (1. Continue or 2. Q to quit): ").lower
                    if check == 'q':
                        break
                elif check == '2':
                    a = search_surname_filtered(a)
                    check = input("Would you like to continue? (1. Continue or 2. Q to quit): ").lower
                    if check == 'q':
                        break
                elif check == '3':
                    a = search_gender_filtered(a)
                    check = input("Would you like to continue? (1. Continue or 2. Q to quit): ").lower
                    if check == 'q':
                        break
                elif check == '4':
                    a = search_age_filtered(a)
                    check = input("Would you like to continue? (1. Continue or 2. Q to quit): ").lower
                    if check == 'q':
                        break
                elif check == '5':
                    a = search_survstat_filtered(a)
                    check = input("Would you like to continue? (1. Continue or 2. Q to quit): ").lower
                    if check == 'q':
                        break
                elif check == '6':
                    a = search_embarklocation_filtered(a)
                    check = input("Would you like to continue? (1. Continue or 2. Q to quit): ").lower
                    if check == 'q':
                        break
                elif check == '7':
                    a = search_boat_filtered(a)
                    check = input("Would you like to continue? (1. Continue or 2. Q to quit): ").lower
                    if check == 'q':
                        break






#Search Algo Function
def search_algo():
    check = ""
    list_of_options = ['1','2','3','4','5','6','7']

    while check != "q":
        print("----------------------------------------------------------")
        check = (input("Which category do you want to search in?(1. [Passenger Class] 2. [Surname] 3. [Gender] 4. [Age] 5. [Survival Status] 6. [Embarkation Location] 7.[Boat they used to get off] OR [Q] to quit): ")).lower()
        if check != "q":
            if check not in list_of_options:
                print("You did not enter a valid option! Please try again.")
                continue
            elif check in list_of_options:
                if check == "1":
                    a = search_passengerclass()
                    while check == '1':
                        search_algo_filter(a,check)     
                        break      
                elif check == "2":
                    a = search_surname()
                    while check == '2':
                        search_algo_filter(a,check)     
                        break      
                elif check == "3":
                    a = search_gender()
                    while check == '3':
                        search_algo_filter(a,check)     
                        break      
                elif check == "4":
                    a = search_age()
                    while check == '4':
                        search_algo_filter(a,check)     
                        break      
                elif check == "5":
                    a = search_survivalstat()
                    while check == '5':
                        search_algo_filter(a,check)     
                        break      
                elif check == "6":
                    a = search_embarklocation()
                    while check == '6':
                        search_algo_filter(a,check)     
                        break      
                if check == "7":
                    a = search_boat()
                    while check == '7':
                        search_algo_filter(a,check)     
                        break      
        break
                #         while check != 'q' and check == '1':
                #             print('(1. [Passenger Class] 2. [Surname] 3. [Gender] 4. [Age] 5. [Survival Status] 6. [Embarkation Location] 7.[Boat they used to get off] OR [Q] to quit)')
                #             check = input('Which other category would you like to search: ')
                #             if check not in list_of_options:
                #                 print("You did not enter a valid option! Please try again.")
                #             elif check in list_of_options:
                #                 if check == '2':
                #                     a = search_surname_filtered(a)
                #                     check = input("Would you like to continue? (1. Continue or 2. Q to quit)").lower

                #                 elif check == '3':
                #                     a = search_gender_filtered(a)
                #                     check = input("Would you like to continue? (1. Continue or 2. Q to quit)").lower

                #                 elif check == '4':
                #                     a = search_age_filtered(a)
                #                     check = input("Would you like to continue? (1. Continue or 2. Q to quit)").lower

                #                 elif check == '5':
                #                     a = search_survstat_filtered(a)
                #                     check = input("Would you like to continue? (1. Continue or 2. Q to quit)").lower

                #                 elif check == '6':
                #                     a = search_embarklocation_filtered(a)
                #                     check = input("Would you like to continue? (1. Continue or 2. Q to quit)").lower

                #                 elif check == '7':
                #                     a = search_boat_filtered(a)
                #                     check = input("Would you like to continue? (1. Continue or 2. Q to quit)").lower
                #             if check == '1':
                #                 continue
                #             elif check == 'q':
                #                 break


                #     check = ""
                # elif check == "2":
                #         b = search_surname()

                #         check = ""
                # elif check == "3":
                #         c = search_gender()

                #         check = ""
                # elif check == "4":
                #         d = search_age()

                #         check = ""
                # elif check == "5":
                #         e = search_survivalstat()

                #         check = ""
                # elif check == "6":
                #         f = search_embarklocation()

                #         check = ""
                # elif check == "7":
                #         g = search_boat()



##################
# Main Programme #
##################

load_titanic('titanic.csv')
print('Welcome to the Titanic Dataset Explorer')
option = 'A'

while option.upper() != 'Q': 
    print('Select an option')
    print('(1) Display names of first-class passengers')
	# TODO: Change the menu here
    print('(2) Ask for user input to find the details of the specific person that the user wants to look for(give first name and last name)')
    print('(3) Display the Survival Rate of woman who are married and not married respectively')
    print('(4) Use the search algo')
    print('(5) Display name, survival status and age and boat of first-class passengers')
    print('(6) Display name, survival status and boat and mortality rate of first-class passengers')
    print('(Q) Quit')
    option = input('> ')
    print()
    
    if option == '1':
        display_first_class()
    # TODO: To add on access to new functionalities here
    
    elif option == '2':
        find_person_details()

    elif option == '3':
        option_5()
    
    elif option == '4':
        search_algo()
        print("----------------------------------------------------------")
        print("Thank You For Using The Search Algo")
        print("----------------------------------------------------------")
    
    elif option == '5':
        first_class_survival_age()

    elif option == '6':
        first_class_survival_boat()

    elif option.upper() =='Q':
        print('Thank you for using the Titanic Dataset Explorer')
    else:
        print('Invalid option')
        print()

