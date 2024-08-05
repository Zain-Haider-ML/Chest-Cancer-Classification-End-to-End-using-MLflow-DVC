# Chest Cancer Classifier

This project is designed to classify chest cancer using deep learning techniques. It leverages various tools and frameworks including DVC for data version control, MLFlow for experiment tracking, DagsHub for versioned dataset storage and collaboration, Flask for API creation, and Microsoft Azure for deployment.

## Project Structure

```bash
Chest-Cancer-Classifier/
├── artifacts/
│   └── training/
│       └── model.h5
├── config/
│   └── config.yaml
├── research/
│   ├── 01_prepare_model.ipynb
│   ├── 02_model_trainer.ipynb
│   └── 03_model_evaluation_with_mlflow.ipynb
│   └── trials.ipynb
├── src/
│   ├── FineTunedClassifier/
│   │   ├── __pycache__/
│   │   ├── components/
│   │   ├── config/
│   │   ├── constants/
│   │   ├── entity/
│   │   ├── pipeline/
│   │   └── utils/
│   │   └── __init__.py
│   └── FineTunedClassifier.egg-info
├── templates/
│   └── index.html
├── .gitignore
├── app.py
├── dvc.yaml
├── LICENSE
├── main.py
├── params.yaml
├── README.md
├── requirements.txt
├── setup.py
└── template.py
```

## Setup

### Prerequisites

- Python 3.8+
- [DVC](https://dvc.org/doc/install)
- [MLFlow](https://mlflow.org/docs/latest/quickstart.html)
- [DagsHub](https://dagshub.com/)
- Flask
- Azure Account for deployment

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Zain-Haider-ML/Chest-Cancer-Classification-End-to-End-using-MLflow-DVC.git
    cd Chest-Cancer-Classifier
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up DVC:
    ```bash
    dvc init
    ```

4. Set up MLFlow with DagsHub:
    - Follow the [DagsHub documentation](https://dagshub.com/docs/integration/mlflow/) to set up MLFlow with DagsHub for tracking your experiments.

5. Configure your Azure deployment settings.

## Usage

### Data Preparation

1. Prepare your dataset and configure paths in `config/config.yaml`.
2. Track your data with DVC:
    ```bash
    dvc add path/to/your/data
    dvc push
    ```

### Research and Experimentation

1. Use the Jupyter notebooks in the `research` directory for experimentation before integrating code into the pipeline:
    - `01_prepare_model.ipynb`: Data preparation and preprocessing experiments.
    - `02_model_trainer.ipynb`: Model training experiments.
    - `03_model_evaluation_with_mlflow.ipynb`: Model evaluation and experiment tracking with MLFlow and DagsHub.
    - `trials.ipynb`: For experimenting with different models or configurations.

### Model Pipeline

1. Integrate your validated code into the pipeline located in the `src` directory:
    - `components/`: Contains various components of the model pipeline.
    - `config/`: Configuration files.
    - `constants/`: Constant values used across the project.
    - `entity/`: Defines the entities and data structures.
    - `pipeline/`: Assembles the components into a complete pipeline.
    - `utils/`: Utility functions.

### API Creation

1. Create an API using Flask:
    ```bash
    python app.py
    ```
   The API will be available at `http://127.0.0.1:5000`.

### Deployment

1. Deploy your model to Azure. Follow the official Azure deployment guide.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [DVC](https://dvc.org/)
- [MLFlow](https://mlflow.org/)
- [DagsHub](https://dagshub.com/)
- [Flask](https://flask.palletsprojects.com/)
- [Microsoft Azure](https://azure.microsoft.com/)