import pandas as pd
import numpy as np

main = pd.read_csv("Grades.csv")
main.rename(
    {
        "8-4": "Last Name",
        "Unnamed: 1": "First Name",
        "Unnamed: 2": "Email",
        "Unnamed: 3": "Average",
    },
    axis=1,
    inplace=True,
)
main.at[1, "First Name"] = 100
main.at[1, "Email"] = 100
main.at[1, "Average"] = 100
main.at[0, "Last Name"] = "Last Name"
main.at[0, "First Name"] = "First Name"
main.at[0, "Email"] = "Email"
main.at[0, "Average"] = "Average"
df = pd.DataFrame()

for x in range(main.iloc[1].size):
    if main.iloc[1, x] is not np.NaN:
        temp = main.iloc[:, x].tolist()
        df[temp[0]] = temp[1:]

df.to_csv("graded.csv")
