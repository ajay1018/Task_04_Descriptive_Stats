# 🧠 Task 04 – Descriptive Statistics & Social Media Analysis (2024 US Elections)

## 📘 Objective
Build a system that computes descriptive statistics and visualizations on political ad activity during the 2024 U.S. Presidential election using:
- Pure Python
- Pandas
- Polars

---

## 📂 Files Included
| Filename               | Description                                 |
|------------------------|---------------------------------------------|
| `pure_python_stats.py` | Descriptive stats using only base Python    |
| `pandas_stats.py`      | Analysis using pandas                       |
| `polars_stats.py`      | Fast analysis using polars                  |
| `bonus_visuals.ipynb`  | Visual insights using matplotlib/seaborn    |

---

## 📊 Dataset Info
We used the following real-world datasets (not included in this repo):

- 📁 `2024_fb_ads_president_scored_anon.csv`
- 📁 `2024_fb_posts_president_scored_anon.csv`
- 📁 `2024_tw_posts_president_scored_anon.csv`

📥 Download Link:  
[Facebook & Twitter Election Ads Dataset](https://drive.google.com/file/d/1Jq0fPb-tq76Ee_RtM58fT0_M3o-JDBwe/view?usp=sharing)

> ⚠️ These files are excluded from the repo as per instructions.

---

## 🚀 How to Run the Scripts

You can run each script from the command line:

```bash
python pure_python_stats.py data/2024_fb_ads_president_scored_anon.csv
python pandas_stats.py data/2024_fb_posts_president_scored_anon.csv
python polars_stats.py data/2024_tw_posts_president_scored_anon.csv
```
## 📈 Visual Highlights

Visualizations were created using seaborn and matplotlib inside bonus_visuals.ipynb.

Histogram of estimated_impressions showed a highly skewed distribution
Bar chart of top 10 page_ids revealed a few high-activity pages
These visuals help quantify ad reach and campaign dominance

## ✅ Comparison Summary

| Feature        | Pure Python        | Pandas          | Polars               |
| -------------- | ------------------ | --------------- | -------------------- |
| Setup          | No installation    | Easy to install | Requires pip install |
| Speed          | Slowest            | Moderate        | Fastest              |
| Code Length    | Long/Manual        | Concise         | Very concise         |
| Learning Value | High (educational) | Great for EDA   | Ideal for large data |
| Recommend to   | Learners           | Analysts        | Performance users    |


##💡 Key Observations

Facebook ads tend to have low estimated_impressions, with a few extreme outliers
A small group of page_ids posted most content, showing high campaign activity
Ads frequently touched on themes like economy, education, and governance
Visualization highlighted skewness in estimated_spend and estimated_impressions
Pandas and Polars made EDA fast and intuitive, while base Python was verbose but insightful
Polars performed noticeably faster with large files
