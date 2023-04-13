## FastAPI Demo

1.创建虚拟环境 venv

```
python3 -m venv venv
```

2.进入虚拟环境

```
source ./venv/bin/activate
```

3.安装 Poetry

```
pip3 install poetry
```

4.下载依赖

```
poetry install
```

5.启动项目

```
uvicorn main:app --reload
```

6.查看接口文档

```
http://127.0.0.1:8000/docs#
```

7.退出虚拟环境

```
deactivate
```
