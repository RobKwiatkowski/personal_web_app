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
    """

    Returns: data retrieved from the UCI Repository

    """
    mushroom = fetch_ucirepo(id=73)
    x, y = mushroom.data.features, mushroom.data.targets
    data = pd.concat([x, y], axis=1)

    label = LabelEncoder()
    for col in data.columns:
        data[col] = label.fit_transform(data[col])

    return data


@st.cache_data(persist=True)
def split_data(dataframe):
    """
    Splits data into train and test datasets
    Args:
        dataframe: pandas Dataframe

    Returns:
        Tuple of x_train, x_test, y_train, y_test

    """
    y = dataframe["poisonous"]
    x = dataframe.drop(columns=["poisonous"])
    x_tr, x_te, y_tr, y_te = train_test_split(x, y, test_size=0.25, random_state=0)
    return x_tr, x_te, y_tr, y_te


def plot_metrics(metrics_list: list, y_te: list, pred: list):
    """

    Args:
        metrics_list:
        y_te:
        pred:

    Returns:

    """
    if "Confusion Matrix" in metrics_list:
        st.subheader("Confusion Matrix")
        matrix = ConfusionMatrixDisplay.from_predictions(y_te, pred)
        st.pyplot(matrix.figure_)
    if "ROC curve" in metrics_list:
        pass
    if "Precision-Recall Curve" in metrics_list:
        pass


def run_model(model):
    """

    Args:
        model:

    Returns:

    """
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = model.score(X_test, y_test)
    st.write(f"Accuracy: {accuracy:.2f}")
    plot_metrics(metrics, y_test, predictions)


st.title("Binary Classification Web App")

df_raw = load_data_from_web()

X_train, X_test, y_train, y_test = split_data(df_raw)

class_names = ["edible", "poisonous"]

st.subheader("Choose classifier")
classifier = st.selectbox("Classifier", options=["SVM", "Random Forest"])
metrics = st.multiselect("Choose evaluation metrics", ["Confusion Matrix"])
# metrics = st.multiselect("Choose evaluation metrics", ["Confusion Matrix", "ROC curve", "Precision-Recall Curve"])

if classifier == "SVM":
    st.subheader("Select Hyperparameters")
    user_C = st.number_input("Regularization parameter C", 0.1, 10.0, step=0.1)
    user_kernel = st.radio("Kernel type (Kernel Coefficient)", ["rbf", "linear"], key="kernel")
    user_gamma = st.radio("Gamma", ["scale", "auto"])

    if st.button("Classify", key="classify"):
        st.subheader("Support Vector Machine")
        clf = SVC(C=user_C, kernel=user_kernel, gamma=user_gamma)
        run_model(clf)

if classifier == "Random Forest":
    st.subheader("Select Hyperparameters")
    user_n_estimators = st.number_input(label="Number of estimators", min_value=1, max_value=1000, value=100)
    user_max_depth = st.number_input(label="Max_depth", min_value=1, max_value=10, value=2)

    if st.button("Classify", key="classify"):
        st.subheader("Random Forest")
        clf = RandomForestClassifier(n_estimators=user_n_estimators, max_depth=user_max_depth, random_state=0)
        run_model(clf)

if st.checkbox("Show Raw Data", False):
    st.subheader("Mushroom Data Set")
    st.write(df_raw)


