
def unique_list(filename, index):
    """Takes the filename and the index of the category [Country (1), Category(2)]
        as parameters and outputs a list of all the unique values."""
    #opens the file
    inline = open(filename, "r")
    #initializes the list to be returned
    result = []
    line = inline.readline()
    line = inline.readline()
    while line != "":
        #each element of the line separated by a comma is put into a list
        line_list = line.strip().split(',')
        country = line_list[index]
        count = 0
        #if country is already in the result list, it does nothing, if it is not in the list it appends the country into the list
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
    #opens the file
    inline = open(filename, "r")
    line = inline.readline()
    line = inline.readline()
    total = 0
    while line != "":
        #each element of the line separated by a comma is put into a list
        line_list = line.strip().split(',')
        # if the country in the line matches the given country it finds the visitors in that line and adds it to the total variable
        if (country_name == line_list[1]):
            total += int(line_list[3])
        
        line = inline.readline()
    inline.close()

    return total

def choice_1(filename):
    """Reads the file, outputs the total number of visitors per country 
        and states the country with the most visitors."""
    #for fromatting:
    print("="*50)
    print(" "*9,"Visitors per Country")
    print("="*50)
    print("Country"," "*(15),"Visitors")
    print("-"*50)
    max = 0
    country_index = 1
    #gets a list of unique countries
    countries = unique_list(filename,country_index)
    for i in range(len(countries)):
        country = countries[i]
        # gets the total visitors of the given country
        total = visitors_by_country_name(country, filename)
        #for find the country with the most visitors
        if total>max:
            max = total
            max_country = country
        space = " "*(15 - len(country))
        #prints the unique coutnries on the left (1 per line) and prints their corresponding total visitors on the right
        print(f"Country: {country}{space}Total Visitors: {total}")
    #prints the country with the most visitors
    print("\nCountry with highest Visitors: ",max_country)
    print("-"*50)


def avg_rating_by_country_name(country_name,filename):
    """Takes the country name and filename as the parameter and returns the average 
        rating of the country by adding up all the ratings for all the locations of 
        the country and dividing it by the number of locations."""
    #opens the file
    inline = open(filename, "r")
    line = inline.readline()
    count = 0
    total = 0
    while line != "":
        line_list = line.strip().split(',')
        #if the country in the line is the same as the given country it finds the rating from that line and adds it to the total variable
        #the countr variable also keeps track of the number of locations (since its finding the average, this number will be used to divide by)
        if(line_list[1]==country_name):
            total += float(line_list[4])
            count += 1
        line = inline.readline()
    inline.close()
    if total == 0:
        return 0
    return total/count

def choice_2(filename):
    """Reads the file and outputs the average ratings per country and 
        states the country with the highest average rating."""
    # for formatting:
    print("="*50)
    print(" "*9,"Ratings per Country")
    print("="*50)
    print("Country"," "*(15),"Ratings")
    print("-"*50)

    country_index = 1
    # gets a list of unique countries
    countries = unique_list(filename,country_index)
    max_rating = 0
    max_rating_country = 0
    for i in range(len(countries)):
        country = countries[i]
        # gets the average rating for the given country
        rating = avg_rating_by_country_name(country, filename)
        # the max_rating keeps track of the largest rating, while the max_rating_country keeps track of the country with the max ratings
        if rating > max_rating:
            max_rating = rating
            max_rating_country = country
        space = " "*(15 - len(country))
        #prints the unique countries on the left (1 per line) and their corresponding average ratings on the right
        print(f"Country: {country}{space}Rating: {round(rating,3)}")
    # prints the country with the highest average rating
    print("\nCountry with highest Ratings: ",max_rating_country)
    print("-"*50)


