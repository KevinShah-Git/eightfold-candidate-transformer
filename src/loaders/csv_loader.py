import pandas as pd


def load_csv(path: str):

    df = pd.read_csv(path)

    records = df.to_dict(orient="records")

    if len(records) == 0:
        return {}

    return records[0]