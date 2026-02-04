from config import config
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler

# Data Preprocessing

def data_preprocessing(df):
        
    X = df.drop(columns = 'strength',)
    y = df['strength']

    # Use Train Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                            test_size=0.3,
                                                            random_state=1)
        
    # Use Scaling Techniques
    rs = RobustScaler().fit(X_train,y_train)
    X_train= rs.fit_transform(X_train)
    X_test= rs.transform(X_test)
        
    return X_train, X_test, y_train, y_test