import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    i = 0
    for s in employees["salary"]:
        employees["salary"][i] = s*2
        i += 1
    return employees