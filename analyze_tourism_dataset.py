
def unique_countries_list(filename):
    inline = open(filename, "r")
    countries = []
    line = inline.readline()
    line = inline.readline()
    while line != "":
        line_list = line.strip().split(',')
        country = line_list[1]
        index = 0
        for i in range(len(countries)):
            if (countries[i] == country):
                index += 1
        if index == 0:
            countries.append(country)

        line = inline.readline()

    inline.close()
    return countries

def visitors_by_country_name(country_name, filename):
    inline = open(filename, "r")
    line = inline.readline()
    line = inline.readline()
    total = 0
    while line != "":
        line_list = line.strip().split(',')
        if (country_name == line_list[1]):
            total += int(line_list[3])
        
        line = inline.readline()
    inline.close()

    return total

def choice_1(filename):
    print("="*50)
    print(" "*9,"Visitors per Country")
    print("="*50)
    print("Country"," "*(15),"Visitors")
    print("-"*50)
    max = 0
    countries = unique_countries_list(filename)
    for i in range(len(countries)):
        country = countries[i]
        total = visitors_by_country_name(country, filename)
        if total>max:
            max = total
            max_country = country
        space = " "*(15 - len(country))
        print(f"Country: {country}{space}Total Visitors: {total}")
    print("\nCountry with highest Visitors: ",max_country)
    print("-"*50)

def avg_rating_by_country_name(country_name,filename):
    inline = open(filename, "r")
    line = inline.readline()
    count = 0
    total = 0
    while line != "":
        line_list = line.strip().split(',')
        if(line_list[1]==country_name):
            total += float(line_list[4])
            count += 1
        line = inline.readline()
    inline.close()
        
    return total/count

def choice_2(filename):
    print("="*50)
    print(" "*9,"Ratings per Country")
    print("="*50)
    print("Country"," "*(15),"Ratings")
    print("-"*50)
    #can make a separate function for this above code ^^^

    countries = unique_countries_list(filename)
    max_rating = 0
    max_rating_country = 0
    for i in range(len(countries)):
        country = countries[i]
        rating = avg_rating_by_country_name(country, filename)
        if rating > max_rating:
            max_rating = rating
            max_rating_country = country
        space = " "*(15 - len(country))
        print(f"Country: {country}{space}Rating: {round(rating,3)}")
    print("\nCountry with highest Ratings: ",max_rating_country)
    print("-"*50)










def main():
    print("Welcome To ______!")
    print("Select your choice by typing in the number you want.")
    print("1. Visitors by Country")
    print("2. Average Ratings by Country")
    print("3. Get Recommendation based on Category/Country")
    
    choice = int(input("\nYour Choice: "))  # add an exception when lettrs or characters are inputted
    while choice<1 or choice>4:
        print("Your input was invalid. Choose your preference from 1-4.")
        choice = int(input("Your Choice: "))
    print()
    if choice == 1:
        choice_1("tourism_dataset_unique_trimmed.csv")
    elif choice == 2:
        choice_2("tourism_dataset_unique_trimmed.csv")



if __name__ == "__main__":
    main()