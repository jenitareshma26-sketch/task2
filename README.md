# California Housing Price Prediction using Linear Regression

## 📌 Project Overview

This project demonstrates a complete Machine Learning regression pipeline using the California Housing dataset.

The goal is to build a **Linear Regression model** that predicts the median house value based on different housing and location-related features.

---

## 🎯 Objective

- Understand the basics of Regression
- Explore the California Housing dataset
- Train a Linear Regression model
- Make house value predictions
- Evaluate the model using MAE, MSE, and R²

---

## 📊 Dataset

The California Housing dataset contains information about housing districts in California.

### Features

- **MedInc** – Median income
- **HouseAge** – Median house age
- **AveRooms** – Average number of rooms
- **AveBedrms** – Average number of bedrooms
- **Population** – Population of the district
- **AveOccup** – Average occupancy
- **Latitude** – Geographic latitude
- **Longitude** – Geographic longitude

### Target

**MedHouseVal** – Median house value.

The target is represented in units of **$100,000**.

For example:

`3.41` ≈ `$341,000`

---

## 🔄 Machine Learning Pipeline

The project follows these steps:

1. Load the dataset
2. Separate features and target
3. Split the data into training and testing sets
4. Create a Linear Regression model
5. Train the model
6. Make predictions
7. Evaluate the model
8. Predict the value of a new house

---

## 🧠 Model Used

### Linear Regression

Linear Regression is a supervised learning algorithm used to predict a continuous numerical value.

In this project:

**Input:** Housing and location features

**Output:** Predicted median house value

---

## 📈 Train-Test Split

The dataset was divided into:

- **80% Training Data**
- **20% Testing Data**

The training data is used to teach the model, while the testing data is used to evaluate how well the model performs on unseen data.

---

## 📏 Model Evaluation

The model was evaluated using three metrics.

### MAE – Mean Absolute Error

```text
MAE = 0.5332
