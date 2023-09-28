FROM python:3.9
#代码添加到code文件夹
ADD . /code
# 设置code文件夹是工作目录
WORKDIR /code
EXPOSE 5000
# 安装支持
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt
CMD ["python", "index.py"]