# PIL Learning

## 安装

```sh
$ pip3 install pillow
```

## 功能

* 图像归档
* 图像处理

[更多PIL库内容](http://effbot.org/imagingbook/)

## PIL库Image类解析

Image是PIL最重要的类，它代表一张图片，引入这个类的方法如下：

```sh
>>> from PIL import Image
```

#### Image 类的图像读取和创建方法：

|Index|方法|描述|
|:---:|:---|:---|
|1|Image.open(\<filename>)||
|2|Image.new(mode, size, color)||
|3|Image.open(StringIO.StringIO(buffer)||
|4|Image.frombytes(mode, size, data)||
|5|Image.verify()||

#### Image类的常用属性

|Index|属性|描述|
|:---:|:---|:---|
|1|Image.format||
|2|Image.mode||
|3|Image.size||
|4|Image.palette||

### 序列图像

序列类图像文件

* GIF
* FLI
* FLC
* TIFF

#### 序列类文件的操作方法

|Index|method|discribtion|
|:---:|:---|:---|
|1|Image.seek(frame)|跳转并发挥图像中的指定帧|
|2|Image.tell()|返回当前帧号|
