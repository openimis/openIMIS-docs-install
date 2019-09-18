

Web application installation guide
==================================

**v1.3.0 and later**

Install IIS
-----------

Follow these steps to install IIS:

- In the Server manager → Dashboard → Add Roles and Features
- Select Role-based or feature-based installation
- Select your server from the server pool, and select your server from the list
- In Server Roles → select Web Server (IIS) → Add Features
- In Features

    - Select .NET Framework 3.5

    - Select .NET Framework 4.6 and ASP.NET 4.6

- In Web Server Role (IIS) → Role Services

    - In Web Server, ensure that Common HTTP Features → Static Content is ticked

    - In Application Development, select .NET Extensibility, ASP, ASP.NET, ISAPI Extensions, ISAPI Filters and Websocket Protocol

    - Management tools → Tick all boxes

- Click on Install and wait for the features to be installed.
- Restart the server if required

Copy openIMIS Web Application
-----------------------------

Download and unzip the release from Github web_app_vb repository
(https://github.com/openimis/web_app_vb/releases/latest) into a new folder under
the IIS wwwroot (For example C:\\inetpub\\wwwroot\\openIMIS).

Configure IIS
-------------

The configuration of IIS done through Internet Information Service (IIS) Manager.

Add a site
~~~~~~~~~~

In Internet Information Service (IIS) manager:

- Select your server name → Sites
- Remove the Default Web Site (if new installation)
- Right click on Sites → Add Website
- Enter a site name for your openIMIS instance (i.e. openIMIS.X.Y.Z)
- Enter or select the physical path name: C:\\inetpub\\wwwroot\\openIMIS (unless you have installed IIS somewhere else)
- If you have a SSL certificate, select binding type to HTTPS (port 443) and select your certificate, if not select binding type to HTTP (port 80)

If you have selected the binding type to HTTPS (port 443), then you will have to add also the binding type for HTTP:

- Right click on the new added website
- Select Edit Bindings
- Select binding type http (port 80) and click ok

Globalisation
~~~~~~~~~~~~~

Depending on the server's initial configuration, the date format may
differ from the expected DD/mm/YYYY. To force the date format, go
to the openIMIS site, then select .NET Globalisation Under Culture, and select
English (United Kingdom) (en-GB) as a culture.

Configure openIMIS Web Application
----------------------------------

Edit the web.config
~~~~~~~~~~~~~~~~~~~

The web.config provides the configuration for openIMIS Web Application, including database connection string and necessary folders.

To configure the database connection string, go in openIMIS root folder (usually C:\\inetpub\\wwwroot\\openIMIS), locate the web.config file and edit “IMISConnectionString”, so that the connection string points to the database created in openIMIS database section with the right credentials. For example:

.. code-block:: xml
   :linenos:

	<connectionStrings>
		<add name="IMISConnectionString" connectionString="Data Source=WIN-H4E4ARREBFH\SQLEXPRESS;Initial Catalog=IMIS;User ID=ImisUser;Password=password1234" providerName="System.Data.SqlClient" />
	</connectionStrings>

Other configuration settings can be found within the appSettings tag and should be modified with caution.

Assign permission to source folders
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the source files (usually C:\\inetpub\\wwwroot\\openIMIS), IIS_IUSRS need to
be given full control of the following folders:

- Archive
- Extracts
- FromPhone
- Images
- Workspace

Repeat the following steps for each folder listed above:

- Right click on the folder and select properties
- Ensure that the folder is not read only
- Select the Security tab
- Click on Edit
- Select IIS_IUSRS and allow full control (in the below section).
- Then apply and click OK.

Edit permissions to Windows event logs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click on the Windows Start menu of run “regedit” via the search box:

- In the Registry Editor, select HKEY_LOCAL_MACHINE → System → CurrentControlSet → Services → Eventlog
- Right click on the EventLog Node, select Permission. Give full permissions to IIS_IUSRS, as described in the above paragraph (Assign permission to source folders)
- Now repeat the same steps for Eventlog → Security node, as it can be required depending on the server's environment

Open the application
--------------------

Open your Internet browser and type the following URL in the browser
address bar \ http://localhost/

You can connect with the admin default credentials:

- Login name: Admin
- Password: Admin
