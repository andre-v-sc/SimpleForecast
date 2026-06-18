# 🌬️ SimpleForecast

**A real-time Air Quality Index (AQI) web app — search any U.S. zip code and instantly see local air quality, health advisories, and AQI ratings.**

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-Framework-092E20?logo=django&logoColor=white)
![AirNow API](https://img.shields.io/badge/AirNow-API-green)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 📖 Overview

SimpleForecast is a full-stack web application that gives users real-time air quality information for any U.S. location. Built with Django and powered by the AirNow API, it translates raw AQI data into color-coded, easy-to-read health summaries — no environmental science background required.

Developed solo over approximately half a college semester as a practical exercise in API integration, back-end web development, and responsive UI design.

---

## 📸 Screenshot

> *Search any U.S. zip code for instant AQI data and health guidance.*

![SimpleForecast Demo](assets/screenshot.png)

---

## ✨ Features

- **Zip Code AQI Lookup** — Enter any U.S. zip code to retrieve up-to-the-minute air quality data
- **Color-Coded AQI Display** — Background color dynamically reflects AQI severity (Good → Hazardous)
- **Health Advisory Text** — Plain-language health guidance based on current AQI level
- **Real-Time Data** — Integrates directly with the AirNow API for live readings
- **Responsive Design** — Accessible and visually consistent across desktop and mobile devices

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend Framework | Django |
| Language | Python 3.7+ |
| External API | [AirNow API](https://www.airnowapi.org/) |
| Data Processing | NumPy |
| Async Support | Tornado |
| Frontend | HTML, CSS |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- A free [AirNow API key](https://www.airnowapi.org/account/request/)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/andre-v-sc/SimpleForecast.git
cd SimpleForecast
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
```

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure your AirNow API key**

Create a `.env` file in the project root and add your key:
```
AIRNOW_API_KEY=your_api_key_here
```

**5. Apply database migrations**
```bash
python manage.py migrate
```

**6. Run the development server**
```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/`

---

## 📋 Usage

1. Enter a valid U.S. zip code into the search bar
2. Click the search button (🔍)
3. View your location's current AQI score, category, and health advisory

### AQI Reference

| Color | Category | AQI Range |
|---|---|---|
| 🟢 Green | Good | 0–50 |
| 🟡 Yellow | Moderate | 51–100 |
| 🟠 Orange | Unhealthy for Sensitive Groups | 101–150 |
| 🔴 Red | Unhealthy | 151–200 |
| 🟣 Purple | Very Unhealthy | 201–300 |
| 🟤 Maroon | Hazardous | 301–500 |

---

## 👤 Author

**Andre** — [github.com/andre-v-sc](https://github.com/andre-v-sc)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
