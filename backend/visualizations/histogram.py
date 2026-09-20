import plotly.express as px

def create_histogram(data, bins):
    figure = px.histogram(
        x = data, 
        nbins = bins
    )

    figure.update_layout(
        title = 'histogram',
        xaxis_title = 'Values',
        yaxis_title = 'Frequency'
    )

    return figure


if __name__ == "__main__":
    data = [10, 20, 20, 30, 40, 50]

    figure = create_histogram(data, bins=5)

    figure.write_html("histogram.html")