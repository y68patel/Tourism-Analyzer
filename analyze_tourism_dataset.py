
def unique_list(filename, index):
    """Takes the filename and the index of the category [Country (1), Category(2)]
        as parameters and outputs a list of all the unique values."""
    inline = open(filename, "r")
    result = []
    line = inline.readline()
    line = inline.readline()
    while line != "":
        line_list = line.strip().split(',')
        country = line_list[index]
        count = 0
        for i in range(len(result)):
            if (result[i] == country):
                count += 1
        if count == 0:
            result.append(country)

        line = inline.readline()

    inline.close()
    return result


def visitors_by_country_name(country_name, filename):
    """Takes the filename and the country name as parameters 
        and returns the total number of visitors for that country."""
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
    """Reads the file, outputs the total number of visitors per country 
        and states the country with the most visitors."""
    print("="*50)
    print(" "*9,"Visitors per Country")
    print("="*50)
    print("Country"," "*(15),"Visitors")
    print("-"*50)
    max = 0
    country_index = 1
    countries = unique_list(filename,country_index)
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

    country_index = 1
    countries = unique_list(filename,country_index)
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


def popular_category(user_country, filename):
    category_index = 2
    unique_categories = unique_list(filename, category_index)
    visitors_per_category = []
    for i in range(len(unique_categories)):
        visitors_per_category.append(0)

    inline = open(filename, "r")
    lines = inline.readlines()

    for i in range(len(unique_categories)):
        visitors = 0
        for j in range(1,len(lines)):
            line_list = lines[j].split(',')
            if line_list[1] == user_country:
                if line_list[2] == unique_categories[i]:
                    visitors += int(line_list[3])
        visitors_per_category[i] = visitors

    max_visitors = 0
    max_visitor_index = 0
    for i in range (len(visitors_per_category)):
        if visitors_per_category[i] > max_visitors:
            max_visitors = visitors_per_category[i]
            max_visitor_index = i
    return unique_categories[max_visitor_index]

def get_locations_by_popular_category(filename, country):
    result = []
    inline= open(filename, "r")
    line = inline.readline()
    line = inline.readline()
    while(line != ""):
        line_list = line.strip().split(',')
        if line_list[1] == country:
            if(line_list[2] == popular_category(country, filename)):
                location = line_list[0]
                visitors = line_list[3]
                rating = line_list[4]
                accomodation = line_list[6]
                result.append(f"Location: {location}{" "*(40-len("Location: ")-len(location))}Visitors: {visitors}{" "*(25-len("Visitors: ")-len(visitors))}Rating: {rating}{" "*(20-len("Rating: ")-len(rating))}Accomodation Available: {accomodation}")
        line = inline.readline()
    inline.close()
    return result


def top_rated(user_country, filename):
    inline = open(filename, "r")
    line = inline.readline()
    line = inline.readline()
    max_rating = 0
    while line != "":
        line_list = line.strip().split(',')
        if line_list[1] == user_country:
            rating = float(line_list[4])
            if rating > max_rating:
                max_rating = rating
                location = line_list[0]
                category = line_list[2]
                visitors = line_list[3]
                accomodation = line_list[6]
        line = inline.readline()
    inline.close()
    return (f"Location: {location}{" "*(30-len("Location: ")-len(location))}Category: {category}{" "*(25-len("Category: ")-len(category))}Visitors: {visitors}{" "*(20-len("Visitors: ")-len(visitors))}Rating: {max_rating}{" "*(15-len("Rating: ")-len(str(max_rating)))}Accomodation Available: {accomodation}\n")

def most_visitors(user_country, filename):
    max_visitors = 0
    inline = open(filename, "r")
    line = inline.readline()
    line = inline.readline()
    while line!="":
        line_list = line.strip().split(',')
        if line_list[1] == user_country:
            visitors = int(line_list[3])
            if visitors > max_visitors:
                max_visitors = visitors
                location = line_list[0]
                category = line_list[2]
                rating = line_list[4]
                accomodation = line_list[6]
        line = inline.readline()
    inline.close()
    return (f"Location: {location}{" "*(30-len("Location: ")-len(location))}Category: {category}{" "*(25-len("Category: ")-len(category))}Visitors: {max_visitors}{" "*(20-len("Visitors: ")-len(str(max_visitors)))}Rating: {rating}{" "*(15-len("Rating: ")-len(str(rating)))}Accomodation Available: {accomodation}\n")

def num_of_accomodations(user_country, filename):
    inline = open(filename, "r")
    line = inline.readline()
    line = inline.readline()
    count = 0
    num_accomodation = 0
    while line!="":
        line_list = line.strip().split(',')
        if line_list[1] == user_country:
            if line_list[6] == "Yes":
                num_accomodation += 1
            count+=1
        line = inline.readline()
    inline.close()
    return round(((num_accomodation/count)*100),2)

