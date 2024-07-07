# iplogger
Language: `Python 3`

Library: `Flask`

License: `unlicense`

## Setup

1. Ensure Python is installed (version 3.12 recommended).
2. Create a virtual environment:
    ```bash
    python -m venv env
    ```
3. Install the required libraries:
    ```bash
    env/bin/pip install -r requirements.txt
    ```
4. Configure the `config.py` file.
5. Run the application:
    ```bash
    env/bin/python main.py
    ```
6. Check:<br>
    Visit http://SERVERADDR:PORT/LOGGERNAME in your browser.

    Check `logs/LOGGERNAME.log`, you must see:
    ```plaintext
    $TIME: IP: "$IP" User Agent: "$UserAgent"
    ``` 

## Configuration Details
- `port` (int): Port on which the webserver will run.
- `debug` (bool): Enable or disable debug mode. It is strongly recommended to set this to `False` unless you are debugging.
- `loggers` (dict): Mapping of logger names to their redirect links.


P.S. Ни за что не открывайте main.py. Там лютый говнокод