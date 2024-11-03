from pandas import Series
from plotly.graph_objects import Figure, Scatter
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def _create_base_traces(
    x_Ser: Series,
    y_Ser: Series,
    mR_data: Series,
    x_type: str,
    chart_line_color: str = "black",
    chart_marker_color: str = "black",
    chart_line_width: int = 1,
    chart_marker_size: int = 6,
) -> list:
    """Create base traces for XmR chart"""
    
    # Handle hover template based on x-axis type
    if x_type == "date_time":
        hovertemplate = (
            "<b>Date:</b> %{x|%Y-%m-%d}<br>"
            "<b>Value:</b> %{y:.2f}<br>"
            "<extra></extra>"
        )
    elif x_type == "numeric":
        hovertemplate = (
            "<b>Position:</b> %{x}<br>"
            "<b>Value:</b> %{y:.2f}<br>"
            "<extra></extra>"
        )
    else:  # categorical
        hovertemplate = (
            "<b>Category:</b> %{x}<br>"
            "<b>Value:</b> %{y:.2f}<br>"
            "<extra></extra>"
        )

    traces = [
        go.Scatter(
            x=x_Ser,
            y=y_Ser,
            mode="lines+markers",
            name=y_Ser.name,
            line={"color": chart_line_color, "width": chart_line_width},
            marker={"color": chart_marker_color, "size": chart_marker_size},
            hovertemplate=hovertemplate,
        ),
        go.Scatter(
            x=x_Ser,
            y=mR_data,
            mode="lines+markers",
            name="Moving Range",
            line={"color": chart_line_color, "width": chart_line_width},
            marker={"color": chart_marker_color, "size": chart_marker_size},
            xaxis="x2",
            yaxis="y2",
            hovertemplate=hovertemplate.replace("Value", "Range"),
        ),
    ]
    return traces

# def _base_traces(
#     x_Ser: Series, x_Ser_dt: Series, y_Ser: Series, mr_Data: Series
# ) -> Figure:
#     """
#     Create base traces for XmR chart

#     Parameters:
#         x_Ser (Series): Series of x-values
#         x_Ser_dt (Series): Series of x-values, datetime format
#         y_Ser (Series): Series of y-values
#         mR_data (Series): Series of moving range values

#     Returns:
#         Figure: Base XmR figure object
#     """

#     # Add XmR traces to figure
#     fig = make_subplots(
#         rows=2,
#         cols=1,
#         row_heights=[6, 4],
#         vertical_spacing=0.5,
#         shared_xaxes=True,
#         shared_yaxes=False,
#         column_titles=list(x_Ser),
#     )

#     fig.add_trace(
#         Scatter(
#             x=x_Ser,
#             y=y_Ser,
#             name=y_Ser.name,
#             marker_color="black",
#             hovertemplate=f"""<b>{x_Ser.name}:</b> """
#             """%{x|%B %Y}<br>"""
#             f"""<b>{y_Ser.name}:</b> """
#             """%{y}<br>"""
#             """<extra></extra>""",
#         ),
#         row=1,
#         col=1,
#     )
#     fig.add_trace(
#         Scatter(
#             x=x_Ser,
#             y=mr_Data,
#             name="Moving Range (mR)",
#             marker_color="black",
#             hovertemplate=f"""<b>{x_Ser.name}:</b> """
#             """%{x|%B %Y}<br>"""
#             f"""<b>{y_Ser.name} mR:</b> """
#             """%{y}<br>"""
#             """<extra></extra>""",
#         ),
#         row=2,
#         col=1,
#     )

#     return fig
