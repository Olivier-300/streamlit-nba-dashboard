# 🏀 Basketball Stats & Analysis App

![Basketball Stats](basketball_stats.png)

**Basketball Stats & Analysis** is a **Streamlit** web application that allows users to analyze **NBA player statistics**, visualize **shot charts**, and explore **dynamic performance metrics**. The application leverages **Pandas, Plotly, and Matplotlib** to provide rich visualizations and insights.

## 🚀 Features

✅ **Player Performance Analysis**: Compare player stats across different seasons.  
✅ **Dynamic Visualizations**: Graphs and interactive charts for better insights.  
✅ **Shot Chart Visualization**: See where players make and miss shots on a **basketball court map**.  
✅ **Filters & Search Options**: Customize your search by season, team, and player.  
✅ **NBA Data Scraping & Machine Learning**: Automate data retrieval and make predictions.  

## 📂 Project Structure

```
BasketballStats/
│── app.py                  # Main Streamlit application
│── players_stats_regular.xlsx  # Regular season player statistics
│── players_stats_playoff.xlsx  # Playoff season player statistics
│── nba_shot_data_2023_2024.csv  # Shot chart data for NBA players
│── requirements.txt        # Python dependencies
│── images/                 # Folder for images used in the README
```

## 🛠️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-repo/BasketballStats.git
cd BasketballStats
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application
```bash
streamlit run app.py
```

The application will be accessible at `http://localhost:8501/`.

## 📊 Usage

### 🏀 Player Profile Page
![Player Profile](images/player_profile.png)
- View **detailed player stats** and **background information**.
- Explore **career achievements, skills, and project experiences**.

### 📈 Data Analysis Page
![Data Analysis](images/data_analysis.png)
- **Filter by season, team, or player** to see relevant statistics.
- View **interactive graphs** for Points, Rebounds, Assists, and more.
- Compare players **side-by-side** using **bar plots, scatter plots, and bubble charts**.

### 🎯 Shot Chart - Court Map Visualization
![Shot Chart](images/shot_chart.png)
- **View NBA shot maps** for selected players.
- Analyze **made vs. missed shots** using **red and green markers**.
- Identify shooting efficiency **from different spots on the court**.

## 🎯 How It Works

1️⃣ **Select a season** (Regular or Playoff).  
2️⃣ **Choose teams and players** from the sidebar filters.  
3️⃣ **View performance statistics** and compare key metrics.  
4️⃣ **Analyze shot accuracy** and shooting trends using the court map.  

## 🔐 Technologies Used

- **Streamlit** 🎛️: Web app framework for data visualization.
- **Pandas** 🐼: Data processing and analysis.
- **Plotly & Matplotlib** 📊: Dynamic and interactive data visualization.
- **NBA API & Web Scraping** 🕵️‍♂️: Data retrieval for player statistics.

## 📜 License

This project is licensed under **MIT**. See the [LICENSE](LICENSE) file for more details.

---

💡 *Want to contribute? Feel free to open an issue or pull request!* 🚀
