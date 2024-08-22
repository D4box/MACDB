from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json

app = FastAPI()

def tagtolist(tag):
    taglist = []
    try:
        with open("./un/"+tag+".txt", "r", encoding='utf-8') as file: #别问为什么是un，我也不知道
            for line in file.readlines():
                taglist.append(line.strip('\n'))
    except FileNotFoundError:
        return "没有Tag:"+tag
    return taglist[1:]

@app.get("/gettags/{tag}")
def read_root(tag: str):
    header = {"Content-Type": "application/json",
              "Access-Control-Allow-Origin": "*",
              "Cache-Control":"max-age=86400"}
    return JSONResponse(content=tagtolist(tag), headers=header)

@app.get("/gettaglist/")
def read_root():
    header = {"Content-Type": "application/json",
              "Access-Control-Allow-Origin": "*",
              "Cache-Control":"max-age=86400"}
    with open("./taglist.json", "r", encoding='utf-8') as file:
        files = json.load(file)
    return JSONResponse(content=files, headers=header)