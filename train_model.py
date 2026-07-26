import pandas as pd
import os
import joblib

# Sklearn imports
from sklearn.model_selection import GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# XGBoost
from xgboost import XGBRegressor

# -------------------------------
# Load Dataset
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "hotel_bookings.csv")
df = pd.read_csv(file_path)
df = df.sample(30000, random_state=42)
print("Columns:", df.columns)

# -------------------------------
# Target Column
# -------------------------------
target = "adr"

# Drop irrelevant columns
df = df.drop(columns=["reservation_status", "reservation_status_date"], errors="ignore")

# Split features and target
X = df.drop(columns=[target])
y = df[target]

# -------------------------------
# Column Types
# -------------------------------
num_cols = X.select_dtypes(include=['int64', 'float64']).columns
cat_cols = X.select_dtypes(include=['object', 'string']).columns

# -------------------------------
# Preprocessing Pipelines
# -------------------------------
num_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])

cat_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", num_pipeline, num_cols),
    ("cat", cat_pipeline, cat_cols)
])

# -------------------------------
# Models
# -------------------------------
models = {
    "ridge": Ridge(),
    "rf": RandomForestRegressor(),
    "xgb": XGBRegressor(objective='reg:squarederror', verbosity=0)
}

# -------------------------------
# Hyperparameters
# -------------------------------
params = {
    "ridge": {
        "model__alpha": [0.1, 1.0, 10]
    },
    "rf": {
        "model__n_estimators": [100],
        "model__max_depth": [5, 10]
    },
    "xgb": {
        "model__n_estimators": [100],
        "model__learning_rate": [0.05, 0.1],
        "model__max_depth": [3, 6]
    }
}

best_model = None
best_score = float("inf")

# -------------------------------
# Training Loop
# -------------------------------
# 🔥 ADD THIS BEFORE LOOP (important)
from sklearn.model_selection import train_test_split

X = X.drop(columns=[
    "reservation_status",
    "reservation_status_date"
],errors="ignore")

X = X.fillna(0)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 🔁 UPDATED LOOP
for name in models:
    print(f"\nTraining {name}...")

    pipe = Pipeline([
        ("prep", preprocessor),
        ("model", models[name])
    ])

    grid = GridSearchCV(pipe, params[name], cv=5,
                        scoring="neg_mean_absolute_error",
                        n_jobs=-1)

    grid.fit(X_train, y_train)

    preds = grid.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    print(f"{name} MAE:", mae)
    print(f"{name} R2:", r2)

    if mae < best_score:
        best_score = mae
        best_model = grid.best_estimator_

# -------------------------------
# Save Model
# -------------------------------
joblib.dump(best_model, "best_model.pkl")

print("\n✅ Best model saved as best_model.pkl")