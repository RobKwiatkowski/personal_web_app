import streamlit as st

st.set_page_config(layout="centered")

st.sidebar.success("Welcome page, a short summary and CV")

st.title("Welcome to my personal webpage")
st.write(
    """This is a space where you can find some info about myself, my interests and personal projects.
Below some basic info about me."""
)

col1, col2, col3 = st.columns([0.25, 0.15, 0.6])

with col1:
    st.image("ML Engineer.png")

with col2:
    st.write(
        """
    Name:<br>Surname:<br>
    Profession:<br>
    Location<br>
    LinkedIn: 
    """,
        unsafe_allow_html=True,
    )

with col3:
    st.write(
        """
    Robert<br>Kwiatkowski<br>
    Machine Learning Engineer<br>
    Warsaw, Poland
    https://www.linkedin.com/in/robertkwiatkowski01/
    """,
        unsafe_allow_html=True,
    )

st.write(
    """
I'm a ML/DS with over 10 years of experience in programming and with a background in the aerospace engineering.
My expertise is in Data Science and Machine Learning, Cloud Computing and MLOps.

Expertise:
* Data Science, Machine Learning
* Data Engineering
* Cloud Architecture
* Systems Engineering
* MLOps

Devset:
* Python, Go
* SQL and noSQL (Redis, MongoDB)
* Docker, Kubernetes, Kubeflow, MLflow, Airflow
* Cloud platforms: GCP, AWS
* Backend: FastAPI, Django
* Basics of frontend: HTML, CSS and JavaScript

Languages:
* :flag-gb: | English - level C1
* :flag-de: | German - level B2
* :flag-es: | Spanish - level B1
* :flag-fr: | French - level A1
"""
)

col1, col2, col3 = st.columns(3)
col1.write("""---""")
col2.markdown("<h3 style='text-align: center'>Experience</h3>", unsafe_allow_html=True)
col3.write("""---""")

with st.expander(
    "01-2022 - currently, **Orange**, Tech Lead/ ML Engineer, Poland :flag-pl:"
):
    st.write(
        """
    Orange is a multinational telecom corporation with HQ in *Paris, France* :flag-fr:  
    * Working in Data & AI International Team
    * Design and development of AI/ML solutions in the Google Cloud Platform throughout the full product 
    lifecycle: from early concepts, data acquisition up to fine-tuning and putting models 
    into production using pipelines
    * Managing and organising databases and data marts with peta-/terabytes of data
    * Working in direct collaboration with the business units and external teams
    * Working in and promoting Agile concepts and frameworks (Scrum, Kanban)
    """
    )

with st.expander(
    "09-2014 - 12-2021, **Rolls-Royce**, Designer/Data Analyst, Germany :flag-de:"
):
    st.write(
        """Rolls-Royce is a multinational engineering aerospace :airplane: company developing jet engines. 
             Its HQ is in *Derby, UK* :uk:"""
    )
    if st.checkbox("04-2019 - 12-2021, Turbines subsystem"):
        st.write(
            """
        * Optimising subsystem's architecture by integration and analysis of data from multiple sources
        * Creating ETL pipelines and data dashboards to extract actionable insights
        * Preprocessing data for other specialist groups
        * Writing work automation scripts in Python, C++ and VBA
        * Translating Excel-based dashboards to Power BI
        * Supporting team members in Python and VBA based tasks
        * Supporting NPI and Fleet design activities
        * Carrying out Root Cause Investigations for Fleet and NPI projects"""
        )
    if st.checkbox("09-2014 - 03-2019, Compressor subsystem"):
        st.write(
            """
        * Working in the "Future Projects and Technologies" team
        * Conceptual designing of the subsystem architecture to meet project's requirements
        * Optimisation of subsystem design using numerical methods (e.g. genetic optimisation algorithms, FEM)
        * Developing Python scripts for data analysis and work automation
        * Preparing software validation and verification plans
        * Extracting, transforming and preparing datasets for external specialists groups (e.g. Stress, Aero, Project)
        * Performing numerical optimisation of design and carrying out their robustness analyses
        * Preparing subsystem technical documentation, e.g.: General Arrangements, reports, BOMs
        * Toolset: Python, NX, DOORS, SAP, Qualica, Teamcenter, ANSYS, Isight,"""
        )

