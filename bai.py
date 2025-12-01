"""all functions for BAI file"""

import pandas as pd


def get_filename() -> str:
    """return the filename for the BAI csv"""
    return "/data/BAI_ALL-eb2d8ab266d6499b9f002c3f63975a1a-export.csv"


def read_df() -> pd.DataFrame:
    """read the dataframe for the BAI csv"""
    df = pd.read_csv(get_filename(), sep=",", dtype={
            "CustomerReference": str,
            "Comment": str,
            "TypeCodeDesc": str,
            "BankReference": str, 
            "TxnAmount": str
        }, parse_dates=["TransactionDate"])
    return df

def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    """clean the dataframe for the BAI csv"""
    columns_to_keep = ["TransactionDate", "CustomerReference", "Comment", "TxnAmount", "TypeCodeDesc"]
    df["TransactionDate"] = df["TransactionDate"].dt.date
    df = df[columns_to_keep]
    df["TxnAmount"] = df["TxnAmount"].str.replace(",", "").str.strip().astype(float)

    return df