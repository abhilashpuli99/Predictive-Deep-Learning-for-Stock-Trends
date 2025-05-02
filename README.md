# 🧠 MarketMind: Predictive Deep Learning for Stock Trends

An innovative deep learning project for analyzing and forecasting stock market movements using PyTorch and GRU networks.

---

## 📈 Overview

The stock market is a dynamic, complex ecosystem where predicting future trends can yield significant advantages. This project leverages Gated Recurrent Units (GRU) and deep learning to analyze and forecast stock trends of major companies including Google, Microsoft, IBM, and Amazon.

**Our objective:**  
Analyze historical stock data → Extract patterns → Predict future prices  
_All powered by cutting-edge neural architectures._

---

## 🧩 Problem Space

Predicting stock price trends is notoriously difficult due to:

- Market volatility  
- Non-linear dependencies  
- Time-based irregularities

We tackle this with a dual-phase approach:

- **Exploratory Data Analysis (EDA)** – Understand past behaviors, anomalies, and trends  
- **Forecasting** – Predict future "High" prices using GRU-powered models

---

## 📊 Dataset

- **Sources:** Yahoo Finance  
- **Companies:** Google, Microsoft, IBM, Amazon  
- **Features include:** Open, High, Low, Close, Volume  

---

## 🔍 Analysis Highlights

- Microsoft showed a linear upward trend over time.  
- Amazon surged exponentially after 2012, overtaking Google by 2018.  
- IBM remained relatively flat with minor fluctuations.  
- Google reflected strong seasonality and steady growth post-2012.  

---

## 🔮 Forecasting with GRU

### Why GRU?

GRUs are simplified RNN variants that:

- Use fewer parameters than LSTM  
- Handle temporal dependencies effectively  
- Are faster to train, ideal for sequence data

We apply GRU to learn from past "High" values and forecast upcoming stock movements with promising accuracy.

---

## 🚀 Tech Stack

- **Language:** Python  
- **Frameworks:** PyTorch, Matplotlib, Pandas, Scikit-learn  
- **Model:** GRU-based Recurrent Neural Network  
- **Visualization:** Matplotlib + Seaborn  

---

## 📁 Project Structure

```bash
├── data/               # Stock CSV files  
├── models/             # GRU model architecture  
├── results/            # Forecasting plots  
├── trend1,2,3...jpg          # Visual trends  
├── README.md           # You are here  
└── .gitignore          # Standard Python ignores  

THANK YOU
