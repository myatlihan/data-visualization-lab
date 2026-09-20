"""
Descriptive statistics functions.

This module contains basic statistical measures such as
mean, median, mode, range, variance, and standard deviation.
"""


def validate_data(data):
    """
    Validate that the dataset is not empty.

    Raises:
        ValueError: If the dataset is empty.
    """
    if not data:
        raise ValueError("Dataset cannot be empty.")


def mean(data):
    """
    Calculate the arithmetic mean of a dataset.

    Formula:
        mean = sum of values / number of observations
    """

    validate_data(data)
    total = sum(data)

    count = len(data)
    
    return round(total / count, 2)


def median(data):
    """
    Calculate the median of a dataset.

    The data is sorted first.
    - Odd number of observations: return the middle value.
    - Even number of observations: return the average of the two middle values.
    """

    validate_data(data)
    sorted_data = sorted(data)

    count = len(data)

    middle = count // 2

    if count % 2  != 0:
        return sorted_data[middle]

    left = sorted_data[middle -1]
    right = sorted_data[middle]
    
    return (left + right ) / 2


def mode(data):
    """
    Calculate the mode of a dataset.

    The mode is the value that occurs most frequently.
    This implementation returns the first value with the highest frequency.
    """

    validate_data(data)
    frequencies = {}

    for value in data:
        if value in frequencies:
            frequencies[value] += 1
        else:
            frequencies[value] = 1

    most_frequent_value = None
    highest_count = 0

    for value in frequencies:
        if frequencies[value] > highest_count:
            highest_count = frequencies[value]
            most_frequent_value = value
    
    return most_frequent_value

                
def minimum(data):
    """
    Return the smallest value in a dataset.

    The function compares each value with the current minimum
    and keeps the smaller one.
    """  
    validate_data(data)

    smallest = data[0]

    for value in data:
        if value < smallest:
            smallest = value
    
    return smallest

def maximum(data):
    """
    Return the largest value in a dataset.

    The function compares each value with the current maximum
    and keeps the larger one.
    """

    validate_data(data)
    largest = data[0]

    for value in data:
        if value > largest:
            largest = value
    
    return largest


def data_range(data):
    """
    Calculate the range of a dataset.

    Formula:
        range = maximum - minimum
    """

    validate_data(data)
    range = maximum(data) - minimum(data)
    
    return range



def first_quartile(data):
    """
    Calculate the first quartile (Q1) using the median-of-halves method.

    Q1 is the median of the lower half of the sorted dataset.
    """

    validate_data(data)
    sorted_data = sorted(data)

    count = len(sorted_data)
    middle = count // 2

    lower_half = sorted_data[:middle]
    
    return median(lower_half)


def third_quartile(data):
  
    """
    Calculate the third quartile (Q3) using the median-of-halves method.

    Q3 is the median of the upper half of the sorted dataset.
    The overall median is excluded when the dataset has an odd number
    of observations.
    """

    validate_data(data)

    sorted_data = sorted(data)
    count = len(sorted_data)

    middle = count // 2

    if count % 2 != 0:
        upper_half = sorted_data[middle + 1:]
    else:
        upper_half = sorted_data[middle:]

    return median(upper_half)




def interquartile_range(data):
    """
    Calculate the interquartile range (IQR) of a dataset.

    Formula:
        IQR = Q3 - Q1

    IQR represents the spread of the middle 50% of the data.
    """

    validate_data(data)
    iqr = third_quartile(data) - first_quartile(data)
    
    return iqr


def variance(data):
    """
    Calculate the population variance of a dataset.

    Variance measures how far the values are spread from the mean.

    Formula:
        variance = sum((x - mean)^2) / number of observations
    """ 
    validate_data(data)

    avarage = mean(data)

    squared_differece = []

    for value in data:
        difference = (avarage -value) 
        difference = difference ** 2
        squared_differece.append(difference)

    sum_data = 0
    for value in squared_differece:
        sum_data += value

    
    return round(sum_data / len(squared_differece), 2)


def standard_deviation(data):
    """
    Calculate the population standard deviation of a dataset.

    Standard deviation is the square root of variance and
    represents the typical spread of values around the mean.

    Formula:
        standard deviation = sqrt(variance)
    """

    validate_data(data)

    return round(variance(data) ** 0.5, 2)



def outliers(data):
    """
    Identify outliers using the 1.5 × IQR rule.

    Values below Q1 - 1.5 × IQR or above
    Q3 + 1.5 × IQR are considered outliers.
    """
    validate_data(data)

    q1 = first_quartile(data)
    q3 = third_quartile(data)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    result = []

    for value in data:
        if value < lower_bound or value > upper_bound:
            result.append(value)
    return result

          

if __name__ == "__main__":
    data = [10, 10, 20, 30, 40, 50, 60, 70, 80, 500]

    print("Dataset:", data)
    print("Mean:", mean(data))
    print("Median:", median(data))
    print("Mode:", mode(data))
    print("Minimum:", minimum(data))
    print("Maximum:", maximum(data))
    print("Range:", data_range(data))
    print("Q1:", first_quartile(data))
    print("Q3:", third_quartile(data))
    print('IQR:', interquartile_range(data))
    print('Variance:', variance(data))
    print("Standard Deviation:", standard_deviation(data))
    print("Outliers:", outliers(data))