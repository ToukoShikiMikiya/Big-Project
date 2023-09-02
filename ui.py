# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import random
import shutil
import sys

import cv2
import imagesize
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QApplication, QMainWindow, QMessageBox
from paddleseg.core.predict import preprocess, save_image, watershed_algorithm
from paddleseg.core.infer import inference
from tools.train import train1
from tools.predict import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1330, 811)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 1311, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_2.addWidget(self.lineEdit_5)
        self.label_i = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_i.setObjectName("label_i")
        self.horizontalLayout_2.addWidget(self.label_i)
        self.lineEdit_i = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_i.setObjectName("lineEdit_i")
        self.horizontalLayout_2.addWidget(self.lineEdit_i)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_2.addWidget(self.lineEdit_9)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 90, 1311, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_3.addWidget(self.lineEdit_6)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 50, 1311, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 130, 1311, 671))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def open1(self):
        self.train_dirname = QFileDialog.getExistingDirectory(self, '选择文件夹', os.getcwd())
        self.lineEdit_5.setText(self.train_dirname)

    def change(self):
        img_names = os.listdir(self.train_dirname)
        os.makedirs(os.path.join(self.train_dirname, 'origin_images'), exist_ok=True)
        os.makedirs(os.path.join(self.train_dirname, 'origin_masks'), exist_ok=True)
        os.makedirs(os.path.join(self.train_dirname, 'images', 'train'), exist_ok=True)
        os.makedirs(os.path.join(self.train_dirname, 'images', 'val'), exist_ok=True)
        os.makedirs(os.path.join(self.train_dirname, 'annotations', 'train'), exist_ok=True)
        os.makedirs(os.path.join(self.train_dirname, 'annotations', 'val'), exist_ok=True)
        for img_name in img_names:
            if img_name.split('.')[-1] not in ['jpg', 'png', 'jpeg']:
                continue
            if ''.join(img_name.split('.')[:-1]).endswith('mask'):
                shutil.move(os.path.join(self.train_dirname, img_name),
                            os.path.join(self.train_dirname, 'origin_masks',
                                         ''.join(img_name.split('.')[:-1])[:-5] + '.' + img_name.split('.')[-1]))
            else:
                shutil.move(os.path.join(self.train_dirname, img_name),
                            os.path.join(self.train_dirname, 'origin_images', img_name))
        images_names = os.listdir(os.path.join(self.train_dirname, 'origin_images'))
        random_images = random.sample(images_names, int(len(images_names) / 5))
        for name in images_names:
            if name in random_images:
                shutil.copy(os.path.join(self.train_dirname, 'origin_images', name),
                            os.path.join(self.train_dirname, 'images', 'val', name))
                name1 = os.path.join(self.train_dirname, 'annotations', 'val', name)
                shutil.copy(os.path.join(self.train_dirname, 'origin_masks', name), name1)
                img = cv2.imread(name1, 0)
                for i in range(img.shape[0]):
                    for j in range(img.shape[1]):
                        if img[i][j] >= 128:
                            img[i][j] = 1
                        else:
                            img[i][j] = 0
                cv2.imwrite(name1, img)
            else:
                shutil.copy(os.path.join(self.train_dirname, 'origin_images', name),
                            os.path.join(self.train_dirname, 'images', 'train', name))
                name1 = os.path.join(self.train_dirname, 'annotations', 'train', name)
                shutil.copy(os.path.join(self.train_dirname, 'origin_masks', name), name1)
                img = cv2.imread(name1, 0)
                for i in range(img.shape[0]):
                    for j in range(img.shape[1]):
                        if img[i][j] >= 128:
                            img[i][j] = 1
                        else:
                            img[i][j] = 0
                cv2.imwrite(name1, img)
        QMessageBox.about(self, '提示', '整理完毕！')

    def open2(self):
        self.save_dirname = QFileDialog.getExistingDirectory(self, '选择文件夹', os.getcwd())
        self.lineEdit_9.setText(self.save_dirname)

    def train(self):
        iters = int(self.lineEdit_i.text())
        batch_size = int(self.lineEdit_4.text())
        lr = float(self.lineEdit_3.text())
        ret = train1(self.train_dirname, self.save_dirname, iters, batch_size, lr)
        QMessageBox.about(self, '提示', '训练完毕！')
        self.label_7.setText(f"性能指标: {ret}")

    def open3(self):
        model_filename = QFileDialog.getOpenFileName(self, '选择模型', os.getcwd(), '*')
        self.model_filename = model_filename[0]
        if not model_filename:
            return
        self.lineEdit_6.setText(self.model_filename)
        args = parse_args()
        assert args.config is not None, \
            'No configuration file specified, please set --config'
        args.model_path = self.model_filename
        cfg = Config(args.config)
        builder = SegBuilder(cfg)
        utils.show_env_info()
        utils.show_cfg_info(cfg)
        utils.set_device('gpu')
        self.model = builder.model
        self.transforms = Compose(builder.val_transforms)
        utils.load_entire_model(self.model, args.model_path)
        self.model.eval()

    def infer1(self):
        filename, _ = QFileDialog.getOpenFileName(self, '选择图像', os.getcwd(), '*')
        w, h = imagesize.get(filename)
        if max(h, w) > 640:
            if h >= w:
                w = int(w / (h / 640))
                h = 640
            else:
                h = int(h / (w / 640))
                w = 640
        self.label.setPixmap(QPixmap(filename).scaled(w, h))
        with paddle.no_grad():
            data = preprocess(filename, self.transforms)
            pred, _ = inference(
                self.model,
                data['img'],
                trans_info=data['trans_info'],
                is_slide=False,
                stride=None,
                crop_size=None)
            mask = paddle.squeeze(pred, axis=0)
            pred = paddle.squeeze(pred)
            pred = pred.numpy().astype('uint8')
            mask_saved_dir = os.path.join('output/result', 'mask_prediction')
            o_path = mask_saved_dir + '/' + filename.split('/')[-1]
            save_image(mask, o_path)
        self.label_2.setPixmap(QPixmap(o_path).scaled(w, h))

    def infer2(self):
        dir_name = QFileDialog.getExistingDirectory(self, '选择文件夹', os.getcwd())
        infer(self.model_filename, dir_name)
        QMessageBox.about(self, '提示', '结果已保存在output/result文件夹下！')

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "选择训练图片文件夹"))
        self.pushButton.clicked.connect(self.open1)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_i.setText(_translate("Form", "iters:"))
        self.lineEdit_i.setText(_translate("Form", "40000"))
        self.label_6.setText(_translate("Form", "batch-size:"))
        self.lineEdit_4.setText(_translate("Form", "4"))
        self.label_5.setText(_translate("Form", "learning-rate:"))
        self.lineEdit_3.setText(_translate("Form", "0.01"))
        self.pushButton_8.setText(_translate("Form", "选择模型保存路径"))
        self.pushButton_8.clicked.connect(self.open2)
        self.pushButton_6.setText(_translate("Form", "选择模型"))
        self.pushButton_6.clicked.connect(self.open3)
        self.pushButton_3.setText(_translate("Form", "选择单张图片推理"))
        self.pushButton_3.clicked.connect(self.infer1)
        self.pushButton_7.setText(_translate("Form", "选择图片文件夹推理"))
        self.pushButton_7.clicked.connect(self.infer2)
        self.pushButton_2.setText(_translate("Form", "一键整理数据集"))
        self.pushButton_2.clicked.connect(self.change)
        self.pushButton_4.setText(_translate("Form", "开始训练"))
        self.pushButton_4.clicked.connect(self.train)
        self.label_7.setText(_translate("Form", "性能指标:"))


class Main_ui(Ui_Form, QMainWindow):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)  # 创建应用
    w = Main_ui()  # 创建窗口
    w.setWindowTitle("图像分割工具")  # 窗口标题
    w.show()  # 显示窗口
    sys.exit(app.exec_())  # 退出程序


main()  # 调用主函