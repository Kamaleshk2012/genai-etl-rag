import pandas as pd

def load_files(files):
    dataframes = {}

    for file in files:
        filename = file.filename

        if filename.endswith(".csv"):
            df = pd.read_csv(file.file)
        elif filename.endswith(".xlsx"):
            df = pd.read_excel(file.file)
        else:
            raise ValueError(f"Unsupported format: {filename}")

        dataframes[filename] = df

    return dataframes