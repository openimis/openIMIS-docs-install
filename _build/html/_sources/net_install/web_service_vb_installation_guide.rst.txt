
Web service installation guide
==================================

**v1.2.0 and later**

Prerequisites
-------------

In order to install openIMIS Web Services, you need first to install openIMIS Database and Web Application.

If not yet installed please follow the steps from the database and web application
installation guides.


Copy openIMIS Web Services
--------------------------

Download and unzip the release from Github web_service_vb repository
(https://github.com/openimis/web_service_vb/releases/latest) in a new folder (openIMIS.WS.X.Y.Z)
under the IIS wwwroot (usually in C:\\inetpub\\wwwroot).


Configure openIMIS Web Services in IIS
--------------------------------------

In Internet Information Service (IIS) Manager, right click on the previous added IMIS site and select Add application. Fill in the form
as follows:

-  Alias: Services (mandatory for the mobile apps)
-  Physical Path: The path of the Services Folder in the sources (usually
   C:\\inetpub\\wwwroot\\openIMIS.WS.X.Y.Z)

Configure openIMIS Web services
-------------------------------

Edit the web.config:

- Similarly, the Web services needs that the database connection string to be updated
- In the services source files (usually C:\\inetpub\\wwwroot\\openIMIS.WS.X.Y.Z),
   locate the the file “web.config” and edit it accordingly. For example:

.. code-block:: xml
   :linenos:

   <connectionStrings>
    <remove name="CHF_CENTRALConnectionString" />
    <add name="CHF_CENTRALConnectionString" connectionString="Data Source=[DatabaseIPAdress];Initial Catalog=IMIS;User ID=[ImisUserId];Password=[ImisUserPassword]" providerName="System.Data.SqlClient" />
   </connectionStrings>

- -Important note-: the name attribute must remain “CHF_CENTRALConnectionString”
