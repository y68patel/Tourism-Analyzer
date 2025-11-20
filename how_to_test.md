
# How to Test

A). How to pytest:
    1. Testing the whole file:
    pytest -- verbose filename
        Ex: pytest --verbose test_tourism_dataset.py

    2. Testing individual functions:
    pytest --verbose filename::function_name
        Ex: pytest --verbose test_tourism_dataset.py::test_country_unique_list


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




