# ESG AI Platform

## 1. Introduction

This project is an AI-powered ESG analysis platform that evaluates companies based on Environmental, Social, and Governance metrics.

## 2. Objectives

* Extract ESG insights from company data
* Provide ESG scoring and visualization
* Enable portfolio-level ESG analysis

## 3. Features

* ESG score dashboard (Radar + Trend)
* Peer comparison
* Controversy timeline
* Clickable evidence viewer
* ESG screener
* Portfolio analyzer (CSV upload)
* PDF report export
* REST API

## 4. System Architecture

Frontend: React
Backend: FastAPI
Data: JSON-based ESG dataset

## 5. Workflow

1. User selects company
2. Backend calculates ESG score
3. Frontend displays charts
4. User analyzes evidence
5. Portfolio analysis via CSV
6. Report exported as PDF

## 6. API Endpoints

* /score/{ticker}
* /history/{ticker}
* /news/{ticker}
* /portfolio/upload
* /screener
* /report/{ticker}

## 7. Results

* Accurate ESG scoring
* Interactive visualization
* Portfolio ESG exposure calculation

## 8. Conclusion

The system provides a complete ESG analysis pipeline with visualization, filtering, and reporting capabilities.

## 9. Future Work

* Real ESG extraction (NLP)
* FinBERT sentiment
* MSCI comparison
