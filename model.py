from includes import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

def train_model(data, labels):
    """Kouluttaa koneoppimismallin."""
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    print(f"Model trained with accuracy: {accuracy}")
    joblib.dump(model, "model.pkl")
    joblib.dump(scaler, "scaler.pkl")
    return model, scaler
