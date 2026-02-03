from flask import Flask, render_template, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Data Loading Logic
def get_data():
    df_detailed = pd.read_csv('baltistan_population_2020_2026.csv')
    df_trends = pd.read_csv('baltistan_population_trends.csv')
    
    # Yearly Aggregation
    df_yearly = df_detailed.groupby('year').agg({
        'total_population': 'sum',
        'male_population': 'sum',
        'female_population': 'sum'
    }).reset_index()
    
    # District 2026 Data
    df_2026 = df_detailed[df_detailed['year'] == 2026]
    
    # Map Coordinates (Simplified mapping for visualization)
    coords = {
        'Skardu': {'x': 75.6, 'y': 35.3},
        'Ghanche': {'x': 76.8, 'y': 35.2},
        'Shigar': {'x': 75.7, 'y': 35.8},
        'Kharmang': {'x': 76.1, 'y': 34.9},
        'Roundu': {'x': 74.8, 'y': 35.5}
    }
    
    district_list = []
    for _, row in df_2026.iterrows():
        d_name = row['district']
        district_list.append({
            'name': d_name,
            'pop': int(row['total_population']),
            'gdp': int(row['gdp_per_capita_pkr']),
            'literacy': float(row['literacy_rate']),
            'x': coords.get(d_name, {}).get('x', 75.0),
            'y': coords.get(d_name, {}).get('y', 35.0)
        })
        
    # Advanced Analytics for Complex Charts
    df_2026_totals = df_2026[['age_0_14', 'age_15_64', 'age_65_plus']].sum()
    age_demographics = [
        {'label': 'Youth (0-14)', 'value': int(df_2026_totals['age_0_14'])},
        {'label': 'Working Age (15-64)', 'value': int(df_2026_totals['age_15_64'])},
        {'label': 'Seniors (65+)', 'value': int(df_2026_totals['age_65_plus'])}
    ]

    employment_stats = {
        'employed': int(df_2026['employed'].sum()),
        'unemployed': int(df_2026['unemployed'].sum())
    }

    correlations = []
    for _, row in df_detailed.iterrows():
        correlations.append({
            'literacy': float(row['literacy_rate']),
            'gdp': int(row['gdp_per_capita_pkr']),
            'district': row['district']
        })

    dist_metrics = {
        'population': df_detailed['total_population'].tolist(),
        'gdp': df_detailed['gdp_per_capita_pkr'].tolist(),
        'literacy': df_detailed['literacy_rate'].tolist()
    }

    # Analytical Calculations for all 14 points
    df_yearly['change'] = df_yearly['total_population'].diff().fillna(0)
    df_yearly['growth_rate'] = (df_yearly['total_population'].pct_change() * 100).fillna(0)
    df_yearly['cumulative_growth'] = df_yearly['total_population'] - df_yearly['total_population'].iloc[0]
    
    # 1. & 14. Long-Term Trend
    long_term_trend = df_trends.groupby('year')['population'].sum().reset_index().to_dict(orient='records')
    
    # 3. Highest vs Lowest District by Year
    hi_lo_districts = []
    for year in df_detailed['year'].unique():
        yr_data = df_detailed[df_detailed['year'] == year]
        hi = yr_data.loc[yr_data['total_population'].idxmax()]
        lo = yr_data.loc[yr_data['total_population'].idxmin()]
        hi_lo_districts.append({
            'year': int(year),
            'hi_name': hi['district'], 'hi_val': int(hi['total_population']),
            'lo_name': lo['district'], 'lo_val': int(lo['total_population'])
        })

    # 7. Consistency
    growth_rates = df_yearly['growth_rate'].iloc[1:]
    consistency = 100 - (growth_rates.std() / growth_rates.mean() * 100) if not growth_rates.empty else 100
    
    # 12. Outlier Analysis
    pop_2026 = df_2026['total_population']
    q1, q3 = pop_2026.quantile(0.25), pop_2026.quantile(0.75)
    iqr = q3 - q1
    outliers = df_2026[(pop_2026 < (q1 - 1.5 * iqr)) | (pop_2026 > (q3 + 1.5 * iqr))]['district'].tolist()

    # Process Torrent/Flood Data
    df_torrent = pd.read_csv('gb_torrent_data_2020_2026.csv')
    df_torrent_baltistan = df_torrent[df_torrent['is_baltistan'] == True]
    
    # Yearly flood metrics for Baltistan
    torrent_yearly = df_torrent_baltistan.groupby('year').agg({
        'rainfall_mm': 'mean',
        'economic_loss_million_pkr': 'sum',
        'houses_affected': 'sum'
    }).reset_index().to_dict(orient='records')

    # District-wise vulnerability
    vulnerability = df_torrent_baltistan.groupby('district').agg({
        'economic_loss_million_pkr': 'sum',
        'rainfall_mm': 'max'
    }).reset_index().to_dict(orient='records')

    return {
        'yearly': df_yearly.to_dict(orient='records'),
        'districts': district_list,
        'age_demo': age_demographics,
        'employment': employment_stats,
        'correlations': correlations,
        'distribution': dist_metrics,
        'torrent': {
            'yearly': torrent_yearly,
            'vulnerability': vulnerability
        },
        'analytics': {
            'long_term': long_term_trend,
            'hi_lo': hi_lo_districts,
            'total_growth': int(df_yearly['total_population'].iloc[-1] - df_yearly['total_population'].iloc[0]),
            'avg_pop': float(df_yearly['total_population'].mean()),
            'max_growth_year': int(df_yearly.loc[df_yearly['change'].idxmax()]['year']),
            'min_growth_year': int(df_yearly.loc[df_yearly['change'].idxmin()]['year']),
            'consistency': float(consistency),
            'outliers': outliers,
            'cumulative': df_yearly[['year', 'cumulative_growth']].to_dict(orient='records'),
            'yoy_change': df_yearly[['year', 'change', 'growth_rate']].to_dict(orient='records')
        }
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def data_api():
    try:
        data = get_data()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting Baltistan Population Dashboard Server...")
    print("Access it at: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
