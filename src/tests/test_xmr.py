from pandas import to_datetime


def test_inputs(XmR, date_parts) -> bool:

    test_xmr_func_val(XmR.xmr_function)
    test_sloped_val(XmR.sloped)
    test_date_part_resolution_val(XmR.date_part_resolution, date_parts)
    test_custom_date_part_val(XmR.date_part_resolution, XmR.custom_date_part)

    return True

def test_x_type(x_type: str, x_type_options: dict):
    """Test x_type parameter"""
    if x_type not in x_type_options:
        raise ValueError(
            f"x_type must be one of {list(x_type_options.keys())}"
        )

    return True

def test_xmr_func_val(xmr_func_val):
    if xmr_func_val.lower() not in ["mean", "median"]:
        e = f"{xmr_func_val} not a valid xmr function option. Must be 'mean' or 'median'"
        raise ValueError(e)

    return True


def test_date_resolution(date_part_resolution: str, date_parts: dict):
    """Test date_part_resolution parameter"""
    if date_part_resolution not in date_parts:
        raise ValueError(
            f"date_part_resolution must be one of {list(date_parts.keys())}"
        )

    return True


def test_custom_date_part_val(date_part_resolution_val, custom_date_part_val):
    if date_part_resolution_val == "custom":
        if custom_date_part_val is None or custom_date_part_val == "":
            e = "Must specify a valid date part format. Please visit https://d3js.org/d3-time-format for reference."
            raise ValueError(e)

    return True


def test_x_ser_name_val(x_ser_name, data):
    if x_ser_name in data.columns or x_ser_name == data.index.name:
        return True
    else:
        e = f"{x_ser_name} not a valid column or index in your dataframe"
        raise ValueError(e)


def test_x_ser_is_date(x_Ser):
    try:
        to_datetime(x_Ser)
    except:
        e = f"{x_Ser.name} can not be converted to datetime format. Please inspect data for erroneous values."
        raise TypeError(e)


def test_y_ser_name_val(y_ser_name, data):
    if y_ser_name not in data.columns:
        e = f"{y_ser_name} not a valid column"
        raise ValueError(e)

    return True


def test_cutoff_val(cutoff_val, x_Ser):
    if cutoff_val is None or cutoff_val in x_Ser.values:
        return True
    else:
        print(cutoff_val)
        print(x_Ser)
        e = f"{cutoff_val} not present in {x_Ser.name}"
        raise ValueError(e)


def test_begin_val(begin_val, x_Ser):
    if begin_val is None or begin_val in x_Ser.values:
        return True
    else:
        print(begin_val)
        print(x_Ser)
        e = f"{begin_val} not present in {x_Ser.name}"
        raise ValueError(e)


def test_sloped_val(sloped_val):
    if not isinstance(sloped_val, bool):
        e = f"sloped parameter must be a boolean value"
        raise ValueError(e)

def test_numeric_sequence():
    """Test numeric sequence handling"""
    data = pd.DataFrame({
        'position': [1, 3, 4, 7, 8],  # Note the gaps
        'value': [10, 12, 11, 13, 15]
    })
    
    with pytest.warns(UserWarning):
        chart = xmr.XmR(
            data=data,
            x_ser_name='position',
            y_ser_name='value',
            x_type='numeric'
        )

def test_categorical_sequence():
    """Test categorical sequence handling"""
    data = pd.DataFrame({
        'station': ['B', 'A', 'D', 'C'],  # Unsorted
        'value': [10, 12, 11, 13]
    })
    
    with pytest.warns(UserWarning):
        chart = xmr.XmR(
            data=data,
            x_ser_name='station',
            y_ser_name='value',
            x_type='categorical'
        )

