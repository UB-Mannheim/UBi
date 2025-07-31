import plotly.graph_objects as go
import requests
from translations import translate


def get_occupancy_data():
    url = "https://www2.bib.uni-mannheim.de/occupancy/?output=json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def make_plotly_figure(areas, detected_language: str = "German"):
    """
    Plot seat availability.
    """
    sorted_areas = sorted(
        areas.values(), key=lambda a: a["percent"], reverse=True
    )

    labels = []
    occupancy = []
    colors = []
    percent_text = []
    top_annotations = []

    for area in sorted_areas:
        name = area["name"]
        percent = area["percent"]
        capacity = area["capacity"]
        occupied = round((percent / 100) * capacity)

        labels.append(name)
        occupancy.append(percent)

        if percent >= 80:
            colors.append("#FF6B6B")  # red
        elif percent >= 50:
            colors.append("#FFA940")  # orange
        else:
            colors.append("#002F5C")  # cooler green

        percent_text.append(f"{percent}%")
        top_annotations.append(
            dict(
                x=name,
                y=percent + 4,
                text=f"{occupied} / {capacity}",
                showarrow=False,
                font=dict(size=14),
                yanchor="bottom",
            )
        )

    fig = go.Figure(
        data=[
            go.Bar(
                x=labels,
                y=occupancy,
                marker_color=colors,
                text=percent_text,
                textposition="inside",
                insidetextanchor="middle",
                insidetextfont=dict(size=14, color="white", family="Arial"),
                hoverinfo="x+y",
            )
        ]
    )

    fig.update_layout(
        title={
            "text": translate("seats_plot_title", detected_language),
            "font": {
                "size": 18,
                "family": "Arial Black, Arial, sans-serif",
                "color": "black",
            },
        },
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(family="Arial", size=14),
        yaxis=dict(
            title=translate("seats_label_y_axis", detected_language),
            title_font_size=14,
            tickfont_size=14,
            range=[0, 100],
            gridcolor="rgba(0,0,0,0.05)",
            zeroline=False,
            showline=False,
        ),
        xaxis=dict(tickfont_size=14, showline=False),
        height=550,
        margin=dict(t=80, b=70, l=60, r=60),
        annotations=top_annotations,
    )

    return fig
