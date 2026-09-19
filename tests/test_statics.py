from backend.statistics.statics import (
    mean,
    median,
    mode,
    minimum,
    maximum,
    data_range,
    first_quartile,
    third_quartile,
    interquartile_range,
    variance,
    standard_deviation,
    outliers
)
import pytest




    
def test_mean():
    data = [10, 20, 30, 40, 50]

    result = mean(data)

    assert result == 30


def test_median_odd():
    data = [10, 30, 20, 50, 40]

    result = median(data)

    assert result == 30


def test_median_even():
    data = [10, 40, 20, 30]

    result = median(data)

    assert result == 25


def test_median_unsorted():
    data = [50, 10, 40, 20, 30]

    result = median(data)

    assert result == 30

def test_mode():
    data = [10, 20, 20, 30, 40, 20]
    result = mode(data)
    assert result == 20


def test_mode_unsorted():
    data = [30, 10, 20, 30, 40, 20, 30]

    result = mode(data)

    assert result == 30

def test_minimum():
    data = [30, 10, 50, 20, 40]

    result = minimum(data)

    assert result == 10


def test_maximum():
    data = [30, 10, 50, 20, 40]

    result = maximum(data)

    assert result == 50


def test_data_range():
    data = [10, 20, 30, 40, 50]

    result = data_range(data)

    assert result == 40

def test_first_quartile():
    data = [1, 2, 3, 4, 5, 6, 7, 8]

    result = first_quartile(data)

    assert result == 2.5


def test_third_quartile():
    data = [1, 2, 3, 4, 5, 6, 7, 8]

    result = third_quartile(data)

    assert result == 6.5


def test_interquartile_range():
    data = [1, 2, 3, 4, 5, 6, 7, 8]

    result = interquartile_range(data)

    assert result == 4

def test_variance():
    data = [2, 4, 6, 8, 10]

    result = variance(data)

    assert result == 8


def test_standard_deviation():
    data = [2, 4, 6, 8, 10]

    result = standard_deviation(data)

    assert result == 8 ** 0.5


def test_outliers():
    data = [10, 11, 12, 13, 14, 15, 100]

    result = outliers(data)

    assert result == [100]

def test_mean_empty():
    with pytest.raises(ValueError, match="Dataset cannot be empty."):
        mean([])

def test_median_empty():
    with pytest.raises(ValueError, match="Dataset cannot be empty."):
        median([])


def test_mode_empty():
    with pytest.raises(ValueError, match="Dataset cannot be empty."):
        mode([])


def test_minimum_empty():
    with pytest.raises(ValueError, match="Dataset cannot be empty."):
        minimum([])


def test_maximum_empty():
    with pytest.raises(ValueError, match="Dataset cannot be empty."):
        maximum([])


def test_variance_empty():
    with pytest.raises(ValueError, match="Dataset cannot be empty."):
        variance([])

def test_first_quartile_empty():
    with pytest.raises(ValueError, match="Dataset cannot be empty."):
        first_quartile([])


def test_third_quartile_empty():
    with pytest.raises(ValueError, match="Dataset cannot be empty."):
        third_quartile([])

def test_standard_deviation_empty():
    with pytest.raises(ValueError, match="Dataset cannot be empty."):
        standard_deviation([])

def test_data_range_empty():
    with pytest.raises(ValueError, match="Dataset cannot be empty."):
        data_range([])


def test_interquartile_range_empty():
    with pytest.raises(ValueError, match="Dataset cannot be empty."):
        interquartile_range([])


def test_outliers_empty():
    with pytest.raises(ValueError, match="Dataset cannot be empty."):
        outliers([])