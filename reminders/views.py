from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .dboperation import get_reminders_db, upsert_reminder_db

@api_view(['GET'])
def get_reminders(request):
    """
    Retrieves reminders from the database.

    This endpoint retrieves all reminders stored in the database and returns them as a JSON response.

    Returns:
    - status: Indicates the success or failure of the operation (1 for success, 0 for failure).
    - statusCode: HTTP status code of the response (200 for success, 400 for failure).
    - error: Any error message encountered during the operation (None if successful).
    - message: Descriptive message indicating the outcome of the operation.
    - data: List of reminders retrieved from the database.
    """
    response_body = {"status": 1, "statusCode": 200, 'error' : None, "message": "Data Fetched Successfully", 'data' : None}
    try:
        res = get_reminders_db()

        if res is not None and len(res) > 0:
            response_body['data'] = res
        else:
            response_body['status'] = 0
            response_body['message'] = 'No Data Found.'

    except Exception as e:
        response_body['status'] = 0
        response_body['statusCode'] = 400
        response_body['error'] = str(e)
        response_body['message'] = 'Something went wrong.'

    return Response(response_body, status=response_body['statusCode'])


@api_view(['POST'])
def upsert_reminder(request):
    """
    Adds or updates a reminder in the database.

    This endpoint accepts a JSON payload containing reminder details and adds or updates the reminder in the database accordingly.

    Parameters:
    - id: Identifier of the reminder (optional for new reminders, required for updates).
    - date: Date of the reminder.
    - time: Time of the reminder.
    - message: Text message of the reminder.
    - reminder_type: Type of reminder (e.g., SMS, Email).
    - added_by: Identifier of the user who added the reminder.

    Returns:
    - status: Indicates the success or failure of the operation (1 for success, 0 for failure).
    - statusCode: HTTP status code of the response (200 for success, 400 for failure).
    - error: Any error message encountered during the operation (None if successful).
    - message: Descriptive message indicating the outcome of the operation.
    - data: Additional data related to the operation (e.g., identifier of the added or updated reminder).
    """
    response_body = {"status": 1, "statusCode": 200, 'error': None, "message": "Reminder Updated Successfully", 'data': None}
    try:
        data = json.loads(request.body.decode("utf-8"))
        _id = data['id']
        _date = data['date']
        _time = data['time']
        _message = data['message']
        _reminder_type = data['reminder_type']
        _added_by = data['added_by']

        reminder_id = upsert_reminder_db(_id, _date, _time, _message, _reminder_type, _added_by)

        response_body['data'] = {"id": reminder_id}

    except Exception as e:
        response_body['status'] = 0
        response_body['statusCode'] = 400
        response_body['error'] = str(e)
        response_body['message'] = 'Something went wrong.'

    return Response(response_body, status=response_body['statusCode'])
