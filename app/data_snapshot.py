import time
import pandas as pd

def main():
    df = pd.read_csv('data/job_descriptions.csv')
    print(f"{'-'*104}\n")
    print(f"{'-'*44} SUMMARY REPORT {'-'*44}\n")

    print(f"{'-'*104}\n")

    # Shape of data
    print(f"Shape of data:\n\n\trows\t\t{df.shape[0]}\n\tcolumns\t\t{df.shape[1]}\n")
    print(f"{'-'*104}\n")

    # Datatypes of each column
    dtypes = "\n\t".join(str(df.dtypes).split("\n"))
    print(f"Datatypes of each column:\n\n\t{dtypes}\n")
    print(f"{'-'*104}\n")

    # Count missing values in each column
    nulls = "\n\t".join(str(df.isnull().sum()).split("\n"))
    print(f"Missing values in each column:\n\n\t{nulls}\n")
    print(f"{'-'*104}\n")

    # Count duplicated records
    print(f"Number of duplicated records: {df.duplicated().sum()}\n")
    print(f"{'-'*104}\n")

    for column in df.columns:
        print(f"{[v for k,v in df[column][:5].items()]}")
        print(f"Column: {column}  dtype: {df[column].dtype}\n")
        print(f"{'-'*104}\n")

    


if __name__=="__main__":
    start_time = time.time()
    main()
    print(f"Elapsed time: {time.time()-start_time} seconds")