# INTROEXTROAMBI – Personality Synthetic App (Streamlit)

A simple Streamlit web app that loads a synthetic personality dataset, allows filtering, and provides visual insights through charts and summaries.

## 🌟 Features

✅ Load dataset from `Dataset/personality_synthetic_dataset.csv`  
✅ Display dataset preview and summary (shape, columns, data types)  
✅ Filter data by categorical columns using the sidebar  
✅ Visualize data with:
- Histogram
- Box Plot
- Correlation Heatmap  

---

## 📂 Project Structure

IntroExtroAmbi/
├── app.py
├── Dataset/
│ └── personality_synthetic_dataset.csv
└── README.md

yaml
Copy
Edit

---

## ⚙ Requirements

Install the required Python packages:

```bash
pip install streamlit pandas matplotlib seaborn
🚀 Run the App
From your project directory:

bash
Copy
Edit
streamlit run app.py
📝 Notes
Ensure that personality_synthetic_dataset.csv is placed inside the Dataset/ folder.

You can add more visualizations or filters as needed.

