import pandas

data_file = pandas.read_csv("2018_Squirrel_Data.csv")

color_col = data_file["Primary Fur Color"]
color_list = color_col.to_list()

gray_sq = color_list.count("Gray")
cinnamon_sq = color_list.count("Cinnamon")
black_sq = color_list.count("Black")

final_data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_sq, cinnamon_sq, black_sq]
}

final_data = pandas.DataFrame(final_data)

final_data.to_csv("squirrel_count.csv")

