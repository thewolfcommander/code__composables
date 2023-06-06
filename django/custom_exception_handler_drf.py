from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data = {}
        response.data['status'] = False
        errors = []
        for field, value in response.data.items():
            errors.append("{}: {}".format(field, " ".join(value)))

        response.data['message'] = errors

    return response


"""
In settings
"""

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'my_project.my_app.utils.custom_exception_handler'
}
