# More Testing

Here are descriptions of some additional testing:

1. test_country_unique_list()
    - Checks that the function correctly returns a list of UNIQUE countries

2. test_category_unique_list()
    - Checks that the function correctly returns a list of UNIQUE categories

    - the above 2 tests avoid duplicates in the list
    - they correctly read the correct column

3. test_one_location_visitors_by_country_name()
    - Checks the visitor total for a country that appears once in the given file (France)

4. test_multiple_locations_visitors_by_country_name()
    - Checks the visitor total for a country that appears more than 1 time in the given file (India)
    - Ensures that the correct number of visitors for each location of the country are summed

5. test_zero_locations_visitors_by_country_name()
    - Tests a country that does not exist in the given dataset (small_dataset_2.txt)
    - Since the country is not present in the dataset, the total should be 0

    - the above tests reads and sum visitors
    - returns 0 if country not found

6. test_one_location_avg_rating_by_country_name()
    - Checks average rating for a country with only 1 location in the given file
    - Average rating is the rating of that location itself

7. test_multiple_location_avg_rating_by_country_name()
    - Checks average rating for a country with multiple locations in the given file
    - Ensures proper sum of the ratings and division by the number of locations

8. test_zero_location_avg_rating_by_country_name()
    - When country does not exist in the given dataset, the output should be a 0

    - The above tests ensures correct average calculation
    - They ensures division only when valid (cannot divide by 0)

9. test_single_category_popular_category()
    - The country, Australia, has only one location in the dataset
    - The popular category is therefore, the corresponding category of that location

10. test_multiple_category_popular_category()
    - The country, India, has more than 1 locations in the dataset
    - The visitors are summed based on the category and the category with the highest visitors is the popular category of the country
    - In this case, Nature had more visitors than Beach

    - The above tests compare multiple categories
    - They correctly handle an instance with 1 category

11. test_no_accomodation_available_num_of_accomodations()
    - Checks the % of locations that provide accomodations when none of them provide an accomodation
    - All of the locations of the country, France, in the small dataset do not provide accomodations
    - So, 0% of the locations provide accomodations

12. test_all_accomodation_available_num_of_accomodations()
    - Checks the % of locations that provide accomodations when all of them provide an accomodation
    - All of the locations of the country, India, in the small dataset provide accomodations
    - So, 100% of the locations provide accomodations

13. test_no_country_num_of_accomodations()
    - Check the % of locations that provide accomodations when the country does not exist
    - Egypt does not exist in the small_dataset_2.txt, so returns 0%

    - The above tests correctly caulates the percentages

14. test_one_location_total_revenue()
    - Checks the total revenue when there is one location of the given country in the given dataset
    - There is only one location of Brazil in the small dataset, so it does not need to sum anything and simply return the corresponding revenue of that location

15. test_multiple_locations_total_revenue()
    - Check the total revenue when there is more than 1 location of the given country in that given dataset
    - India has multiple location in the dataset
    - The revenue of each location must be summed and returned

    - The above tests ensure correct sum of total revenue

16. test_multiple_locations_get_locations_by_popular_category()
    - Checks if all the locations that match the given country and the popular category are put into the list
    - For India in the small_dataset.txt, the popular category is Cultural
    - In that dataset only 1 location has a Cultural category, therefore only that location, Jaipur, is put into the list

17. test_one_locations_get_locations_by_popular_category()
    - Checks if the list if correctly outputted when there is only one location of the country in the dataset
    - France has only 1 location in small_dataset.txt so only that location will be outputten in the list

    - The above tests correctly match the country and popular category
    - They also follow a particular string format to ensure when outputted, it looks organized

18. test_multiple_locations_top_rated()
    - Checks if the correct top rated location is returned when there are multiple locations of that country
    - All the ratings of the given country, India, are compared and the highest rated location, Jim Corbett National Park, is returned

19. test_one_locations_top_rated()
    - Checks if the correct top rated location is returned when there is only 1 location of that country in the given dataset
    - The rating of the 1 location available would be considered top rated
    - The only location of the country is therefore resulted

    - The above tests correctly finds the highest rating of the locations of the given country and returns the corresponding location
    - They also follow a particular string format to ensure when outputted, it looks organized

20. test_multiple_locations_most_visitors()
    - Checks if the correct location of the most visitors is returned when there are multiple location
    - All the number of visitors for each location of the given country, India, are compared and the location of the highest visitors is returned

21. test_one_locations_most_visitors()
    - Checks if the correct location of the most visitors is returned where is only one location in the given dataset
    - For the given country, China, there exists only 1 location in the given dataset and therefore that location is considered the most visited location

    - The above tests correctly identify the greatest number of visitors
    - They also follow a particular string format to ensure when outputted, it looks organized
