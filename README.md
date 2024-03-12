Below are step-by-step instructions on how to run the project and explanations of what was done to create the API.
### Running the "Remind-me-later" Project

🚀 **Getting Started**
1. Clone the repository to your local machine using the command:
   ```
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```
   cd remind-me-later
   ```

🏗️ **Setting Up the Environment**
3. Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
4. Create a virtual environment for the project:
   ```
   python -m venv venv
   ```
5. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

🛠️ **Installing Dependencies**
6. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

🔧 **Database Setup**
7. Ensure PostgreSQL is installed and running on your machine. You can download it from [postgresql.org](https://www.postgresql.org/download/).
8. Create a PostgreSQL database named `reminder_db`.
9. Update the database settings in `settings.py` to match your PostgreSQL configuration.

⚙️ **Running the Server**
10. Apply migrations to create necessary database tables:
    ```
    python manage.py migrate
    ```
11. Start the Django development server:
    ```
    python manage.py runserver
    ```

🌐 **Accessing the API**
12. The API endpoints are accessible at:
    - `http://127.0.0.1:8000/api/get-reminders/` (GET request to fetch reminders)
    - `http://127.0.0.1:8000/api/upsert-reminder/` (POST request to upsert reminders)

📝 **API Usage**
13. To retrieve reminders, send a GET request to `http://127.0.0.1:8000/api/get-reminders/`.
14. To add or update a reminder, send a POST request to `http://127.0.0.1:8000/api/upsert-reminder/` with JSON data containing the reminder details.

🎉 **Congratulations!** You have successfully set up and run the "Remind-me-later" project. 🎉

Feel free to modify the instructions or add additional details as needed for your project. Once you've updated the README.md file with these instructions, you can commit and push the changes to your GitHub repository. 




-----------------------------------------------------------------------------------------
```markdown
# Reminder App

📅 This web app allows users to set reminders with messages and specify the reminder type.

## Database Schema

### Table: reminder

| Column         | Type                  | Description                                |
|----------------|-----------------------|--------------------------------------------|
| id             | SERIAL PRIMARY KEY    | Unique identifier for the reminder         |
| date           | DATE NOT NULL         | Date of the reminder                       |
| time           | TIME NOT NULL         | Time of the reminder                       |
| message        | TEXT NOT NULL         | Text message of the reminder               |
| reminder_type  | VARCHAR(10) NOT NULL | Type of reminder (e.g., 'SMS', 'Email')    |
| added_by       | BIGINT NOT NULL       | Identifier of the user who added the reminder |
| added_on       | TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP | Timestamp when the reminder was added |
| modified_on    | TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP | Timestamp when the reminder was last modified |
| modified_by    | BIGINT NOT NULL       | Identifier of the user who last modified the reminder |
| isactive       | BOOLEAN NOT NULL DEFAULT TRUE | Indicates whether the reminder is active |

### Function: public.get_reminders()

```sql
-- Retrieves all reminders from the 'reminder' table and returns them as a JSON document
CREATE OR REPLACE FUNCTION public.get_reminders()
    RETURNS TABLE(document json) 
    LANGUAGE plpgsql
    COST 100
    VOLATILE PARALLEL UNSAFE
    ROWS 1000

AS $BODY$
BEGIN
    -- This function retrieves all reminders from the 'reminder' table
    -- and returns them as a JSON document.

    RETURN QUERY
    SELECT row_to_json(row) 
    FROM (
        SELECT 
            reminder.id, 
            reminder.date, 
            reminder.time, 
            reminder.message, 
            reminder.reminder_type, 
            reminder.added_by, 
            reminder.added_on, 
            reminder.modified_on, 
            reminder.modified_by, 
            reminder.isactive
        FROM reminder
		WHERE isactive = true
    ) AS row;
END;
$BODY$;

ALTER FUNCTION public.get_reminders()
    OWNER TO your_owner_role;
```

### Function: public.udf_upsert_reminder()

```sql
-- Adds or updates a reminder in the database
CREATE OR REPLACE FUNCTION public.udf_upsert_reminder(
    _id integer,
    _date date,
    _time time,
    _message text,
    _reminder_type character varying,
    _added_by bigint)
    RETURNS integer
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
AS $BODY$
BEGIN
/*
	Object: User Defined Function
	Created By: Rajat
	Created On: 12th March 2024
	Updated By:
	Updated On:
	Purpose of Update (if Updated):
	Parameters: _id integer,
				_date date,
				_time time,
				_message text,
				_reminder_type character varying,
				_added_by bigint
				
	Description: This function updates the reminder table for a specific ID
	or inserts data into the reminder table if ID is null.
	*/
IF _id IS NULL THEN
    INSERT INTO reminder(
        date,
        time,
        message,
        reminder_type,
        added_by
    )
    VALUES(
        _date,
        _time,
        _message,
        _reminder_type,
        _added_by
    )
    RETURNING id INTO _id;
ELSE 
    UPDATE reminder SET
        date = _date,
        time = _time,
        message = _message,
        reminder_type = _reminder_type,
        modified_by = _added_by,
        modified_on = NOW()
    WHERE id = _id;
END IF;
RETURN _id;
END;

$BODY$;

ALTER FUNCTION public.udf_upsert_reminder(integer, date, time, text, character varying, bigint)
    OWNER TO your_owner_role;
```

## Running the Project

🚀 Follow these steps to run the project locally:

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/your-username/reminder-app.git
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a PostgreSQL database named `reminder_db`:
   ```sql
   CREATE DATABASE reminder_db;
   ```

4. Apply database migrations:
   ```
   python manage.py migrate
   ```

5. Run the Django development server:
   ```
   python manage.py runserver
   ```

6. Access the API endpoints in your browser or using tools like Postman:
   - `GET /api/get-reminders/`: Retrieves all reminders from the database.
   - `POST /api/upsert-reminder/`: Adds or updates a reminder in the database.

Feel free to explore and use the API endpoints as needed! 🎉
```
