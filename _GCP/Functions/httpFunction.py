
# main.py
import functions_framework
import json

# from cloudevents.http import CloudEvent
# from cloudevents.pydantic import CloudEvent as CloudEventPydantic
# from cloudevents.exceptions import CloudEventValidationException

@functions_framework.http
def echo_input(request):
    
    """
    HTTP Cloud Function that echoes back the request data.
    Args:
        request: The request object containing the request data
    Returns:
        A tuple containing the response data and status code
    """
    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
    }

    try:
        # Extract request data
        request_data = {
            'method': request.method,
            'args': dict(request.args),
            'headers': dict(request.headers),
        }

        # Handle request body
        if request.content_type == 'application/json':
            try:
                request_data['body'] = request.get_json()
            except ValueError:
                request_data['body'] = None
        else:
            request_data['body'] = request.data.decode('utf-8') if request.data else None

        response_data = {
            'status': 'success',
            'message': 'Request received successfully',
            'data': request_data
        }

        return json.dumps(response_data), 200, headers
    
    except Exception as e:
        error_response = {
            'status': 'error',
            'message': str(e)
        }
        return json.dumps(error_response), 500, headers