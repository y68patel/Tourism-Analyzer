import pandas as pd
import numpy as np

def choice_1(df):
    """Outputs the total number of visitors per country 
        and states the country with the most visitors."""
    print("="*50)
    print(" "*9,"Visitors per Country")
    print("="*50)
    print("Country"," "*(15),"Visitors")
    print("-"*50)

    visitors_per_country = df.groupby('Country')['Visitors'].sum()
    max_visitors_country = visitors_per_country.idxmax()

    for country, total_visitors in visitors_per_country.items():
        space = " "*(15 - len(country))
        print(f"Country: {country}{space}Total Visitors: {total_visitors}")
    
    print("\nCountry with highest Visitors: ", max_visitors_country)
    print("-"*50)


def choice_2(df):
    """Outputs the average ratings per country and 
        states the country with the highest average rating."""
    print("="*50)
    print(" "*9,"Ratings per Country")
    print("="*50)
    print("Country"," "*(15),"Ratings")
    print("-"*50)

    avg_ratings_per_country = df.groupby('Country')['Rating'].mean()
    max_rating_country = avg_ratings_per_country.idxmax()

    for country, avg_rating in avg_ratings_per_country.items():
        space = " "*(15 - len(country))
        print(f"Country: {country}{space}Rating: {round(avg_rating,3)}")

    print("\nCountry with highest Ratings: ", max_rating_country)
    print("-"*50)


def popular_category(df, user_country):
    """Outputs the most popular category in that country."""
    country_df = df[df['Country'] == user_country]
    return country_df.groupby('Category')['Visitors'].sum().idxmax()


def get_locations_by_popular_category(df, country):
    """Returns a list of locations that match the popular category and are from the given country."""
    pop_cat = popular_category(df, country)
    locations = df[(df['Country'] == country) & (df['Category'] == pop_cat)]
    
    result = []
    for index, row in locations.iterrows():
        location = row['Location']
        visitors = str(row['Visitors'])
        rating = str(row['Rating'])
        accomodation = row['Accommodation_Available']
        result.append(f"Location: {location}{' '*(40-len('Location: ')-len(location))}Visitors: {visitors}{' '*(25-len('Visitors: ')-len(visitors))}Rating: {rating}{' '*(20-len('Rating: ')-len(rating))}Accomodation Available: {accomodation}")
    return result


def top_rated(df, user_country):
    """Returns the top rated location from that country"""
    country_df = df[df['Country'] == user_country]
    top_location = country_df.loc[country_df['Rating'].idxmax()]
    
    location = top_location['Location']
    category = top_location['Category']
    visitors = str(top_location['Visitors'])
    rating = str(top_location['Rating'])
    accomodation = top_location['Accommodation_Available']

    return (f"Location: {location}{' '*(40-len('Location: ')-len(location))}Category: {category}{' '*(25-len('Category: ')-len(category))}Visitors: {visitors}{' '*(20-len('Visitors: ')-len(visitors))}Rating: {rating}{' '*(15-len('Rating: ')-len(rating))}Accomodation Available: {accomodation}\n")


def most_visitors(df, user_country):
    """Returns the location with the most visitors from that country."""
    country_df = df[df['Country'] == user_country]
    top_location = country_df.loc[country_df['Visitors'].idxmax()]

    location = top_location['Location']
    category = top_location['Category']
    visitors = str(top_location['Visitors'])
    rating = str(top_location['Rating'])
    accomodation = top_location['Accommodation_Available']

    return (f"Location: {location}{' '*(30-len('Location: ')-len(location))}Category: {category}{' '*(25-len('Category: ')-len(category))}Visitors: {visitors}{' '*(20-len('Visitors: ')-len(visitors))}Rating: {rating}{' '*(15-len('Rating: ')-len(rating))}Accomodation Available: {accomodation}\n")


