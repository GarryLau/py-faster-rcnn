本工程旨在说明如何利用faster RCNN建立自己的检测任务。
需要建立自己的检测任务时可比较本工程的py-faster-rcnn和rbg大神的原版py-faster-rcnn，差异的地方就是需要修改、添加的地方。


由于很多时候我们的数据是不够的，需要进行数据增强，因此本工程里加入了和https://github.com/GarryLau/imgaug 中的数据增强方法相结合使用的内容。
我们知道在读取文件夹中的内容时如果文件夹中的文件太多很可能导致程序卡死，因此在srd.py中加入了将xml中目标框坐标保存到txt中，这样在使用imgaug的时候可以读取txt来获得文件的名称、目标框坐标信息。具体使用方法请参考https://github.com/GarryLau/imgaug/blob/master/garylau/imgaug.py 
