# %%
import pandas as pd
import numpy as np


X = pd.read_csv("train_data.csv")
y = pd.read_csv("train_data.csv")["Suitability"].map({"Favorable": 1, "Unfavorable": 0})

# %%
X.head()

# %%
X.info()

# %%
def augment_X(X: pd.DataFrame) -> pd.DataFrame:
    augmented_X = X.copy().drop(columns=["ID"])
    if "Suitability" in X.columns:
        augmented_X.drop(columns=["Suitability"], inplace=True)
    augmented_X["Irrigation"].fillna(inplace=True, value="None")
    augmented_X["Moisture"].fillna(inplace=True, value=augmented_X["Moisture"].median())
    
    augmented_X["Nutrient_Index"] = (0.4 * augmented_X["Nitrogen"] + 
                                     0.3 * augmented_X["Phosphorus"] + 
                                     0.3 * augmented_X["Potassium"]).round(4)
    return augmented_X

augmented_X = augment_X(X)


# %%
from sklearn.compose import make_column_selector, make_column_transformer
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from xgboost import XGBClassifier

model = make_pipeline(
    make_column_transformer(
        (OneHotEncoder(), make_column_selector(dtype_include=object)),
        (StandardScaler(), make_column_selector(dtype_exclude=object))
    ),
    XGBClassifier(
        n_estimators=2000
    )
)

# %%
cross_val_score(model, augmented_X, y, cv=10, scoring="f1")

# %%
model.fit(augmented_X, y)

# %%
test_X_IDs = pd.read_csv("test_data.csv")["ID"]
test_X = augment_X(pd.read_csv("test_data.csv"))
test_y_pred = model.predict(test_X)

# %%
soil_counts = augmented_X["Soil_Type"].value_counts()

pd.concat((
    pd.DataFrame({
        "subtaskID": 1,
        "datapointID": test_X_IDs,
        "answer": test_X["Nutrient_Index"]
    }),
    pd.DataFrame({
        "subtaskID": 2,
        "datapointID": test_X_IDs,
        "answer": (1 * (test_X["pH"] < 6.0) + 2 * ((6.0 <= test_X["pH"]) & (test_X["pH"] <= 7.5)) + 3 * (test_X["pH"] > 7.5)).map({
            1: "Acid",
            2: "Neutral",
            3: "Alkaline"
        })
    }),
    pd.DataFrame({
        "subtaskID": 3,
        "datapointID": test_X_IDs,
        "answer": 1 * (test_X["Moisture"] > augmented_X["Moisture"].median())
    }),
    pd.DataFrame({
        "subtaskID": 4,
        "datapointID": test_X_IDs,
        "answer": test_X["Soil_Type"].map(soil_counts).fillna(0).astype(int) 
    }),
    pd.DataFrame({
        "subtaskID": 5,
        "datapointID": test_X_IDs,
        "answer": pd.Series(test_y_pred).map({0: "Unfavorable", 1: "Favorable"})
    }),
)).to_csv("submission.csv")