def popular_category(user_country, filename):
    """Takes the country name, given by user, and the filename as the parameters and 
        outputs the most popular category in that country. A popular category is defined
        by the category with the most visitors."""
    category_index = 2
    # gets a list of unique categories
    unique_categories = unique_list(filename, category_index)
    #initializes a lsit
    visitors_per_category = []
    for i in range(len(unique_categories)):
        #initialized the list by adding number of unique categories 0s
        visitors_per_category.append(0)

    inline = open(filename, "r")
    #reads all the lines from the file and saves them as a list of strings
    lines = inline.readlines()

    for i in range(len(unique_categories)):
        visitors = 0
        for j in range(1,len(lines)):
            #it takes the jth element from lines and puts the elements of that line into a list
            line_list = lines[j].split(',')
            #if the country from that line is the same as the given country and teh category from that line is the same 
            #as the given category, it finds the visitors from that line and adds it to the visitors variable
            if line_list[1] == user_country:
                if line_list[2] == unique_categories[i]:
                    visitors += int(line_list[3])
        #it adds the visitors for that country to the country's corresponding place in the visitors_per_category list
        visitors_per_category[i] = visitors

    max_visitors = 0
    max_visitor_index = 0
    for i in range (len(visitors_per_category)):
        #finds the index number with the highest visitors
        if visitors_per_category[i] > max_visitors:
            max_visitors = visitors_per_category[i]
            max_visitor_index = i
    # outputs the category at that index being the popular category
    return unique_categories[max_visitor_index]

def get_locations_by_popular_category(filename, country):
    """Takes the filename and the country name as the parameters and returns
        a list of locations (along with other info: visitors, rating, accomodation) 
        that match the popular category and are from the given country."""
    #initializes the list
    result = []
    inline= open(filename, "r")
    line = inline.readline()
    line = inline.readline()
    while(line != ""):
        line_list = line.strip().split(',')
        #if the country from the line is the same as the given country, and the category in that line is the same as the popular
        # category of that country, it saves the location, visitors, rating and accomodations of that line
        if line_list[1] == country:
            if(line_list[2] == popular_category(country, filename)):
                location = line_list[0]
                visitors = line_list[3]
                rating = line_list[4]
                accomodation = line_list[6]
                #all the collected info is formatted into a list
                result.append(f"Location: {location}{" "*(40-len("Location: ")-len(location))}Visitors: {visitors}{" "*(25-len("Visitors: ")-len(visitors))}Rating: {rating}{" "*(20-len("Rating: ")-len(rating))}Accomodation Available: {accomodation}")
        line = inline.readline()
    inline.close()
    return result


def top_rated(user_country, filename):
    """Takes the country name and the filename as the parameters and
        returns the top rated location (along with other relevant info: 
        Category, Visitors, Rating, availability of accomodations) from 
        that country"""
    inline = open(filename, "r")
    line = inline.readline()
    line = inline.readline()
    max_rating = 0
    while line != "":
        line_list = line.strip().split(',')
        #if the country in the line is the same as the given country, it saves the rating from that line
        if line_list[1] == user_country:
            rating = float(line_list[4])
            #max_rating tracks the largest rating, and also saves the corresponding location, category, visitors and accomodation
            if rating > max_rating:
                max_rating = rating
                location = line_list[0]
                category = line_list[2]
                visitors = line_list[3]
                accomodation = line_list[6]
        line = inline.readline()
    inline.close()
    #returns a formatted string with all the collected info
    return (f"Location: {location}{" "*(40-len("Location: ")-len(location))}Category: {category}{" "*(25-len("Category: ")-len(category))}Visitors: {visitors}{" "*(20-len("Visitors: ")-len(visitors))}Rating: {max_rating}{" "*(15-len("Rating: ")-len(str(max_rating)))}Accomodation Available: {accomodation}\n")

def most_visitors(user_country, filename):
    """Takes the country name and the filename as parameters and
        returns the location (along with other relevant info: category, 
        visitors, rating, availability of accomodation) from that 
        country with the most visitors."""
    max_visitors = 0
    inline = open(filename, "r")
    line = inline.readline()
    line = inline.readline()
    while line!="":
        line_list = line.strip().split(',')
        # if the country in the line is the same as the given country, it saves the visitors from that line
        if line_list[1] == user_country:
            visitors = int(line_list[3])
            #max_visitors tracks the largest number of visitors, and also saves the corresponding location, category, rating and accomodation
            if visitors > max_visitors:
                max_visitors = visitors
                location = line_list[0]
                category = line_list[2]
                rating = line_list[4]
                accomodation = line_list[6]
        line = inline.readline()
    inline.close()
    #returns a formatted string with all the collected info
    return (f"Location: {location}{" "*(30-len("Location: ")-len(location))}Category: {category}{" "*(25-len("Category: ")-len(category))}Visitors: {max_visitors}{" "*(20-len("Visitors: ")-len(str(max_visitors)))}Rating: {rating}{" "*(15-len("Rating: ")-len(str(rating)))}Accomodation Available: {accomodation}\n")