with st.expander(
    "08-2011 - 08-2014, **ETC-PZL Aerospace Industries**, Design Engineer, Poland :flag-pl:"
):
    st.write(
        """ETC-PZL Aerospace Industries is a multinational engineering delivering advanced simulators mostly for 
    the aerospace industry but also for police and military"""
    )
    st.write(
        """
    * Designing systems and subsystems of aviation and automotive simulators
    * Preparing CAD models and production drawings
    * Performing numerical stress calculations
    * Calculating fatigue life of critical components
    * Integration of mechanical, electrical and electronic systems
    * Redesigning original parts and introducing changes to existing designs
    * Using a wide range of manufacturing methods: machining, turning, 3D printing, laser cutting, etc.
    * Toolset: Autodesk Inventor, AutoCAD Mechanical, Autodesk Showcase"""
    )

with st.expander(
    "03-2011 - 12-2013, **Warsaw University of Technology**, R&D Engineer, Poland :flag-pl:"
):
    st.write(
        """Warsaw University of Technology, Faculty of Power and Aeronautical Engineering."""
    )
    st.write(
        """
        * Developing composite materials for high-temperature applications and heat management
        * Preparing plug-ins and analysis scripts in C++, Python and APDL, 
        * Conducting numerical stress analyses using ANSYS APDL and Workbench.
        * Conducting numerical thermal analyses using ANSYS FLUENT,
        * Preparing CAD models in CATIA V5 and UG NX,
        * Mesh preparation in Hypermesh and Gambit,
        * Toolset: Python, ANSYS Workbench, ANSYS APDL, ANSYS FLUENT, CATIA V5, UG NX, Gambit, Hypermesh"""
    )

col1, col2, col3 = st.columns(3)
col1.write("""---""")
col2.markdown("<h3 style='text-align: center'>Education</h3>", unsafe_allow_html=True)
col3.write("""---""")

with st.expander(
    "10-2005 - 03-2011, **Warsaw University of Technology**, Master of Science, Poland :flag-pl:"
):
    st.write(
        """Warsaw University of Technology, Faculty of Power and **Aeronautical Engineering**.  
    **Specialisation**: Aerospace Propulsion  
    **Thesis title**: *'Numerical Heat Transfer Analysis of High-Load Turbine Blades'*
    """
    )


col1, col2, col3 = st.columns(3)
col1.write("""---""")
col2.markdown("<h3 style='text-align: center'>Articles</h3>", unsafe_allow_html=True)
col3.write("""---""")

st.write(
    """
In my free time I write articles about programming and Machine Learning. Most of them are published on
Towards Data Science.
* [Gradient Descent Algorithm — a deep dive](https://towardsdatascience.com/gradient-descent-algorithm-a-deep-dive-cf04e8115f21)
* [Monte Carlo Simulation — a practical guide](https://towardsdatascience.com/monte-carlo-simulation-a-practical-guide-85da45597f0e)
* [Is Moore’s Law Dead? Dying? Or still Alive?](https://robertkwiatkowski01.medium.com/is-moores-law-dead-dying-or-still-alive-a931ad9475a9)
* [Batch, Mini-Batch and Stochastic Gradient Descent for Linear Regression](https://towardsdatascience.com/batch-mini-batch-and-stochastic-gradient-descent-for-linear-regression-9fe4eefa637c)
* [Performing Linear Regression Using the Normal Equation](https://towardsdatascience.com/performing-linear-regression-using-the-normal-equation-6372ed3c57)
"""
)

col1, col2, col3 = st.columns(3)
col1.write("""---""")
col2.markdown("<h3 style='text-align: center'>Talks</h3>", unsafe_allow_html=True)
col3.write("""---""")

st.write(
    """
* [Machine Learning Week Europe](https://machinelearningweek.eu/agenda/), Berlin, Nov 2023, "Anomaly Detection in Telco Network at Orange"
"""
)
