import pandas as pd

import bai, oracle, gl

def main():

    bai_df = bai.clean_df(bai.read_df())
    print(bai_df.head())

    oracle_df = oracle.clean_df(oracle.read_df())
    print(oracle_df.head())

    gl_df = gl.clean_df(gl.read_df())
    print(gl_df.head())

    # GL_Clean, {"Fgbtrnh Trans Desc"}, Oracle_Clean, {"FDOC_DESC"}, "GL_Raw", JoinKind.LeftOuter),
    # Left outer join gl_df with oracle_df on matching columns
    merged_df = pd.merge(
        gl_df, 
        oracle_df, 
        left_on="Fgbtrnh Trans Desc", 
        right_on="FDOC_DESC", 
        how="left"
    )
    # print the stats for merged_df
    print("Merged DataFrame Stats:")
    print(merged_df.describe(include='all'))
    merged_df.to_csv('/data/merged_df.csv', index=False)


if __name__ == "__main__":
    # main("debug")
    # main("prod")
    main()

