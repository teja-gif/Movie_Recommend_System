# 🎬 Movie Recommender System

A simple yet effective **content-based movie recommendation app** built with **Python** and **Streamlit**.  
It suggests the top 5 most similar movies based on the one you select using **precomputed similarity scores**.

---

## Output Screenshots

### Project Screenshots

![Screenshot 2025-08-09 160926](https://github.com/user-attachments/assets/c0ce22ee-75c1-4edb-9f26-243a5ce22860)
*Movie Searching*

![Screenshot 2025-08-09 160959](https://github.com/user-attachments/assets/d907c78c-7894-4753-92f5-0596dd08b14a)
*Top 5 Recommended Movies based on similarity*

---

## ✨ Features
- 🎯 **Content-based filtering** – recommends movies similar to your selection  
- 🖥 **Interactive UI** with Streamlit  
- ⚡ Instant recommendations without long processing times  
- 🛠 Easily extendable to include movie posters, genres, and more  

---

## 🛠 Tech Stack
- **Python 3.x**
- **Pandas** – data handling
- **Pickle** – model & data storage
- **Streamlit** – web UI framework

---

## 📂 Project Structure
📦 Movie-Recommender-System
-├── 📄 app.py # Main Streamlit app
-├── 📓 Movie_Recommender_System.ipynb # Notebook used for building similarity data
-├── 📦 movie_dict.pkl # Movie dataset in dictionary format
-├── 📦 similarity.pkl # Precomputed similarity matrix
-├── 📄 requirements.txt # Dependencies
-└── 📄 README.md # Project documentation

---

## 🚀 How to Run
1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/Movie-Recommender-System.git
   cd Movie-Recommender-System
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
3. **Run the application**
   ```bash
   streamlit run app.py




