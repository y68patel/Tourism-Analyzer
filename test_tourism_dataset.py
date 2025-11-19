from analyze_tourism_dataset import unique_list
from analyze_tourism_dataset import visitors_by_country_name


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