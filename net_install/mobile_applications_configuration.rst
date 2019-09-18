


Mobile application configuration guide
======================================

**v1.3.0 and later**

Mobile apps need to be re-compiled with the correct server's IP address
for it to be functional.

To do so:

-  Open Android Studio

-  Open the mobile app project you want to configure (available on
   `openIMIS github <https://github.com/openimis>`__)

-  For the Claim and Enquiry apps, locate the file called General.java in the project explorer

-  For the IMIS app, locate the class AppInformation in the project explorer: App\\src\\main\\java\\tz\\co\\exact\\imis\\AppInformation.java

-  Edit the class by replacing the server's IP address or server name,
   and save

-  Build the app via the tools menu

-  The new .apk file is now available in the release folder indicated by Android Studio
