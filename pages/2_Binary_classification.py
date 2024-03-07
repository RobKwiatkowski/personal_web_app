import streamlit as st
import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay, precision_recall_curve
from sklearn.preprocessing import LabelEncoder

pd.set_option("mode.copy_on_write", True)


@st.cache_data(persist=True)
def load_data_from_web():
    mushroom = fetch_ucirepo(id=73)
    x, y = mushroom.data.features, mushroom.data.targets
    data = pd.concat([x, y], axis=1)

    label = LabelEncoder()
    for col in data.columns:
        data[col] = label.fit_transform(data[col])

    return data


@st.cache_data(persist=True)
def split_data(dataframe):
    y = dataframe["poisonous"]
    x = dataframe.drop(columns=["poisonous"])
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)
    return x_train, x_test, y_train, y_test


# def plot_metrics(metrics_list, y_test, predictions):
#     if "Confusion Matrix" in metrics_list:
#         st.subheader("Confusion Matrix")
#         ConfusionMatrixDisplay(y_test, predictions)
#         st.pyplot()
#     if "ROC curve" in metrics_list:
#         pass
#     if "Precision-Recall Curve" in metrics_list:
#         pass
#     #     st.subheader("ROC Curve")
#     #     RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc, estimator_name='example estimator')
#     #     st.pyplot()


st.title("Binary Classification Web App")

df_raw = load_data_from_web()

X_train, X_test, y_train, y_test = split_data(df_raw)

class_names = ["edible", "poisonous"]

st.subheader("Choose classifier")
classifier = st.selectbox("Classifier", options=["SVM", "LR", "RF"])

if classifier == "SVM":
    st.subheader("Select Hyperparameters")
    param_C = st.number_input("Regularization parameter C", 0.1, 10.0, step=0.1)
    kernel = st.radio("Kernel type (Kernel Coefficient)", ["rbf", "linear"], key="kernel")
    gamma = st.radio("Gamma", ["scale", "auto"])

    metrics = st.multiselect("Coose evaluation metrics", ["Confusion Matrix", "ROC curve", "Precision-Recall Curve"])

if st.button("Classify", key="classify"):
    st.subheader("Support Vector Machine")
    model = SVC(C=1, kernel="linear", gamma=0.9)
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    st.write(f"Accuracy:{accuracy}",)

if st.checkbox("Show Raw Data", False):
    st.subheader("Mushroom Data Set")
    st.write(df_raw)

