# Using JSONRPC to fetch yesterday data from fems

### OS
    Used with Windows 11, but check with Linux using SPREADSHEET_PATH='/tmp/'

### How to create the .env file
    USER="..."
        Ask google, bing, ...
    PASSWORD="..."
        Ask google, bing, ...
    WEBSOCKET_URI="ws://192.168.178.42:8085/websocket"
        but change 192.168.178.42 to your local fems ip address
    SPREADSHEET_PATH='C:\\fems\\'
        has to be an existing path, write access allowed

### How to run
    python3 fems_history.py
    Call above command every day at 03:00 using a Task Scheduler Job.

### What you get
    Two files inside SPREADSHEET_PATH.
    First is the .xlsx file of yesterday with 15 minutes resolution.
    Second ist a .txt file containing "generated energy", "used energy" and "independence"

### Links
[OpenEMS](https://community.openems.io/c/english/8)  
[Fenecon](https://fenecon.de/en/)  
[JSON-RPC](https://www.jsonrpc.org/specification)  
