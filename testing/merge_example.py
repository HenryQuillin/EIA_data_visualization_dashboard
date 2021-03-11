import pandas as pd
climate_precip = pd.read_csv("https://github.com/realpython/materials/raw/master/introduction-combining-data-pandas-merge-join-and-concat/climate_precip.csv")
climate_temp = pd.read_csv('https://github.com/realpython/materials/raw/master/introduction-combining-data-pandas-merge-join-and-concat/climate_temp.csv')
precip_one_station = climate_precip[climate_precip["STATION"] == "GHCND:USC00045721"]

inner_merged = pd.merge(precip_one_station, climate_temp)
outer_merged = pd.merge(precip_one_station, climate_temp, how="outer", on=["STATION", "DATE"])
left_merged = pd.merge(precip_one_station, climate_temp, how="left", on=["STATION", "DATE"])
print('JOIN ----------')
print(precip_one_station.join(climate_temp, lsuffix="_left", rsuffix="_right"))


print(outer_merged.shape)
print(left_merged.shape)
