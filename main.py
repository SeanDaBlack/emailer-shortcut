import functions_framework


ALERT = False

ALERT_MESSAGE = """Hello! Thank you for using Gen-Z for Change's Email Tool.
We are currently sunsetting this tool and will no longer be supporting it after December 31, 2025
If you would like to keep up to date with our work, please refer to our website at genzforchange.org

Thank you, keep meddling!
"""


def build_alert():
    print("Alert Triggered!")
    
    alert_object = {
        "hasAlert": ALERT,
        "message": ALERT_MESSAGE
    }
    print(alert_object)
    return alert_object

@functions_framework.http
def handle_call(request):
    """HTTP Cloud Function to handle incoming requests.
    
    Args:
        request (flask.Request): The request object.
            <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    
    if ALERT:
        obj = build_alert()
        return obj
    else:
        return {"hasAlert": False}
        
    
    
    
    



# def hello_http(request):
#     """HTTP Cloud Function.
#     Args:
#         request (flask.Request): The request object.
#         <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
#     Returns:
#         The response text, or any set of values that can be turned into a
#         Response object using `make_response`
#         <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
#     """
#     request_json = request.get_json(silent=True)
#     request_args = request.args

#     if request_json and 'name' in request_json:
#         name = request_json['name']
#     elif request_args and 'name' in request_args:
#         name = request_args['name']
#     else:
#         name = 'World'
#     return 'Hello {}!'.format(name)
