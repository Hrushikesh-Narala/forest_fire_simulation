import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def train_baseline_model(df):
    """Train a Random Forest classifier to predict fire occurrence (dummy example)."""
    # For demonstration, use brightness and frp as features, confidence as label (dummy)
    X = df[['brightness', 'frp']]
    y = (df['confidence'] == 'h').astype(int)  # 1 for high confidence fire, else 0
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))
    return clf

# Placeholder for advanced deep learning models (CNN, LSTM, etc.)
def train_advanced_model(df):
    """Train advanced spatio-temporal models (to be implemented)."""
    # TODO: Implement advanced models
    return None

if __name__ == "__main__":
    from preprocess import preprocess_fire_data
    from data_ingest import load_fire_data
    fire_csv = "../data/fire_nrt_J1V-C2_631066.csv"
    fire_df = load_fire_data(fire_csv)
    fire_df = preprocess_fire_data(fire_df)
    train_baseline_model(fire_df) 