def num_of_accomodations(df, user_country):
    """Returns the percentage of locations that provide accomodations."""
    country_df = df[df['Country'] == user_country]
    accomodation_count = country_df[country_df['Accommodation_Available'] == 'Yes'].shape[0]
    total_locations = country_df.shape[0]

    if total_locations == 0:
        return 0
    
    return round(((accomodation_count/total_locations)*100),2)


def choice_3_preference_1(write_filename, df, country):
    """Writes a report of the country to the given file."""
    with open(write_filename, "w") as outline:
        outline.write("="*50 + f"\n{country}\n" + "="*50)
        outline.write(f"\n\nThe top rated location in {country}:\n")
        outline.write(top_rated(df, country))
        outline.write("-"*25)
        outline.write(f"\nThe most visited location in {country}:\n")
        outline.write(most_visitors(df, country))
        outline.write("-"*25)
        outline.write(f"\n{num_of_accomodations(df, country)}% of the locations in {country} have Accomodations available.\n")
        outline.write("-"*25)
        pop_cat = popular_category(df, country)
        outline.write(f"\nMost popular type of tourism in {country} is '{pop_cat}'\n")
        outline.write(f"Here is a list of {pop_cat} places in {country}:\n\n")
        locations_by_pop_category = get_locations_by_popular_category(df, country)
        for location in locations_by_pop_category:
            outline.write(f"{location}\n")


def choice_3_preference_2(write_filename, df, country, category):
    """Writes a list of locations to the given file, corresponding to the given country and category."""
    with open(write_filename,"w") as outline:
        outline.write(f"Here are a list of locations based on your preferences. Country: {country}     Category: {category}\n\n")
        
        filtered_df = df[(df['Country'] == country) & (df['Category'] == category)]

        for index, row in filtered_df.iterrows():
            location = row['Location']
            visitors = row['Visitors']
            rating = row['Rating']
            accomodation = row['Accommodation_Available']
            outline.write(f"Location: {location}{' '*(40-(len('Location: '))-len(location))}Visitors: {visitors}{' '*(25-(len('Visitors: '))-len(visitors))}Rating: {rating}{' '*(20-(len('Rating: '))-len(rating))}Accomodation Available: {accomodation}\n")


def choice_4(df):
    """Prints the total revenue for each country."""
    print("="*50)
    print("Here is the Total Revenue for each Country:")
    print("="*50+"\n")
    
    revenue_per_country = df.groupby('Country')['Revenue'].sum()

    for country, revenue in revenue_per_country.items():
        space = " "*(15 - len(country))
        print(f"Country: {country}{space}Revenue: {round(revenue,2)}")


def main():
    df = pd.read_csv("tourism_dataset_refined.csv")

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
                print("Invalid Input. Please enter a number between 1 and 4.\n")
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 4.\n")

    print()
    if choice == 1:
        choice_1(df)
    elif choice == 2:
        choice_2(df)
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

        if preference == 1:
            country_list = df['Country'].unique()
            while True:
                country = input(f"Enter Country {np.array2string(country_list, separator=', ')}: ")
                if country in country_list:
                    break
                else:
                    print("Data for your chosen country is not available. Please choose from the given list.\n")
            choice_3_preference_1("recommendation_by_country.txt", df, country)
        if preference == 2:
            country_list = df['Country'].unique()
            category_list = df['Category'].unique()
            while True:
                country = input(f"Enter Country {np.array2string(country_list, separator=', ')}: ")
                category = input(f"Enter Category {np.array2string(category_list, separator=', ')}: ")
                if (country in country_list) and (category in category_list):
                    break
                elif country in country_list:
                    print("Invalid Category. Please choose from the given list.\n")
                elif category in category_list:
                    print("Invalid Country. Please choose from the given list.\n")
                else:
                    print("Invalid Country and Category. Please choose from the given list.\n")

            choice_3_preference_2("recommendation_by_country.txt", df, country, category)

    elif choice == 4:
        choice_4(df)


if __name__ == "__main__":
    main()