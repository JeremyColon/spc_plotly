from pandas import DataFrame


def get_line_endpoints(path: list, data: DataFrame):
    """
    Get line endpoints from a path

    Parameters:
        path (list[tuple]): List of tuples representing points in a contiguous path
        data (DataFrame): Series of values

    Returns:
        dict: Start and end (x,y) values
    """
    start_y = path[0][1]
    end_y = path[len(path) - 1][1]

    start_x = data.index[path[0][0]]
    end_x = data.index[data.shape[0] - 1]

    return {"start": dict(x=start_x, y=start_y), "end": dict(x=end_x, y=end_y)}
