import requests
import json
import base64

def whatsappApi(phone,text):

    url = "https://rapidapi.rmlconnect.net/wbm/v1/message" 

    payload = json.dumps({
    "phone": phone,
    "text": text,

    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': '617bf1a1245383001100f7c0'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

def SMSApi(phone,text):

    url = "https://rapidapi.rmlconnect.net:9443/bulksms/bulksms?username=rapid-Kx8h7956210000&password=618a1fc50fcc5f0012910a49&type=0&dlr=0&destination="+str(phone)+"&source=RMLPRD&message="+str(text)
    
    payload={}

    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

def EmailAPISignup(mail):


    pay = {"message":{"to":[{"email":mail,"name":"","type":"to"}],"html":"Dear "+str(name)+",\n Welcome to Cropwayy!!!\nYou are a Cropwian now. We encourage you to explore various services at Cropwayy and use them wisely.\nIf you have any questions, please feel free to email us at support@cropwayy.co . In the meantime, stay tuned for upcoming notifications and updates soon. \n\n We wish you an amazing journey at Cropwayy, see you onboard :) \n\nBest Regards \nCropwayy Team"  ,"subject":"Welcome to Cropwayy","from_email":"noreply@rapidemail.rmlconnect.net","from_name":""},"owner_id":"67417601","token":"uUDVKVwyNfZubR2SjgTHBZey","smtp_user_name":"smtp83099742"}

    r = requests.post("http://rapidemail.rmlconnect.net/v1.0/messages/sendMail", json = pay )


def EmailAPI(mail,a,b,c,d,e,f):

    
    sample_string= """
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <title>Invoince</title>
    <style>
        /* -------------------------------------
    GLOBAL
    A very basic CSS reset
------------------------------------- */
        * {
            margin: 0;
            padding: 0;
            font-family: "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;
            box-sizing: border-box;
            font-size: 14px;
        }

        img {
            max-width: 100%;
        }

        body {
            -webkit-font-smoothing: antialiased;
            -webkit-text-size-adjust: none;
            width: 100% !important;
            height: 100%;
            line-height: 1.6;
        }

        /* Let's make sure all tables have defaults */
        table td {
            vertical-align: top;
        }

        /* -------------------------------------
    BODY & CONTAINER
------------------------------------- */
        body {
            background-color: #f6f6f6;
        }

        .body-wrap {
            background-color: #f6f6f6;
            width: 100%;
        }

        .container {
            display: block !important;
            max-width: 600px !important;
            margin: 0 auto !important;
            /* makes it centered */
            clear: both !important;
        }

        .content {
            max-width: 600px;
            margin: 0 auto;
            display: block;
            padding: 20px;
        }

        /* -------------------------------------
    HEADER, FOOTER, MAIN
------------------------------------- */
        .main {
            background: #fff;
            border: 1px solid #e9e9e9;
            border-radius: 3px;
        }

        .content-wrap {
            padding: 20px;
        }

        .content-block {
            padding: 0 0 20px;
        }

        .header {
            width: 100%;
            margin-bottom: 20px;
        }

        .footer {
            width: 100%;
            clear: both;
            color: #999;
            padding: 20px;
        }

        .footer a {
            color: #999;
        }

        .footer p,
        .footer a,
        .footer unsubscribe,
        .footer td {
            font-size: 12px;
        }

        /* -------------------------------------
    TYPOGRAPHY
------------------------------------- */
        h1,
        h2,
        h3 {
            font-family: "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;
            color: #000;
            margin: 40px 0 0;
            line-height: 1.2;
            font-weight: 400;
        }

        h1 {
            font-size: 32px;
            font-weight: 500;
        }

        h2 {
            font-size: 24px;
        }

        h3 {
            font-size: 18px;
        }

        h4 {
            font-size: 14px;
            font-weight: 600;
        }

        p,
        ul,
        ol {
            margin-bottom: 10px;
            font-weight: normal;
        }

        p li,
        ul li,
        ol li {
            margin-left: 5px;
            list-style-position: inside;
        }

        /* -------------------------------------
    LINKS & BUTTONS
------------------------------------- */
        a {
            color: #1ab394;
            text-decoration: underline;
        }

        .btn-primary {
            text-decoration: none;
            color: #FFF;
            background-color: #1ab394;
            border: solid #1ab394;
            border-width: 5px 10px;
            line-height: 2;
            font-weight: bold;
            text-align: center;
            cursor: pointer;
            display: inline-block;
            border-radius: 5px;
            text-transform: capitalize;
        }

        /* -------------------------------------
    OTHER STYLES THAT MIGHT BE USEFUL
------------------------------------- */
        .last {
            margin-bottom: 0;
        }

        .first {
            margin-top: 0;
        }

        .aligncenter {
            text-align: center;
        }

        .alignright {
            text-align: right;
        }

        .alignleft {
            text-align: left;
        }

        .clear {
            clear: both;
        }

        /* -------------------------------------
    ALERTS
    Change the class depending on warning email, good email or bad email
------------------------------------- */
        .alert {
            font-size: 16px;
            color: #fff;
            font-weight: 500;
            padding: 20px;
            text-align: center;
            border-radius: 3px 3px 0 0;
        }

        .alert a {
            color: #fff;
            text-decoration: none;
            font-weight: 500;
            font-size: 16px;
        }

        .alert.alert-warning {
            background: #f8ac59;
        }

        .alert.alert-bad {
            background: #ed5565;
        }

        .alert.alert-good {
            background: #1ab394;
        }

        /* -------------------------------------
    INVOICE
    Styles for the billing table
------------------------------------- */
        .invoice {
            margin: 40px auto;
            text-align: left;
            width: 80%;
        }

        .invoice td {
            padding: 5px 0;
        }

        .invoice .invoice-items {
            width: 100%;
        }

        .invoice .invoice-items td {
            border-top: #eee 1px solid;
        }

        .invoice .invoice-items .total td {
            border-top: 2px solid #333;
            border-bottom: 2px solid #333;
            font-weight: 700;
        }

        /* -------------------------------------
    RESPONSIVE AND MOBILE FRIENDLY STYLES
------------------------------------- */
        @media only screen and (max-width: 640px) {

            h1,
            h2,
            h3,
            h4 {
                font-weight: 600 !important;
                margin: 20px 0 5px !important;
            }

            h1 {
                font-size: 22px !important;
            }

            h2 {
                font-size: 18px !important;
            }

            h3 {
                font-size: 16px !important;
            }

            .container {
                width: 100% !important;
            }

            .content,
            .content-wrap {
                padding: 10px !important;
            }

            .invoice {
                width: 100% !important;
            }
        }
    </style>
</head>

<body>
    <div class="container">
        <!-- invoice -->

        <table class="body-wrap">
            <tbody><tr>
                <td></td>
                <td class="container" width="600">
                    <div class="content">
                        <table class="main" width="100%" cellpadding="0" cellspacing="0">
                            <tbody><tr>
                                <td class="content-wrap aligncenter">
                                    <table width="100%" cellpadding="0" cellspacing="0">
                                        <tbody><tr>
                                            <td class="content-block">
                                            <center>
                                                <h2>Thanks for using our services</h2>
                                                </center>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="content-block">
                                            <center>
                                                <h3>Invoice for Crop Purchase</h3>
                                                </center>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="content-block">
                                                <table class="invoice">
                                                    <tbody>
                                                    <tr>
                                                        <td>Invoice No: """+str(a)+"""<br>Invoice Date: """+str(b)+"""<br><br>Buyer:<br>"""+str(c)+"""<br><br></td>
                                                    </tr>
                                                   
                                                    <tr>
                                                        <td>
                                                            <table class="invoice-items" cellpadding="0" cellspacing="0">
                                                            <thead>
                                                            <th colspan="2">SNo.
                                                            </th>
                                                            <th colspan="6">Crop Name
                                                            </th>
                                                             <th colspan="4">Total
                                                            </th>
                                                            </thead>
                                                                <tbody><tr>
                                                        
                                                                 
                                                                    <td colspan="2">1</td>
                                                                    <td colspan = "6">"""+str(d)+"""</td>
                                                                    <td colspan = "4">"""+str(e)+"""</td>
                                                                </tr>
                                                              
                                                                <tr class="total">
                                                                 <td colspan="2"></td>    
                                                                    <td colspan = "6" class="alignright" width="100%">Total&nbsp;</td>
                                                                    <td colspan = "4" class="alignright">"""+str(f)+"""</td>
                                                                </tr>
                                                            </tbody></table>
                                                        </td>
                                                    </tr>
                                                </tbody></table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="content-block">
                                            <center>
                                                <a href="www.cropwayy.com">CROPWAYY</a>
                                                 </center>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="content-block">
                                             <center>
                                                Cropwayy (c) 2021
                                                 </center>
                                            </td>
                                        </tr>
                                    </tbody></table>
                                </td>
                            </tr>
                        </tbody></table>
                        <div class="footer">
                            <table width="100%">
                                <tbody><tr>
                                    <td class="aligncenter content-block">Questions? Email <a href="mailto:">support@company.inc</a></td>
                                </tr>
                            </tbody></table>
                        </div></div>
                </td>
                <td></td>
            </tr>
        </tbody></table>

</body>

</html>"""

    sample_string_bytes = sample_string.encode("ascii")
    
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    
    pay = {"message":{"to":[{"email":"giantkillerkushagra@gmail.com","name":"","type":"to"}],  'attachments': [{'type':'text/plain',
        'name': 'myfile.html','content': base64_string}],"html":"Invoice of your purchase","subject":"Invoice of your purchase","from_email":"noreply@rapidemail.rmlconnect.net","from_name":""},"owner_id":"67417601","token":"uUDVKVwyNfZubR2SjgTHBZey","smtp_user_name":"smtp83099742"}

    # headers = {
        
    # 'Reply-To': 'message.reply@example.com',
    # 'X-Unique-Id': 'id',
        
    # }

    r = requests.post("http://rapidemail.rmlconnect.net/v1.0/messages/sendMail", json = pay )
