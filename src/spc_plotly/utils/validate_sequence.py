from pandas import DataFrame
import warnings
import pandas as pd

def validate_sequence(data: DataFrame, x_ser_name: str, x_type: str) -> tuple[bool, bool]:
    """
    Validates that the input sequence is properly ordered and identifies gaps.
    
    Args:
        data: DataFrame containing the data
        x_ser_name: Name of the column containing x-axis values
        x_type: Type of x-axis data ('date_time', 'numeric', or 'categorical')
    
    Returns:
        tuple: (is_sorted, has_gaps)
    """
    is_sorted = True
    has_gaps = False
    
    x_series = data[x_ser_name] if x_ser_name in data.columns else data.index
    
    # Check if data is sorted
    if x_type == "date_time":
        try:
            x_series_dt = pd.to_datetime(x_series)
            is_sorted = x_series_dt.is_monotonic_increasing
            # Check for gaps in date sequence (only for day resolution or finer)
            if x_series_dt.dtype == 'datetime64[ns]':
                min_diff = x_series_dt.diff().min()
                max_diff = x_series_dt.diff().max()
                if max_diff > min_diff * 2:  # Simple gap detection
                    has_gaps = True
        except:
            is_sorted = x_series.is_monotonic_increasing
            
    elif x_type == "numeric":
        is_sorted = x_series.is_monotonic_increasing
        # Check for gaps in numeric sequence
        if x_series.dtype in ['int64', 'float64']:
            min_diff = x_series.diff().min()
            max_diff = x_series.diff().max()
            if max_diff > min_diff * 2:  # Simple gap detection
                has_gaps = True
            
    elif x_type == "categorical":
        is_sorted = x_series.is_monotonic_increasing
    
    if not is_sorted:
        warnings.warn(
            "Data is not sorted. Data will be automatically sorted, but please verify the order is correct.",
            UserWarning
        )
        
    if has_gaps:
        warnings.warn(
            "Gaps detected in the sequence. Chart will be created without gaps, but please verify this is intended.",
            UserWarning
        )
    
    return is_sorted, has_gaps