def choice_3_preference_1(write_filename, read_filename, country):
    outline = open(write_filename, "w")
    outline.write("="*50 + f"\n{country}\n" + "="*50)
    outline.write(f"\n\nThe top rated location in {country}:\n")
    outline.write(top_rated(country, read_filename))
    outline.write("-"*25)
    outline.write(f"\nThe most visited location in {country}:\n")
    outline.write(most_visitors(country, read_filename))
    outline.write("-"*25)
    outline.write(f"\n{num_of_accomodations(country, read_filename)}% of the locations in {country} have Accomodations available.\n")
    outline.write("-"*25)
    outline.write(f"\nMost popular type of tourism in {country} is '{popular_category(country, read_filename)}'\n")
    outline.write(f"Here is a list of {popular_category(country, read_filename)} places in {country}:\n\n")
    locations_by_pop_category = get_locations_by_popular_category(read_filename, country)
    for i in range(len(locations_by_pop_category)):
        outline.write(f"{locations_by_pop_category[i]}\n")
    outline.close()

def choice_3_preference_2(write_filename, read_filename, country, category):
    inline = open(read_filename, "r")
    outline = open(write_filename,"w")
    outline.write(f"Here are a list of locations based on your preferences. Country: {country}     Category: {category}\n\n")
    line = inline.readline()
    line = inline.readline()
    while line != "":
        line_list = line.strip().split(',')
        if line_list[1] == country:
            if line_list[2] == category:
                location = line_list[0]
                visitors = line_list[3]
                rating = line_list[4]
                accomodation = line_list[6]
                outline.write(f"Location: {location}{" "*(40-(len("Location: "))-len(location))}Visitors: {visitors}{" "*(25-(len("Visitors: "))-len(visitors))}Rating: {rating}{" "*(20-(len("Rating: "))-len(rating))}Accomodation Available: {accomodation}\n")
        line = inline.readline()
    inline.close()
    outline.close()


def choice_3(filename, preference):
    if preference == 1:
        country_list = unique_list(filename, 1)
        while True:
            country = input("Enter Country [India, USA, Brazil, France, Egypt, China, Australia]: ")
            if country in country_list:
                break
            else:
                print("Data for your chosen country is not available. Please choose from the given list.\n")
        choice_3_preference_1("recommendation_by_country.txt", filename, country)
    elif preference == 2:
        country_list = ["India", "USA", "Brazil", "France", "Egypt", "China", "Australia"]
        category_list = ["Nature", "Historical", "Cultural", "Beach", "Adventure", "Urban"]

        while True:
            country = input("Enter Country [India, USA, Brazil, France, Egypt, China, Australia]: ")
            category = input("Enter Category [Nature, Historical, Cultural, Beach, Adventure, Urban]: ")
            if (country in country_list) and (category in category_list):
                break
            elif country in country_list:
                print("Invalid Category. Please choose from the given list.")
            elif category in category_list:
                print("Invalid Country. Please choose from the given list.")
            else:
                print("Invalid Country and Category. Please choose from the given list.")

        choice_3_preference_2("recommendation_by_country.txt", filename, country, category)
        

def total_revenue(country, filename):
    inline = open(filename, "r")
    line = inline.readline()
    line = inline.readline()
    total = 0
    while line!="":
        line_list = line.strip().split(',')
        if country == line_list[1]:
            total += float(line_list[5])
        line = inline.readline()
    inline.close()
    return total

def choice_4(filename):
    print("="*50)
    print("Here is the Total Revenue for each Country:")
    print("="*50+"\n")
    country = unique_list(filename, 1)
    for i in range(len(country)):
        revenue = total_revenue(country[i],filename)
        space = " "*(15 - len(country[i]))
        print(f"Country: {country[i]}{space}Revenue: {round(revenue,2)}")


def main():
    print("-"*50)
    print("| WELCOME TO TOURISM ANALYTICS!"+" "*(50-len("| Welcome To TOURISM ANALYTICS!"))+"|")
    print("-"*50)
    print("\nSelect your choice by typing in the number you want.")
    print("-"*50)
    print("1. Visitors by Country")
    print("2. Average Ratings by Country")
    print("3. Get Recommendations based on Country, Category")
    print("4. Total revenue by Country")
    
    while True:
        try:
            choice = int(input("Enter Your Choice: "))
            if choice >= 1 and choice <= 4:
                break
            else:
                print("Invalid Input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 4.)")

    print()
    if choice == 1:
        choice_1("tourism_dataset_refined.csv")
    elif choice == 2:
        choice_2("tourism_dataset_refined.csv")
    elif choice == 3:
        while True:
            try:
                preference = int(input("Do you want recommendations based on (1) Country (2) Country & Category (Enter 1 or 2): "))
                if preference == 1 or preference == 2:
                    break
                else:
                    print("Invalid Input! Please enter 1 or 2.")
            except ValueError:
                print("Invalid Input! Please enter 1 or 2.")
        choice_3("tourism_dataset_refined.csv", preference)
    elif choice == 4:
        choice_4("tourism_dataset_refined.csv")


if __name__ == "__main__":
    main()