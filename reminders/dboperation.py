from django.db import connection

def get_reminders_db():
    """
    Retrieves reminders from the database.

    This function executes a database query to retrieve all reminders stored in the database.

    Returns:
    - List of reminders retrieved from the database.
    """
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
    """
    Adds or updates a reminder in the database.

    This function executes a database query to add or update a reminder in the database.

    Parameters:
    - _id: Identifier of the reminder (optional for new reminders, required for updates).
    - _date: Date of the reminder.
    - _time: Time of the reminder.
    - _message: Text message of the reminder.
    - _reminder_type: Type of reminder (e.g., SMS, Email).
    - _added_by: Identifier of the user who added the reminder.

    Returns:
    - Identifier of the added or updated reminder.
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT udf_upsert_reminder(%s, %s, %s, %s, %s, %s)",
                (_id, _date, _time, _message, _reminder_type, _added_by)
            )
            return cursor.fetchone()[0]
    except Exception as e:
        raise ValueError(e)
