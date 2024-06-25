import os
import time

import cv2
import mysql
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk
from PyQt5.QtWidgets import QFileDialog,QTableWidgetItem
import formNguyHiem_CC,formCD,formCam,formBienPhu,formHL
import numpy
from PIL import ImageTk, Image
import bienBao_DTO

from keras.models import load_model
model = load_model('modelTrain.h5')

classes = { 1:'Biển báo đường cấm',
            2: 'Biển báo Cấm rẽ phải',
            3: 'Biển báo Cấm đi thẳng, rẽ phải',
            4: 'Biển báo Cấm đi thẳng, rẽ trái',
            5: 'Biển báo Cấm đi thẳng',
            6: 'Biển báo Cấm đỗ xe',
            7: 'Biển báo Cấm dừng xe và đỗ xe',
            8: 'Biển báo cấm ngược chiều',
            9: 'Biển báo Cấm người đi bộ',
            10: 'Biển báo Cấm quay đầu xe',
            11: 'Biển báo Cấm rẽ trái, rẽ phải',
            12: 'Biển báo Cấm rẽ trái',
            13: 'Biển báo Cấm rẽ và quay đầu xe',
            14: 'Biển báo Cấm sử dụng còi',
            15: 'Biển báo Cấm vượt',
            16: 'Biển báo Cấm xe 3 bánh có động cơ',
            17: 'Biển báo Cấm xe 3 bánh không động cơ',
            18: 'Biển báo Cấm xe công nông và các loại xe tương tự',
            19: 'Biển báo Cấm xe đạp',
            20: 'Biển báo Cấm xe máy',
            21: 'Biển báo Cấm xe người kéo đẩy',
            22: 'Biển báo Cấm xe ô tô quay đầu',
            23: 'Biển báo Cấm xe ô tô rẽ và quay đầu xe',
            24: 'Biển báo Cấm xe súc vật kéo',
            25: 'Biển báo Cấm xe tải vượt',
            26: 'Biển báo Cự ly tối thiểu giữa hai xe',
            27: 'Biển báo Hạn chế chiều cao xe',
            28: 'Biển báo Hạn chế chiều dài xe ô tô, máy kéo mooc hoặc sơ-mi-rơ-mooc',
            29: 'Biển báo Hạn chế chiều dài xe',
            30: 'Biển báo Hạn chế chiều ngang xe',
            31: 'Biển báo Hạn chế tải trọng toàn bộ xe',
            32: 'Biển báo Hạn chế tải trọng trục xe',
            33: 'Biển báo Hết cấm vượt',
            34: 'Biển báo Hết hạn chế tốc độ tối đa',
            35: 'Biển báo Hết tất cả các lệnh cấm',
            36: 'Biển báo Kiểm tra',
            37: 'Biển báo Nhường đường cho xe cơ giới đi ngược chiều qua đường hẹp',
            38: 'Biển báo Tốc độ tối đa cho phép vào ban đêm',
            39: 'Biển báo Tốc độ tối đa cho phép',
            40: 'Biển cấm chuyên chở hàng nguy hiểm vào',
            41: 'Biển cấm ô tô',
            42: 'Biển cấm oto rẻ phải',
            43: 'Biển cấm oto rẻ trái',
            44: 'Biển cấm xe máy và oto',
            45: 'Biển cấm xe máy',
            46: 'Biển cấm xe tải chuyên chở trọng tải lớn hơn giá trị ghi trên biển báo',
            47: 'Biển cấm xe tải',
            48: 'Cấm các loại máy kéo',
            49: 'Cấm các loại xe cơ giới kéo',
            50: 'Cấm các loại xe ô tô chở khách, xe tải, xe máy kéo, xe máy thi công chuyên dụng đi vào (trừ xe ưu tiên theo quy định)',
            51: 'Cấm xe đạp thô',
            52: 'Bắt đầu đường ưu tiên',
            53: 'Bắt đầu khu đông dân cư',
            54: 'Bến xe buýt',
            55: 'Bệnh viện',
            56: 'Cầu vượt qua đường cho người đi bộ 1',
            57: 'Cầu vượt qua đường cho người đi bộ 2',
            58: 'Chỗ quay xe',
            59: 'Được ưu tiên qua đường hẹp',
            60: 'Đường có làn đường dành cho ô tô khách',
            61: 'Đường cụt 1',
            62: 'Đường cụt 2',
            63: 'Đường cụt 3',
            64: 'Đường dành cho ô tô, xe máy',
            65: 'Đường dành cho ôtô',
            66: 'Đường một chiều 1',
            67: 'Đường một chiều 2',
            68: 'Đường một chiều 3',
            69: 'Đường người đi bộ sang ngang 1',
            70: 'Đường người đi bộ sang ngang 2',
            71: 'Hầm chui qua đường cho người đi bộ 1',
            72: 'Hầm chui qua đường cho người đi bộ 2',
            73: 'Hết đoạn đường ưu tiên',
            74: 'Hết đường dành cho ô tô, xe máy',
            75: 'Hết đường dành cho ô tô',
            76: 'Hết khu đông dân cư',
            77: 'Hướng đi trên mỗi làn đường theo vạch kẻ đường',
            78: 'Khu vực quay xe',
            79: 'Làn đường dành cho ôtô con',
            80: 'Làn đường dành cho ôtô khách',
            81: 'Làn đường dành cho ôtô tải',
            82: 'Làn đường dành cho xe môtô',
            83: 'Nơi đỗ xe',
            84: 'Trạm cảnh sát giao thông',
            85: 'Trạm cấp cứu',
            86: 'Trạm cung cấp xăng dầu',
            87: 'Ấn còi',
            88: 'Chỉ được đi thẳng và rẽ phải',
            89: 'Chỉ được đi thẳng và rẽ trái',
            90: 'Chỉ được rẽ phải và trái',
            91: 'Chỉ được rẽ phải',
            92: 'Chỉ được rẽ trái',
            93: 'Đường dành cho người đi bộ',
            94: 'Đường dành cho xe thô sơ',
            95: 'Hết hạn tốc độ tối thiểu',
            96: 'Hướng đi phải phải theo',
            97: 'Hướng đi phải theo cho các xe chở hàng nguy hiểm 2',
            98: 'Hướng đi phải theo cho các xe chở hàng nguy hiểm 3',
            99: 'Hướng đi phải theo cho các xe chở hàng nguy hiểm',
            100: 'Hướng đi phải theo',
            101: 'Hướng đi trái phải theo',
            102: 'Hướng phải đi vòng sang phải',
            103: 'Hướng phải đi vòng sang trái',
            104: 'Tốc độ tối thiểu',
            105: 'Tuyến đường cầu vượt cắt qua',
            106: 'Tuyến đường cầu vượt cắt qua 2',
            107: 'vòng xuyến',
            108: 'Bến phà',
            109: 'Cầu hẹp',
            110: 'Cầu tạm',
            111: 'Cầu vồng',
            112: 'Cầu xoay cầu cất',
            113: 'Chổ ngoặt nguy hiểm vòng bên phải',
            114: 'Chổ ngoặt nguy hiểm vòng bên trái',
            115: 'Chướng ngại vật 2',
            116: 'Chướng ngại vật',
            117: 'Chướng ngại vật 1',
            118: 'Công trường',
            119: 'Cửa chui',
            120: 'Đi chậm',
            121: 'Đoạn đường hay xảy ra tai nạn',
            122: 'Đường hẹp trái',
            123: 'Đường bị hẹp',
            124: 'Đường cao tốc phía trước',
            125: 'Đường cáp điện phía trên',
            126: 'Đường đôi',
            127: 'Đường giao nhau 4',
            128: 'Đường giao nhau',
            129: 'Đường giao nhau 1',
            130: 'Đường giao nhau 2',
            131: 'Đường giao nhau 3',
            132: 'Đường hai chiều',
            133: 'Đường hầm',
            134: 'Đường hẹp phải',
            135: 'Đường không bằng phẳng',
            136: 'Đường ngắn',
            137: 'Đường người đi xe đạp cắt ngang',
            138: 'Đường trơn',
            139: 'Gia súc',
            140: 'Giải máy bay lên xuống',
            141: 'Giao nhau chạy theo vòng xuyến',
            142: 'Giao nhau có tín hiệu đèn',
            143: 'giao nhau đường sắt',
            144: 'Giao nhau với đường hai chiều',
            145: 'Giao nhau với đường không ưu tiên 1',
            146: 'Giao nhau với đường không ưu tiên 2',
            147: 'Giao nhau với đường không ưu tiên 5',
            148: 'Giao nhau với đường không ưu tiên 6',
            149: 'Giao nhau với đường không ưu tiên 7',
            150: 'Giao nhau với đường không ưu tiên',
            151: 'Giao nhau với đường sắt có rào chắn',
            152: 'Giao nhau với đường sắt không có rào chắn',
            153: 'Giao nhau với đường ưu tiên',
            154: 'Gió ngang',
            155: 'Hết đường đôi',
            156: 'Kè, vực sâu phía trước',
            157: 'Lề đường nguy hiểm',
            158: 'Người đi bộ cắt ngang',
            159: 'Nguy hiểm khác',
            160: 'Nhiều chỗ ngoặt nguy hiểm liên tiếp 1',
            161: 'Nhiều chỗ ngoặt nguy hiểm liên tiếp 2',
            162: 'Sỏi đá bắn lên',
            163: 'Thú rừng vượt qua đường',
            164: 'Trẻ em',
            165: 'Ùn tắc giao thông',
            166: 'Hướng đường ưu tiên 1',
            167: 'Hướng đường ưu tiên 2',
            168: 'Hướng rẽ',
            169: 'Hướng tác dụng của biển',
            170: 'Khoảng cách đến đối tượng báo hiệu',
            171: 'Loại xe',
            172: 'Phạm vi tác dụng của biển',
            173: 'Thuyết minh biển chính 1'
}
class Ui_MainWindow(object):
    listBienBao=[]
    imgPath=""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(986, 713)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widgetTieuDe = QtWidgets.QWidget(self.centralwidget)
        self.widgetTieuDe.setGeometry(QtCore.QRect(0, 0, 991, 121))
        font = QtGui.QFont()
        font.setKerning(True)
        self.widgetTieuDe.setFont(font)
        self.widgetTieuDe.setAutoFillBackground(False)
        self.widgetTieuDe.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.widgetTieuDe.setObjectName("widgetTieuDe")
        self.lb_AnhTD = QtWidgets.QLabel(self.widgetTieuDe)
        self.lb_AnhTD.setGeometry(QtCore.QRect(-6, 0, 201, 121))
        self.lb_AnhTD.setText("")
        self.lb_AnhTD.setPixmap(QtGui.QPixmap("../anh/logoduongboVN.jpg"))
        self.lb_AnhTD.setScaledContents(True)
        self.lb_AnhTD.setObjectName("lb_AnhTD")
        self.lb_tieude = QtWidgets.QLabel(self.widgetTieuDe)
        self.lb_tieude.setGeometry(QtCore.QRect(270, 20, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.lb_tieude.setFont(font)
        self.lb_tieude.setStyleSheet("color: rgb(255, 0, 0);")
        self.lb_tieude.setObjectName("lb_tieude")
        self.lb_tenBien = QtWidgets.QLabel(self.centralwidget)
        self.lb_tenBien.setGeometry(QtCore.QRect(120, 420, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tenBien.setFont(font)
        self.lb_tenBien.setObjectName("lb_tenBien")
        self.lb_YNghia = QtWidgets.QLabel(self.centralwidget)
        self.lb_YNghia.setGeometry(QtCore.QRect(120, 490, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_YNghia.setFont(font)
        self.lb_YNghia.setObjectName("lb_YNghia")
        self.lb_Anh = QtWidgets.QLabel(self.centralwidget)
        self.lb_Anh.setGeometry(QtCore.QRect(120, 200, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_Anh.setFont(font)
        self.lb_Anh.setObjectName("lb_Anh")
        self.lb_ChuaAnh = QtWidgets.QLabel(self.centralwidget)
        self.lb_ChuaAnh.setGeometry(QtCore.QRect(310, 130, 200, 200))
        self.lb_ChuaAnh.setStyleSheet("border: 1px solid #000000;")
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lb_ChuaAnh.setFont(font)
        self.lb_ChuaAnh.setText("")
        self.lb_ChuaAnh.setObjectName("lb_ChuaAnh")
        self.bt_chonAnh = QtWidgets.QPushButton(self.centralwidget)
        self.bt_chonAnh.setGeometry(QtCore.QRect(610, 210, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_chonAnh.setFont(font)
        self.bt_chonAnh.setObjectName("bt_chonAnh")
        self.bt_nhanDang = QtWidgets.QPushButton(self.centralwidget)
        self.bt_nhanDang.setGeometry(QtCore.QRect(610, 270, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_nhanDang.setFont(font)
        self.bt_nhanDang.setObjectName("bt_nhanDang")
        self.bt_camera = QtWidgets.QPushButton(self.centralwidget)
        self.bt_camera.setGeometry(QtCore.QRect(280, 350, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_camera.setFont(font)
        self.bt_camera.setObjectName("bt_camera")
        self.lb_tenBien_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.lb_tenBien_2.setGeometry(QtCore.QRect(270, 420, 550, 55))
        self.lb_tenBien_2.setStyleSheet("border: 1px solid #000000;")
        self.lb_tenBien_2.setStyleSheet("background-color: #ffffff; font-family: Arial; font-size: 13pt; font-weight: bold;")
        self.lb_tenBien_2.setObjectName("lb_tenBien_2")
        self.lb_tenBien_2.setReadOnly(True)
        self.lb_yNghia = QtWidgets.QTextEdit(self.centralwidget)
        self.lb_yNghia.setReadOnly(True)# vô hiệu hóa QtextEdit
        self.lb_yNghia.setGeometry(QtCore.QRect(270, 489, 550, 55))
        self.lb_yNghia.setStyleSheet("border: 1px solid #000000;")
        self.lb_yNghia.setStyleSheet("background-color: #ffffff; font-family: Arial; font-size: 12pt; font-weight: bold;")
        self.lb_yNghia.setObjectName("lb_yNghia")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 986, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pic_cam_folder = 'pic_cam'
        if not os.path.exists(self.pic_cam_folder):
            os.makedirs(self.pic_cam_folder)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.bt_chonAnh.clicked.connect(self.chon_anh)
        self.bt_nhanDang.clicked.connect(self.show_classify_button)
        self.getAllBB()
        self.bt_camera.clicked.connect(self.classify_from_camera)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hệ thống quản lí biển báo giao thông"))
        self.lb_tieude.setText(_translate("MainWindow", "Tra cứu biển báo giao thông bằng hình ảnh"))
        self.lb_tenBien.setText(_translate("MainWindow", "Đây là biển:"))
        self.lb_YNghia.setText(_translate("MainWindow", "Ý nghĩa:"))
        self.lb_Anh.setText(_translate("MainWindow", "Ảnh"))
        self.bt_chonAnh.setText(_translate("MainWindow", "Chọn ảnh"))
        self.bt_nhanDang.setText(_translate("MainWindow", "Nhận dạng"))
        self.bt_camera.setText(_translate("MainWindow", "Mở camera và nhận dạng"))
    def getAllBB(self):
        try:
            conn = mysql.connector.connect(user='root', password='123456789', host='localhost', database='doan_py')
            query = "SELECT * FROM bienbaophu"
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                tenBien, yNghia, imgPath = row
                bb = bienBao_DTO.bienbao(tenBien, yNghia, imgPath)
                self.listBienBao.append(bb)
            query = "SELECT * FROM bienbaocam"
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                tenBien, ynghia, imgPath = row
                bb = bienBao_DTO.bienbao(tenBien, ynghia, imgPath)
                self.listBienBao.append(bb)
            query2 = "SELECT * FROM bienbaonguyhiem"
            cursor2 = conn.cursor()
            cursor2.execute(query2)
            rows2 = cursor.fetchall()
            for row2 in rows2:
                tenBien2, yNghia2, imgPath2 = row2
                bb2 = bienBao_DTO.bienbao(tenBien2, yNghia2, imgPath2)
                self.listBienBao.append(bb2)
            query3 = "SELECT * FROM bienbaochidan"
            cursor3 = conn.cursor()
            cursor3.execute(query3)
            rows3 = cursor3.fetchall()
            for row3 in rows3:
                tenBien3, yNghia3, imgPath3 = row3
                bb3 = bienBao_DTO.bienbao(tenBien3, yNghia3, imgPath3)
                self.listBienBao.append(bb3)
            query4 = "SELECT * FROM bienbaohieulenh"
            cursor4 = conn.cursor()
            cursor4.execute(query4)
            rows4 = cursor4.fetchall()
            for row4 in rows4:
                tenBien4, yNghia4, imgPath4 = row4
                bb4 = bienBao_DTO.bienbao(tenBien4, yNghia4, imgPath4)
                self.listBienBao.append(bb4)
        except mysql.connector.Error as error:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Kết nối mysql thất bại {}".format(error))
    def layYNghia(self,ten):
        for bb in self.listBienBao:
            ten_bien_1 = bb.get_tenBien().lower()
            ten_bien_2 = ten.lower()  # Chuyển biến ten thành chữ thường
            if ten_bien_1==ten_bien_2:
                return bb.get_yNghia()
        return ""
    def chon_anh(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
        file_dialog.setViewMode(QFileDialog.Detail)
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                image_path = selected_files[0]
                self.imgPath=image_path
                pixmap = QtGui.QPixmap(image_path)
                scaled_pixmap = pixmap.scaled(450, 120, 200, 200)
                self.lb_ChuaAnh.setPixmap(scaled_pixmap)
                self.lb_ChuaAnh.setScaledContents(True)  # Cài đặt thuộc tính scaledContents để tự động điều chỉnh kích thước của hình ảnh
    #test ảnh
    def classify(self,file_path):
        try:
            # Thêm code để thêm kênh alpha vào ảnh
            def add_alpha_channel(image_path):
                image = Image.open(image_path)
                new_image = Image.new("RGBA", image.size)
                new_image.paste(image, (0, 0))
                return new_image

            image_with_alpha = add_alpha_channel(file_path)
            # Thực hiện resize ảnh và chuyển đổi thành numpy array
            image_with_alpha = image_with_alpha.resize((50, 50))
            image_with_alpha = np.array(image_with_alpha)
            image_with_alpha = np.expand_dims(image_with_alpha, axis=0)

            pred_probabilities = model.predict(image_with_alpha)[0]
            pred = pred_probabilities.argmax(axis=-1)
            sign = classes[pred + 1]
            self.lb_tenBien_2.setText(sign)
            self.lb_yNghia.setText(self.layYNghia(sign))
        except Exception as e:
            self.lb_tenBien.configure(foreground='#FF0000', text="Lỗi xảy ra, không thể dự đoán.")


    def show_classify_button(self):
        if(self.imgPath==""):
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Vui lòng chọn ảnh để kiểm tra")
        else:
            self.classify(self.imgPath)

    def classify_from_camera(self):
        try:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Thông báo", "Bấm phím C để chụp và phím Space để bất đầu nhận dạng khi chọn khung ảnh xong")
            cap = cv2.VideoCapture(0)

            # Set the desired width and height for the camera window
            cap.set(3, 300)  # Width
            cap.set(4, 300)  # Height

            temp_image_path = os.path.join(self.pic_cam_folder, f"temp_image_{int(time.time())}.jpg")  # Temporary image path
            while True:
                ret, frame = cap.read()
                cv2.imshow('Camera', frame)

                key = cv2.waitKey(1) & 0xFF
                if key == ord('c'):
                    cv2.imwrite(temp_image_path, frame)
                    cap.release()
                    cv2.destroyAllWindows()

                    # Open the image again to display a frame for selection
                    image = cv2.imread(temp_image_path)
                    clone = image.copy()
                    cv2.namedWindow("Select Region")
                    rect = cv2.selectROI("Select Region", clone, fromCenter=False, showCrosshair=True)
                    cv2.destroyWindow("Select Region")

                    # Crop the selected region
                    x, y, w, h = rect
                    cropped_image = image[y:y + h, x:x + w]

                    # Save the cropped image
                    cropped_image_path = os.path.join(self.pic_cam_folder, f"cropped_image_{int(time.time())}.jpg")
                    # self.imgPath=cropped_image_path
                    cv2.imwrite(cropped_image_path, cropped_image)

                    # Display the cropped image on a Label

                    uploaded = QtGui.QPixmap(cropped_image_path)
                    scaled_uploaded=uploaded.scaled(450,120,200,200)

                    self.lb_ChuaAnh.setPixmap(scaled_uploaded)
                    self.lb_ChuaAnh.setScaledContents(True)

                    # Call classify function after selecting and cropping the region
                    self.imgPath="D:/vietcpp/.vscode/doan_py/GUI/"+cropped_image_path
                    # print(self.imgPath)
                    self.classify(self.imgPath)
                    break

            if cap.isOpened():
                cap.release()
        except Exception as e:
            print("Error:", e)
            self.lb_tenBien.configure(foreground='#FF0000', text="Lỗi xảy ra khi sử dụng camera.")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

