India-Specific Carbon Footprint Calculator
1. Project Overview
This project is a web-based carbon footprint calculator specifically designed for the Indian context. It addresses a critical gap left by generic international calculators, which often use emission factors that are not representative of India's unique energy grid, transportation systems, and common fuel types (like LPG).

The primary goal is to provide users in India with a more accurate and relevant estimate of their annual CO2e (carbon dioxide equivalent) emissions, empowering them to make informed decisions to reduce their environmental impact.

The application is built using Python and the Streamlit library, making it lightweight, interactive, and easy to deploy.

2. Features
Localized Emission Factors: Uses India-specific data for calculations.

Comprehensive Categories: Covers major sources of personal emissions:

Household Energy: Monthly electricity (in Units/kWh) and LPG (in kg).

Personal Vehicles: Annual travel distance and fuel efficiency for cars and motorbikes.

Air Travel: Number of domestic (short) and international (long) return flights.

Public Transport: Annual travel distance by bus, train, tram/subway, and taxi.

Instantaneous Results: Calculates and displays the total annual carbon footprint in metric tons.

Detailed Breakdown: Provides a clear summary of emissions contributed by each category.

3. Methodology & Emission Factors
The calculator employs a Rule-Based Calculation Algorithm. It is not a predictive model but a deterministic tool that applies a standard formula:

Total Emissions = User Input × Emission Factor

This approach ensures transparency and verifiability. The emission factors used are based on Indian emission standards (approximated for 2025) and global GHG Protocol guidelines.

4. Technology Stack
Language: Python 3.x

Web Framework: Streamlit

Data Analysis & Visualization: Pandas, Matplotlib (for the analysis notebook)

5. How to Run the Calculator
To run the carbon footprint calculator on your local machine, follow these steps:

Prerequisites:

Python 3.7+ installed.

pip (Python package installer).

Step 1: Clone or download the project files
Ensure you have the carbon.py file.

Step 2: Install required libraries
Open your terminal or command prompt and run:

pip install streamlit

Step 3: Run the Streamlit application
In your terminal, navigate to the directory containing carbon.py and run the following command:

streamlit run carbon.py

Your web browser will automatically open with the calculator interface.

6. How to Perform Contribution Analysis
The project also includes a Jupyter Notebook script to analyze the contribution of each category to a user's total footprint.

Prerequisites:

Jupyter Notebook or JupyterLab installed.

Pandas and Matplotlib libraries.

pip install pandas matplotlib

Instructions:

Launch Jupyter Notebook.

Open the analysis notebook file (analysis.ipynb or similar).

Run the cells sequentially to:

Load the emission factors.

Define sample user data.

Perform the calculations.

Generate a pie chart visualizing the percentage contribution of each category.

Display a detailed table of the emissions breakdown.

7. Sources & Global Context
The emission factors and methodology are informed by established standards and data sources to ensure accuracy and relevance.

GHG Protocol: Provides the global standard methodologies for calculating GHG emissions, which forms the basis for our calculation logic. The tools and guidance for stationary combustion (for fuels like LPG) are particularly relevant.

GHG Protocol Calculation Tools

India-Specific Data: Official reports from Indian governmental bodies are crucial for localized factors.

GHG Platform India: https://ghgplatform-india.org/

Central Electricity Authority (CEA): https://cea.nic.in/

Global Data for Comparison:

International Energy Agency (IEA): Provides data on global sectors like aviation. https://www.iea.org/energy-system/transport/aviation
