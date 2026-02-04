from src.data_ingestion import data_ingestion
from src.data_exploration import data_exploration
from src.data_preprocessing import data_preprocessing
from src.model_building import model_building
from src.model_evaluation import model_evaluation
def main():
    df = data_ingestion()
    numerical_stats_report = data_exploration(df)
    X_train, X_test, y_train, y_test = data_preprocessing(df)
    models = model_building(df)
    r2scores = model_evaluation(models, X_train, X_test, y_train, y_test)
    print(r2scores)
if __name__ == "__main__":
    main()
