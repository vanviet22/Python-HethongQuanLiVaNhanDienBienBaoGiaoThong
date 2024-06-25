
from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk
from PyQt5.QtWidgets import QFileDialog,QTableWidgetItem
import formNguyHiem_CC
import mysql.connector
import  os
import bienBao_DTO


class Ui_MainWindow(object):
    listBBNH = []
    imgPath = ""
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
        self.widgetTieuDe.setAutoFillBackground(True)
        self.widgetTieuDe.setObjectName("widgetTieuDe")
        self.lb_AnhTD = QtWidgets.QLabel(self.widgetTieuDe)
        self.lb_AnhTD.setGeometry(QtCore.QRect(0, 0, 191, 121))
        self.lb_AnhTD.setText("")
        self.lb_AnhTD.setPixmap(QtGui.QPixmap("../anh/logoduongboVN.jpg"))
        self.widgetTieuDe.setStyleSheet("background-color:  rgb(107, 255, 176);")
        self.lb_AnhTD.setScaledContents(True)
        self.lb_AnhTD.setObjectName("lb_AnhTD")
        self.lb_tieudeBP = QtWidgets.QLabel(self.widgetTieuDe)
        self.lb_tieudeBP.setGeometry(QtCore.QRect(380, 20, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.lb_tieudeBP.setFont(font)
        self.lb_tieudeBP.setObjectName("lb_tieudeBP")
        
        self.tableBienPhu = QtWidgets.QTableWidget(self.centralwidget)
        self.tableBienPhu.setGeometry(QtCore.QRect(35, 260, 911, 391))
        self.tableBienPhu.setObjectName("tableBienPhu")
        self.tableBienPhu.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableBienPhu.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBienPhu.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBienPhu.setHorizontalHeaderItem(2, item)
        self.tableBienPhu.horizontalHeader().setDefaultSectionSize(293)
        MainWindow.setCentralWidget(self.centralwidget)
        # Đặt chiều cao của hàng
        self.tableBienPhu.verticalHeader().setDefaultSectionSize(150)
        self.tableBienPhu.setColumnWidth(0, 150)
        self.tableBienPhu.setColumnWidth(1, 350)
        self.tableBienPhu.setColumnWidth(2, 400)
        
        self.lb_tenBP = QtWidgets.QLabel(self.centralwidget)
        self.lb_tenBP.setGeometry(QtCore.QRect(80, 140, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tenBP.setFont(font)
        self.lb_tenBP.setObjectName("lb_tenBP")
        self.tx_tenBP = QtWidgets.QTextEdit(self.centralwidget)
        self.tx_tenBP.setGeometry(QtCore.QRect(180, 140, 481, 31))
        self.tx_tenBP.setObjectName("tx_tenBP")
        self.lb_AnhBP = QtWidgets.QLabel(self.centralwidget)
        self.lb_AnhBP.setGeometry(QtCore.QRect(680, 170, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_AnhBP.setFont(font)
        self.lb_AnhBP.setObjectName("lb_AnhBP")
        self.lb_AnhChuaBP = QtWidgets.QLabel(self.centralwidget)
        self.lb_AnhChuaBP.setGeometry(QtCore.QRect(720, 140, 151, 111))
        self.lb_AnhChuaBP.setStyleSheet("border: 1px solid #000000;")
        self.lb_AnhChuaBP.setText("")
        self.lb_AnhChuaBP.setObjectName("lb_AnhChuaBP")
        self.bt_layAnhBP = QtWidgets.QPushButton(self.centralwidget)
        self.bt_layAnhBP.setGeometry(QtCore.QRect(880, 150, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_layAnhBP.setFont(font)
        self.bt_layAnhBP.setObjectName("bt_layAnhBP")
        self.lb_yNghiaBP = QtWidgets.QLabel(self.centralwidget)
        self.lb_yNghiaBP.setGeometry(QtCore.QRect(80, 185, 81, 55))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_yNghiaBP.setFont(font)
        self.lb_yNghiaBP.setObjectName("lb_yNghiaBP")
        self.tx_yNghiaBP = QtWidgets.QTextEdit(self.centralwidget)
        self.tx_yNghiaBP.setGeometry(QtCore.QRect(180, 200, 481, 35))
        self.tx_yNghiaBP.setObjectName("tx_yNghiaBP")
        self.bt_Them = QtWidgets.QPushButton(self.centralwidget)
        self.bt_Them.setGeometry(QtCore.QRect(880, 190, 30, 30))
        self.bt_Them.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../anh/icons8-add-27.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_Them.setIcon(icon)
        self.bt_Them.setIconSize(QtCore.QSize(25, 25))
        self.bt_Them.setObjectName("bt_Them")
        self.bt_Sua = QtWidgets.QPushButton(self.centralwidget)
        self.bt_Sua.setGeometry(QtCore.QRect(910, 190, 30, 30))
        self.bt_Sua.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../anh/icons8-update-left-rotation-27.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_Sua.setIcon(icon1)
        self.bt_Sua.setIconSize(QtCore.QSize(25, 25))
        self.bt_Sua.setObjectName("bt_Sua")
        self.bt_Xoa = QtWidgets.QPushButton(self.centralwidget)
        self.bt_Xoa.setGeometry(QtCore.QRect(940, 190, 30, 30))
        self.bt_Xoa.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../anh/Button-Delete-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_Xoa.setIcon(icon2)
        self.bt_Xoa.setIconSize(QtCore.QSize(25, 25))
        self.bt_Xoa.setObjectName("bt_Xoa")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 986, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.bt_layAnhBP.clicked.connect(self.chon_anh)
        self.hienThi()
        self.bt_Them.clicked.connect(self.them)
        self.tableBienPhu.itemClicked.connect(self.tableClick)
        self.bt_Sua.clicked.connect(self.sua)
        self.bt_Xoa.clicked.connect(self.xoa)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lb_tieudeBP.setText(_translate("MainWindow", "Quản lí biển phụ"))
        item = self.tableBienPhu.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ảnh"))
        item = self.tableBienPhu.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên biển"))
        item = self.tableBienPhu.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ý nghĩa"))
        self.lb_tenBP.setText(_translate("MainWindow", "Tên biển"))
        self.lb_AnhBP.setText(_translate("MainWindow", "Ảnh"))
        self.bt_layAnhBP.setText(_translate("MainWindow", "Chọn ảnh"))
        self.lb_yNghiaBP.setText(_translate("MainWindow", "Ý nghĩa"))

    def chon_anh(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
        file_dialog.setViewMode(QFileDialog.Detail)
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                image_path = selected_files[0]
                self.imgPath = image_path
                pixmap = QtGui.QPixmap(image_path)
                scaled_pixmap = pixmap.scaled(490, 140, 151, 111)
                self.lb_AnhChuaBP.setPixmap(scaled_pixmap)
                self.lb_AnhChuaBP.setScaledContents(True)  # Cài đặt thuộc tính scaledContents để tự động điều chỉnh kích thước của hình ảnh

    def hienThi(self):
        try:
            conn = mysql.connector.connect(user='root', password='123456789', host='localhost', database='doan_py')
            query = "SELECT * FROM bienbaophu"
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                tenBien, yNghia, imgPath = row
                bb = bienBao_DTO.bienbao(tenBien, yNghia, imgPath)
                self.listBBNH.append(bb)

            if(len(self.listBBNH) > 0):
                for row_index, bb in enumerate(self.listBBNH):
                    self.tableBienPhu.insertRow(row_index)

                    #anh
                    pixmap = QtGui.QPixmap("../anh/imgBienBao/" + bb.get_imgPath()).scaled(150,150)
                    img_item = QTableWidgetItem()
                    img_item.setData(QtCore.Qt.DecorationRole, pixmap)
                    self.tableBienPhu.setItem(row_index, 0, img_item)

                    #ten
                    name_item = QTableWidgetItem(bb.get_tenBien())
                    self.tableBienPhu.setItem(row_index, 1, name_item)

                    #mieuta
                    self.tableBienPhu.setItem(row_index, 2, QTableWidgetItem(bb.get_yNghia()))
        except mysql.connector.Error as error:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Kết nối mysql thất bại {}".format(error))

    def checkTenBien(self, ten):
        for bb in self.listBBNH:
            if (bb.get_tenBien() == ten):
                return False
        return True

    def them(self):
        if self.tx_tenBP.toPlainText() == "":
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Vui lòng nhập tên biển báo")
            self.tx_tenBP.setFocus()
        elif self.tx_yNghiaBP.toPlainText() == "":
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Vui lòng nhập ý nghĩa của biển báo")
            self.tx_yNghiaBP.setFocus()
        elif self.imgPath == "":
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Vui lòng chọn ảnh")
        elif self.checkTenBien(self.tx_tenBP.toPlainText()) != True:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Tên biển báo đã có trong hệ thống!! Vui lòng nhập tên khác")
            self.tx_tenBP.setText("")
            self.tx_tenBP.setFocus()
        else:
            file_name = os.path.basename(self.imgPath)
            self.imgPath = ""
            bb = bienBao_DTO.bienbao(self.tx_tenBP.toPlainText(), self.tx_yNghiaBP.toPlainText(), file_name)
            self.listBBNH.append(bb)
            sohang = self.tableBienPhu.rowCount()
            self.tableBienPhu.insertRow(sohang)

            #anh
            pixmap = QtGui.QPixmap("../anh/imgBienBao/" + bb.get_imgPath()).scaled(150,150)
            img_item = QTableWidgetItem()
            img_item.setData(QtCore.Qt.DecorationRole, pixmap)
            self.tableBienPhu.setItem(sohang, 0, img_item)

            #ten va ynghia
            self.tableBienPhu.setItem(sohang, 1, QTableWidgetItem(bb.get_tenBien()))
            self.tableBienPhu.setItem(sohang, 2, QTableWidgetItem(bb.get_yNghia()))

            try:
                conn =mysql.connector.connect(user = 'root', password = '123456789', host='localhost', database='doan_py')
                cursor = conn.cursor()
                sql = "INSERT INTO bienbaophu (Ten_BienBaoPhu,Mieuta,HinhAnhBBP) VALUES (%s,%s,%s)"
                val = (bb.get_tenBien(), bb.get_yNghia(), bb.get_imgPath())
                cursor.execute(sql, val)
                conn.commit()
                self.tx_tenBP.setText("")
                self.tx_yNghiaBP.setText("")
                self.lb_AnhChuaBP.setPixmap(QtGui.QPixmap())
                QtWidgets.QMessageBox.warning(self.centralwidget, "Thành công", "thêm biển báo mới thành công")
            except mysql.connector.Error as error:
                QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Lỗi khi thêm dữ liệu vào MySQL: {}".format(error))
            finally:
                # Đóng kết nối
                if conn.is_connected():
                    cursor.close()
                    conn.close()

    def tableClick(self, item):
        row = item.row()
        if row >= 0 and row < len(self.listBBNH):
            ten_bien = self.tableBienPhu.item(row, 1).text()
            self.tx_tenBP.setText(ten_bien)
            yNghia = self.tableBienPhu.item(row, 2).text()
            self.tx_yNghiaBP.setText(yNghia)

            img_item = self.tableBienPhu.item(row, 0)
            if img_item is not None:
                pixmap = img_item.data(QtCore.Qt.DecorationRole)
                if not pixmap.isNull():
                    scaled_pixmap = pixmap.scaled(490,140,151,111)
                    self.lb_AnhChuaBP.setPixmap(scaled_pixmap)
                    self.lb_AnhChuaBP.setScaledContents(True)

    def sua(self):
        selected_row = self.tableBienPhu.currentRow()
        tenBien_old = self.listBBNH[selected_row].get_tenBien()
        if selected_row >=0 and selected_row < len(self.listBBNH):
            if self.tx_tenBP.toPlainText() == "":
                QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Hãy nhập tên biển báo")
                self.tx_tenBP.setFocus()
            elif tenBien_old != self.tx_tenBP.toPlainText() and self.checkTenBien(self.tx_tenBP.toPlainText()) != True:
                QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi","Tên biển báo đã có trong hệ thống vui lòng kiểm tra lại")
                self.tx_tenBP.setText("")
                self.tx_tenBP.setFocus()
            elif self.tx_yNghiaBP.toPlainText() == "":
                QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Hãy nhập ý nghãi của biển báo đó")
                self.tx_yNghiaBP.setFocus()
            else:
                tenbien = self.tx_tenBP.toPlainText()
                yNghia = self.tx_yNghiaBP.toPlainText()
                img_path = self.listBBNH[selected_row].get_imgPath()

                #Cap nhat du lieu trong bang
                self.tableBienPhu.setItem(selected_row, 1, QTableWidgetItem(tenbien))
                self.tableBienPhu.setItem(selected_row, 2, QTableWidgetItem(yNghia))
                if self.imgPath != "":
                    img_path = os.path.basename(self.imgPath)
                    self.imgPath = ""
                pixmap = QtGui.QPixmap("../anh/imgBienBao/" + img_path).scaled(150,150)
                image_item = QTableWidgetItem()
                image_item.setData(QtCore.Qt.DecorationRole, pixmap)
                self.tableBienPhu.setItem(selected_row, 0, image_item)

                #cap nhat mysql
                try:
                    conn = mysql.connector.connect(user='root', password='123456789', host='localhost', database='doan_py')
                    cursor = conn.cursor()
                    sql = "UPDATE bienbaophu SET Ten_BienBaoPhu = %s, Mieuta = %s, HinhAnhBBP = %s WHERE Ten_BienBaoPhu = %s"
                    val = (tenbien, yNghia, img_path, self.listBBNH[selected_row].get_tenBien())
                    cursor.execute(sql, val)
                    conn.commit()
                    self.tx_tenBP.setText("")
                    self.tx_yNghiaBP.setText("")
                    self.lb_AnhChuaBP.setPixmap(QtGui.QPixmap())
                    QtWidgets.QMessageBox.information(self.centralwidget, "Thành công","Đã cập nhật thông tin thành công")
                except mysql.connector.Error as error:
                    QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Lỗi khi cập nhật dữ liệu trong MySQL: {}".format(error))
                finally:
                    if conn.is_connected():
                        cursor.close()
                        conn.close()

                # cập nhật dữ liệu trong list
                self.listBBNH[selected_row].set_imgPath(img_path)
                self.listBBNH[selected_row].set_tenBien(tenbien)
                self.listBBNH[selected_row].set_yNghia(yNghia)
        else:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Chọn hàng cần sửa")
    def xoa(self):
        selected_row = self.tableBienPhu.currentRow()
        if selected_row >= 0 and selected_row < len(self.listBBNH):

            #xoa dong khoi bang hien thi
            self.tableBienPhu.removeRow(selected_row)

            #xoa mysql
            try:
                conn = mysql.connector.connect(user='root', password='123456789', host='localhost', database='doan_py')
                cursor = conn.cursor()
                sql = "DELETE FROM bienbaophu WHERE Ten_BienBaoPhu = %s"
                val = (self.listBBNH[selected_row].get_tenBien(),)
                cursor.execute(sql, val)
                conn.commit()
                QtWidgets.QMessageBox.information(self.centralwidget, "Thành công", "Đã xóa thành công")


            except mysql.connector.Error as error:
                QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Lỗi khi xóa dữ liệu trong MySQL: {}".format(error))

            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()
            # Sau khi xóa, cập nhật lại listBBCD
            del self.listBBNH[selected_row]
            self.tx_tenBP.setText("")
            self.tx_yNghiaBP.setText("")
            self.lb_AnhChuaBP.setPixmap(QtGui.QPixmap())
        else:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Chọn hàng cần xoa")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())