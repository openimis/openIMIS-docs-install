# Multi-language support

## Video tutorial

{% embed url="https://youtu.be/KiAjKdmL5Q4" %}

## Language translations

Web Application .Net is supporting up to two languages. The language translation is done on the Web Application source code level \(this page\) and on the database level \(see [WA4.1 Language selection and translation tables](https://openimis.atlassian.net/wiki/spaces/OP/pages/906887227/WA4.1+Language+selection+and+translation+tables)\). 

The Web Application language localisation is using the default [ASP.Net Globalization](https://docs.microsoft.com/en-us/dotnet/standard/globalization-localization/) and [Culture configuration](https://docs.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo.currentuiculture). The translation is based on resource files. The generic application is translated into [English-language](https://github.com/openimis/web_app_vb/blob/master/IMIS/App_GlobalResources/Resource.resx) and [French-language](https://github.com/openimis/web_app_vb/blob/master/IMIS/App_GlobalResources/Resource.fr.resx).

In order to facilitate the translation of the Web Application and to have a common repository for language packs for openIMIS, we have subscribed to [lokalise.com](http://lokalise.com/). If you wish to add new languages to openIMIS Web Application, you can request the access by visiting the [Web Application project](https://app.lokalise.com/public/671284105ca5b4ac06f8e4.60698059/) on lokalise. For more information on the translation platform please check [Translation Management platform](https://openimis.atlassian.net/wiki/spaces/OP/pages/759070721) page.

![](https://openimis.atlassian.net/wiki/download/thumbnails/759070721/Lokalise-Logo-Horizontal.png?version=1&modificationDate=1564051176818&cacheVersion=1&api=v2&width=707&height=150)

### **Add a new language for Web Application in lokalise**

#### Add new language to the project

From the [Web Application project](https://lokalise.com/project/671284105ca5b4ac06f8e4.60698059) press the `+` button to add a new language.

![](../.gitbook/assets/image%20%287%29.png)

From the `Add languages` modal select the language to add. You can filter the languages by writing in the input field. In this example, we will choose French \(Cameroon\). Multiple languages can be added at once.

![](../.gitbook/assets/image%20%286%29.png)

Click the Add button. 

#### Translate [the glossary](https://openimis.atlassian.net/wiki/spaces/OP/pages/907018273/WA3.2+Language+translation#WA3.2Languagetranslation-why_glossary_is_important) to the new language 

From the [Web Application project](https://lokalise.com/project/671284105ca5b4ac06f8e4.60698059) press the `Glossary` button to add a new language.

![](../.gitbook/assets/image%20%289%29.png)

For each glossary term, translate in the new added language.

![](../.gitbook/assets/image%20%2810%29.png)

#### Translate the Web Application into the new language

For each term in the [Web Application project](https://lokalise.com/project/671284105ca5b4ac06f8e4.60698059), translate it in the new language.

![](../.gitbook/assets/image%20%2811%29.png)

#### Export the language as .Net resource file

From the [Web Application project](https://lokalise.com/project/671284105ca5b4ac06f8e4.60698059) press the `Download` button.

![](../.gitbook/assets/image%20%285%29.png)

Select the language you want to download and the different download settings.

![](../.gitbook/assets/image%20%288%29.png)

Press `Build and download` button. This will download a ZIP file with resource files for all selected languages. Unzip the file in a local folder. 

### **Add the new language in the Web Application project** 

Open in Visual Studio the Web Application .Net solution downloaded from [Github](https://github.com/openimis/web_app_vb).

In the `Solution Explorer` window, navigate to `IMIS project` → `App_GlobalResources` folder and open the contextual menu with right-click.

Select `Add → Existing Item...`.

Select the resource file for the new language and press `Add.` This will copy the file to the `App_GlobalResources` folder and add it to the project.

\(Optional\) you can check the new language by opening the resource file. 

To use the new language, the Web Application .Net solution needs to be [published and deployed](https://openimis.atlassian.net/wiki/spaces/OP/pages/906690638/WA3.3+Publish+and+deploy+the+customised+Web+Application). Nevertheless, you cannot use the new language unless you update the [language selection and translation tables](https://openimis.atlassian.net/wiki/spaces/OP/pages/906887227) in the database. 

## **Why Glossary is important**

Because there is multiple truth and it is often complex and can change over time, the terminology must have the same meaning and same wording in the whole Web Application. It is also important that the country-specific names are validated by the country implementing openIMIS. 

When using a glossary you ensure that you will use the same 'truth' across your application. In the case of lokalise, every time it will detect the glossary term, it will show the definition and the translation, allowing to be consistent in the translation package.

For example, in Tchad there are the different organisation names which must be adapted in openIMIS:

| openIMIS default name | Tchad official old name | Tchad official new name | Tchad health zones |
| :--- | :--- | :--- | :--- |
| Regions | Région | Province | Délégation Sanitaire Provinciale |
| District | Prefecture | Département | District sanitaires |
| Municipality | Sous-préfecture | Commune | Zone de résponsabilité |
| Village | Village | Village | Village |

