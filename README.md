# 🚦 Smart Traffic Violation Pattern Detector

A data-driven **Streamlit dashboard** that helps analyze **traffic
violation patterns** using Python.\
It provides insights into violation trends, hotspots, fine amounts,
vehicle types, weather conditions, and more.

------------------------------------------------------------------------

## 📌 Features

-   📤 Upload custom CSV dataset\
-   📊 Interactive Streamlit dashboard\
-   🗂️ Category-wise analytics (Violation Types, Hotspots, Fines,
    Vehicle vs Fine, Weather, etc.)\
-   🧮 Automatic data cleaning (dates, time, duplicates)\
-   📈 Visualizations using **Matplotlib** and **Seaborn**\
-   🧠 Caching for faster data loading\
-   🖼️ Responsive layout with Streamlit\
-   🚓 Insights that support road-safety decision making

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   **Python**
-   **Streamlit**
-   **NumPy**
-   **Pandas**
-   **Matplotlib**
-   **Seaborn**
-   **Dashboard UI**

------------------------------------------------------------------------

## 🚀 Quick Start

### **1. Clone the Repository**

``` bash
git clone https://github.com/ishwari1992/Smart-Traffic-Violation-Pattern-Detector-Project.git

```

### **2. Create Virtual Environment **

``` bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

### **3. Install Dependencies**

``` bash
pip install -r requirements.txt
```

### **4. Run the Application**

``` bash
streamlit run app.py
```

------------------------------------------------------------------------

## 📂 Project Structure

    ├── assets/
    │   ├── T03.jpg
    ├── data/
    │   └── Indian_Traffic_Violations.csv
    ├── app.py
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## 📥 Installation

### Install Required Libraries Manually:

``` bash
pip install streamlit numpy pandas matplotlib seaborn
```

------------------------------------------------------------------------

## 📑 Usage

1.  Launch the Streamlit app\
2.  Upload your **Indian_Traffic_Violations.csv file**\
3.  Navigate through the sidebar\
4.  Explore:
    -   Overview\
    -   Top violation types\
    -   Hotspots\
    -   Fines distribution\
    -   Vehicle type vs fine pie chart\
    -   Average fine per location\
    -   Weather & condition insights

------------------------------------------------------------------------

## 📊 Example Screenshots
dashboard screenshots:
![alt text](<Screenshot 2025-11-26 183520.png>) ![alt text](<Screenshot 2025-12-08 145743.png>) ![alt text](<Screenshot 2025-12-08 145905.png>) ![alt text](<Screenshot 2025-12-08 145942.png>) ![alt text](<Screenshot 2025-12-08 150022.png>) ![alt text](<Screenshot 2025-12-08 150046.png>) ![alt text](<Screenshot 2025-12-08 150118.png>) ![alt text](<Screenshot 2025-12-08 151404.png>) ![alt text](<Screenshot 2025-12-08 151535.png>) ![alt text](<Screenshot 2025-12-08 151559.png>)
------------------------------------------------------------------------

## 🧪 Example Code Snippet

``` python
df = load_data(uploaded_file if uploaded_file else None)
if not df.empty:
    st.sidebar.write(f"Rows: {df.shape[0]} | Cols: {df.shape[1]}")
```

------------------------------------------------------------------------

## 🏷️ Badges

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red)
![License](https://img.shields.io/badge/License-MIT-green)
![Visualization](https://img.shields.io/badge/Charts-Matplotlib%20%7C%20Seaborn-yellow)

------------------------------------------------------------------------

## 📄 MIT License

    MIT License

    Copyright (c) 2025 

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files...

------------------------------------------------------------------------

## 👩‍💻 Author

**Ishwari Deshmukh**\
Software Developer\
Pune\
📧 deshmukhishu9@gmail.com

------------------------------------------------------------------------
