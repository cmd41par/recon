"""all functions for Oracle file"""

import pandas as pd


def get_filename() -> str:
    """return the filename for the Oracle csv"""
    return "/data/GA Payroll Finance Check Reconciliation (REAL TIME).csv"


def read_df() -> pd.DataFrame:
    """read the dataframe for the Oracle csv"""
    df = pd.read_csv(get_filename(), sep=",", dtype={
            "PHRDOCM_DOC_NO": str,
            "PHRDOCM_NET_SUM": float
            
        }, parse_dates=["PHRDOCM_DOC_DATE"])
    return df

def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    """clean the dataframe for the Oracle csv"""
    columns_to_keep = ["PHRDOCM_YEAR", "PHRDOCM_PICT_CODE", "PHRDOCM_PAYNO", "PHRDOCM_SEQ_NO", "PHRDOCM_DOC_NO", "PHRDOCM_DOC_DATE", "PHRDOCM_NET_SUM", "RECON IND", "PHRDOCM_RECON_DATE", "PHRDOCM_REISSUE_IND", "SPRIDEN_ID", "PAY TYPE", "DOC TYPE", "FDOC_DESC"]

    df["PHRDOCM_DOC_DATE"] = df["PHRDOCM_DOC_DATE"].dt.date
    df = df[columns_to_keep]
    # df["TxnAmount"] = df["TxnAmount"].str.replace(",", "").str.strip().astype(float)

    return df