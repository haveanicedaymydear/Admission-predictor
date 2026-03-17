# Admission-predictor

A lightweight machine learning project that predicts graduate admission outcomes using logistic regression and an interactive Streamlit interface.

## Overview

This project is a personal implementation of a binary classification workflow for admission prediction.

The main purpose of this repository is not only to build a simple predictor, but also to better understand how a classical machine learning model works from the ground up.  
It includes data preprocessing, normalization, logistic regression logic, evaluation metrics, and a small interactive frontend for testing predictions.

## Features

- Logistic Regression implementation for binary classification
- Interactive Streamlit web interface
- Prediction based on academic and profile-related inputs
- Simple and lightweight project structure for learning and demonstration
- End-to-end workflow from data to user-facing prediction

## Input Features

The model uses the following inputs:

- GRE Score
- TOEFL Score
- University Rating
- SOP Strength
- LOR Strength
- CGPA
- Research Experience

## Dataset

This project uses an admission prediction dataset with applicant-level academic features.  
For binary classification, the target is converted into an admitted / not admitted outcome using a defined threshold.

## Why This Project Matters

This repository reflects my interest in building interpretable and lightweight ML systems.

It demonstrates:

- core understanding of supervised learning
- feature-based tabular prediction
- practical model evaluation
- simple ML app deployment with Streamlit

Although small in scale, it is useful as a foundational ML portfolio project because it connects theory, implementation, and presentation.

## Tech Stack

- Python
- NumPy
- Pandas
- Matplotlib
- Streamlit

## Learning Goals

Through this project, I aimed to strengthen my understanding of:

- logistic regression fundamentals
- data preprocessing and normalization
- binary classification metrics
- turning an ML workflow into a small interactive application

## Project Structure

```text
.devcontainer/
admission_data.csv
streamlit_app.py
requirements.txt
README.md
LICENSE
