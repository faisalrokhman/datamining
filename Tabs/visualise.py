import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import plot_confusion_matrix
from sklearn import tree
import streamlit as st

from web_function import train_model

def app(df, x, y ):

    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPylotGlobalUse',False)

    st.title("visual prediksi batu ginjal")

    if st.checkbox("Plot Confusion matrix"):
        model, score = train_model(x, y)
        plt.figure(figsize=(10,6))
        plot_confusion_matrix(model,x , y, values_formst='d')
        st.pyplot()

    if st.checkbox("plot decision tree"):
        model,score = train_model(x, y)
        dot_data = tree.export_graphviz(
            decision_tree=model, max_depth=4, out_file=None, filled=True,rounded=True,
            feature_names=x.columns, class_names=['nockd','ckd']
        )

        st.graphviz_chart(dot_data)