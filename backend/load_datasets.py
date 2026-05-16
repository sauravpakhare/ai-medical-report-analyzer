import pandas as pd

# Load datasets
raw = pd.read_csv("datasets/RAW_DATASET.csv")
reference = pd.read_csv("datasets/REFERENCE_DATASET.csv")
processed = pd.read_csv("datasets/PROCESSED_DATASET.csv")

datasets = {
    "RAW DATASET": raw,
    "REFERENCE DATASET": reference,
    "PROCESSED DATASET": processed
}

for name, df in datasets.items():
    print("\n" + "="*50)
    print(name)
    print("="*50)

    print("Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nDatatypes:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())