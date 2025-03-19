import functions_framework
import flask


@functions_framework.cloud_event
def hello_world(event):
    """Cloud Event Function.
    Args:
        event: Cloud event for the function trigger
    """
    print("Hello, stdout!")


@functions_framework.http
def hello(request: flask.Request) -> flask.typing.ResponseReturnValue:
    return "Hello world!"
