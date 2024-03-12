# from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .dboperation import get_reminders_db ,upsert_reminder_db

@api_view(['GET'])
def get_reminders(request):
    """_summary_
        This is the reminders retrieval API.
    """
    response_body = {"status": 1, "statusCode": 200, 'error' : None, "message": "Data Fetched Successfully", 'data' : None}
    try:
        # Assuming get_reminders_db returns reminders data
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
    """_summary_
        This is the reminder upsert API.
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

        # Call the upsert function
        reminder_id = upsert_reminder_db(_id, _date, _time, _message, _reminder_type, _added_by)

        response_body['data'] = {"id": reminder_id}

    except Exception as e:
        response_body['status'] = 0
        response_body['statusCode'] = 400
        response_body['error'] = str(e)
        response_body['message'] = 'Something went wrong.'

    return Response(response_body, status=response_body['statusCode'])

