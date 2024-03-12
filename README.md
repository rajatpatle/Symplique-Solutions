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