def num_of_accomodations(user_country, filename):
    """Takes the country name and the filename as the parameters and
        returns the percentage of locations that provide accomodations."""
    inline = open(filename, "r")
    line = inline.readline()
    line = inline.readline()
    count = 0
    num_accomodation = 0
    while line!="":
        line_list = line.strip().split(',')
        # if the country from the line is the same as the given country and accomodation is available, num_accomodation increases by 1
        #num_accomodation tracks the number of locations that provide an accomodation
        if line_list[1] == user_country:
            if line_list[6] == "Yes":
                num_accomodation += 1
            # the count variable keeps track of the total number of locations checked (to later find the percentage)
            count+=1
        line = inline.readline()
    inline.close()
    #this is so that there is no error of dividing by 0 if that ever occurs
    if count == 0:
        return 0
    return round(((num_accomodation/count)*100),2)

def choice_3_preference_1(write_filename, read_filename, country):
    """Takes the name of the file to read, file to write and the name of 
        the country as the parameters and writes a report of the country
        to the given file. The report includes: the top rated location in
        that country, the most visited location in that country, the % of
        locations in that country that provide accomodations, the most popular
        type of tourism in that country and a list of locations that correspond
        to that popular category."""
    #opens a file to write
    outline = open(write_filename, "w")
    #for formatting
    outline.write("="*50 + f"\n{country}\n" + "="*50)
    #writes the top rated location in the country
    outline.write(f"\n\nThe top rated location in {country}:\n")
    outline.write(top_rated(country, read_filename))
    outline.write("-"*25)
    #writes the most visited location in that country
    outline.write(f"\nThe most visited location in {country}:\n")
    outline.write(most_visitors(country, read_filename))
    outline.write("-"*25)
    #writes the percentage of locations in that country that provide an accomodation
    outline.write(f"\n{num_of_accomodations(country, read_filename)}% of the locations in {country} have Accomodations available.\n")
    outline.write("-"*25)
    #writes the most popular type of category followed by a list of location in that country that match the popular category
    outline.write(f"\nMost popular type of tourism in {country} is '{popular_category(country, read_filename)}'\n")
    outline.write(f"Here is a list of {popular_category(country, read_filename)} places in {country}:\n\n")
    locations_by_pop_category = get_locations_by_popular_category(read_filename, country)
    for i in range(len(locations_by_pop_category)):
        outline.write(f"{locations_by_pop_category[i]}\n")
    outline.close()

def choice_3_preference_2(write_filename, read_filename, country, category):
    """Takes the name of the file to read, name of the file to write, the name of 
        the country and the name of the category as the parameters and writes a 
        list of locations, to the given file, corresponding to the given country 
        and category."""
    #opens the file to read
    inline = open(read_filename, "r")
    #opens the file to write
    outline = open(write_filename,"w")
    outline.write(f"Here are a list of locations based on your preferences. Country: {country}     Category: {category}\n\n")
    line = inline.readline()
    line = inline.readline()
    while line != "":
        line_list = line.strip().split(',')
        # if the country in the line is the same as the given country, and the category in the line is the same as the given category,
        # it saves the location, visitors, rating, and availability of accomodation
        if line_list[1] == country:
            if line_list[2] == category:
                location = line_list[0]
                visitors = line_list[3]
                rating = line_list[4]
                accomodation = line_list[6]
                #writes all the collected info into the file
                outline.write(f"Location: {location}{" "*(40-(len("Location: "))-len(location))}Visitors: {visitors}{" "*(25-(len("Visitors: "))-len(visitors))}Rating: {rating}{" "*(20-(len("Rating: "))-len(rating))}Accomodation Available: {accomodation}\n")
        line = inline.readline()
    inline.close()
    outline.close()
        

