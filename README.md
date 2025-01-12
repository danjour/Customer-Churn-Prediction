# Customer Churn Prediction

[![LinkedIn][linkedin-shield]][linkedin-url]
[![Outlook][outlook-shield]][outlook-url]


## Project Overview

The goal of this project is to develop a predictive model that anticipates customer churn. By identifying customers at risk of leaving, we can take proactive measures to retain them and improve business outcomes.

---

## Objective

The objective of this project is to train a compact machine learning model capable of predicting customer churn. With this model, businesses can identify high-risk customers and take appropriate actions to retain them, reducing churn rates and improving customer satisfaction.

---

## Dataset

The dataset used in this project contains several customer attributes and their subscription details. Below is a sample of the data:

| Age | Gender | Tenure | Monthly Charges | Contract Type   | Tech Support | Churn |
| --- | ------ | ------ | --------------- | -------------- | ------------ | ----- |
| 34  | Female | 24     | 70.5            | Month-to-Month | Yes          | 0     |
| 45  | Male   | 12     | 80.2            | One Year       | No           | 1     |
| 27  | Female | 6      | 55.3            | Two Year       | Yes          | 0     |

---

## Model

For this project, we used a **K-Nearest Neighbors (KNN)** model due to its simplicity and effectiveness in handling classification tasks. The model is trained using the customer attributes, and it predicts whether the customer is likely to churn (leave the company).

### Steps Involved:

1. **Data Preprocessing**: Cleaning and transforming the dataset to ensure it is in the right format for modeling.
2. **Feature Engineering**: Creating new features and encoding categorical variables.
3. **Model Training**: Training the KNN model with the processed data.
4. **Model Evaluation**: Evaluating the model performance using metrics like accuracy, precision, recall, and F1-score.

---

## Features

The model takes the following customer attributes as input:

- **Age**: The age of the customer.
- **Gender**: The gender of the customer (Male/Female).
- **Tenure**: The duration (in months) the customer has been with the company.
- **Monthly Charges**: The monthly payment made by the customer.
- **Contract Type**: Type of contract the customer has (Month-to-Month, One Year, Two Year).
- **Tech Support**: Whether the customer has access to technical support (Yes/No).
- **Churn**: The target variable indicating whether the customer churned (1 for churned, 0 for not churned).

---

## Installation

To run this project on your local machine, follow the steps below:

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction
```

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/eduardodanjour/
[facebook-shield]:	https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=555
[facebook-url]: https://www.facebook.com/eduardo.danjour/
[outlook-shield]:https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=555
[outlook-url]: https://www.facebook.com/eduardo.danjour/
