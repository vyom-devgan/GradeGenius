import pandas as pd
import numpy as np

main = pd.read_csv("graded.csv")
avgs = main.loc[:, "Average"]
averages = []
for x in avgs:
    if x is np.NaN:
        averages.append("BLANK")
    elif x is not np.NaN:
        x = eval(x[:-1])
        if 95 <= x <= 100:
            averages.append("A+")
        elif 87 <= x < 95:
            averages.append("A")
        elif 80 <= x < 87:
            averages.append("A-")
        elif 77 <= x < 80:
            averages.append("B+")
        elif 73 <= x < 77:
            averages.append("B")
        elif 70 <= x < 73:
            averages.append("B-")
        elif 67 <= x < 70:
            averages.append("C+")
        elif 63 <= x < 67:
            averages.append("C")
        elif 60 <= x < 63:
            averages.append("C-")
        elif 57 <= x < 60:
            averages.append("D+")
        elif 53 <= x < 57:
            averages.append("D")
        elif 50 <= x < 53:
            averages.append("D-")
        elif x < 50:
            averages.append("F")
        else:
            averages.append("ERROR")

indices = [x for x in range(len(averages))]
ser = pd.Series(np.array(averages), index=indices)
main.insert(4, column="Letter Grade", value=ser)
main.to_csv("graded.csv")
