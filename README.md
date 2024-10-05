# Air Pollution Prediction

## Overview

The **Air Pollution Prediction** project leverages machine learning to predict air quality based on various meteorological factors. This project is designed to help individuals and organizations understand air pollution levels, enabling them to make informed decisions regarding health and safety.

## Features

- Predicts air quality based on input parameters such as wind speed, rainfall, and stormy days.
- Implements multiple machine learning models, including Logistic Regression, Random Forest, and Support Vector Classifier (SVC).
- Scalable and easy to use with a web interface powered by Flask.

## Technologies Used

- **Python**: The main programming language used for data analysis and model building.
- **Flask**: A lightweight web framework for building the web application.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computations.
- **Scikit-learn**: For implementing machine learning models.
- **Pickle**: For saving the trained model for later use.

## Data Description

The dataset used for training the models is located in the `data.csv` file. It contains various features related to air quality, with the target variable indicating whether the air quality is good or bad.

| Column Name                    | Description                          |
|--------------------------------|--------------------------------------|
| Annual average wind speed      | Average wind speed in the area      |
| Total rainy days during the year | Total rainy days recorded          |
| Total stormy days              | Total days with storms               |
| placed                         | Target variable (0 = Bad, 1 = Good) |

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/bibasrairockz/air-pollution-prediction.git
   cd air-pollution-prediction
   ```
