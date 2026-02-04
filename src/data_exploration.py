from config import config
import pandas as pd
# data exploration
from collections import OrderedDict

def data_exploration(df):
    df = pd.read_csv(config.filepath)
    
    numerical_stats = []
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    LW = Q1 - 1.5 * IQR
    UW = Q3 + 1.5 * IQR
    Outlier_Count = ((df < LW) | (df > UW)).sum()
    Outlier_Percentage = (Outlier_Count / df.shape[0]) * 100
    for i in df:
        
        num_stats = OrderedDict({
            "features": i,
            "Maximum": df[i].max(),
            "Minimum": df[i].min(),
            "Mean": df[i].mean(),
            "Median": df[i].median(),
            "Q1": Q1[i],
            "Q3": Q3[i],
            "IQR": IQR[i],
            "Lower Whisker": LW[i],
            "Upper Whisker": UW[i],
            "Outlier Count": Outlier_Count[i],
            "Outlier Percentage": Outlier_Percentage[i],
            "Standard Deviation": df[i].std(),
            "Skewness": df[i].skew(),
            "Kurtosis": df[i].kurtosis()
            })
        numerical_stats.append(num_stats)
        numerical_stats_report = pd.DataFrame(numerical_stats)
    
    return numerical_stats_report
