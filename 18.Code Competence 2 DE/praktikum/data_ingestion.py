import os
import pandas as pd
import numpy as np

class DataLakeBuilder:
    def read_csv_data(self, file_path):
        return pd.read_csv(file_path)
    
    def handle_missing_values(self, df):
        numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
        
        df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
        return df
    
    def handle_outliers(self, df, column):
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df[column] = np.where((df[column] < lower_bound) | (df[column] > upper_bound), df[column].median(), df[column])
        return df
    
    def save_to_parquet(self, df, file_name):
        df.to_parquet(file_name)
    
    def validate_data(self, file_path):
        df = pd.read_parquet(file_path)
        print(df.head())  
        print("\n" + df.describe().to_string())
        print("\n")  


if __name__ == "__main__":
    builder = DataLakeBuilder()

    folder_path = 'data_source'

    csv_files = os.listdir(folder_path)
    for csv_file in csv_files:
        if csv_file.endswith('.csv'):
            csv_file_path = os.path.join(folder_path, csv_file)
            parquet_file_path = os.path.splitext(csv_file_path)[0] + '.parquet'

            data = builder.read_csv_data(csv_file_path)

            data = builder.handle_missing_values(data)

            if 'amount' in data.columns:
                data = builder.handle_outliers(data, 'amount')

            builder.save_to_parquet(data, parquet_file_path)

    for csv_file in csv_files:
        if csv_file.endswith('.csv'):
            parquet_file_path = os.path.join(folder_path, os.path.splitext(csv_file)[0] + '.parquet')
            print(f"Ringkasan Data dari file {parquet_file_path}:")
            builder.validate_data(parquet_file_path)
