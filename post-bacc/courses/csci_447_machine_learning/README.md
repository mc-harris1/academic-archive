# CSCI-447-Machine-Learning-Soft-Computing

An exploration of biologically inspired machine learning models and algorithms, including evolutionary algorithms, neural networks, swarm intelligence, and fuzzy systems.

## Structure

- `project_1/`: archived dataset outputs and the ARFF conversion helper in `src/arff_converter.py`.
- `project_2/`: Rosenbrock-function experiments for `src/mlp.py` and `src/rbf.py` driven by `src/project2.py`.
- `project_3/`: classification experiments that reuse the neural-network code with ARFF datasets and a genetic algorithm workflow.
- `project_4/`: clustering work, including k-means, competitive learning, DBSCAN, PSO, and ACO variants.

## Current Cleanup Notes

- This course folder is preserved as an archive, so the goal is safe execution and readability rather than full modernization.
- `project_4/` now resolves dataset files relative to its own directory instead of depending on the shell working directory.
- `project_4/clustering/kmeans.py` and `project_4/clustering/competitive_learning.py` are script entry points and no longer run automatically on import.

## Practical Entry Points

- `project_1/src/arff_converter.py`: ARFF conversion utility.
- `project_2/src/project2.py`: Rosenbrock regression experiments.
- `project_3/project2.py`: dataset-backed classification experiment.
- `project_4/clustering/aco.py`: ACO clustering run.
- `project_4/clustering/kmeans.py`: k-means clustering run.
- `project_4/clustering/competitive_learning.py`: competitive learning run.

## Known Constraints

- These projects mix legacy script style, local imports, and archived datasets.
- `project_2/` and `project_3/` still contain duplicated network code and would need a larger refactor to share one maintained implementation.
- `project_4/sample_runs/` and other generated artifacts are retained as historical outputs.
