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
def split(df):
    y = df["poisonous"]
    X = df.drop(columns=["poisonous"])
    X_train, X_test, y_train, X_train = train_test_split(X, y, test_size=0.3, random_state=0)
    return X_train, X_test, y_train, X_train


def plot_metrics(metrics_list, y_test, predictions):
    if "Confusion Matrix" in metrics_list:
        st.subheader("Confusion Matrix")
        ConfusionMatrixDisplay(y_test, predictions)
        st.pyplot()
    # if "Confusion Matrix" in metrics_list:
    #     st.subheader("ROC Curve")
    #     RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc, estimator_name='example estimator')
    #     st.pyplot()


st.title("Binary Classification Web App")

df = load_data_from_web()
X_train, X_test, y_train, y_train = split(df)

class_names = ["edible", "poisonous"]

# plot_metrics()

st.subheader("Choose classifier")
classifier = st.selectbox("Classifier", options=["SVM", "LR", "RF"])

if classifier == "SVM":
    st.subheader("Select Hyperparameters")
    param_C = st.number_input("Regularization parameter C", 0.1, 10.0, step=0.1)
    kernel = st.radio("Kernel type (Kernel Coefficient)", ["TBF", "Linear"], key="kernel")
    gamma = st.radio("Gamma", ["scale", "auto"])

if st.checkbox("Show Raw Data", False):
    st.subheader("Mushroom Data Set")
    st.write(df)

