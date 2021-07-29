# Database installation

## Install SQL Server

{% hint style="info" %}
openIMIS has been developed and tested using SQL Server 2017. Newer or old versions might require adaptations to both these installation guide and openIMIS code.
{% endhint %}

1. Download the desired version of SQL Server \(for example, if you want to test openIMIS, you can download and install [SQL Server 2017 Developer](https://download.microsoft.com/download/5/A/7/5A7065A2-C81C-4A31-9972-8A31AC9388C1/SQLServer2017-SSEI-Dev.exe) version - not for production\).
2. When the installation wizard opens, select the manual configuration option in order to fine-tune the installation process.
3. On the Features selection:
   1. In `Shared Feature` section, select `SQL Client Connectivity SDK`
   2. For installations with Data Warehouse, select `Analysis Services`, `Reporting Services` and `Integration Services` \(not available for the Express edition\)
4. On the Instance configuration, the default name `SQLEXPRESS` can be used, unless it is already used by another instance.
5. On Database engine configuration, select `Mixed Mode` \(SQL Server authentication and Windows authentication\) in Authentication Mode.
6. Continue the setup process until the installation is complete.

## Configure SQL Server

1. Open the SQL Server Configuration Manager
   1. On the left panel, select `SQL Server Network Configuration` → `Protocols for SQLEXPRESS` \(or the name of your SQL Server instance\) → Enable Named Pipes and TCP/IP
   2. Select SQL Server Services → right-click on SQL Server instance name and select Restart

## Initialize openIMIS database

To facilitate the setting up of the openIMIS database, we suggest installing [SQL Server Management Studio](https://docs.microsoft.com/sql/ssms/download-sql-server-management-studio-ssms) \(SSMS\). The following procedure is based on SSMS, but you can use the standard SQL Server prompt to proceed with the setup.

1. First, download the openIMIS database SQL files and migration scripts from [Github repository](https://github.com/openimis/database_ms_sqlserver/releases/latest) \(the source code ZIP file\).
2. If you wish to initialize the database using SSMS, follow the steps: 
3. Create a new database for the openIMIS instance \(e.g. openIMIS.1.4.0, where 1.4.0 is the openIMIS database version\).
4. Open the [**openIMIS\_ONLINE.sql**](https://github.com/openimis/database_ms_sqlserver/blob/master/Empty%20databases/openIMIS_ONLINE.sql) file \(from the Empty databases folder\) and execute the script \(make sure the selected database is the one created in step a.\)
5. If you prefer to initialize the database using the shell:

   1. Be careful to adapt the queries to your setup, in the command lines example those assumptions were made:
      1. The database is called **`IMIS_DATABASENAME`**
      2. The SQL server is called **`SQL_Server_Name`**
   2. Run the following commands:

   ```
   $ SqlCmd -E –Q "CREATE DATABASE IMIS_DATABASENAME" 2SqlCmd -E -S SQL_Server_Name -d IMIS_DATABASENAME –i X:\PathToSQLFile\openIMIS_ONLINE.sql
   ```

6. Create a dedicated user with full privilege on the openIMIS database only:
   1. In the **Security** → **Logins** → right-click and select “**New Login…**”
   2. In General page:
      1. Give a login name \(e.g. ImisUser\)
      2. Select SQL Server authentication and provide a password
      3. Unselect Enforce password expiration
      4. Change the default database to openIMIS
   3. In User Mapping page:
      1. Map openIMIS database to ImisUser user
      2. Give the role of **db\_owner**

#### Initialize specific openIMIS database <a id="Initialize-specific-openIMIS-database"></a>

There are three specific openIMIS databases to chose from:

* **Offline** \([openIMIS\_OFFLINE.sql](https://github.com/openimis/database_ms_sqlserver/blob/master/Empty%20databases/openIMIS_OFFLINE.sql)\): this mode is used for remote insurance offices without Internet connectivity. Note: the synchronization of data with the central server is manual.
* **Offline HF** \([openIMIS\_OFFLINE\_HF.sql](https://github.com/openimis/database_ms_sqlserver/blob/master/Empty%20databases/openIMIS_OFFLINE_HF.sql)\): this mode can be used in remote health facilities without Internet connectivity. Note: the synchronization of data with the central server is manual.
* **Demo** \([openIMIS\_demo\_ONLINE.sql](https://github.com/openimis/database_ms_sqlserver/blob/master/Demo%20database/openIMIS_demo_ONLINE.sql)\): this script initialize the empty database with the demo dataset.

To initialize one of the specific openIMIS databases, follow the steps:

1. Initialize the openIMIS database by following the previous section steps
2. Run the specific database script on the already initialized openIMIS database

#### Upgrade the openIMIS database <a id="Upgrade-the-openIMIS-database"></a>

The upgrading process should always be performed on a copy of the database to ensure the proper execution of the migration script. In case of any issue arriving from the upgrading process, you can get back to the previous version of the database. Please report using [openIMIS Service Desk](https://openimis.atlassian.net/servicedesk) any issue you may face in the upgrading process.

The upgrade can be done with [SQL Server Management Studio](https://docs.microsoft.com/sql/ssms/download-sql-server-management-studio-ssms) \(SSMS\) or from the shell \(be careful to adapt the querries to your setup\).

To update a production instance and to prevent impacting the production if the migration script failed because of customizations in your openIMIS instance:

1. During the upgrade make sure the is not reachable from the applications \(you should stop the openIMIS website in Web Application IIS\).
2. Duplicate the database using SSMS or shell \(create a full backup of the database and restore it with another database name, e.g. openIMIS.1.4.0\)
   1. Shell commands \(e.g. duplicate 'openIMIS.1.3.0' database to 'openIMIS.1.4.0' database; please adapt to your situation\):`1SqlCmd -E -S SQL_Server_Name –Q "BACKUP DATABASE [openIMIS.1.3.0] TO DISK='X:\PathToBackupLocation\openIMIS.1.3.0.bak'" 2SqlCmd -E -S SQL_Server_Name –Q "RESTORE DATABASE [openIMIS.1.4.0] FROM DISK='X:\PathToBackupLocation\openIMIS.1.3.0.bak' WITH MOVE 'openIMIS.1.3.0' TO 'C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\DATA\openIMIS.1.4.0.mdf', MOVE 'openIMIS.1.3.0_log' TO 'C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\DATA\openIMIS.1.4.0_log.ldf'"`
3. Download the openIMIS database SQL files and migration scripts from [Github repository](https://github.com/openimis/database_ms_sqlserver/releases/latest) \(the source code ZIP file\).
4. Execute the migration script on the copy of the database in SSMS or shell
   1. Shell command \(e.g. from the current version 1.3.0 to the new version 1.4.0\)`1SqlCmd -E -S SQL_Server_Name -d openIMIS.1.4.0 –i "X:\PathToMigrationScript\openIMIS migration v1.3.0 - v1.4.0.sql"`
5. [Configure the openIMIS Web Application to use the newly migrated database](https://openimis.atlassian.net/wiki/spaces/OP/pages/906952742/WA2.2+Web+Application+installation#WA2.2WebApplicationinstallation-edit_web_config) \(e.g. openIMIS.1.4.0\).
6. [Configure the openIMIS Backup Windows Service](https://openimis.atlassian.net/wiki/spaces/OP/pages/906723349/WA2.3+Windows+Services+installation#WA2.3WindowsServicesinstallation-config_backup) or your own backup application/service to use the newly migrated database \(e.g. openIMIS.1.4.0\).
7. Start your openIMIS website.

