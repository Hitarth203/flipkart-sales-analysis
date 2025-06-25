# Flipkart Sales Analysis 📦📊

This project involves cleaning, analyzing, and visualizing e-commerce sales data from a Flipkart-like online orders dataset. The goal is to derive insights such as the best sales month, peak purchase hours, top-selling products, and popular product categories.

---

## 📁 Dataset

The dataset used belongs to the Client work (can be shared) and contains:

- Product names
- Brands
- Retail and discounted prices
- Timestamps (`crawl_timestamp`)
- Product category hierarchy
- Ratings and more

---

## 🧹 Data Cleaning Steps

- Removed outliers in the `retail_price` column using Z-score
- Standardized brand names to title case
- Extracted `year`, `month`, `day`, `hour`, `minute` from the `crawl_timestamp`
- Cleaned `product_category_tree` and extracted the `Main_Category`
- Reordered columns and added serial numbers
- Final cleaned data exported as Excel file

---

## 📊 Analysis Questions Answered

### 1. **What was the best month for sales?**
- **January** had the highest total revenue.
- Shown using a **pie chart** of monthly sales distribution.

### 2. **What time should we display advertisements to maximize purchases?**
- Peak purchasing hours identified using a **line chart** of order frequency by hour.

### 3. **Which product category sold the most?**
- `Main_Category` extracted and visualized via a **bar chart** showing top categories.

### 4. **Top 10 products sold in the six-month period?**
- Most frequently sold products visualized in a **bar chart**.

---

## 📷 Visual Outputs

- **Pie Chart** – Sales Distribution by Month  
- **Line Plot** – Hourly Purchase Distribution  
- **Bar Chart** – Top 10 Products Sold  
- **Bar Chart** – Top Product Categories  

All saved inside the `images/` folder for sharing or presentation.

---

## 🛠️ Tools Used

- **Python**
- **Pandas & NumPy** – Data cleaning and manipulation
- **Matplotlib & Seaborn** – Visualizations
- **SciPy** – Z-score for outlier detection
- **Jupyter Notebook / VS Code** – Development environment

---

## ✅ Project Status

✔️ Completed and ready to upload on GitHub  
✔️ Can be used in portfolio or resume  
✔️ Easy to extend with more EDA or ML models

---

## 🙋‍♂️ Author

**Hitarth Wadhwani**  
BCA in AI & ML | Aspiring Data Scientist  
📧 Reach out for collaborations or suggestions!



