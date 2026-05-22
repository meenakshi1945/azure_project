I completed the project code updates and write-up, but I was unable to complete the live Azure deployment because I could not get access to an active Azure subscription.
I first tried to use Azure for Students, but the student verification process could not find or verify my university ID. I then tried to create a regular Azure Free Account, but Azure would not accept my card during the signup/payment verification step. Because of this, I was unable to create the required live Azure resources, including the Resource Group, Azure SQL Database, Storage Account, App Service, and Microsoft Entra ID redirect URI.
The submitted code still includes the required application changes:

- Microsoft sign-in implementation using the `msal` library in `FlaskWebProject/views.py`.
- Login logging for invalid login attempts and successful admin login attempts.
- Logging setup in `FlaskWebProject/__init__.py`.
- Environment-variable based configuration in `config.py`.
- A completed `WRITEUP.md` comparing VM deployment and Azure App Service deployment, with App Service selected and justified.
If I am able to resolve the Azure subscription issue, the next step would be to deploy this code to Azure App Service, create the SQL Database and Blob Storage resources, configure the App Service environment variables, add the Microsoft redirect URI, and capture the required Azure Portal screenshots.
