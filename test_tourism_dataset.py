import pandas as pd
from analyze_tourism_dataset import popular_category
from analyze_tourism_dataset import num_of_accomodations
from analyze_tourism_dataset import get_locations_by_popular_category
from analyze_tourism_dataset import top_rated
from analyze_tourism_dataset import most_visitors

def test_single_category_popular_category():
    df = pd.read_csv("Tourism-Analyzer/small_dataset.txt")
    country_name = "Australia"
    expected_result = "Nature"
    result = popular_category(df, country_name)
    assert expected_result == result

def test_multiple_category_popular_category():
    df = pd.read_csv("Tourism-Analyzer/small_dataset_2.txt")
    country_name = "India"
    Nature_visitors = 589849 + 677699
    Beach_visitors = 466796 + 439423
    if Nature_visitors > Beach_visitors:
        expected_result = "Nature"
    else:
        expected_result = "Beach"
    result = popular_category(df, country_name)
    assert expected_result == result


def test_no_accomodation_available_num_of_accomodations():
    df = pd.read_csv("Tourism-Analyzer/small_dataset.txt")
    country = "France"
    expected_result = 0.00
    result = num_of_accomodations(df, country)
    assert expected_result == result

def test_all_accomodation_available_num_of_accomodations():
    df = pd.read_csv("Tourism-Analyzer/small_dataset.txt")
    country = "India"
    expected_result = 100.00
    result = num_of_accomodations(df, country)
    assert expected_result == result

def test_no_country_num_of_accomodations():
    df = pd.read_csv("Tourism-Analyzer/small_dataset_2.txt")
    country = "Egypt"
    expected_result = 0.00
    result = num_of_accomodations(df, country)
    assert expected_result == result

def test_multiple_locations_get_locations_by_popular_category():
    df = pd.read_csv("Tourism-Analyzer/small_dataset.txt")
    country = "India"
    expected_result = ["Location: Jaipur                        Visitors: 811018         Rating: 1.5         Accomodation Available: Yes"]
    result = get_locations_by_popular_category(df, country)
    assert expected_result == result

def test_one_locations_get_locations_by_popular_category():
    df = pd.read_csv("Tourism-Analyzer/small_dataset.txt")
    country = "France"
    expected_result = ["Location: French Alps                   Visitors: 324369         Rating: 1.85        Accomodation Available: No"]
    result = get_locations_by_popular_category(df, country)
    assert expected_result == result


def test_multiple_locations_top_rated():
    df = pd.read_csv("Tourism-Analyzer/small_dataset.txt")
    country = "India"
    expected_result = "Location: Jim Corbett National Park     Category: Nature         Visitors: 589849    Rating: 4.82   Accomodation Available: Yes\n"
    result = top_rated(df, country)
    assert expected_result == result

def test_one_locations_top_rated():
    df = pd.read_csv("Tourism-Analyzer/small_dataset.txt")
    country = "USA"
    expected_result = "Location: Miami Beach                   Category: Beach          Visitors: 859352    Rating: 4.85   Accomodation Available: No\n"
    result = top_rated(df, country)
    assert expected_result == result

def test_multiple_locations_most_visitors():
    df = pd.read_csv("Tourism-Analyzer/small_dataset.txt")
    country = "India"
    expected_result = "Location: Jaipur              Category: Cultural       Visitors: 811018    Rating: 1.5    Accomodation Available: Yes\n"
    result = most_visitors(df, country)
    assert result in expected_result

def test_one_locations_most_visitors():
    df = pd.read_csv("Tourism-Analyzer/small_dataset.txt")
    country = "China"
    expected_result = "Location: Great Wall          Category: Historical     Visitors: 652046    Rating: 2.5    Accomodation Available: Yes\n"
    result = most_visitors(df, country)
    assert result in expected_result