# install (python3 and python2)
`pip install -U git+http://github.com/biolee/tensorflow_serving_api_python.git`

# use
```python
from tensorflow_serving.apis import predict_pb2, prediction_service_pb2

channel = implementations.insecure_channel(host, port)
stub = prediction_service_pb2.beta_create_PredictionService_stub(channel)

serving_request = predict_pb2.PredictRequest()
serving_results = stub.Predict(serving_request, time_out)
```