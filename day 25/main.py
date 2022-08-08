# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# t_list = data["temp"]
#
# # avg = sum(t_list)/ len(t_list)
# # print(avg)
# # print(data["temp"].mean())
# # print(data["temp"].max())
#
# # print(data[data.temp == data.temp.max()])
#
#
# # Create a new dataframe from scratch
# data_di = {
#     "students": ["A", "B", "C"],
#     "scores": [80, 90, 95]
# }
# data = pandas.DataFrame(data_di)
# data.to_csv("new csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
G_sq = len(data[data["Primary Fur Color"] == "Gray"])
C_sq = len(data[data["Primary Fur Color" ]== "Cinnamon"])
B_sq = len(data[data["Primary Fur Color"] == "Black"])

data_di = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [G_sq, C_sq, B_sq]
}

df = pandas.DataFrame(data_di)
df.to_csv("Sq_count.csv")







