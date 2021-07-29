# Web Application installation

## **Video tutorial** 

{% embed url="https://youtu.be/0CX3y6QfBXQ" %}

## **Install** Internet Information Services \(**IIS**\)

In Windows Server, follow these steps to install IIS:

1. In the `Server Manager` → `Dashboard` → `Add Roles and Features`
2. Select `Role-based or feature-based` installation
3. Select your server from the server pool, and select your server from the list
4. In `Server Roles` → select `Web Server (IIS)` → `Add Features`
5. In `Features`
   1. Select `.NET Framework 3.5`
   2. Select `.NET Framework 4.6` and `ASP.NET 4.6` \(or later\)
6. In `Web Server Role (IIS)` → `Role Services`
   1. In `Web Server`, ensure that `Common HTTP Features` → `Static Content` is ticked
   2. In `Application Development`, select `.NET Extensibility`, `ASP`, `ASP.NET`, `ISAPI Extensions`, `ISAPI Filters` and `Websocket Protocol`
   3. In `Management tools`**,** tick all boxes
7. Click on Install and wait for the features to be installed
8. Restart the server if required

## **Download openIMIS Web Application**

Download and unzip the desired release from Github [web\_app\_vb repository](https://github.com/openimis/web_app_vb/releases/latest) into a new folder under the IIS wwwroot \(e.g. C:\inetpub\wwwroot\openIMIS.1.4.0\).

## **Configure IIS** 

The configuration of IIS is done through Internet Information Service \(IIS\) Manager.

### **Add the openIMIS Site**

In Internet Information Service \(IIS\) Manager:

1. Select your server name → `Sites`
2. Remove the Default Web Site \(if new installation\)
3. Right-click on `Sites` → `Add Website`
4. Enter a site name for your openIMIS instance \(e.g. openIMIS.1.4.0\)
5. Enter or select the physical pathname \(e.g. C:\inetpub\wwwroot\openIMIS.1.4.0\)
6. If you have an SSL certificate, select binding type to HTTPS \(port 443\) and select your certificate
7. If you don't have an SSL certificate, select binding type to HTTP \(port 80\)

If you have selected the binding type to HTTPS \(port 443\), then you will have to add also the binding type for HTTP

1. Right-click on the new added website
2. Select Edit Bindings
3. Select binding type HTTP \(port 80\) and click ok

If you have a DNS address \(e.g. [demo.openimis.org](http://demo.openimis.org/)\) that is mapped to your server IP address, you can add it in the site binding configuration as the hostname. This will allow having multiple Sites deserving same ports \(80 and 443\) and can be used to have, for example, openIMIS development \(e.g. [dev.openimis.org](http://dev.openimis.org/)\) and production \(e.g. [demo.openimis.org](http://demo.openimis.org/)\) sites on the same server. 

### **Change Globalisation**

Depending on the server’s initial configuration, the date format may differ from the expected `DD/mm/YYYY` format. To force the date format, go to the openIMIS site, then select `Culture` → `.NET Globalisation`, and select `English (United Kingdom) (en-GB)` as a culture.

## Configure openIMIS Web Application

### **Edit the web.config** 

The web.config file provides the configuration for openIMIS Web Application, including database connection string and necessary folders.

{% hint style="warning" %}
For the Web Application to work, make sure the [openIMIS Database is installed](database-installation.md).  
{% endhint %}

To configure the database connection string, go in openIMIS root folder \(e.g. C:\inetpub\wwwroot\openIMIS.1.4.0\), locate the web.config file and edit `IMISConnectionString` entry so that the connection string points to the [database created in openIMIS database section](https://openimis.atlassian.net/wiki/spaces/OP/pages/906592471#WA2.1Databaseinstallation-create_db) with the right credentials. For example:

```markup
<connectionStrings> 
    <add name="IMISConnectionString" connectionString="Data Source=WIN-H4E4ARREBFH\SQLEXPRESS;Initial Catalog=openIMIS.1.4.0;User ID=ImisUser;Password=password1234" providerName="System.Data.SqlClient" /> 
</connectionStrings>
```

Other configuration settings can be found within the `<appSettings>` tag and should be modified with caution.

### **Assign permission to source folders**

openIMIS Web Application needs to have full right in certain folders. For this, IIS\_IUSRS Windows user must have full control access to the following folders in openIMIS root folder \(e.g. C:\inetpub\wwwroot\openIMIS.1.4.0\): 

* `Archive`
* `Extracts`
* `FromPhone`
* `Images`
* `Workspace`

Repeat the following steps for each folder listed above:

1. In Windows Explorer, right-click on the folder and select properties
2. Ensure that the folder is not read-only
3. Select the `Security` tab
4. Click on `Edit`
5. Select `IIS_IUSRS` and allow full control \(in the below section\).
6. Then apply and click OK.

### Edit permissions to Windows event logs

Click on the Windows Start menu of run `Regedit` via the search box:

1. In the Registry Editor, select `HKEY_LOCAL_MACHINE` → `System` → `CurrentControlSet` → `Services` → `Eventlog`.
2. Right-click on the `EventLog` node, select `Permission`. Give full permissions to `IIS_IUSRS`, as described in the above paragraph \(Assign permission to source folders\). If the IIS\_IUSRS user is not present in the list, then click `Add` button to add it manually. 
3. Now repeat the same steps for `Eventlog` → `Security` and `Eventlog` **→** `State` node, as it can be required depending on the server’s environment.

Additional resources:

* [How to fix permissions error on Windows event logs?](https://openimis.atlassian.net/wiki/spaces/KB/pages/1957986327)

## Open the Web Application

Open your Internet browser and type the following URL in the browser address bar: [http://localhost/](http://localhost/)

If you have initiated the openIMIS Blank Database, use the following credentials:

* Login name: `Admin`
* Password: `Admin`

If you have initiated the openIMIS Demo Database, use the following credentials:

* Login name: `Admin`
* Password: `admin123`

