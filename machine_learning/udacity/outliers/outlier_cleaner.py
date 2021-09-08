#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    import numpy as np
        
    cleaned_data = []

    ### your code goes here
    # calculate residuals
    residuals = np.abs(predictions - net_worths)
    
    
    # remove the 10% with highest errors
    n = int(ages.shape[0] * 0.90)
    print(n)
    
    non_outliers = np.argsort(residuals.flatten())[:n]
    
    residuals = residuals[non_outliers]
    clean_ages = ages[non_outliers]
    clean_networths = net_worths[non_outliers]
    
    for age, net_worth, error in zip(clean_ages, clean_networths, residuals):
        cleaned_data.append((age, net_worth, error))
    
    return cleaned_data

