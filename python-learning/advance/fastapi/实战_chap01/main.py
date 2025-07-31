import pathlib, pyprojroot
from fastapi import FastAPI, Request
from typing import Optional
from fastapi.responses import HTMLResponse

PROJ_ROOT = pyprojroot.here()
print("根目录：", PROJ_ROOT)

app = FastAPI(title="学习FastAPI框架文档", 
              version="0.0。1", 
              description="以下是关于FastAPI框架文档的介绍和描述")

# 路由注册，就是提供一个对应的URL地址来关联或绑定定义的函数。
@app.get("/app/hello", tags=['app实例对象注册接口-示例'])
def app_hello():
    return {"hello": "app api"}

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>我的第一个 FastAPI 网站</title>
        </head>
        <body>
            <h1>Hello, FastAPI!</h1>
            <p>第一个 FastAPI 网站，欢迎访问我的网站</p>
        </body>
    </html>
    """
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000)