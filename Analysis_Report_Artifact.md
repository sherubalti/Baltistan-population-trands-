# 📊 Baltistan Population Study (2017–2026) - Project Artifact

## 📋 Executive Summary
This project analyzes the demographic and socio-economic landscape of the **Baltistan region** in Gilgit-Baltistan, Pakistan. By integrating two datasets—Long-term Trends (2017-2026) and Detailed Socio-Economic Metrics (2020-2026)—we have developed a comprehensive analysis of the region's growth, education, and economy.

---

## 📂 Dataset Overview
1.  **Long-term Population Trends (2017-2026)**:
    *   **Scope**: Year, District, Population, Growth Rate, Area, Density.
    *   **Purpose**: Provides a macro view of the regional expansion over a decade.
2.  **Detailed Population Data (2020-2026)**:
    *   **Scope**: 31 columns including Gender splits, Age brackets, Literacy rates, GDP per capita, Poverty rates, and Employment.
    *   **Purpose**: Enables deep-dive analysis into the quality of life and economic health.

---

## 📈 Key Analysis Results (Answering the 15 Questions)

### 1. Population Change (2020 to 2026)
*   The total population of Baltistan has grown from approximately **620,679** in 2020 to a projected **697,176** by 2026.
*   This represents an overall increase of **~12.3%** over 6 years.

### 2. Year-wise Trends
*   The region shows a very stable, linear upward trend.
*   **Regression Analysis**: $R^2$ values indicate a highly predictable growth model with minimal variance.

### 3 & 4. Population Extremes
*   **Highest Population**: **2026** (Peak of the current study period).
*   **Lowest Population**: **2020** (Base year of the detailed study).

### 5 & 6. Growth & Average
*   **Total Growth**: **76,497** residents added since 2020.
*   **Average Population**: **658,240** across the 2020-2026 period.

### 7 & 8. Consistency vs. Fluctuation
*   Growth is **exceptionally consistent**. 
*   Annual increases fluctuate slightly between **11,500 and 13,500**, but the growth rate (%) remains stable around **1.8% to 2.1%**.

### 9 & 10. Growth Rate Extremes
*   **Highest Rate**: Skardu district at **2.1%**.
*   **Lowest Rate**: Roundu district at **1.7%**.

### 11. Spikes or Drops
*   No sudden demographic "shocks" were observed. The population follows a planned projection model.

### 12. Cumulative Growth
*   Cumulative growth accelerates slightly each year due to the expanding base population.

### 13. Outliers
*   **Skardu** acts as a statistical outlier in terms of scale, containing nearly **37%** of the total region's population.

### 14. Year-to-Year Comparison
*   Districts like **Ghanche** and **Shigar** show parallel growth paths, while **Skardu** pulls further ahead as the primary hub.

### 15. Long-term Observation
*   The region is transitioning from purely rural demographics to more concentrated "hub" populations, with Skardu leading the trend.

---

## 💹 Socio-Economic Insights
*   **Literacy**: Significant improvement from ~50% to ~57% on average across districts.
*   **Economy**: GDP per capita (PKR) shows a steady rise, with Skardu having the highest economic output.
*   **Gender**: A healthy balance is maintained, though male population growth is slightly faster in urbanized hubs.

---

## 💻 Technical Implementation
*   **Backend**: Flask-based Python API serving JSON data.
*   **Frontend**: High-aesthetic HTML5/CSS3 dashboard using **Chart.js** with:
    *   Bubble Map Charts for Geographic Visualization.
    *   Polar Area Charts for District Share Analysis.
    *   Multi-series Line Charts for Gender Comparisons.
*   **Notebook**: `Population_Analysis_Final.ipynb` contains the raw exploratory data analysis (EDA).
