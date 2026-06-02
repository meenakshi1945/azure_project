Local logging screenshot steps

The reviewer said localhost terminal logs are acceptable for the logging criterion. Use these steps if Azure access is still blocked.

1. Open the project in VS Code.

2. Activate the Python 3.10 virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Create the local SQLite database and admin user:

```powershell
python create_local_db.py
```

4. Start the Flask app:

```powershell
python application.py
```

5. Open the local app in your browser:

```text
https://localhost:5555/login
```

The app uses a local development certificate, so the browser may show a privacy warning. Continue to the site for this local test.

6. Try a failed login:

```text
Username: wrong
Password: wrong
```

7. Try a successful login:

```text
Username: admin
Password: pass
```

8. Screenshot the VS Code terminal showing both log lines:

```text
Invalid login attempt for username: wrong
admin logged in successfully
```

Save the screenshot as:

```text
06_login_logs_local.png
```

Faster option:

You can also generate the same local login logs without manually using the browser:

```powershell
python generate_local_login_logs.py
```

Screenshot the terminal output after running that command.
