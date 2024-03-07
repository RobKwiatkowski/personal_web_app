import streamlit as st
import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay, PrecisionRecallDisplay
from sklearn.preprocessing import LabelEncoder

pd.set_option("mode.copy_on_write", True)


@st.cache_data(persist=True)
def load_data_from_web(set_id):
    """

    Returns: data retrieved from the UCI Repository

    """
    dataset = fetch_ucirepo(id=set_id)
    x, y = dataset.data.features, dataset.data.targets
    data = pd.concat([x, y], axis=1)
    return data


def encode_data(data):
    label = LabelEncoder()
    for col in data.columns:
        data[col] = label.fit_transform(data[col])

    return data


@st.cache_data(persist=True)
def split_data(dataframe, target_column):
    """
    Splits data into train and test datasets
    Args:
        target_column:
        dataframe: pandas Dataframe

    Returns:
        Tuple of x_train, x_test, y_train, y_test

    """
    y = dataframe[target_column]
    x = dataframe.drop(columns=[target_column])
    x_tr, x_te, y_tr, y_te = train_test_split(x, y, test_size=0.3, random_state=0)
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
        st.subheader("ROC-Curve")
        matrix = RocCurveDisplay.from_predictions(y_te, pred)
        st.pyplot(matrix.figure_)
    if "Precision-Recall Curve" in metrics_list:
        st.subheader("Precision-Recall Curve")
        matrix = PrecisionRecallDisplay.from_predictions(y_te, pred)
        st.pyplot(matrix.figure_)


def run_model(model):
    """

    Args:
        model:

    Returns:

    """
    st.subheader("Results:")
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = model.score(X_test, y_test)
    st.write(f"Accuracy: {accuracy:.2f}")
    plot_metrics(metrics, y_test, predictions)


st.title("Binary Classification Web App")

dataset_id = st.radio("Choose a dataset", ["Mushrooms", "Phishing Websites"], help="Data Sets from UCI ML repository")
df_raw = None
target_col = None
if dataset_id == "Mushrooms":
    df_raw = load_data_from_web(73)
    class_names = ["edible", "poisonous"]
    target_col = "poisonous"

if dataset_id == "Phishing Websites":
    df_raw = load_data_from_web(327)
    class_names = ["yes", "no"]
    target_col = "result"

st.write("Data samples in the dataset is: ", df_raw.shape[0])
st.write(f"Number of features: ", df_raw.shape[1])

if st.toggle("Show Raw Data", False):
    st.write(df_raw)

df_encoded = encode_data(df_raw)
X_train, X_test, y_train, y_test = split_data(df_encoded, target_col)

st.subheader("Choose classifier")
classifier = st.selectbox("Classifier", options=["SVM", "Random Forest"])
metrics = st.multiselect("Choose evaluation metrics", ["Confusion Matrix", "ROC curve", "Precision-Recall Curve"])

if classifier == "SVM":
    st.subheader("Select Hyperparameters")
    user_C = st.number_input("Regularization parameter C", 0.1, 10.0, step=0.1)
    user_kernel = st.radio("Kernel type", ["rbf", "linear"], key="kernel")
    user_gamma = st.radio("Gamma", ["scale", "auto"])

    if st.button("Classify", key="classify"):
        clf = SVC(C=user_C, kernel=user_kernel, gamma=user_gamma)
        run_model(clf)

if classifier == "Random Forest":
    st.subheader("Select Hyperparameters")
    user_n_estimators = st.number_input(label="Number of estimators", min_value=1, max_value=1000, value=100)
    user_max_depth = st.number_input(label="Max_depth", min_value=1, max_value=10, value=2)

    if st.button("Classify", key="classify"):
        clf = RandomForestClassifier(n_estimators=user_n_estimators, max_depth=user_max_depth, random_state=0)
        run_model(clf)



