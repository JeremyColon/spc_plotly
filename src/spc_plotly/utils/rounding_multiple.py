from math import log10, floor, ceil


def rounding_multiple(value: float, rounding_direction: str = "down") -> int:
    """
    Calculate ideal multiple based on value. This is primarily used to help calculate
        the y-axis min/max range values.

    Parameters:
        value (float): Raw value to use for calculations
        rounding_direction (str): Round up or down

    Returns:
        dict: Start and end (x,y) values
    """

    if rounding_direction not in ["up", "down"]:
        raise "rounding direction must be 'up' or 'down'"

    orders_of_magnitude = log10(value) - 1
    rounding_multiple = (10 ** floor(orders_of_magnitude)) / 2
    dtick_multiple = (10**orders_of_magnitude) / rounding_multiple

    # If there is a positive order of magnitude then we are most likely working with
    #   counts. In this case, we want a multiple that is easily countable and will produce
    #   a clean y-axis. 50, 500, etc.
    #   If order of magnitude is negative, then we are most likely working with rates and
    #   so we have to use a decimal multiple.
    if orders_of_magnitude > 0:
        if rounding_direction == "down":
            return int(floor(dtick_multiple) * rounding_multiple)
        else:
            return int(ceil(dtick_multiple) * rounding_multiple)
    else:
        return round(dtick_multiple * rounding_multiple, -floor(orders_of_magnitude))
