# Instructions

This is a Tourism Analytics Tool that reads data from a csv file and provides 4 different useful insights based on your choice.

The Program's 4 Analysis:

    1. Visitors by Country
        - Calculates the total number of visitors for each country
        - Identifies the country with the most visitors
    
    2. Average Rating by Country
        - Calculates the average tourist attraction rating for each country
        - Identifies the country with the highest average rating

    3. Travel Recommendations
        User has 2 choices:
        A) Recomendations based on Country ONLY
            - The top rated location in the selected country
            - The most visited attraction in the selected country
            - The percentage of locations that provide accomodations
            - The most popular category of tourism in that country
            - A detailed list of locations from that country in the most 
              popular category

        B) Recommendations based on Country AND Category
            - A detailed list of all locations that match the selected Country 
              and Category

    4. Total Revenue by Country
        - Sums the revenue of all the locations in each country
        - Displays the revenue per country
    

How to Run the Code:

    1. Make sure you have the file, "tourism_dataset_refined.csv".
        - This is the file that will be used to analyze the data
        - It should have the data in the form:
            - Location, Country, Category, Visitors, Rating, Revenue, Accomodation
        - Ensure this data file is in the same folder as "analyze_tourism_dataset.py", where the code will be run from

    2. Click on the Run button or type the following into the terminal to run the file: "python analyze_tourism_dataset.py"

    3. After running the file, a menu is printed in the terminal
        - 4 options are given

    4. To choose an option, type the corresponding number into the terminal
        - Type '1' to print Visitors by Country
        - Type '2' to print Average Ratings by Country
        - Type '3' to get tourism Recommendations based on Country, Category
        - Type '4' to get the Total Revenue by Country
        - It will continue to ask for your choice until you enter a valid input

    5. If you enter '1':
        - It will output the title, "Visitors per Country", subheadings "Country" and "Visitors", and on each following line it prints the name of the country on the left and its' total visitors on the right
        - It will also output the name of the country with the most visitors
    
    6. If you enter '2':
        - It will output the title, "Ratings per Country", subheadings "Country" and "Ratings", and on each following line it prints the name of the country on the left and its' average rating on the right
        - It will also output the name of the country with the highest average rating

    7. If you enter '3':
        - You are asked to get recommendations based on (1) Country (2) Country & Category
        - Type '1' or '2' according to your preference (It will continue to ask for your choice until you enter a valid input)
)
        - If you type '1':
                - You are asked to enter the name of the country from the provided list: [Brazil, India, USA, France, Egypt, China, Australia]
                            -->  you should type the country in the terminal exactly like it is written in the list
                - You will receive a detailed report outputted in "recommendation_by_country.txt"
        - If you type '2':
                - You are asked to enter the name of the country from the provided list: [Brazil, India, USA, France, Egypt, China, Australia]    
                            -->  you should type the country in the terminal exactly like it is written in the list
                - You are asked to enter a category from the provided list: [Nature, Historical, Cultural, Beach, Adventure, Urban]
                - You will receive a detailed report outputted in "recommendation_by_country.txt"
    
    8. If you enter '4':
        - It will output the title, "Here is the Total Revenue for each Country:", and on each following line it prints the name of the country on the left and its' total revenue on the right

