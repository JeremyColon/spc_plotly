from plotly.graph_objects import Figure


def _menu(
    fig: Figure,
    limit_lines: list,
    limit_line_annotations: list,
    long_run_shapes: list,
    short_run_shapes: list,
) -> Figure:
    """
    Creates menu on figure for user to show anomalous points, long runs, or short runs

    Parameters:
        fig (Figure): XmR Chart figure object to be updated
        limit_lines (list): List of dictionaries representing limit line shapes, specifically "lines".
        limit_line_annotations (list): List of dictionaries representing chart annotations.
        long_run_shapes (list): List of dictionaries representing "path" shapes for long runs.
        short_run_shapes (list): List of dictionaries representing "path" shapes for short runs.

    Returns:
        Figure: Passed in XmR chart figure object updated to include menu for selecting anomalous point, long runs, or short runs
    """
    return fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                direction="right",
                active=0,
                x=0.5,
                xanchor="center",
                y=1.2,
                buttons=list(
                    [
                        dict(
                            label="None",
                            method="update",
                            args=[
                                {"visible": [True, True, False, False]},
                                {
                                    "shapes": limit_lines,
                                    "annotations": limit_line_annotations,
                                },
                            ],
                        ),
                        dict(
                            label="Anomalies",
                            method="update",
                            args=[
                                {"visible": [True, True, True, True]},
                                {
                                    "shapes": limit_lines,
                                    "annotations": limit_line_annotations,
                                },
                            ],
                        ),
                        dict(
                            label="Long Runs",
                            method="update",
                            args=[
                                {"visible": [True, True, False, False]},
                                {
                                    "shapes": limit_lines + long_run_shapes,
                                    "annotations": limit_line_annotations,
                                },
                            ],
                        ),
                        dict(
                            label="Short Runs",
                            method="update",
                            args=[
                                {"visible": [True, True, False, False]},
                                {
                                    "shapes": limit_lines + short_run_shapes,
                                    "annotations": limit_line_annotations,
                                },
                            ],
                        ),
                        dict(
                            label="All",
                            method="update",
                            args=[
                                {"visible": [True, True, True, True]},
                                {
                                    "shapes": limit_lines
                                    + long_run_shapes
                                    + short_run_shapes,
                                    "annotations": limit_line_annotations,
                                },
                            ],
                        ),
                    ]
                ),
            )
        ]
    )
