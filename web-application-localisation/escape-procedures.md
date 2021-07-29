# Escape procedures

## Video tutorial 

{% embed url="https://youtu.be/XYtyojSHE0Q" %}

## Escape procedures localisation

The role of the Escape procedures is to allow adaptation of the Web Application to different insurance contexts. There are situated in a single class, [EscapeBL](https://github.com/openimis/web_app_vb/blob/master/IMIS_BL/EscapeBL.vb), which makes it easier to access and modify without having to worry about messing with the whole Web Application source code. To modify the escape procedure, first download the source code [from Github Web Application repository](https://github.com/openimis/web_app_vb). Within the solution, go to IMIS\_BL folder and open the [EscapeBL.vb](https://github.com/openimis/web_app_vb/blob/master/IMIS_BL/EscapeBL.vb) file. 

There are 2 escape procedures that can be modified: 

1. [isValidInsuranceNumber](https://github.com/openimis/web_app_vb/blob/master/IMIS_BL/EscapeBL.vb#L32) allows validating the insuree number based on predefined rules. It is used, for example, when a new family or insuree are enrolled in openIMIS to ensure insuree number validity and to prevent typing errors.
2. [SendSMS](https://github.com/openimis/web_app_vb/blob/master/IMIS_BL/EscapeBL.vb#L35) allows sending SMS messages through a specific SMS Gateway. It is used, for example, in Web Application Policy Renewal form to send the renewal SMS message to the family.

## **Localise the insuree number validation escape procedure**

In this guide, we will localise the **isValidInsuranceNumber** method. 

| **Parameters**  | **Returns** |
| :--- | :--- |
| **InsuranceNumber** _String_ the insuree number to validate | _Boolean_ **true** if the insuree number is valid, otherwise, **false** |

This is the generic implementation of the method:

```text
Public Function isValidInsuranceNumber(ByVal InsuranceNumber As String) As Boolean 
    Return True 
End Function
```

The generic method is returning always true, meaning any insuree number will be a valid one. 

Let's take for example the following insuree number requirements:

1. The insuree number must follow the modulo 9 rule: the last digit is the modulo 9 of the number without the last digit
2. The insuree number must have 10 digits \('0' at the beginning must be saved\)

These requirements are satisfied by the following escape procedure: 

```text
Public Function isValidInsuranceNumber(ByVal InsuranceNumber As String) As Boolean 
    If Not InsuranceNumber.ToString.Length = 10 Then Return False 
    Dim N As String = Left(InsuranceNumber.ToString, 9) 
    Dim Modulo As String = Right(InsuranceNumber.ToString, 1) 
    If Modulo = N - (Int(N / 9) * 9) Then Return True 
    Return False 
End Function
```

The isValidInsuranceNumber is executing the following steps: 

1. validates the length of the insuree number \(line 2\)
2. splits the insuree number into number and modulo parts \(lines 3 and 4\)
3. validates the insuree number if the modulo part is equal to the modulo result \(line 5\)
4. all other cases are invalidated \(line 6\)

Other validations rules can be applied.

To apply the new modification to the escape procedures, the Web Application .Net solution needs to be [published and deployed](https://openimis.atlassian.net/wiki/spaces/OP/pages/906690638). 