def total_revenue(country, filename):
    """Takes the country name and the filename as the parameters and
        returns the total revenue for the given country."""
    inline = open(filename, "r")
    line = inline.readline()
    line = inline.readline()
    total = 0
    while line!="":
        line_list = line.strip().split(',')
        #if country in the line is the same as the given country, it finds the revenue in that line and adds it to the total variable
        if country == line_list[1]:
            total += float(line_list[5])
        line = inline.readline()
    inline.close()
    #returns the total revenue for the given country
    return total

def choice_4(filename):
    #for formatting:
    print("="*50)
    print("Here is the Total Revenue for each Country:")
    print("="*50+"\n")
    #gets a list of unique countries
    country = unique_list(filename, 1)
    for i in range(len(country)):
        #gets the total revenue for the given country
        revenue = total_revenue(country[i],filename)
        #for formatting:
        space = " "*(15 - len(country[i]))
        #prints the unique countries on the left (1 per line) and prints the corresponding total revenue on the right
        print(f"Country: {country[i]}{space}Revenue: {round(revenue,2)}")


def main():
    # formatting + menu:
    print("-"*50)
    print("| WELCOME TO TOURISM ANALYTICS!"+" "*(50-len("| Welcome To TOURISM ANALYTICS!"))+"|")
    print("-"*50)
    print("\nSelect your choice by typing in the number you want.")
    print("-"*50)
    print("1. Visitors by Country")
    print("2. Average Ratings by Country")
    print("3. Get Recommendations based on Country, Category")
    print("4. Total revenue by Country")
    
    #input validation for choosing an option from the menu
    while True:
        try:
            choice = int(input("Enter Your Choice: "))
            if choice >= 1 and choice <= 4:
                break
            else:
                print("Invalid Input. Please enter a number between 1 and 4.\n")
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 4.\n")

    print()
    if choice == 1:
        choice_1("tourism_dataset_refined.csv")
    elif choice == 2:
        choice_2("tourism_dataset_refined.csv")
    elif choice == 3:
        #input validation for choosing the preference under choice 3
        while True:
            try:
                preference = int(input("Do you want recommendations based on (1) Country (2) Country & Category (Enter 1 or 2): "))
                if preference == 1 or preference == 2:
                    break
                else:
                    print("Invalid Input! Please enter 1 or 2.")
            except ValueError:
                print("Invalid Input! Please enter 1 or 2.")

        if preference == 1:
            country_list = unique_list("tourism_dataset_refined.csv", 1)
            #input validation for chosing a country
            while True:
                country = input("Enter Country [India, USA, Brazil, France, Egypt, China, Australia]: ")
                if country in country_list:
                    break
                else:
                    print("Data for your chosen country is not available. Please choose from the given list.\n")
            choice_3_preference_1("recommendation_by_country.txt", "tourism_dataset_refined.csv", country)
        if preference == 2:
            country_list = ["India", "USA", "Brazil", "France", "Egypt", "China", "Australia"]
            category_list = ["Nature", "Historical", "Cultural", "Beach", "Adventure", "Urban"]
            #input validation for chooosing a country and a category
            while True:
                country = input("Enter Country [India, USA, Brazil, France, Egypt, China, Australia]: ")
                category = input("Enter Category [Nature, Historical, Cultural, Beach, Adventure, Urban]: ")
                if (country in country_list) and (category in category_list):
                    break
                elif country in country_list:
                    print("Invalid Category. Please choose from the given list.\n")
                elif category in category_list:
                    print("Invalid Country. Please choose from the given list.\n")
                else:
                    print("Invalid Country and Category. Please choose from the given list.\n")

            choice_3_preference_2("recommendation_by_country.txt", "tourism_dataset_refined.csv", country, category)

    elif choice == 4:
        choice_4("tourism_dataset_refined.csv")


if __name__ == "__main__":
    main()