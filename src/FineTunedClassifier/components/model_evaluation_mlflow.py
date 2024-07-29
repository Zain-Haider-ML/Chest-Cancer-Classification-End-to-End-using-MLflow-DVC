import tensorflow as tf
from pathlib import Path
import mlflow
import mlflow.keras
from urllib.parse import urlparse
import os
from FineTunedClassifier.config.configuration import EvaluationConfig
from FineTunedClassifier.utils.common import *




class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config
        # Set environment variables for MLflow tracking
        os.environ['MLFLOW_TRACKING_URI'] = 'https://dagshub.com/hzain8206/Chest-Cancer-Classification-End-to-End-using-MLflow-DVC.mlflow'
        os.environ['MLFLOW_TRACKING_USERNAME'] = 'hzain8206'
        os.environ['MLFLOW_TRACKING_PASSWORD'] = '23fd9f7c1c75603a0376d3ba7291d1d4d6c909c5'


    
    def _test_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            # validation_split=0.30
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        test_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.test_generator = test_datagenerator.flow_from_directory(
            directory=self.config.testing_data,
            # subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )


    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._test_generator()
        self.score = self.model.evaluate(self.test_generator)
        self.save_score()

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)

    
    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(
                {"loss": self.score[0], "accuracy": self.score[1]}
            )
            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.keras.log_model(self.model, "model", registered_model_name="VGG16Model")
            else:
                mlflow.keras.log_model(self.model, "model")