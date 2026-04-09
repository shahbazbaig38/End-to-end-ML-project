# End-to-End ML Project: Customer Churn Prediction

This is an end-to-end machine learning project that predicts customer churn for a telecommunications company using the Telco Customer Churn dataset. The project demonstrates a complete ML pipeline from data preprocessing to model deployment.

## Features

- **Data Processing**: Automated data loading and preprocessing from the Telco Customer Churn dataset
- **Model Training**: Logistic Regression model with feature engineering using DictVectorizer
- **API Deployment**: FastAPI-based REST API for real-time predictions
- **Containerization**: Docker setup for easy deployment
- **Cloud Deployment**: Ready-to-deploy configuration for Fly.io
- **Testing**: Automated testing scripts for the prediction API

## Tech Stack

- **Python**: 3.12+
- **Machine Learning**: scikit-learn, pandas, numpy
- **API Framework**: FastAPI with Uvicorn
- **Dependency Management**: uv
- **Containerization**: Docker
- **Deployment**: Fly.io

## Project Structure

```
├── train.py          # Model training script
├── predict.py        # FastAPI prediction service
├── test.py           # API testing script
├── Dockerfile        # Docker container configuration
├── fly.toml          # Fly.io deployment configuration
├── pyproject.toml    # Project dependencies and metadata
├── uv.lock           # Locked dependency versions
└── README.md         # This file
```

## Dataset

The project uses the [Telco Customer Churn dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) from Kaggle, which contains information about telecom customers and whether they churned.

**Features used:**
- Demographic info: gender, senior citizen status, partner, dependents
- Services: phone service, multiple lines, internet service, online security, etc.
- Account info: tenure, contract type, payment method, monthly charges, total charges

**Target:** Churn (Yes/No)

## Installation

### Prerequisites

- Python 3.12 or higher
- uv (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd end-to-end-ml-project
```

2. Install dependencies using uv:
```bash
uv sync
```

3. Train the model:
```bash
uv run python train.py
```

This will create a `model.bin` file containing the trained model.

## Usage

### Running the API Locally

1. Start the FastAPI server:
```bash
uv run python predict.py
```

The API will be available at `http://localhost:9696`

### API Endpoint

**POST** `/predict`

Predicts churn probability for a customer.

**Request Body:**
```json
{
  "gender": "female",
  "seniorcitizen": 1,
  "partner": "yes",
  "dependents": "no",
  "phoneservice": "no",
  "multiplelines": "no_phone_service",
  "internetservice": "dsl",
  "onlinesecurity": "yes",
  "onlinebackup": "yes",
  "deviceprotection": "no",
  "techsupport": "no",
  "streamingtv": "no",
  "streamingmovies": "no",
  "contract": "month-to-month",
  "paperlessbilling": "no",
  "paymentmethod": "electronic_check",
  "tenure": 0,
  "monthlycharges": 0.85,
  "totalcharges": 2.85
}
```

**Response:**
```json
{
  "churn_probability": 0.85,
  "churn": true
}
```

### Testing the API

Run the test script to verify the API is working:

```bash
uv run python test.py
```

## Docker Deployment

### Build and Run Locally

```bash
# Build the Docker image
docker build -t churn-prediction .

# Run the container
docker run -p 9696:9696 churn-prediction
```

### Deploy to Fly.io

1. Install Fly CLI and login:
```bash
fly auth login
```

2. Deploy:
```bash
fly deploy
```

The API will be available at the URL provided by Fly.io.

## Model Details

- **Algorithm**: Logistic Regression with liblinear solver
- **Features**: 19 categorical + 3 numerical features
- **Preprocessing**: DictVectorizer for categorical encoding
- **Pipeline**: sklearn Pipeline combining vectorizer and classifier

## Development

### Code Quality

The project uses modern Python practices with type hints and Pydantic models for API validation.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## Acknowledgments

- Dataset from [Kaggle Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- Based on ML Zoomcamp modules 3, 4, and 5
- Uses uv for fast Python package management