from config import config
from sklearn.metrics import r2_score

# Model Evaluation
def model_evaluation(models, X_train, X_test, y_train, y_test):
    r2scores = {}

    for model_name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        r2scores[model_name] = r2_score(y_test, y_pred)
    return r2scores