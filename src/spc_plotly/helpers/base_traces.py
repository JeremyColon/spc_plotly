from pandas import Series
from plotly.graph_objects import Figure, Scatter
from plotly.subplots import make_subplots


def _base_traces(
    x_Ser: Series, x_Ser_dt: Series, y_Ser: Series, mr_Data: Series
) -> Figure:
    """
    Create base traces for XmR chart

    Parameters:
        x_Ser (Series): Series of x-values
        x_Ser_dt (Series): Series of x-values, datetime format
        y_Ser (Series): Series of y-values
        mR_data (Series): Series of moving range values

    Returns:
        Figure: Base XmR figure object
    """

    # Add XmR traces to figure
    fig = make_subplots(
        rows=2,
        cols=1,
        row_heights=[6, 4],
        vertical_spacing=0.5,
        shared_xaxes=True,
        shared_yaxes=False,
        column_titles=list(x_Ser),
    )

    fig.add_trace(
        Scatter(
            x=x_Ser,
            y=y_Ser,
            name=y_Ser.name,
            marker_color="black",
            hovertemplate=f"""<b>{x_Ser.name}:</b> """
            """%{x|%B %Y}<br>"""
            f"""<b>{y_Ser.name}:</b> """
            """%{y}<br>"""
            """<extra></extra>""",
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        Scatter(
            x=x_Ser,
            y=mr_Data,
            name="Moving Range (mR)",
            marker_color="black",
            hovertemplate=f"""<b>{x_Ser.name}:</b> """
            """%{x|%B %Y}<br>"""
            f"""<b>{y_Ser.name} mR:</b> """
            """%{y}<br>"""
            """<extra></extra>""",
        ),
        row=2,
        col=1,
    )

    return fig
