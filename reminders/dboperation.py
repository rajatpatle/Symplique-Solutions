from django.db import connection

def get_reminders_db():
    try:
        result = []
        with connection.cursor() as cursor:
            cursor.execute("SELECT get_reminders()")
            data = cursor.fetchall()
            if len(data) > 0:
                for item in data:
                    result.append(item[0])
            return result
    except Exception as e:
        raise ValueError(e)



def upsert_reminder_db(_id, _date, _time, _message, _reminder_type, _added_by):
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT udf_upsert_reminder(%s, %s, %s, %s, %s, %s)",
                (_id, _date, _time, _message, _reminder_type, _added_by)
            )
            return cursor.fetchone()[0]
    except Exception as e:
        raise ValueError(e)
