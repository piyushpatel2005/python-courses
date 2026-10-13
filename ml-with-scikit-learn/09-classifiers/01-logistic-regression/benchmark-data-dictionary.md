# External benchmark fixtures

These are educational benchmarks bundled with scikit-learn, not HomeHurray Inc. business data. The lessons call the bundled loaders; they do not redistribute raw benchmark tables or fetch data at runtime. Row positions are local array indices, not personal identifiers.

## Iris

`load_iris()` supplies 150 rows, four numeric measurement columns and a species target. Features are sepal length, sepal width, petal length and petal width, all in centimeters. No missing entries occur in this bundled table. Measurements are the inputs; the species label is the prediction target. The benchmark has no business prediction timestamp and does not establish prospective data availability.

The logistic and Gaussian naive Bayes demos use all four columns. The neighbors demo uses petal length and petal width only (`data.data[:, 2:]`). `data.target_names` maps integer labels to species names; fitted `classes_` determines probability-column order.

Attribution: R. A. Fisher, Iris, UCI Machine Learning Repository, DOI **10.24432/C56C76**. The UCI record identifies the dataset license as **Creative Commons Attribution 4.0 International (CC BY 4.0)**. This attribution is distinct from scikit-learn's software license. The bundled `data.DESCR` supplies further source and measurement details.

## Wine

`load_wine()` supplies 178 rows and 13 measured constituents from wines associated with three cultivars. No missing entries occur in this bundled table. The three integer cultivar labels are targets, not feature values. Its historical analytical measurements have no HomeHurray prediction timestamp.

The logistic exercise selects alcohol, malic acid, ash and alcalinity of ash (`:4`). The naive Bayes exercise uses the first three of those (`:3`). The neighbors exercise selects alcohol and flavanoids (`[0, 6]`). Each is a numeric laboratory measurement in the benchmark's recorded scale. The bundled description names constituents but does not provide a complete unit dictionary for all selected measurements; the course deliberately does not invent physical units. See `data.feature_names` and `data.DESCR` rather than reinterpreting these columns as product weights or prices.

Attribution: Stefan Aeberhard and M. Forina, Wine, UCI Machine Learning Repository, DOI **10.24432/C5PC7J**. The UCI record identifies the dataset license as **CC BY 4.0**, separately from the software license.

## Partition and preprocessing policy

Each lesson uses the explicitly supplied stratified `train_test_split` seed and fraction. Raw feature rows and labels are split together. Fit every scaler and estimator only on training rows. Queries use saved training state. These fixtures illustrate API behavior and evaluation boundaries; their prediction output is not evidence of company performance.
