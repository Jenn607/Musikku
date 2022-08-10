from pyrogram import Client

API_KEY = int(input("68ac3255-43e9-417c-8adf-429ca60f6125: "))
API_HASH = input("eda35365e336d67a8354ce83813b9a73: ")
with Client(":memory:", api_id=API_KEY, api_hash=API_HASH) as app:
    print(app.export_session_string())
