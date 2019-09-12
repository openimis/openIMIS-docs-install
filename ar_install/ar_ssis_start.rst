.. include:: /_sidebar.rst.inc

Execute SSIS
~~~~~~~~~~~~

Once both the SSIS and SSAS packages are deployed successfully, it’s time to start the ETL process. To start the ETL Process, follow the instructions below.

#. Navigate to the folder where the SSIS package was installed. Find the file named "IMISDW" and double click the package to begin the process(:ref:`Image -  Run SSIS <ssis_run>`).

    .. _ssis_run:

    .. figure:: /img/ar_install/ssis_run.png
       :align: center

       `Image - Run SSIS`

#. This process might take a while to finish depending on the data volume. Once the process is completed successfully, the SSAS package is now ready for the reporting(:ref:`Image -  SSIS Results <ssis_results>`).

    .. _ssis_results:

    .. figure:: /img/ar_install/ssis_results.png
       :align: center

       `Image - SSIS Results`