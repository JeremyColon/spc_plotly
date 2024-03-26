def calc_xmr_func(data, func="mean"):
    """
    Calculate aggregate function

    Parameters:
        data (Series): Series of values
        func (str): Mean or median

    Returns:
        Float: Mean or median value of data
    """
    if func == "mean":
        return data.mean()
    elif func == "median":
        return data.median()
    else:
        raise ValueError("Invalid function")
