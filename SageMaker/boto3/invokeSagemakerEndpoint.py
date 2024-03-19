
import boto3
import json

text1 = 'astonishing ... ( frames ) profound ethical and philosophical questions in the form of dazzling pop entertainment'
text2 = 'simply stupid , irrelevant and deeply , truly , bottomlessly cynical '
newline, bold, unbold = '\n', '\033[1m', '\033[0m'

def query_endpoint(encoded_text):
    endpoint_name = 'jumpstart-dft-tf-tc-bert-en-cased-l-20240318-164743'
    client = boto3.client('runtime.sagemaker')
    response = client.invoke_endpoint(EndpointName=endpoint_name, ContentType='application/x-text', Body=encoded_text, Accept='application/json;verbose')
    return response

def parse_response(query_response):
    model_predictions = json.loads(query_response['Body'].read())
    probabilities, labels, predicted_label = model_predictions['probabilities'], model_predictions['labels'], model_predictions['predicted_label']
    return probabilities, labels, predicted_label

for text in [text1, text2]:
    query_response = query_endpoint(text.encode('utf-8'))
    probabilities, labels, predicted_label = parse_response(query_response)
    print (f"Inference:{newline}"
            f"Input text: '{text}'{newline}"
            f"Model prediction: {probabilities}{newline}"
            f"Labels: {labels}{newline}"
            f"Predicted Label: {bold}{predicted_label}{unbold}{newline}")