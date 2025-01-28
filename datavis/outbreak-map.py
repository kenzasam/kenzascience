import pandas as pd
import math
import plotly.express as px
import plotly.graph_objects as go

# Assuming your data has columns: latitude, longitude, location_name, cases, date
# If you need to get coordinates from location names, you can use the geocoding part below
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter



def get_coordinates(location):
    try:
        loc = geocode(location)
        return pd.Series([loc.latitude, loc.longitude])
    except:
        return pd.Series([None, None])

def create_outbreak_map(df):
    """
    Create an interactive map showing outbreak locations and intensity
    
    Parameters:
    df: pandas DataFrame with columns:
        - latitude: float
        - longitude: float
        - location_name: str
        - cases: int (number of culled birds)
    """
    
    # Create a better scaling function for sizes between 0 and 3 million
    def scale_size(x):
        if x == 0:
            return 0
        # Using log base transformation for better distribution
        # Multiply by 7 to get a good visual range
        return min(max(math.log(x + 1, 10) * 7, 5), 50)
    

    # Create the base map
    fig = go.Figure()

    # Add the scatter mapbox trace
    fig.add_trace(go.Scattergeo(
        lon=df['longitude'],
        lat=df['latitude'],
        text=df.apply(lambda row: f"Location: {row['location_name']}<br>"
                                 f"Cases: {row['cases']:,}<br>",
                     axis=1),
        mode='markers',
        marker=dict(
            size=df['cases'].apply(scale_size),  # Scale marker size
            color=df['cases'],
            colorscale='Reds',
            colorbar_title="# Cases",
            showscale=True,
            opacity=0.7,
        ),
        hoverinfo='text'
    ))

    # Update the layout
    fig.update_layout(
        geo=dict(
            scope='usa',  # Can be changed to 'world', 'europe', etc.
            showland=True,
            landcolor='rgb(243, 243, 243)',
            countrycolor='rgb(204, 204, 204)',
            showsubunits=True,
            subunitcolor='rgb(155, 155, 155)',
            showlakes=True,
            lakecolor='rgb(255, 255, 255)',
            showocean=True,
            oceancolor='rgb(230, 230, 250)'
        ),
    )

    return fig


# Read your data
fig_path ="" #your file path
data_path="" #your raw data cvs path
df = pd.read_csv(data_path, encoding = 'utf-16', sep ='\t')
df['location_name'] = df['State'] + ', ' + df['County Name']
# convert string to an integer
df['cases'] = df['cases'].str.replace(",", "")
df['cases'] = df['cases'].fillna(0).astype(int)
print("data loaded")
# If you need to geocode locations:
geolocator = Nominatim(user_agent="outbreak_ks")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
df[['latitude', 'longitude']] = df['location_name'].apply(get_coordinates)
print ('got coordinates')
# Create and show the map
fig = create_outbreak_map(df)
fig.show()
fig.write_html(fig_path, include_plotlyjs=True, full_html=False, config={"responsive": True})