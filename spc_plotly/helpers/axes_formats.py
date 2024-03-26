from pandas import Series
import plotly.graph_objects as go
from spc_plotly.utils import rounded_value, rounding_multiple


def _format_xaxis(anchor: str, matches: str, showticklabels: bool):
    """
    X-axis formatter

    Parameters:
        anchor (str): Axis to anchor on
        matches (str): Axis to match on
        showticklabels (bool): Show axis ticklabels

    Returns:
        dict: Axis formatting
    """
    return {
        "anchor": anchor,
        "domain": [0.0, 1.0],
        "automargin": True,
        "dtick": "M1",
        "matches": matches,
        "showticklabels": showticklabels,
        "tickformat": "%b\n%Y",
        "ticklabelmode": "period",
        "tickangle": 0,
        "showspikes": True,
        "spikemode": "across+toaxis",
        "spikesnap": "cursor",
        "showline": True,
        "showgrid": True,
        "spikedash": "solid",
        "spikecolor": "lightgreen",
    }


def _format_yaxis(
    anchor: str, title: str, domain: list, range: list, tickformat: str, dtick: int
):
    """
    Y-axis formatter

    Parameters:
        anchor (str): Axis to anchor on
        matches (str): Axis to match on
        showticklabels (bool): Show axis ticklabels

    Returns:
        dict: Axis formatting
    """
    return {
        "anchor": anchor,
        "title": {"text": title},
        "domain": domain,
        "range": range,
        "tickformat": tickformat,
        "dtick": dtick,
    }


def _format_XmR_axes(
    npl_upper: float | list,
    npl_lower: float | list,
    mR_upper: float,
    y_Ser: Series,
    mR_data: Series,
    sloped: bool,
) -> go.Figure:
    """
    Apply axes formats

    Parameters:
        npl_upper (float|list): Upper process limit. If sloped is True, this is a list of tuples.
        npl_lower (float|list): Lower process limit. If sloped is True, this is a list of tuples.
        mR_upper (float): Upper moving range limit.
        y_Ser (Series): Series of y-values
        mR_data (Series): Series of moving range values
        sloped (bool): Use sloping approach for limit values.

    Returns:
        dict: Axis formatting
    """

    xaxis_values = _format_xaxis(anchor="y", matches="x", showticklabels=True)
    xaxis_mR = _format_xaxis(anchor="y2", matches="x2", showticklabels=False)

    if sloped:
        value_range = npl_upper[len(npl_upper) - 1][1] - npl_lower[0][1]
        dtick = rounding_multiple.rounding_multiple(value_range)
        min_range = rounded_value.rounded_value(npl_lower[0][1], dtick)
        max_range = rounded_value.rounded_value(
            npl_upper[len(npl_upper) - 1][1], dtick, "up"
        )
    else:
        value_range = npl_upper - npl_lower
        dtick = rounding_multiple.rounding_multiple(value_range)
        min_range = min(
            rounded_value.rounded_value(y_Ser.min(), dtick, "down"),
            rounded_value.rounded_value(npl_lower - (value_range * 0.1), dtick, "down"),
        )
        max_range = max(
            rounded_value.rounded_value(y_Ser.max(), dtick, "up"),
            rounded_value.rounded_value(npl_upper + (value_range * 0.1), dtick, "up"),
        )

    yaxis_values = _format_yaxis(
        anchor="x",
        title=y_Ser.name,
        domain=[0.4, 1.0],
        range=[min_range, max_range],
        tickformat="0",
        dtick=dtick,
    )

    dtick = rounding_multiple.rounding_multiple(mR_upper)
    max_range = max(
        rounded_value.rounded_value(mR_upper.max(), dtick, "up"),
        rounded_value.rounded_value(mR_data.max() + (mR_data.max() * 0.1), dtick, "up"),
    )

    yaxis_mR = _format_yaxis(
        anchor="x2",
        title="Moving Range",
        domain=[0.0, 0.3],
        range=[0, max_range],
        tickformat="0",
        dtick=dtick,
    )

    return {
        "x_values": xaxis_values,
        "x_mR": xaxis_mR,
        "y_values": yaxis_values,
        "y_mR": yaxis_mR,
    }
