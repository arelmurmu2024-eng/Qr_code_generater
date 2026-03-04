import pywebio as pwi
from pywebio import start_server
from pywebio.input import input,actions
from pywebio.output import put_text,put_image
from qr_code import Qcode # Arels's customized qrcode class for exciting features

def run():
    data = input(label= "🔥 Type the data 🥑", placeholder="Type sentence, url")
    qrcode = Qcode(data).return_name() # type: ignore

    if data:
        with open(qrcode,"rb") as f :
            temp = f.read()
            put_image(temp)

start_server(applications=run, 
             auto_open_webbrowser=True, 
             debug= True, 
             host="0.0.0.0", port= 7777)


