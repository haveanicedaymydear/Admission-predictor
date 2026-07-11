# Methodology and Evidence Record

## Dataset

- 768 instances
- 8 numeric predictors
- Binary target: `Outcome`
- Class distribution in the included file:
  - 500 negative cases
  - 268 positive cases

## Preprocessing

The recorded Orange workflow used:

- target assignment through **Select Columns**
- **Average / Most Frequent** imputation
- feature standardisation to `μ = 0`, `σ² = 1`

The dataset file contains no explicit `NaN` cells. However, several medical variables contain zero values that may represent unavailable measurements. The preserved workflow reflects the original experiment and should not be interpreted as a clinically validated missing-data protocol.

## Models

### Logistic Regression

- regularisation: Ridge (L2)
- strength: `C = 1`
- class balancing: disabled

### Random Forest

- number of trees: 100
- minimum subset size: 5
- class balancing: disabled

## Evaluation

- stratified 5-fold cross-validation
- metrics: AUC, classification accuracy, F1, precision, recall, MCC
- ROC curves merged from cross-validation folds

## Recorded results

| Model | AUC | Accuracy | F1 | Precision | Recall | MCC |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.828 | 0.775 | 0.767 | 0.770 | 0.775 | 0.486 |
| Random Forest | 0.824 | 0.764 | 0.760 | 0.759 | 0.764 | 0.468 |

The observed differences are modest. This evidence supports Logistic Regression as the stronger recorded baseline in this configuration, but it does not establish general superiority beyond this experiment.

## Public-release decisions

The full university coursework submission and assessment brief are **not** included. The public branch contains only a curated technical evidence package and a sanitised Orange workflow.
