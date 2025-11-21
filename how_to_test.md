
# How to Test

I have not talked about any specific automated testings in this file because for my project I think the manual testing described below is sufficient for "basic testing".

A) How to run automated tests (pytest):
    1. Ensure the files, analyze_tourism_dataset.py, test_analyze_tourism_dataset.py, small_dataset.txt, small_dataset_2.txt, are in the same file

    2. To test the whole file, type the following in the terminal:
    pytest -- verbose filename
        Ex: pytest --verbose test_tourism_dataset.py

    2. To test individual functions, type the following in the terminal:
    pytest --verbose filename::function_name
        Ex: pytest --verbose test_tourism_dataset.py::test_country_unique_list

    3. All tests should pass

    The automated tests use smaller datasets small_dataset.txt and small_dataset_2.txt to make the testing fast and predictable.



B) How to test Manually:

    1. choice_1():
        i) Make a text file with a smaller dataset
       ii) Run the function manually [Ex: choice_1("small_dataset.txt")]
      iii) Observe the output: It should output a Title "Visitors per Country", subheadings "Country" and "Visitors", a list of       
           countries (per line) with the total visitors to the right and displays the country with the highest number of visitors
       iv) Individually verify the total visitors:
                a) For every country from your small dataset:
                    - Locate all the locations of that country, sum all the visitors
                    - Confirm if your calculated value matches the value outputted
                b) From your calculated total visitors, find the country with the most visitors and confirm with the outputted country


    2. choice_2():
        i) Make a text file with a smaller dataset
       ii) Run the function manually [Ex: choice_2("small_dataset.txt")]
      iii) Observe the output: It should output a Title "Ratings per Country", subheadings "Country" and "Ratings", a list of       
           countries (per line) with their average ratings to the right and displays the country with the highest average rating
       iv) Individually verify the average ratings:
                a) For every country from your small dataset:
                    - Locate all the locations of that country, sum all the ratings and divide by the number of locations of that 
                      country
                    - Round the value to 3 decimal points
                    - Confirm if your calculated value matches the value outputted
                b) From your calculated averages, find the country with the highest average rating and confirm with the outputted 
                   country
    
    3. choice_4():
        i) Make a text file with a smaller dataset
       ii) Run the function manually [Ex: choice_4("small_dataset.txt")]
      iii) Observe the output: It should output a Title "Here is the Total Revenue for each Country:" and a list of       
           countries (per line) with the total revenue to the right
       iv) Individually verify the total revenue:
                a) For every country from your small dataset:
                    - Locate all the locations of that country, sum all the revenue
                    - Confirm if your calculated value matches the value outputted

    4. choice_3_preference_1():
        i) Make a text file with a smaller dataset
       ii) Run the function manually [Ex: choice_3_preference_1("test_output.txt", "small_dataset.txt", "India")]
      iii) Decide the expected output:
            Example from the "small_dataset.txt":
            a) Title of the country: "India"
            b) Top Rated location in India: Jim Corbett National Park
            c) Most Visited location in India: Jaipur
            d) Percentage of locations that provide accomodations in India: 100%
            e) Most popular type of tourism in India: Cultural
            f) A list of Cultural locations in India:
                - Jaipur
       iv) Open the file created after calling the function (test_output.txt) and verify the content with your expected output
        v) This process can be repeated with another country to further verify the function ["USA", "Brazil", "India", "Australia", "China", "France", "Egypt"]

    5. choice_3_preference_2():
        i) Make a text file with a smaller dataset
       ii) Run the function manually [Ex: choice_3_preference_2("test_output.txt", "small_dataset.txt", "France", "Adventure")]
      iii) Decide the expected output:
            Example from the "small_dataset.txt"
            a) Find all locations from the dataset that match the given condition. Country: France   Category: Adventure
                - French Alps
      iv) Open the file created after calling the function (test_output.txt) and verify the content with your expected output
       v) This process can be repeated with other countries or categories 
            - ["USA", "Brazil", "India", "Australia", "China", "France", "Egypt"]
            - ["Cultural", "Historical", "Adventure", "Beach", "Urban", "Nature"]

    6. main()
        i) Run the file by typing the following in the terminal: "python analyze_tourism_dataset.py"
       ii) A welcome banner + a menu is outputted
      iii) When asked to enter your choice, type:
                - letter: a, A
                - character: #, !
                - numbers out of range: -2, 0, 5, 10
                - blank: ""
            - Entering these values should output: "Invalid Input. Please enter a number between 1 and 4.\n\nEnter your choice: "
       iv) Confirm if each inputted choice number, outputs the correct result
            - Typing '1' should output Visitors by Country
            - Typing '2' should output Average Ratings by Country
            - Typing '3' should output further questions:
                    a) When asked to enter your preference (1) recommendation by country (2) recommendation by country & category, type:
                            - letter: a, A
                            - character: #, !
                            - numbers out of range: -2, 0, 3, 10
                            - blank: ""
                        - Entering these values should output: "Invalid Input! Please enter 1 or 2."
                        - If you enter '1', recommendation by country:
                            a) When asked to enter country, type:
                                    - numbers: -5, 0, 10
                                    - character: #, !
                                    - blank: ""
                                    - country not in the list: Canada, Italy
                                - Entering these values should ouput: "Data for your chosen country is not available. Please choose from the given list."
                        - If you enter '2', recommendation by country and category:
                            a) When asked to enter country, type:
                                    - numbers: -5, 0, 10
                                    - character: #, !
                                    - blank: ""
                                    - country not in the list: Canada, Italy
                                - Entering these values should ouput: "Invalid Country. Please choose from the given list."
                            b) When asked to enter category, type:
                                    - numbers: -5, 0, 10
                                    - character: #, !
                                    - blank: ""
                                    - category not in the list: Fun, Sightseeing
                                - Entering these values should output: "Invalid Category. Please choose from the given list."
                                - If both Country and Category are invalid inputs, it will output: "Invalid Country and Category. Please choose from the given list."
                    b) Ensure the "recommendation_by_country.txt" file where choice 3 writes into is correctly updated each time
                        - Run choice 3 a 2-3 times with different inputs and verify the outputted file: "recommendation_by_country.txt"
            - Typing '4' should output Total Revenue by Country
