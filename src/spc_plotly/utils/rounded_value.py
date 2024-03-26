from math import floor, ceil


def rounded_value(
    value: float, multiple: int | float, rounding_direction: str = "down"
) -> int | float:
    """
    Calculate rounded value based on multiple. This is primarily used to help calculate
        the y-axis min/max range values.

    Parameters:
        value (float): Value to round
        multiple (int | float): Multiple to use for rounding (i.e., round to the nearest multiple)
        rounding_direction (str): Round up or down

    Returns:
        int | float: Rounded value
    """

    if rounding_direction not in ["up", "down"]:
        raise "rounding direction must be 'up' or 'down'"

    if multiple >= 1:
        if rounding_direction == "down":
            return int(floor(value / multiple) * multiple)
        else:
            return int(ceil(value / multiple) * multiple)
    else:
        if rounding_direction == "down":
            return floor(value / multiple) * multiple
        else:
            return ceil(value / multiple) * multiple
