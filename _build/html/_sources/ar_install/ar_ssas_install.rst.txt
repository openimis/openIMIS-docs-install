Deploy SSAS
~~~~~~~~~~~

#. Open the SQL Server Management studio and restore the database **IMIS_DW**.
    Close the SQL server management studio

#. Click the windows start button, search for the Deployment Wizard. Click the Deployment wizard icon(:ref:`Image - SSAS deployment wizard, Launch wizard <ssas_deploy>`).

    .. _ssas_deploy:

    .. figure:: /img/ar_install/ssas_deploy.png
       :align: center

       `Image - SSAS deployment wizard, Launch wizard`

#. Click next  to start the installation for SSAS(:ref:`Image - SSAS deployment wizard, Start <ssas_deploy_1>`).

    .. _ssas_deploy_1:

    .. figure:: /img/ar_install/ssas_deploy_1.png
       :align: center

       `Image - SSAS deployment wizard, Start`

#. Click the browse button (three dots) and select the IMIS cubes database from the SSAS deployment package(:ref:`Image - SSAS deployment wizard, Destination folder <ssas_deploy_2>`).
    Click next to continue with the installation.

    .. _ssas_deploy_2:

    .. figure:: /img/ar_install/ssas_deploy_2.png
       :align: center

       `Image - SSAS deployment wizard, Destination folder`

#. If the database does not exist on the Analysis Server, the Analysis Service Deployment Wizard will automatically create the database IMIS Cubes otherwise the database will be overwritten !
    Click next to continue (:ref:`Image - SSAS deployment wizard, Deploy IMIS cubes <ssas_deploy_3>`).

    .. _ssas_deploy_3:

    .. figure:: /img/ar_install/ssas_deploy_3.png
       :align: center

       `Image - SSAS deployment wizard, Deploy IMIS cubes`

#. Specify options for partitions, roles and members according to the requirements.
    Click next to continue(:ref:`Image - SSAS deployment wizard, Partitions & Roles <ssas_deploy_4>`).

    .. _ssas_deploy_4:

    .. figure:: /img/ar_install/ssas_deploy_4.png
       :align: center

       `Image - SSAS deployment wizard, Partitions & Roles`

#. On the providers select box, choose SQL server Native client.
    * On the left side of the connection manager select connection.
    * Click the refresh button and select the instance name.
    * On the Log on to the server panel, provide username and Password for the instance selected.
    * Under the connect to a database panel select the IMIS_DW.
    * Verify the connection by clicking the Test Connection button.
    * Click OK to continue with the installation(:ref:`Image - SSAS deployment wizard, SQL server <ssas_deploy_5_sql>`).

    .. _ssas_deploy_5_sql:

    .. figure:: /img/ar_install/ssas_deploy_5_sql.png
       :align: center

       `Image - SSAS deployment wizard, SQL server`

#. On the  Select Processing Options window, select the appropriate option.
    Click next to continue with the deployment(:ref:`Image - SSAS deployment wizard, Processing <ssas_deploy_6>`).

    .. _ssas_deploy_6:

    .. figure:: /img/ar_install/ssas_deploy_6.png
       :align: center

       `Image - SSAS deployment wizard, Processing`

#. Confirm Deployment. If the deployment script is required, check the Create Deployment Script option and browse to the destination folder.
    Click next to continue(:ref:`Image - SSAS deployment wizard, Finish <ssas_deploy_7>`).

    .. _ssas_deploy_7:

    .. figure:: /img/ar_install/ssas_deploy_7.png
       :align: center

       `Image - SSAS deployment wizard, Finish`

#. Deploying Database
    * Click next to continue(:ref:`Image - Database deployment wizard, Run <db_deploy>`).

    .. _db_deploy:

    .. figure:: /img/ar_install/db_deploy.png
       :align: center

       `Image - Database deployment wizard, Run`

    * Click finish to complete the deployment(:ref:`Image -  Database deployment wizard, Results<db_deploy_1>`).
	
    .. _db_deploy_1:

    .. figure:: /img/ar_install/db_deploy_1.png
       :align: center

       `Image - Database deployment wizard, Results`