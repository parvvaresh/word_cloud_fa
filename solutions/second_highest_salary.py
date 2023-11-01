import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates()
    sorted_salaries = unique_salaries.sort_values(ascending=False)
    if len(sorted_salaries) < 2:
        return pd.DataFrame({"SecondHighestSalary" : [None]})
    else:
        return pd.DataFrame({"SecondHighestSalary" : [sorted_salaries.iloc[1]]})
