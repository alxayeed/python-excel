import pandas as pd
# writing to a single sheet


def write_single_sheet():
    df = pd.DataFrame({'States': ['California', 'Florida', 'Montana', 'Colorodo', 'Washington', 'Virginia'],
                       'Capitals': ['Sacramento', 'Tallahassee', 'Helena', 'Denver', 'Olympia', 'Richmond'],
                       'Population': ['508529', '193551', '32315', '619968', '52555', '227032']})

    df.to_excel('./data/states.xlsx', sheet_name="USA", index=False)


# Writing multiple Dataframe to multiple sheets
def write_multiple_sheets():
    income1 = pd.DataFrame({'Names': ['Stephen', 'Camilla', 'Tom'],
                            'Salary': [100000, 70000, 60000]})

    income2 = pd.DataFrame({'Names': ['Pete', 'April', 'Marty'],
                            'Salary': [120000, 110000, 50000]})

    income3 = pd.DataFrame({'Names': ['Victor', 'Victoria', 'Jennifer'],
                            'Salary': [75000, 90000, 40000]})

    income_sheets = {'Group1': income1, 'Group2': income2, 'Group3': income3}
    writer = pd.ExcelWriter('./data/income.xlsx', engine='xlsxwriter')

    for sheet_name in income_sheets.keys():
        income_sheets[sheet_name].to_excel(
            writer, sheet_name=sheet_name, index=False)

    writer.save()


if __name__ == "__main__":
    write_multiple_sheets()
