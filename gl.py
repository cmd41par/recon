"""all functions for GL file"""

import pandas as pd


def get_filename() -> str:
    """return the filename for the GL csv"""
    return "/data/GL_Transactional_Details-5a3e5cfee3ef4a86be067b85eaf4382c-export.csv"


def read_df() -> pd.DataFrame:
    """read the dataframe for the GL csv"""
    df = pd.read_csv(get_filename(), sep=",", dtype={
            "Fgbtrnd Trans Amt": str
            
        }, parse_dates=["Fgbtrnh Trans Date"])
    return df

def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    """clean the dataframe for the GL csv"""
    columns_to_keep = ["Fgbtrnh Trans Date", "Fgbtrnh Trans Desc", "Fgbtrnd Trans Amt"]

    df["Fgbtrnh Trans Date"] = df["Fgbtrnh Trans Date"].dt.date
    df = df[columns_to_keep]
    df["Fgbtrnd Trans Amt"] = df["Fgbtrnd Trans Amt"].str.replace(",", "").str.strip().astype(float)

    return df