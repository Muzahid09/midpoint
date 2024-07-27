import mlflow
import dagshub

mlflow.set_tracking_uri('https://dagshub.com/Muzahid09/midpoint.mlflow')
dagshub.init(repo_owner='Muzahid09', repo_name='midpoint', mlflow=True)


with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)