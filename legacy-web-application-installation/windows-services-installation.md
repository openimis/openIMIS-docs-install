# Windows Services installation

## Windows Services 

The openIMIS Windows Services are helping with the periodic activities which are required by the implementations. 

### Policy Renewal service

This Windows service periodically marks the policies that will expire in the near future to be renewed and updates the status of the already expired policies. 

Download  [Policy Renewal service](https://github.com/openimis/policy_renewal_service_vb/releases/latest).

### Backup service 

This Windows Service periodically creates a backup of the database.

Download  [Backup service](https://github.com/openimis/imis_backup_service_vb/releases/latest). 

## Install Windows Services

To install the Windows Service, proceed as follows for each Service:

1. Download and unzip the installation setup from [t](https://github.com/openimis/policy_renewal_service_vb/releases/latest)he links mentioned in the available Services
2. Double click on the setup file
3. Select the installation path \(for example `C:\Program Files\openIMIS\Windows Services`\), and click Next
4. Close after the installation completes

The installed Service should start automatically as indicated in the system tray. If not, browse to Programs menu and search for the Service name \(the controller of the service\) and execute it.

## Fix broken services 

### Fix initial configuration files

1. Run IMIS Policy Renewal \(if an error window appears, click Continue\)
2. Right-click the Policy Renewal icon in the system tray \(lower-right corner of Windows\) and click `Settings`
3. Fill the newly-created window `Imis Renewal Policy` as follows \(please adapt to your situation\):
   1. Server: `.\SERVERNAME`
   2. Database: `openIMIS.1.3.0` 
   3. User Name: `ImisUser`
   4. Password: `Pa$$w0rd`
   5. Time: `00:00`
   6. Interval: `24`
   7. Untick all `Send SMS to...` options
   8. Click Apply
4. Make a copy of the file ImisPolicyRenewal.exe.config inside C:\Program Files\openIMIS\Windows Services within the same folder
5. Rename the copy into ImisBackup.exe.config

### Fix service startup

1. Run Services
2. Locate `ImisBackup` and `ImisPolicyRenewal`, and do the following for each:
   1. Double-click the said entry
   2. Click the `Log On` tab
   3. Select the `Local System account` option
   4. Tick the `Allow service to interact with desktop` checkbox
   5. Click `OK`
   6. Right-click the said entry
   7. Click either `Restart` or `Start` \(whichever is possible\)
   8. Locate its icon in the system tray \(lower-right corner of Windows\)
   9. Right-click the said icon and click `Settings`
   10. Fix field values, if needed

## Configure Windows Services

### Configure the Imis Policy Renewal Windows Service

This service is used to update insurance policies and runs every day at the specified time. It will do the following actions:

1. If it finds a policy which is about to expire within a specified period of time, it flags it as to be renewed. The list of policies to be renewed can be used by the Enrolment Officers to contact the concerned families. The default policy expiring period of time is 14 days.
2. Sets the policy status to expired to all policies that have expired in between this Service runs.
3. Sends SMS to insuree if their policy is about to expire so that they can renew the policy \(optional\).

After the service installation, the user has to set the name of the server, the database name, the SQL-server instance credentials, and the service schedule for checking which policy is to be flagged as expired policy.

The days specified before the exact policy expiry date is provided in the table `tblIMISDefaults` under openIMIS Live database. The figure below shows the interface for Policy Renewal Service.

![](../.gitbook/assets/image%20%283%29.png)

Under the SMS gateway setting, you need to specify the URL given by SMS Gateway provider. You also need to provide the username and password to allow the service to send SMS to the insuree. 

{% hint style="danger" %}
Each SMS Provider has it's own communication protocol. Please make sure that the published version is working with your SMS Provider. Otherwise, the SMS communication protocol needs to be updated in the source code for this integration to work.
{% endhint %}

### Configure the Imis Backup Windows Service

This service is used for database backup, after the service installation, the user has to set the name of the server, the database name, the SQL-server instance credentials, and the service schedule for the backups.

The backup location is specified in the table [`tblIMISDefaults`](https://openimis.atlassian.net/wiki/spaces/OP/pages/907018332/WA4.3+IMIS+default+configuration) under openIMIS Live database. The figure below shows the interface for the database backup service.

![](../.gitbook/assets/image%20%282%29.png)

