from config import config
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor  
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, BaggingRegressor, AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor

# Model Building
def model_building(df):
    
    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(),
        "Random Forest": RandomForestRegressor(),
        "Gradient Boosting": GradientBoostingRegressor(),
        "Bagging Regressor": BaggingRegressor(),
        "AdaBoost Regressor": AdaBoostRegressor(),
        "Support Vector Regressor": SVR(),
        "K-Neighbors Regressor": KNeighborsRegressor()
        }
    
    return models

