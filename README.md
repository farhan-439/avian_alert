# 🐔 AvianAlert: Early Detection, Immediate Action

A comprehensive AI monitoring system that helps farmers detect poultry diseases early through audio analysis and image classification. Developed for the Cornell Institute for Digital Agriculture Hackathon 2025.

![AvianAlert Logo](media/avian2.png)

---

## 📊 The Problem

Each year, millions of chickens die from disease. Recent outbreaks have been especially devastating:

- 💸 $600M in economic losses in the last quarter  
- 🐔 20M dead chickens  
- 🥚 96.4% increase in egg prices since last year  
- 🌾 $100M in losses for American farmers  

---

## 🧠 Our Solution

AvianAlert addresses these challenges through three key components:

1. **Flock Segmentation**  
   Divides facilities into monitored zones to prevent rapid disease spread and enable precise outbreak identification  
   ![Flock segmentation](media/Screenshot%202025-03-03%20at%202.52.08 PM.png)

2. **AI Sound Analysis**  
   Uses deep learning to classify poultry vocalizations and detect disease early  
   ![AI sound analysis](media/AISoundOverview.png)

3. **AI Excreta Analysis**  
   Analyzes chicken droppings to identify specific diseases (Salmonella, NCD, Coccidiosis, Avian Flu)  
   ![AI Excreta Analysis](media/Screenshot%202025-03-03%20at%202.52.26 PM.png)

---

## 🔬 Technical Implementation

### 🎧 Audio Classification Model

A custom CNN with **Burn Layer** technology classifies poultry sounds into:
- Healthy
- Unhealthy
- Noise (environmental)

**Performance Metrics:**
- 🎯 **Accuracy**: 91.38%
- 🚨 **Unhealthy class**: 100% sensitivity (no sick birds missed)
- 🔧 Uses mel spectrograms + CNN with Burn Layers for noise robustness

---

### 🖼️ Image Classification Model

An **EfficientNetB0** architecture classifies chicken fecal images into:
- Healthy
- Salmonella
- Newcastle Disease (NCD)
- Coccidiosis
- Avian Flu

---

## 📊 Dashboard & User Interface

Our web-based dashboard provides:
- Sound-based health indicators
- Zone-wise outbreak mapping
- Health risk analysis
- Chicken count & migration risk  
![Dashboard UI](media/IMG_8791.png)

---


## 🎬 Video Demo

<video src="https://private-user-images.githubusercontent.com/196995749/431199277-ae1ab94e-8540-467f-96c0-c18d7744723d.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDQwODUyNjQsIm5iZiI6MTc0NDA4NDk2NCwicGF0aCI6Ii8xOTY5OTU3NDkvNDMxMTk5Mjc3LWFlMWFiOTRlLTg1NDAtNDY3Zi05NmMwLWMxOGQ3NzQ0NzIzZC5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDA4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQwOFQwNDAyNDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wNTM3ZDFiMmZlN2IxZTJiM2U0MzM5MzkxYTM2N2NmYjUxNzc0NmQ3YWZmMTFlYzFkMTQyNjk5ZDc4MWEwODZiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.gXRGEpaXzW7mSuxt7DeKjIsgcqFKxGspiM-JMJrLwuc" width="720" height="405" controls></video>


---

## 🗣️ Pitch Video

[Watch our Pitch on YouTube](https://youtu.be/WwGf5H9atKg)

---

## 🌱 Sustainability Impact

- 🐣 **Lower Carbon Footprint** — fewer deaths = less waste  
- 🍳 **Food Security** — stable egg production = affordable protein  
- 💰 **Farmer Profits** — fewer disease losses = better margins  

---

## 📦 Market Readiness

- ✅ Deployment-ready AI models
- 📱 Minimal hardware needed (mic + smartphone)
- 🌍 Scalable across farms and regions

---

## 💵 Financial Overview

- 🐔 Cost per chicken: **$0.08/year**
- 💰 Potential revenue: **$100M**
- 🌎 Global savings: **$2B**
- 🧑‍🌾 Farm savings: **$500M**

---

## 👨‍💻 Team

- **Ahmed Abdulla**
- **Farhan Mashrur**
- **Suresh Kamath Bola**
- **Kiyam Merali**

---

## 📜 License

**Educational Use License**

This software is provided for educational and non-commercial purposes only. Commercial use requires explicit permission from the authors.
