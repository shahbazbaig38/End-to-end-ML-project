import requests

url = 'http://localhost:9696/predict'
# url = 'https://mlzoomcamp-flask-uv.fly.dev/predict'

customer = {
    'gender': 'female',
    'seniorcitizen': 1,
    'partner': 'yes',
    'dependents': 'no',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'yes',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'no',
    'paymentmethod': 'electronic_check',
    'tenure': 0,
    'monthlycharges': 0.85,
    'totalcharges': 2.85
}

response = requests.post(url, json=customer)

predictions = response.json()

if predictions['churn']:
    print('customer is likely to churn, send promo')
else:
    print('customer is not likely to churn')