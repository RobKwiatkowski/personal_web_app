import streamlit as st
import pandas as pd
from freefall import main
import matplotlib.pyplot as plt

st.set_page_config(page_title="FreeFall Demo")

st.markdown("# Free Fall Calculator")
st.sidebar.header("Free Fall Calculator")
st.write(
    """This page contains a script for calculating flight parameters of a free falling
    body taking into account drag and the atmosphere model."""
)

with st.form("my_form"):
    mass = st.number_input(label="Mass [kg]", min_value=0.01, value=1.0, step=0.01)
    diameter = st.number_input(
        label="Diameter [mm]", min_value=0.01, value=50.0, step=0.01
    )
    drag_coefficient = st.number_input(
        label="Coefficient of drag [-]", min_value=0.01, value=0.45, step=0.01
    )
    drop_altitude = st.number_input(
        label="Drop altitude [m]", min_value=1, value=15_000, step=1
    )

    submitted = st.form_submit_button("Submit")

    time_step = 0.1
    if submitted:
        item = main.Object(mass=mass, diameter=diameter, drag_c=drag_coefficient)
        results, flags = item.drop(drop_altitude=drop_altitude, time_step=time_step)
        pd_results = pd.DataFrame(results)
        pd_results["acceleration"] = (
            pd_results["velocity"].shift(1) - pd_results["velocity"]
        ) / time_step

        st.write(
            f'Fall time is: {results["time"][-1]:.1f} s',
        )
        # st.dataframe(pd_results)

        fig, ax = plt.subplots(1, 2, figsize=(12, 10))
        ax[0].plot(pd_results["velocity"], pd_results["altitude"])
        ax[0].set_xlabel("velocity [m/s]")
        ax[0].set_ylabel("height [m]")
        ax[0].set_xlim(0)
        ax[0].set_ylim(0)
        ax[1].plot(pd_results["acceleration"], pd_results["altitude"])
        ax[1].set_xlabel("acceleration [m/s2]")
        ax[1].set_ylabel("height [m]")
        ax[1].set_ylim(0)
        st.pyplot(fig)

        # st.line_chart(pd_results, x="time", y="velocity")
        # st.line_chart(pd_results, x="altitude", y="velocity")
