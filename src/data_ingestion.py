from config import config
import pandas as pd

# Data Ingestion

def data_ingestion():
    try:
        df = pd.read_csv(r'C:\CementStrength_PredictionModel\data\raw\Concrete_Compressive_Strength.csv')
        print("Data Ingestion Successful")
    except:
        print("Data Ingestion Unsuccessful")
    return df