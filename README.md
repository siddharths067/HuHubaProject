# HuHubaProject - siddharths067
## My Solution to the HuHuba Internship Problem:
As was stated in the problem statement I used python to handle FCM messaging from the server. I used flask to handle send requests which further were forwarded using the PyFCM library.

I am sorry I couldn't provide you with an uploaded version to Google App Engine , 
I tried uploading it, It worked fine , But to send HTTPS POST requests ( Which replaced the earlier GCM request mechanism), A dependency lies with SOCKET API.

I examined the Stack Trace on Google Console , it read SOCKET API will be enabled once Billing is set up. 

And I am not allowed Billing on my Debit Card.

I have removed my firebase Web Server API key to prevent unauthorized usage. 
I have sent the API key to Mr Rohit Prakash, Please replace it in helloworld.py line number 13 	api_key="".


## About - helloworld.py
This is a straight forward flask server , 
As soon as the user enters the server-page , I open the send.html file in my templates folder. 
A simple form POST allows to send this file back to the server, 
The server now parses and retrieves the POST parameter and uses the underlying FCM-API to authorize itself ,

A General topic named 'all' is subscribed by the client application automatically when it is opened , so every instance
of the application in Android devices recieve the notification.

I then send the notification to the FCM API.

I guess there is nothing else more to explain.

Works for both foreground and background as per FCM google-services.json norms.

## Deploying on GAE 
Just upload it and activate billing for your account.

## Running on local server
python helloworld.py

that's it 
runs on localhost port 8081

