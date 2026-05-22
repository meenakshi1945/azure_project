Article CMS resubmission checklist

Use this while preparing the final upload. The goal is simple: code included, Azure resources visible, screenshots clear.

Code to include:

- [ ] `FlaskWebProject/__init__.py` has logging setup.
- [ ] `FlaskWebProject/views.py` has Microsoft sign-in and login logging.
- [ ] `config.py` reads important values from environment variables.
- [ ] `WRITEUP.md` explains why App Service was chosen.
- [ ] `requirements.txt` installs with Python 3.10.

Azure resources to create:

- [ ] Resource Group.
- [ ] Azure SQL Server.
- [ ] Azure SQL Database.
- [ ] SQL tables created using the files in `sql_scripts/`.
- [ ] Storage Account.
- [ ] Blob container named `images`.
- [ ] App Service Web App using Python 3.10.
- [ ] Microsoft Entra ID App Registration.
- [ ] Redirect URI: `https://YOUR_APP_NAME.azurewebsites.net/getAToken`.
- [ ] Logout URL: `https://YOUR_APP_NAME.azurewebsites.net/login`.
- [ ] App Service logging turned on.

App Service environment variables:

- [ ] `BLOB_ACCOUNT`
- [ ] `BLOB_CONTAINER`
- [ ] `BLOB_STORAGE_KEY`
- [ ] `BLOB_CONNECTION_STRING`
- [ ] `SQL_SERVER`
- [ ] `SQL_DATABASE`
- [ ] `SQL_USER_NAME`
- [ ] `SQL_PASSWORD`
- [ ] `CLIENT_ID`
- [ ] `CLIENT_SECRET`
- [ ] `SECRET_KEY`

Screenshots to submit:

- [ ] `01_article_created_on_azure.png`
  Shows the Azure URL, black `Article CMS` header, title `Hello World!`, author `Jane Doe`, body text, and uploaded image.

- [ ] `02_resource_group.png`
  Shows the Resource Group with Storage Account, SQL Server, SQL Database, App Service, and App Service Plan.

- [ ] `03_sql_tables.png`
  Shows the `users` table, `posts` table, and at least one query result.

- [ ] `04_blob_endpoint.png`
  Shows the Blob service endpoint URL.

- [ ] `05_redirect_uri.png`
  Shows the Microsoft redirect URI ending in `/getAToken`.

- [ ] `06_login_logs.png`
  Shows one invalid login attempt and one successful admin login.

After grading, delete or stop the Azure resources so they do not keep charging your account.
