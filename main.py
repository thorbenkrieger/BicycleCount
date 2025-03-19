import functions_framework
import flask


@functions_framework.http
def main(request: flask.Request) -> flask.typing.ResponseReturnValue:
    return "Hello world!"
