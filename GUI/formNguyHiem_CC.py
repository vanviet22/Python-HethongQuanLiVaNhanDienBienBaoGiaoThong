import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog

import  bienBao_DTO
import mysql.connector

class Ui_MainWindow(object):
    listBienBaoNH=[]
    imagePath=""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(986, 713)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widgetTieuDe = QtWidgets.QWidget(self.centralwidget)
        self.widgetTieuDe.setStyleSheet("background-color:#FFECB3;")
        self.widgetTieuDe.setGeometry(QtCore.QRect(0, 0, 991, 121))
        font = QtGui.QFont()
        font.setKerning(True)
        self.widgetTieuDe.setFont(font)
        self.widgetTieuDe.setAutoFillBackground(True)
        self.widgetTieuDe.setObjectName("widgetTieuDe")
        self.lb_AnhTD = QtWidgets.QLabel(self.widgetTieuDe)
        self.lb_AnhTD.setGeometry(QtCore.QRect(-6, 0, 201, 121))
        self.lb_AnhTD.setText("")
        self.lb_AnhTD.setPixmap(QtGui.QPixmap("../anh/logoduongboVN.jpg"))
        self.lb_AnhTD.setScaledContents(True)
        self.lb_AnhTD.setObjectName("lb_AnhTD")
        self.label = QtWidgets.QLabel(self.widgetTieuDe)
        self.label.setGeometry(QtCore.QRect(360, 20, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lb_tenBienCD = QtWidgets.QLabel(self.centralwidget)
        self.lb_tenBienCD.setGeometry(QtCore.QRect(150, 160, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tenBienCD.setFont(font)
        self.lb_tenBienCD.setObjectName("lb_tenBienCD")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(240, 160, 481, 31))
        self.textEdit.setObjectName("textEdit")
        self.lb_YNghia = QtWidgets.QLabel(self.centralwidget)
        self.lb_YNghia.setGeometry(QtCore.QRect(150, 210, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_YNghia.setFont(font)
        self.lb_YNghia.setObjectName("lb_YNghia")
        self.txYNghia = QtWidgets.QTextEdit(self.centralwidget)
        self.txYNghia.setGeometry(QtCore.QRect(240, 210, 481, 35))
        self.txYNghia.setObjectName("txYNghia")
        self.lb_AnhCD = QtWidgets.QLabel(self.centralwidget)
        self.lb_AnhCD.setGeometry(QtCore.QRect(150, 280, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_AnhCD.setFont(font)
        self.lb_AnhCD.setObjectName("lb_AnhCD")
        self.lb_ChuaAnh = QtWidgets.QLabel(self.centralwidget)
        self.lb_ChuaAnh.setStyleSheet("border: 1px solid #000000;")
        self.lb_ChuaAnh.setGeometry(QtCore.QRect(240, 250, 151, 111))
        self.lb_ChuaAnh.setText("")
        self.lb_ChuaAnh.setObjectName("lb_ChuaAnh")
        self.bt_layAnhCD = QtWidgets.QPushButton(self.centralwidget)
        self.bt_layAnhCD.setGeometry(QtCore.QRect(420, 280, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_layAnhCD.setFont(font)
        self.bt_layAnhCD.setObjectName("bt_layAnhCD")
        self.bt_Them = QtWidgets.QPushButton(self.centralwidget)
        self.bt_Them.setGeometry(QtCore.QRect(760, 160, 30, 30))
        self.bt_Them.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../anh/icons8-add-27.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_Them.setIcon(icon)
        self.bt_Them.setIconSize(QtCore.QSize(25, 25))
        self.bt_Them.setObjectName("bt_Them")
        self.bt_Sua = QtWidgets.QPushButton(self.centralwidget)
        self.bt_Sua.setGeometry(QtCore.QRect(760, 210, 30, 30))
        self.bt_Sua.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../anh/icons8-update-left-rotation-27.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_Sua.setIcon(icon1)
        self.bt_Sua.setIconSize(QtCore.QSize(25, 25))
        self.bt_Sua.setObjectName("bt_Sua")
        self.bt_Xoa = QtWidgets.QPushButton(self.centralwidget)
        self.bt_Xoa.setGeometry(QtCore.QRect(820, 180, 30, 30))
        self.bt_Xoa.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../anh/Button-Delete-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_Xoa.setIcon(icon2)
        self.bt_Xoa.setIconSize(QtCore.QSize(25, 25))
        self.bt_Xoa.setObjectName("bt_Xoa")
        self.tableBienChiDan = QtWidgets.QTableWidget(self.centralwidget)
        self.tableBienChiDan.setGeometry(QtCore.QRect(40, 390, 941, 301))
        self.tableBienChiDan.setObjectName("tableBienChiDan")
        self.tableBienChiDan.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableBienChiDan.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBienChiDan.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBienChiDan.setHorizontalHeaderItem(2, item)
        self.tableBienChiDan.verticalHeader().setDefaultSectionSize(150)
        self.tableBienChiDan.setColumnWidth(0, 150)
        self.tableBienChiDan.setColumnWidth(1, 350)
        self.tableBienChiDan.setColumnWidth(2, 450)
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
        self.hienThiLenTable()
        self.bt_layAnhCD.clicked.connect(self.chonAnh)
        self.bt_Xoa.clicked.connect(self.xoaBienBao)
        self.bt_Sua.clicked.connect(self.suaBienBao)
        self.bt_Them.clicked.connect(self.themBienBao)
        self.tableBienChiDan.itemClicked.connect(self.tableClick)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hệ thống quản lí biển báo giao thông"))
        self.label.setText(_translate("MainWindow", "Quản lí biển báo nguy hiểm"))
        self.lb_tenBienCD.setText(_translate("MainWindow", "Tên biển"))
        self.lb_YNghia.setText(_translate("MainWindow", "Ý nghĩa"))
        self.lb_AnhCD.setText(_translate("MainWindow", "Ảnh"))
        self.bt_layAnhCD.setText(_translate("MainWindow", "Chọn ảnh"))
        item = self.tableBienChiDan.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ảnh"))
        item = self.tableBienChiDan.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên biển"))
        item = self.tableBienChiDan.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ý nghĩa"))

    def hienThiLenTable(self):
        try:
            connection = mysql.connector.connect(user = 'root', passwd = '123456789', host = 'localhost', database = 'doan_py')
            sql = "SELECT * FROM bienbaonguyhiem"
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                tenBienBao, yNghia, imgPath = row #gán giá trị từ tuple row cho các giá trị
                bienBaoNH = bienBao_DTO.bienbao(tenBienBao, yNghia, imgPath)
                self.listBienBaoNH.append(bienBaoNH)
            if(len(self.listBienBaoNH) > 0):
                for rowIndex, bienBao in enumerate(self.listBienBaoNH):

                     self.tableBienChiDan.insertRow(rowIndex)
                     pixmap = QtGui.QPixmap("../anh/imgBienBao/" + bienBao.get_imgPath()).scaled(150, 150)
                     image_item = QTableWidgetItem()
                     image_item.setData(QtCore.Qt.DecorationRole, pixmap)
                     self.tableBienChiDan.setItem(rowIndex, 0,image_item)
                     self.tableBienChiDan.setItem(rowIndex, 1, QtWidgets.QTableWidgetItem(bienBao.get_tenBien()))
                     self.tableBienChiDan.setItem(rowIndex, 2, QtWidgets.QTableWidgetItem(bienBao.get_yNghia()))
                # self.tableBienChiDan.insertRow(self.tableBienChiDan.rowCount())
        except mysql.connector.Error as error:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Kết nối mysql thất bại {}".format(error))
    def chonAnh(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
        file_dialog.setViewMode(QFileDialog.Detail)
        if (file_dialog.exec_()):
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                image_path = selected_files[0]
                self.imagePath = image_path
                pixmap = (QtGui.QPixmap(image_path)).scaled(490, 140, 151, 111)
                self.lb_ChuaAnh.setPixmap(pixmap)
                self.lb_ChuaAnh.setScaledContents(True)
    def kiemTraBien(self,tenBienBao):
        for bienBao in self.listBienBaoNH:
            if(tenBienBao == bienBao.get_tenBien() ):
                return False
        return True
    def themBienBao(self):
        if (self.textEdit.toPlainText() == ""):
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Vui lòng nhập tên biển báo")
            self.textEdit.setFocus()
        elif self.txYNghia.toPlainText() == "":
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi",
                                          "Vui lòng nhập ý nghĩa của  biển báo bạn muốn thêm")
            self.txYNghia.setFocus()
        elif self.imagePath== "":
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Vui lòng chọn ảnh biển báo ")
        elif (self.kiemTraBien(self.textEdit.toPlainText())) != True:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Biển báo đã tồn tại")
            self.txYNghia.setFocus()
        else:
            img_name = os.path.basename(self.imagePath)
            self.imagePath = ""
            bb = bienBao_DTO.bienbao(self.textEdit.toPlainText(), self.txYNghia.toPlainText(), img_name)
            self.listBienBaoNH.append(bb)
            soHang = self.tableBienChiDan.rowCount()
            self.tableBienChiDan.insertRow(soHang)
            # anh
            pixmap = QtGui.QPixmap("../anh/imgBienBao/" + bb.get_imgPath()).scaled(150, 150)
            image_item = QTableWidgetItem()
            image_item.setData(QtCore.Qt.DecorationRole, pixmap)
            self.tableBienChiDan.setItem(soHang, 0, image_item)
            # ten bien
            self.tableBienChiDan.setItem(soHang, 1, QTableWidgetItem(bb.get_tenBien()))
            # y nghia
            self.tableBienChiDan.setItem(soHang, 2, QTableWidgetItem(bb.get_yNghia()))
            try:
                connection = mysql.connector.connect(user = 'root', passwd = '123456789', host = 'localhost', database = 'doan_py')
                sql = "INSERT INTO bienbaonguyhiem(Ten_BienBaoNguyHiem, Mieuta, HinhAnhBBNH) VALUES (%s, %s, %s)"
                cursor = connection.cursor()
                cursor.execute(sql, (bb.get_tenBien(),bb.get_yNghia(),bb.get_imgPath()))
                connection.commit()
                self.textEdit.clear()
                self.txYNghia.clear()
                self.lb_ChuaAnh.clear()
                QtWidgets.QMessageBox.information(self.centralwidget, "Thành công", "Thêm phần tử mới thành công")
            except mysql.connector.Error as error:
                QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi","Lỗi khi thêm dữ liệu vào MySQL: {}".format(error))
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
    def suaBienBao(self):
        selected_row = self.tableBienChiDan.currentRow()
        if(selected_row >=0 and selected_row < len(self.listBienBaoNH)):
            tenBienBaoCu = self.listBienBaoNH[selected_row].get_tenBien()
            if self.textEdit.toPlainText() == "":
                QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Vui lòng nhập tên biển báo")
                self.textEdit.setFocus()
            elif self.txYNghia.toPlainText() == "":
                QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Vui lòng nhập ý nghĩa của biển báo")
                self.txYNghia.setFocus()
            elif (tenBienBaoCu != self.textEdit.toPlainText() and self.kiemTraBien(self.textEdit.toPlainText()) != True) :
                QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Biển báo này đã tồn tại")
                self.textEdit.setText("")
                self.textEdit.setFocus()
            else:
                tenBienBao = self.textEdit.toPlainText()
                yNghia = self.txYNghia.toPlainText()
                imgPath = self.listBienBaoNH[selected_row].get_imgPath()
                if(self.imagePath!=""):
                        imgPath=os.path.basename(self.imagePath)
                        self.imagePath=""
                self.tableBienChiDan.setItem(selected_row, 1, QTableWidgetItem(tenBienBao))
                self.tableBienChiDan.setItem(selected_row, 2, QTableWidgetItem(yNghia))
                pixmap = QtGui.QPixmap("../anh/imgBienBao/" + imgPath).scaled(150, 150)
                image_item = QTableWidgetItem()
                image_item.setData(QtCore.Qt.DecorationRole, pixmap)
                self.tableBienChiDan.setItem(selected_row, 0, image_item)
                try:
                    connection = mysql.connector.connect(user = 'root', passwd = '123456789', host = 'localhost', database = 'doan_py')
                    sql = "UPDATE bienbaonguyhiem SET Ten_BienBaoNguyHiem = %s, Mieuta = %s, HinhAnhBBNH = %s WHERE Ten_BienBaoNguyHiem = %s"
                    cursor = connection.cursor()
                    cursor.execute(sql, (tenBienBao,yNghia,imgPath,tenBienBaoCu))
                    connection.commit()
                    QtWidgets.QMessageBox.information(self.centralwidget, "Thành công", "Sửa phần tử thành công")
                except mysql.connector.Error as error:
                        QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Lỗi khi cập nhật dữ liệu trong MySQL: {}".format(error))
                finally:
                    if connection.is_connected():
                        cursor.close()
                        connection.close()
                self.listBienBaoNH[selected_row].set_imgPath(imgPath)
                self.listBienBaoNH[selected_row].set_tenBien(tenBienBao)
                self.listBienBaoNH[selected_row].set_yNghia(yNghia)
                self.textEdit.clear()
                self.txYNghia.clear()
                self.lb_ChuaAnh.clear()
        else:QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Chọn hàng cần sửa")
    def xoaBienBao(self):
        selected_row = self.tableBienChiDan.currentRow()
        if(selected_row >=0 and selected_row < len(self.listBienBaoNH)):
            self.tableBienChiDan.removeRow(selected_row)
            try:
                connection = mysql.connector.connect(user = 'root', passwd = '123456789', host = 'localhost', database = 'doan_py')
                sql = "DELETE FROM bienbaonguyhiem WHERE Ten_BienBaoNguyHiem = %s"
                curser = connection.cursor()
                val=( self.listBienBaoNH[selected_row].get_tenBien(),)
                curser.execute(sql,val)
                connection.commit()
                QtWidgets.QMessageBox.information(self.centralwidget, "Thành công", "Xóa phần tử thành công")
            except mysql.connector.Error as error:
                QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Lỗi khi xóa dữ liệu trong MySQL: {}".format(error))
            finally:
                if connection.is_connected():
                    curser.close()
                    connection.close()
            del self.listBienBaoNH[selected_row]
            self.textEdit.clear()
            self.txYNghia.clear()
            self.lb_ChuaAnh.clear()
        else:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Vui lòng chọn phần tử để xóa")
    def tableClick(self, item):
        row = item.row()
        if (row >= 0 and row < len(self.listBienBaoNH)):
            tenbien = self.tableBienChiDan.item(row, 1).text()
            self.textEdit.setText(tenbien)
            ynghia = self.tableBienChiDan.item(row, 2).text()
            self.txYNghia.setText(ynghia)
            img_item = self.tableBienChiDan.item(row, 0)
            if img_item is not None:
                pixmap = img_item.data(QtCore.Qt.DecorationRole)  # Lấy pixmap từ dữ liệu của ô
                if not pixmap.isNull():  # kiem tra pixmap
                    scaled_pixmap = pixmap.scaled(490, 140, 151, 111)
                    self.lb_ChuaAnh.setPixmap(scaled_pixmap)
                    self.lb_ChuaAnh.setScaledContents(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
