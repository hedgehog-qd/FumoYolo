# FumoYolo
Fumo detection based on YOLOv2 using K210

## About this project
### ``[Aya's Camera]``
This is a YOLOv2 object detection model specifically trained to recognize FumoFumo plush toys. Now can recognize these characters: Renko, Shizuha, Yuka, Koishi. More characters will be supported later.

The model has been quantized and successfully deployed on a K210 development board for efficient real-time object detection.

## Images
![img](https://github.com/hedgehog-qd/FumoYolo/blob/main/img1.jpg)
![img](https://github.com/hedgehog-qd/FumoYolo/blob/main/img2.jpg)

## How to use
1. **Clone the repository**
2. **Copy model files into SD card**

   Copy `fumoyolo.kmodel`, `anchors.txt` and `label.txt` into SD card, then plug it into your K210 dev board
3. **Editing the code**

   Open `boot.py` with CanMV IDE, make sure all paths match the files on your SD card
4. **Connect and run**

   Make sure your USB cable is connected, then connect the dev board in your IDE, click the "Run" button

## Acknowledgements

- YOLOv2: [Original YOLOv2 Paper](https://arxiv.org/abs/1612.08242)
- K210: [Kendryte K210](https://www.canaan-creative.com/product/kendryteai)

## Trademark and Copyright Notice

- **FumoFumo** is the trademark of [Gift](https://www.gift-gift.jp/nui/toho.html)
- The characters depicted in the images are from the Touhou Project created by Team Shanghai Alice
