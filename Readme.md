# Recall Monitoring System Documentation

This system automates the collection, extraction, ranking, and reporting of food recalls from FDA & USDA sources. It uses multiple AI-powered agents for data extraction, economic impact estimation, and severity ranking.

## System Workflow

### 1. Data Collection Agent
- Collects recalls from public sources (FDA & USDA).
- Uses BeautifulSoup and requests to scrape recall details.

### 2. Information Extraction Agent
- Extracts key details from raw recall announcements.
- Uses OpenAI's GPT for structured extraction.

### 3. Economic Impact Agent
- Estimates the financial impact of each recall.
- Uses OpenAI to analyze impact factors.

### 4. Severity Ranking Agent
- Ranks recalls based on severity (Health risk, scope, distribution).
- Manual & AI-based ranking for accuracy.

### 5. Report Generation Agent
- Generates a weekly recall report for a VP of Supply Chain.
- Uses OpenAI to summarize recalls in a concise, actionable format.

---

## System Architecture
### Components:
- **FastAPI Backend** – Handles requests & API endpoints.
- **Data Collection Agents** – Scrapes FDA & USDA recall data.
- **AI Extraction Agents** – Uses OpenAI for structured recall data.
- **Economic Impact & Severity Ranking** – AI-powered analysis (manual + OpenAI).
- **Report Generation** – Summary Report.

---

## Installation & Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up Environment Variables
Create a `.env` file and add your credentials.

### 3. Run the System
```bash
python main.py
```

---

## Docker Deployment

### Build & Run the Docker Container
```bash
docker build -t food-recall-analysis .
docker run -d --name recall-analysis food-recall-analysis
```

---

## Severity Ranking Criteria
| Factor         | Low (1)            | Medium (2)            | High (3)                |
|---------------|-------------------|----------------------|-------------------------|
| **Health Risk** | Minor labeling issue | Undeclared allergens | Bacterial/Toxin contamination |
| **Geographic Scope** | Local Recall | Regional Recall | Nationwide Recall |
| **Distribution** | Limited (small stores) | Retail Only | Multi-channel (Retail + Online) |

### **Severity Score Calculation**
**Severity Score** = Health Risk + Scope + Distribution

#### Ranking:
- **Critical:** 8-9
- **High:** 5-7
- **Medium:** 3-4
- **Low:** 1-2

---

## Example Report
### **Recall Report - March 25, 2025**

#### **Critical Recall:**
- **Product:** Wegmans Chicken Nuggets
- **Reason:** Bone Fragment Contamination
- **Economic Impact:** $5M - $10M

#### **High Risk:**
- **Product:** Stouffer's Frozen Meals
- **Reason:** Foreign Matter Contamination
- **Economic Impact:** $2M - $5M

---

## Conclusion
✅ Real-time recall data collection from FDA & USDA  
✅ AI-powered risk assessment & economic impact estimation  
✅ Reports for decision-makers  
✅ Deployed via Docker for scalability  

