from pandas import DataFrame
from spc_plotly.utils import rounded_value, rounding_multiple


def _limit_line_annotation(
    font: dict,
    text: str,
    x: float,
    xanchor: str,
    xref: str,
    y: float,
    yanchor: str,
    yref: str,
    showarrow: bool = False,
):
    """
    Annotation formatter. For documentation, see plotly's official docs

    Parameters:
        font (dict):
        text (str):
        x (float):
        xanchor (str):
        xref (str):
        y (float):
        yanchor (str):
        yref (str):
        showarrow (bool):

    Returns:
        dict: Axis formatting
    """
    return {
        "font": font,
        "text": text,
        "x": x,
        "xanchor": xanchor,
        "xref": xref,
        "y": y,
        "yanchor": yanchor,
        "yref": yref,
        "showarrow": showarrow,
    }


def _create_limit_line_annotations(
    data: DataFrame,
    chart_title: str,
    y_xmr_func,
    mR_upper,
    mR_xmr_func,
    npl_upper,
    npl_lower,
    y_name: str,
    sloped: bool,
):
    """
    Annotation formatter. For documentation, see plotly's official docs

    Parameters:
        data (DataFrame): All data
        chart_title (str): Chart title
        y_xmr_func (float|list): Natural process limit mid-line.
            If sloped is True, this is a list of tuples.
        mr_Upper (float|list): Upper moving range limit.
        mR_xmr_func (float|list): Moving range mid-line.
        npl_upper (float|list): Upper process limit. If sloped is True, this is a list of tuples.
        npl_lower (float|list): Lower process limit. If sloped is True, this is a list of tuples.
        y_name (str): Y-axis title.
        sloped (bool): Use sloping approach for limit values.

    Returns:
        dict: Axis formatting
    """

    other_font = {"size": 10}
    other_x = 0.01
    other_xanchor = "left"
    other_xref = "paper"

    # Create natural limits, mid-range lines, and center line annotations
    annotations = [
        _limit_line_annotation(
            font={"size": 16},
            text=chart_title,
            x=0.5,
            xanchor="center",
            xref="paper",
            y=1.1,
            yanchor="top",
            yref="paper",
        ),
        _limit_line_annotation(
            font=other_font,
            text=f"<b>mR Upper Limit = {round(mR_upper,3)}</b>",
            x=other_x,
            xanchor=other_xanchor,
            xref=other_xref,
            y=mR_upper + (mR_upper * 0.05),
            yanchor="auto",
            yref="y2",
        ),
    ]

    if sloped:
        # If using sloped lines, find the middle of the first and second half of the chart

        value_range = npl_upper[len(npl_upper) - 1][1] - npl_lower[0][1]

        half_idx = data.shape[0] // 2
        first_half_idx = data.values[:half_idx].shape[0] // 2
        first_half_date = first_half_idx / data.shape[0]
        second_half_idx = data.values[half_idx:].shape[0] // 2
        second_half_date = second_half_idx / data.shape[0]

        x_annotations = [
            _limit_line_annotation(
                font=other_font,
                text=f"<b>{round(y_xmr_func[first_half_idx][1],2)} "
                + "\u00B1"
                + f" {round(mR_xmr_func,2)}<b>",
                x=first_half_date,
                xanchor="center",
                xref="paper",
                y=npl_upper[first_half_idx][1] + (value_range * 0.1),
                yanchor="auto",
                yref="y",
            ),
            _limit_line_annotation(
                font=other_font,
                text=f"<b>{round(y_xmr_func[second_half_idx+half_idx][1],2)} "
                + "\u00B1"
                + f" {round(mR_xmr_func,2)}<b>",
                x=second_half_date,
                xanchor="center",
                xref="paper",
                y=npl_lower[half_idx + second_half_idx][1] - (value_range * 0.1),
                yanchor="auto",
                yref="y",
            ),
        ]

    else:

        value_range = npl_upper - npl_lower

        x_annotations = [
            _limit_line_annotation(
                font=other_font,
                text=f"<b>{y_name} Upper Limit = {round(npl_upper,3)}</b>",
                x=other_x,
                xanchor=other_xanchor,
                xref=other_xref,
                y=npl_upper + (value_range * 0.03),
                yanchor="auto",
                yref="y",
            ),
            _limit_line_annotation(
                font=other_font,
                text=f"<b>{y_name} Lower Limit = {round(npl_lower,3)}</b>",
                x=other_x,
                xanchor=other_xanchor,
                xref=other_xref,
                y=npl_lower - (value_range * 0.03),
                yanchor="auto",
                yref="y",
            ),
        ]

    annotations.extend(x_annotations)

    return annotations
