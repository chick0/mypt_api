# api-side
This is **API Server** for my **[Portfolio](https://ch1ck.xyz)**!

## Links
* **new** client: [chick0/ch1ck.xyz](https://github.com/chick0/ch1ck.xyz)

* ~~*old* client: [chick0/mypt_client](https://github.com/chick0/mypt_client)~~

## how to run

1. (optional) set up venv
   ```
   python -m venv venv
   source venv/bin/activate
   ```
2. install requirements
   ```
   pip install -r requirements.txt
   ```
3. start gunicorn
   ```
   gunicorn -c gunicorn.py
   ```
