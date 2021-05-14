from bs4 import BeautifulSoup
import requests
import pandas
import tkinter.filedialog
import tkinter as tk
import config as c
import concurrent.futures


df = pandas.read_csv(tk.filedialog.askopenfilename())
urls = df["url"].tolist()
df_output = pandas.DataFrame(columns=["url","status"])
for url in urls:
    r = requests.get(url).text
    soup = BeautifulSoup(r, "html.parser")
    stock_tag = str(soup.find(c.tag_type, {c.tag_identifier: c.tag_identifier_value}))
    if c.in_stock_str in stock_tag:
        df_output.loc[len(df_output)] = [url, "In stock"]
    elif c.out_of_stock_str in stock_tag:
        df_output.loc[len(df_output)] = [url, "Out of stock"]
    else:
        df_output.loc[len(df_output)] = [url, "Unknown"]
df_output.to_csv("output.csv", index=False)
    