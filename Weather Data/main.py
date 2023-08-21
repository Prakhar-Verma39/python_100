# # import csv
# #
# # with open("weather_data.csv") as f:
# #     data = csv.reader(f)  # iterable object by csv module
# #     temperature = []
# #     #  data exit when file is opened
# #     for row in data:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# #     print(temperature)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# data_list = data["temp"].to_list()
# print(sum(data_list)/len(data_list))
# print(data["temp"].max())
#
# # print a data from a row
# print(data[data.temp == data["temp"].max()])
# monday = data[data.day == "Monday"]
# print((monday.temp*9/5 + 32))

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

df = pandas.DataFrame({"Fur Color": ["Gray", "Cinnamon", "Black"], "Count": [gray_count, red_count, black_count]})
df.to_csv("sq.csv")