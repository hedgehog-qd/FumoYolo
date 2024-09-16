import sensor
import image
import lcd
import KPU as kpu

lcd.init(invert=True)
lcd.rotation(2) # lcd rotation (edit this line if the image is flipped)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224, 224))
sensor.skip_frames(time = 2000)
sensor.set_hmirror(0)
sensor.set_vflip(False) # vertically flip
sensor.run(1)
task = kpu.load("/sd/fumoyolo.kmodel")
f=open("/sd/anchors.txt","r")
anchor_txt=f.read()
L=[]
for i in anchor_txt.split(","):
    L.append(float(i))
anchor=tuple(L)
f.close()
a = kpu.init_yolo2(task, 0.6, 0.3, 5, anchor)
f=open("/sd/lable.txt","r")
labels_txt=f.read()
labels = labels_txt.split(",")
f.close()
while(True):
    img = sensor.snapshot()
    code = kpu.run_yolo2(task, img)
    if code:
        for i in code:
            a=img.draw_rectangle(i.rect(),(0,0,255),2)
            a = lcd.display(img)
            for i in code:
                lcd.draw_string(i.x()+45, i.y()-5, labels[i.classid()]+" "+'%.2f'%i.value(), lcd.WHITE,lcd.BLUE)
    else:
        a = lcd.display(img)
a = kpu.deinit(task)
