import mlflow
import argparse
from train import main
 
mlflow.set_experiment("rabies-risk-pipeline")
 
seeds = [13, 21, 42, 87, 100]
n_splits = 5
 
for seed in seeds:
    results = main(seed, n_splits)
 
    for model_name, metrics in results.items():
        with mlflow.start_run(run_name=f"{model_name}-seed-{seed}"):
            mlflow.log_param("model", model_name)
            mlflow.log_param("seed", seed)
            mlflow.log_param("n_splits", n_splits)
            mlflow.log_param("cv_strategy", "spatial_group_kfold")
 
            mlflow.log_metric("auc_roc_mean", metrics["auc_roc_mean"])
            mlflow.log_metric("auc_roc_std", metrics["auc_roc_std"])
            mlflow.log_metric("pr_auc_mean", metrics["pr_auc_mean"])
            mlflow.log_metric("pr_auc_std", metrics["pr_auc_std"])
            mlflow.log_metric("sensitivity_at_spec90_mean", metrics["sensitivity_at_spec90_mean"])
            mlflow.log_metric("accuracy_mean", metrics["accuracy_mean"])
 
print("\nAll runs logged. Launch UI with: mlflow ui")
 