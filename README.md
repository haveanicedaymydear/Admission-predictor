# Diabetes Prediction in Orange

A reproducible visual machine-learning workflow comparing **Logistic Regression** and **Random Forest** on the Pima Indians Diabetes dataset.

## Project question

Can a transparent linear baseline compete with a nonlinear ensemble on a small tabular healthcare dataset?

## Workflow

1. Import the CSV dataset and assign `Outcome` as the categorical target.
2. Apply mean / most-frequent imputation.
3. Standardise numeric features to mean 0 and variance 1.
4. Configure Logistic Regression with Ridge / L2 regularisation (`C = 1`).
5. Configure Random Forest with 100 trees.
6. Evaluate both learners with stratified 5-fold cross-validation.
7. Compare AUC, accuracy, F1, precision, recall, MCC, and ROC behaviour.

## Recorded results

| Model | AUC | Accuracy | F1 | Precision | Recall | MCC |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | **0.828** | **0.775** | **0.767** | **0.770** | **0.775** | **0.486** |
| Random Forest | 0.824 | 0.764 | 0.760 | 0.759 | 0.764 | 0.468 |

The difference is modest, but Logistic Regression produced the stronger recorded baseline across all reported metrics. For this small tabular dataset, the result supports preferring the simpler and more interpretable model unless further tuning or additional features justify a more complex learner.

## Repository structure

```text
.
├── README.md
├── data/
│   └── diabetes.csv.gz
├── workflow/
│   └── diabetes_prediction.ows.gz
├── results/
│   ├── metrics.csv
│   └── dataset_summary.json
├── docs/
│   └── methodology.md
└── scripts/
    └── unpack.py
```

## Reproduce in Orange

1. Install [Orange Data Mining](https://orangedatamining.com/).
2. Run `python scripts/unpack.py` to restore the CSV and Orange workflow.
3. Open `workflow/diabetes_prediction.ows`.
4. In the **File** widget, select `data/diabetes.csv`.
5. Confirm that `Outcome` is the categorical target.
6. Run **Test & Score** and inspect **ROC Analysis**.

The public workflow has been sanitised to remove local file paths and student identifiers, so the dataset must be re-linked after opening.

## Evidence notes

- Dataset size: 768 rows, 8 numeric predictors, 1 binary target.
- Evaluation: stratified 5-fold cross-validation.
- Logistic Regression: Ridge / L2 regularisation, `C = 1`.
- Random Forest: 100 trees.
- Recorded metrics are preserved in `results/metrics.csv`.
- The methodology and public-release decisions are documented in `docs/methodology.md`.

## Limitations

- This is a small educational tabular-ML experiment, not a clinical diagnostic system.
- No external validation cohort was used.
- Hyperparameter search was limited.
- Zero values in some clinical fields may encode unavailable measurements; the preserved Orange workflow reflects the original experiment and should not be interpreted as a clinically validated cleaning protocol.
- The result is a baseline comparison, not evidence of medical utility.

## Public-release note

The full university coursework submission and assessment brief are not included. This branch contains only a curated technical evidence package and a sanitised Orange workflow.

## Author

**Livan Zhou (ZHOU Liuyuehan)**  
[GitHub profile](https://github.com/haveanicedaymydear)
