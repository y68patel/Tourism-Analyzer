from analyze_tourism_dataset import unique_list
from analyze_tourism_dataset import visitors_by_country_name
from analyze_tourism_dataset import avg_rating_by_country_name
from analyze_tourism_dataset import popular_category
from analyze_tourism_dataset import num_of_accomodations
from analyze_tourism_dataset import total_revenue
from analyze_tourism_dataset import get_locations_by_popular_category
from analyze_tourism_dataset import top_rated

def test_country_unique_list():
    filename = "small_dataset.txt"
    country_index = 1
    expected_result = ["India", "USA", "China", "France", "Brazil", "Australia", "Egypt"]
    result = unique_list(filename, country_index)
    assert sorted(expected_result) == sorted(result)

def test_category_unique_list():
    filename = "small_dataset.txt"
    country_index = 2
    expected_result = ["Beach", "Adventure", "Historical", "Urban", "Cultural", "Nature"]
    result = unique_list(filename, country_index)
    assert sorted(expected_result) == sorted(result)



def test_one_location_visitors_by_country_name():
    filename = "small_dataset.txt"
    country_name = "France"
    expected_result = 324369
    result = visitors_by_country_name(country_name, filename)
    assert expected_result == result

def test_multiple_locations_visitors_by_country_name():
    filename = "small_dataset.txt"
    country_name = "India"
    expected_result = 589849 + 811018 + 466796
    result = visitors_by_country_name(country_name, filename)
    assert expected_result == result

def test_zero_locations_visitors_by_country_name():
    filename = "small_dataset_2.txt"
    country_name = "Egypt"
    expected_result = 0
    result = visitors_by_country_name(country_name, filename)
    assert expected_result == result



def test_one_location_avg_rating_by_country_name():
    filename = "small_dataset.txt"
    country_name = "Brazil"
    expected_result = 4.35 / 1
    result = avg_rating_by_country_name(country_name, filename)
    assert expected_result == result

def test_multiple_location_avg_rating_by_country_name():
    filename = "small_dataset.txt"
    country_name = "India"
    expected_result = (4.82+1.5+3.62) / 3
    result = avg_rating_by_country_name(country_name, filename)
    assert expected_result == result

def test_zero_location_avg_rating_by_country_name():
    filename = "small_dataset_2.txt"
    country_name = "Egypt"
    expected_result = 0
    result = avg_rating_by_country_name(country_name, filename)
    assert expected_result == result


def test_single_category_popular_category():
    filename = "small_dataset.txt"
    country_name = "Australia"
    expected_result = "Nature"
    result = popular_category(country_name, filename)
    assert expected_result == result

def test_multiple_category_popular_category():
    filename = "small_dataset_2.txt"
    country_name = "India"
    Nature_visitors = 589849 + 677699
    Beach_visitors = 466796 + 439423
    if Nature_visitors > Beach_visitors:
        expected_result = "Nature"
    else:
        expected_result = "Beach"
    result = popular_category(country_name, filename)
    assert expected_result == result


def test_no_accomodation_available_num_of_accomodations():
    filename = "small_dataset.txt"
    country = "France"
    expected_result = 0.00
    result = num_of_accomodations(country, filename)
    assert expected_result == result

def test_all_accomodation_available_num_of_accomodations():
    filename = "small_dataset.txt"
    country = "India"
    expected_result = 100.00
    result = num_of_accomodations(country, filename)
    assert expected_result == result

def test_no_country_num_of_accomodations():
    filename = "small_dataset_2.txt"
    country = "Egypt"
    expected_result = 0.00
    result = num_of_accomodations(country, filename)
    assert expected_result == result


def test_one_location_total_revenue():
    filename = "small_dataset.txt"
    country = "Brazil"
    expected_result = 95607.25
    result = total_revenue(country, filename)
    assert expected_result == result

def test_multiple_locations_total_revenue():
    filename = "small_dataset.txt"
    country = "India"
    expected_result = 59869.33 + 303651.03 + 179208.55
    result = total_revenue(country, filename)
    assert expected_result == result


def test_multiple_locations_get_locations_by_popular_category():
    filename = "small_dataset.txt"
    country = "India"
    expected_result = ["Location: Jaipur                        Visitors: 811018         Rating: 1.5         Accomodation Available: Yes"]
    result = get_locations_by_popular_category(filename, country)
    assert expected_result == result

def test_one_locations_get_locations_by_popular_category():
    filename = "small_dataset.txt"
    country = "France"
    expected_result = ["Location: French Alps                   Visitors: 324369         Rating: 1.85        Accomodation Available: No"]
    result = get_locations_by_popular_category(filename, country)
    assert expected_result == result


def test_multiple_locations_top_rated():
    filename = "small_dataset.txt"
    country = "India"
    expected_result = "Location: Jim Corbett National Park     Category: Nature         Visitors: 589849    Rating: 4.82   Accomodation Available: Yes\n"
    result = top_rated(country, filename)
    assert expected_result == result

def test_one_locations_top_rated():
    filename = "small_dataset.txt"
    country = "USA"
    expected_result = "Location: Miami Beach                   Category: Beach          Visitors: 859352    Rating: 4.85   Accomodation Available: No\n"
    result = top_rated(country, filename)
    assert expected_result == result

