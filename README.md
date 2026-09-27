# California Housing Price Prediction using Linear Regression

## 📌 Project Overview

This project demonstrates a complete Machine Learning regression pipeline using the California Housing dataset.

The goal is to build a **Linear Regression model** that predicts the median house value based on different housing and location-related features.

---

## 🎯 Objective

- Understand the basics of Regression
- Explore the California Housing dataset
- Prepare the dataset for Machine Learning
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

Linear Regression is a supervised Machine Learning algorithm used to predict a continuous numerical value.

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

The model was evaluated using three metrics:

### MAE – Mean Absolute Error

**MAE = 0.5332**

MAE represents the average difference between the actual house values and the predicted house values.

Since the target is measured in units of $100,000:

**0.5332 × $100,000 ≈ $53,320**

The model's average prediction error is approximately **$53,320**.

Lower MAE indicates smaller prediction errors.

### MSE – Mean Squared Error

**MSE = 0.5559**

MSE measures the average squared difference between the actual and predicted values.

Lower MSE indicates smaller prediction errors.

### R² – R-squared Score

**R² = 0.5758**

The R² score indicates how much of the variation in house values is explained by the model.

The model explains approximately **57.6% of the variation** in house values.

A higher R² generally indicates that the model explains more of the variation in the target.

---

## 🏠 Example Prediction

The trained model was used to predict the value of a new house.

**Predicted House Value = 3.4108**

Since the target is represented in units of $100,000:

**3.4108 × $100,000 ≈ $341,080**

**Approximate Predicted House Value: $341,080**

---

## 📊 Model Performance

| Metric | Result |
|---|---:|
| MAE | 0.5332 |
| MSE | 0.5559 |
| R² | 0.5758 |

These results were obtained on the test dataset.

---

## 🔍 Model Analysis

The Linear Regression model achieved an **R² score of 0.5758** on the test data.

The model's average prediction error was approximately **$53,320**, based on the MAE value.

Further analysis can be performed by comparing the training and testing performance and comparing the model with a simple baseline.

---

## ✅ Conclusion

A complete Machine Learning regression pipeline was successfully implemented using the California Housing dataset.

A Linear Regression model was trained using **80% of the data** and evaluated using the remaining **20%**.

The model achieved:

- **MAE:** 0.5332
- **MSE:** 0.5559
- **R²:** 0.5758

The model was also successfully used to predict a new house value of approximately **$341,080**.

This project provided practical understanding of the complete regression workflow, from dataset preparation and model training to prediction and evaluation.
