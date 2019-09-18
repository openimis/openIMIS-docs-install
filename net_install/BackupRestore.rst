    Back and restore
    ================

    Backup of the database in SQL Server Management Studio 

    Backup of the database in SQL Server Management Studio 
    
    Restauration can be done in SQL Server Management Studio 

    or the below command line can be used in a shell

        Becareful to addapt the querries to your setup, in the command lines example those assumptions were made:
            * ``Online`` database version 1.30 is to be restored 
            * The database is called ``IMIS_DATABASENAME`` 
            * The SQL server is called ``SQL_Server_Name``

        .. code-block:: dosbatch
           :linenos:

           SqlCmd -E -S SQL_Server_Name –Q "RESTORE DATABASE [IMIS_DATABASENAME] FROM DISK='X:\PathToBackupFile\openIMIS_ONLINE_v1.3.0.bak'"

        In case the database need to be restored on a server that doesn't have the same file structur as the initial server (e.g. from Windows to Linux), the new location of the mlf/mlf files can be specified

        .. code-block:: dosbatch
           :linenos:

           SqlCmd -E -S SQL_Server_Name -Q "RESTORE DATABASE [IMIS_DATABASENAME] FROM DISK=N'/tmp/openIMIS_ONLINE_v1.3.0.bak' WITH MOVE N'CH_CENTRAL' TO '/var/opt/mssql/data/IMIS.mdf', MOVE N'CH_CENTRAL_log' TO '/var/opt/mssql/data/IMIS_log.ldf'"



    The result returned from the procedure should be 0.