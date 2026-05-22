# Article CMS Azure Deployment Write-up

## Resource Option Analysis

### Virtual Machine

**Cost:** A virtual machine requires paying for the VM while it is running, and there can also be costs for disks, networking, and any related monitoring services. Even a small VM can become more expensive than App Service for a simple Flask CMS because the operating system and web server are always allocated.

**Scalability:** Scaling a VM usually requires manually resizing the VM, creating additional VMs, or placing multiple VMs behind a load balancer. This gives a lot of control, but it also adds complexity for a small application.

**Availability:** A single VM is a single point of failure unless additional availability features are configured. To improve availability, I would need to add redundancy such as multiple VMs, availability zones, or backup and recovery processes.

**Workflow:** A VM gives full control over the server, including Nginx, SSL certificates, Python versions, and system packages. However, that also means I am responsible for operating system updates, security patches, process management, and troubleshooting the server environment.

### Azure App Service

**Cost:** Azure App Service is cost-effective for this project because it supports a Free F1 tier for simple development and testing. It avoids the extra overhead of managing a full VM and lets me host the Flask application with fewer infrastructure resources.

**Scalability:** App Service has built-in scaling options. If the CMS receives more traffic later, the app can be scaled up to a larger plan or scaled out to multiple instances without rebuilding the server setup manually.

**Availability:** App Service is a managed platform, so Azure handles much of the host maintenance and platform availability. This is a better fit for a beginner-level CMS project because the deployment can focus on the application, database, and storage integration.

**Workflow:** App Service integrates well with GitHub deployment and Azure application settings. Environment variables for SQL Database, Blob Storage, and Microsoft authentication can be configured in the Azure Portal instead of hardcoding secrets in the code.

## Chosen Deployment Option

I chose **Azure App Service** to deploy the Article CMS. This project is a standard Flask web application that needs to connect to Azure SQL Database, Azure Blob Storage, and Microsoft authentication, and App Service supports those requirements with much less server administration than a VM. App Service is also the better choice for this submission because it provides a straightforward deployment workflow, easy configuration of environment variables, built-in logging features, and a public Azure website URL for screenshots and testing.

## App Changes That Could Change This Decision

I would consider choosing a VM if the application required full control over the operating system, custom networking rules, special background services, or server software that App Service does not support. For example, if the CMS needed custom system packages, long-running worker processes, or a highly customized Nginx/SSL configuration, a VM could be more appropriate.

If the app grew into a larger production system, I would also consider using additional Azure services such as Key Vault for secrets, Application Insights for monitoring, and a stronger App Service pricing tier for production availability. For this project, the main requirements are Flask hosting, SQL storage, blob image uploads, Microsoft login, and login logging, so App Service is the most appropriate option.
