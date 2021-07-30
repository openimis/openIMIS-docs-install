# Deploy the localized Web Application

## Video tutorial 

{% embed url="https://youtu.be/H7fHZqP38HQ" %}

## Publish and deploy the Web Application 

In the previous sections, we have seen how to update the escape procedures and to add new language translation. In this section, we will publish the new customised Web Application in a folder and deploy it over the previously installed generic version. 

{% page-ref page="escape-procedures.md" %}

{% page-ref page="multi-language-support.md" %}

{% page-ref page="../legacy-web-application-installation/web-application-installation.md" %}

### **Publish the customised Web Application** 

For detailed documentation on publishing using Visual Studio, visit the [how to deploy to a local folder](https://docs.microsoft.com/en-us/visualstudio/deployment/quickstart-deploy-to-local-folder) webpage.

Open in Visual Studio the Web Application .Net solution updated in the previous steps.

In Solution Explorer, right-click the IMIS project and choose `Publish` \(or use the `Build` &gt; `Publish` menu item\).

The default target location is the `publish` folder under the Web Application solution folder. If you wish to change the target location then you just edit the configuration.

Press the `Publish` button.

### **Deploy the Web Application** 

To deploy the localized Web Application published in the previous section, please follow the same steps from Web Application installation steps. 

{% page-ref page="../legacy-web-application-installation/web-application-installation.md" %}

#### **Deploy the Web Application as a new site**

To deploy the Web Application as a new site, follow the steps from the [Configure IIS](../legacy-web-application-installation/web-application-installation.md#configure-iis) section. You will need to change the binding ports or map different DNS as hostname.

#### **Deploy the Web Application to upgrade existing site**

To upgrade an existing Web Application site, replace existing files with the files from the published Web Application. 

Please make sure to: 

* not replace/remove Archive, Extracts, FromPhone, Images, and Workspace folders to prevent losing previous work
* [update IMISConnectionString](../legacy-web-application-installation/web-application-installation.md#edit-the-web-config) in Web.config file
* you don't need to edit permissions to Windows event logs again

