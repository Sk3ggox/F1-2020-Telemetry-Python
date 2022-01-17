# F1-2020-Telemetry-Python

A package handler for telemetry data over UDP for the game F1 2020. 
Currently only supports linux and works best when ran on a seperate server.

For setup, firstly get a json auth key for your FireBase Realtime Database.
Paste this in the project root directory (where main.py is located).
Then, alter the firebaseConfig in main.py to your auth data.
Lastly, insert your server IP in server.py.
Then, install all dependencies by running:
~~~
pip install pyrebase
~~~

Then start the service by running:
~~~
python3 main.py
~~~

Then, open up your game and go to preferences -> telemetry settings
There, enable UDP transmission, enter your SERVER IP and set data format to 2020.
The port should be kept at the default of 20777.
Start racing and the data automatically updates in in your FireBase.

To watch the data, see the display.html file as an example.
If you want to use this, enter your auth data in the code.
