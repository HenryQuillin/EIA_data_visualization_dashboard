import eia
import pandas as pd
import plotly.express as px



def retrieve_time_series(api, series_ID):
    """
    Return the time series dataframe, based on API and unique Series ID
    """
    #Retrieve Data By Series ID 
    series_search = api.data_by_series(series=series_ID)
    ##Create a pandas dataframe from the retrieved time series
    df = pd.DataFrame(series_search)
    return df

def main():
    #Create EIA API using your specific API key
    api_key = "3c109e8bc5897c4015d86e77e699ebc6"
    api = eia.API(api_key)
    #Declare desired series ID
    series_ID='TOTAL.SOT5PUS.A'
    global df
    df = retrieve_time_series(api, series_ID)
    #Print the returned dataframe df


if __name__== "__main__":
    main()
print(df)
print(list(df.columns))
#fig = px.line(df, x="Period", y="Value", title='Net generation')
#fig.show()
