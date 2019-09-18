

Windows services installation guide
===================================

**v1.3.0 and later**

Install and configure openIMIS Policy Renewal service
-----------------------------------------------------

To install the Policy Renewal service, proceed as follow:

- Download and unzip the installation setup from https://github.com/openimis/policy_renewal_service_vb/releases/latest
- Double click on the setup file
- Select the installation path (for example C:\\Program Files\\openIMIS\\Windows Services), and click Next
- Then close after the installation completes
- The service should start automatically as indicated in the system tray. If not, browse to Programs menu and search for “IMIS Policy Renewal” (PolicyRenewalController.exe) and execute it.

To configure the Policy Renewal service, right click on the service controller
 application in the system tray, select Settings, and fill in the settings as
 follows for example:

  - Server: TPH-L14005\\SQLEXPRESS (server instance name)
  - Database: IMIS (IMIS database name)
  - User Name: ImisUser
  - Password: **************
  - Time : 00:00
  - Interval: 24
  - Click on Apply. This will run a backup daily at midnight.


Install and configure openIMIS Backup service
---------------------------------------------

- Download and unzip the installation setup from https://github.com/openimis/imis_backup_service_vb/releases/latest
- Follow the same steps as for the Policy Renewal service to configure the service.


Install and configure openIMIS Feedback Prompt service
------------------------------------------------------

- Download and unzip the installation setup from https://github.com/openimis/imis_feedback_prompt_service_vb/releases/latest
- Follow the same steps as for the Policy Renewal service to configure the service.


Troubleshooting Windows Services
--------------------------------

An error message may appear after the services started, saying
that the service failed. In this case, restart it as a Local System
service:

-  Open the Windows Services manager
-  Locate the service that failed
-  Right click on it and select Properties → Log on tab
-  Select Local System account
