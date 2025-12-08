# Smart-Traffic-Violation-Pattern-Detector-Project

This project analyses traffic violation data using Python, NumPy, Pandas, Matplotlib, and Seaborn to identify trends, hotspots, and behavioural patterns in traffic violations.
It aims to provide actionable insights to improve traffic management, enhance road safety, and support data-driven decision-making.

# Project Objective
To transform raw traffic violation data into meaningful insights that help:
Identify peak violation times
Detect high-risk locations (hotspots)
Analyze driver behavior
Understand weather-based impact
Support smarter, safer traffic management

# Step-by-Step Project Workflow:

# Step 1 — Import Required Libraries
import os
import zipfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Step 2 — Load the CSV Data
#Loading and exploring the dataset
df=pd.read_csv('/content/Indian_Traffic_Violations.csv')
df.head() #showing first five rows.
df.tail() #showing last five rows.

# Step 3 — Understand Dataset Structure
df.info()

Total records: 4000
Total columns: 33
Mixed data types (object, int, float)
Missing values exist in:
Helmet_Worn
Seatbelt_Worn
Comments

# Summary Statistics
df.describe()
# Missing Values
df.isnull().sum()
# Duplicate Check
df.duplicated().sum()
# Dataset Shape
df.shape
# Data Types
df.dtypes

# Step 4 — Data Cleaning and Preprocessing
# Drop duplicates
df.drop_duplicates(inplace=True)

# Handle missing values (example: fill NAs or drop rows)
df.dropna(subset=['Date', 'Time'], inplace=True)

# Convert date and time columns if available
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
if 'Time' in df.columns:
    df['Time'] = pd.to_datetime(df['Time'], errors='coerce').dt.time

# Extract useful time-based features
# Drop duplicates
df.drop_duplicates(inplace=True)

# Handle missing values (example: fill NAs or drop rows)
df.dropna(subset=['Date', 'Time'], inplace=True)

# Convert date and time columns if available
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
if 'Time' in df.columns:
    df['Time'] = pd.to_datetime(df['Time'], errors='coerce').dt.time

# Extract useful time-based features
df['Day'] = df['Date'].dt.day_name()
df['Month'] = df['Date'].dt.month_name()
df['Hour'] = pd.to_datetime(df['Date']).dt.hour

print("Data cleaned and new columns added!")
df.head()

✔ Duplicates removed
✔ Missing date/time handled
✔ Extracted features: Day, Month, Hour

# Step 5 — Exploratory Data Analysis (EDA)
Violations by Day of Week
Bar graph showing which weekdays have the most violations.
Violations by Month
Seasonal/monthly trends visualized.

# Step 6 — Violation Type Analysis
✔ Most Common Violation Types(count plot)
✔ Fine Paid vs Vehicle Type (pie chart)
✔ Average Fine per Location (line plot)
✔ Top 5 Violation Types(count plot)

# Step 7 — Additional Analytical Insights
✔ Overspeeding Analysis
overspeed_count = (df['Recorded_Speed'] > df['Speed_Limit']).sum()
overspeed_percentage = (overspeed_count / total_records) * 100

Overspeeding Records: 2361
Overspeeding %: 59.03%

✔ Rainy Weather Impact
rainy_violation_percentage = (rainy_violations / total_rainy) * 100

Rainy Day Violations: 482
Ceiling Violation % in Rain: 59%

# Step 8 — Weather Condition Impact
Countplot showing how different weather conditions affect violations.

# Step 9 — Payment Method Distribution
Bar chart visualizing preferred payment modes.

# Step 10 — Time-based Violation Pattern Detection
✔ Violations by Hour
✔ Heatmap → Violations by Day vs Hour
These outputs reveal peak times of unsafe driving behavior.

# Step 11 — Hotspot Detection (Top Locations)
Top 5 most problematic areas with highest violation count.

# Step 12 — Summary Insights
print("Total Violations:", len(df))
print("Most Common Violation:", df['Violation_Type'].mode()[0])
print("Top Hotspot Location:", df['Location'].mode()[0])
print("Day with Most Violations:", df['Day'].mode()[0])

✔Total Violations: 4000
✔Most Common Violation Type: Drunk Driving
✔Top Hotspot: Gujarat
✔Most Violated Day: Monday

# Conclusion
This project successfully demonstrates how data science transforms raw traffic violation data into actionable intelligence.
Key Takeaways:
✔Time-based analysis reveals strong behavioral trends among drivers.
✔Heatmaps help understand hourly violation spikes.
✔Location-based analysis identifies high-risk areas for enforcement.
✔Weather significantly affects driving violations.
