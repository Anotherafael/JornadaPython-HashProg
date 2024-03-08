import time

import pandas as pd
import pyautogui

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(1)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

time.sleep(1)
pyautogui.press("enter")
time.sleep(2)

pyautogui.click(x=1425, y=318)
pyautogui.write("hashtagtreinamentos@email.com")

pyautogui.press("tab")
pyautogui.write("password123")

pyautogui.press("tab")
pyautogui.press("enter")

db = pd.read_csv("produtos.csv")

for row in db.index:
    pyautogui.click(x=1415, y=225)

    # codigo,marca,tipo,categoria,preco_unitario,custo,obs

    value = db.loc[row, "codigo"]
    pyautogui.write(value)

    pyautogui.press("tab")
    value = db.loc[row, "marca"]
    pyautogui.write(value)

    pyautogui.press("tab")
    value = db.loc[row, "tipo"]
    pyautogui.write(value)

    pyautogui.press("tab")
    value = str(db.loc[row, "categoria"])
    pyautogui.write(value)

    pyautogui.press("tab")
    value = str(db.loc[row, "preco_unitario"])
    pyautogui.write(value)

    pyautogui.press("tab")
    value = str(db.loc[row, "custo"])
    pyautogui.write(value)

    pyautogui.press("tab")
    value = db.loc[row, "obs"]
    if pd.isna(value):
        pyautogui.write("")
    else:
        pyautogui.write(value)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
