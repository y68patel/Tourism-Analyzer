
# Design Report

# Introduction
The purpose of the Tourism Analytics program is to analyze the tourism data and provide meaningful insights to users. I personally love travelling and going to new places, but my family and I always struggle to decide where are next trip should be. Therefore, I thought through this program I can provide some insight to users that can also assist them with their struggle to plan vacations.
The program reads from a csv file that contains information about locations, countries, categories, ratings, number of visitors, revenue, and availability of accomodations and provides the users wih 4 options to get useful insight of the data:
    1. View Total Visitors per Country
    2. View Average Ratings per Country
    3. Receive Recommendation based on Country or Country and Category
    4. View Total Revenue by Country
The main goal of this project was not only to create a working program, but to show a good program design, a clear code structure, automated testing and a clear split between the logic (helper methods) and user interaction (main function). This approach makes the program easier to follow, debug, and test.


# Design
A key design feature I  had in mind from the start was to break down the code into many smaller functions as opposed to a few large functions as well placing all user inputs in the main function instead of any of the helper methods. I aimed to put each task into its' own separate funciton. This allowed the code to be more organized, easy to follow, understand, debug and pytest.

At first, I decided to simply create 4 functions for each of the 4 choices and call them in the main function if the corresponding choice was chosen. However, when I began writing the first function for choice 1, displaying the total visitors by country, I noticed how long and complex the function looked. There was also some bug in the code which I couldn't debug due to the functions' complexity.
Therefore, I divided that function into 3 smaller functions: unique_list(), visitors_by_country_name(), choice_1(). The unique_list() list function returns a list of unique countries, visitors_by_country_name() returns the sum of the visitors in the given country and this is all put together under the choice_1 function. It designs a title and the subheadings, and with proper spacing places all the unique countries on the left and their corresponding total visitors on the right.
The unique_list() function is also used again to extract a list of unique categories. This design minimizes repeated logic.d

Another design choice was to keep the program's logic separate from the user interface. All user interaction such as displaying menu, asking for input and printing results are all handled inside the main() function, while the calculations and data analysis are done by separate helper methods. 

# COME BACK

All of the functions also accept the filename as a parameter. This allowed me to test the function using small test files (small_dataset.txt, small_dataset_2.txt) while also being able to use the data from the original csv file (tourism_dataset_refined.csv) in the main function. Although I started writing the functions by hardcoding the filename, I came to realize it would be easier to pass it as a parameter instead.


# Design Highlights
Additionally, one function that I was proud of was the unique_list() function. Intially, I had designed it so that it would only return a list of unique countries. However, when I also needed a list of uniques categories later on, I realized that the code for both of the functions were exactly the same, other than the index number. Therefore, I combined both the function into 1 by also passing an index parameter. This way, it would be able to return a unique list of items for any of the columns required (location, country, category, etc).
But overall, I was proud of recognizing the various small tasks that I would need to put the program together. This allowed me to organize and divide my code much better. 
Along with this, the functions that required correct string formating, such as most_visitors() and top_rated(), took a while to figure out. When I first ran the function without the spaces in between, the result in the outputted file was very disorganized as the columns were not correctly aligned. With some trial and error, I figured out a way to keep consistent spacing between each column to present it in an organized manner.
There was also another challenge I encountered while designing the third choice, "Get recommendations based on Country, Category". Initially, I had a function name choice_3(), where I got input from the user to select preference 1) get recommendation by country or preference 2) get recommendation by country and category. At first I could not figure out how to design it in a way so that the input is only collected in the main function. Again, after some trial and error, I found it would be easy to simply move the whole choice_3() funciton into the main function and I also conducted some tests to ensure it was operating correctly.

# Areas of Improvement
There are some functions (choice_1(), choice_2(), choice_4()) in the program that directly print to the terminal. As a result, it was difficult for me to design automdated tests (pytests) for these programs. Therefore, if I did have more time, I would definitely want to figure out a way to alter change that, so I can do design a pytest.
At one point, I also felt that some of the code was repeating in a lot of the functions:
    inline = open(filename, "r")
    line = inline.readline()
    line = inline.readline()
    while line != "":
        line_list = line.strip().split(',')
        ...
        line = inline.readline()
    inline.close()
I attempted to find a solution, but I lacked time and could not figure out an appropriate solution. One potential method of doing this could be reading the dataset once and reuse it across the programs.

# Lessons Learned
One of the key lessons I have learned from this project is patience. Despite thinking I have written the code correctly, at time, I did not get the desired output. Sometimes, I was able to identify the bug quickly, while at other times, the debugging took longer. However, with patience it becomes easier to approach these bugs.
I also learned the significance of taking small steps in travelling a larger distance. What I mean is, no matter how big the project is, breaking it down into smaller parts, like the helper methods, makes it easier and much more efficient in designing the project correctly.
Despite disliking the whole process of writing tests, the project taught me its importance. It was through the tests that I recognized some mistakes which allowed me to go back and fix for a more efficient code.
