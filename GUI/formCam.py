from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog

import  bienBao_DTO
import mysql.connector
import  os
class Ui_MainWindow(object):
    dsBB=[]
    imgPath=""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(981, 713)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_tenBienCD = QtWidgets.QLabel(self.centralwidget)
        self.lb_tenBienCD.setGeometry(QtCore.QRect(230, 120, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tenBienCD.setFont(font)
        self.lb_tenBienCD.setObjectName("lb_tenBienCD")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(340, 120, 481, 31))
        self.textEdit.setObjectName("textEdit")
        self.bt_Them = QtWidgets.QPushButton(self.centralwidget)
        self.bt_Them.setGeometry(QtCore.QRect(680, 220, 30, 30))
        self.bt_Them.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../anh/icons8-add-27.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_Them.setIcon(icon)
        self.bt_Them.setIconSize(QtCore.QSize(25, 25))
        self.bt_Them.setObjectName("bt_Them")
        self.lb_AnhCD = QtWidgets.QLabel(self.centralwidget)
        self.lb_AnhCD.setGeometry(QtCore.QRect(230, 250, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_AnhCD.setFont(font)
        self.lb_AnhCD.setObjectName("lb_AnhCD")
        self.lb_ChuaAnh = QtWidgets.QLabel(self.centralwidget)
        self.lb_ChuaAnh.setGeometry(QtCore.QRect(340, 220, 151, 111))
        self.lb_ChuaAnh.setText("")
        self.lb_ChuaAnh.setObjectName("lb_ChuaAnh")
        self.lb_ChuaAnh.setStyleSheet("border: 1px solid #000000;")
        self.bt_layAnhCD = QtWidgets.QPushButton(self.centralwidget)
        self.bt_layAnhCD.setGeometry(QtCore.QRect(510, 260, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_layAnhCD.setFont(font)
        self.bt_layAnhCD.setObjectName("bt_layAnhCD")
        self.bt_Sua = QtWidgets.QPushButton(self.centralwidget)
        self.bt_Sua.setGeometry(QtCore.QRect(740, 220, 30, 30))
        self.bt_Sua.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../anh/icons8-update-left-rotation-27.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_Sua.setIcon(icon1)
        self.bt_Sua.setIconSize(QtCore.QSize(25, 25))
        self.bt_Sua.setObjectName("bt_Sua")
        self.bt_Xoa = QtWidgets.QPushButton(self.centralwidget)
        self.bt_Xoa.setGeometry(QtCore.QRect(790, 220, 30, 30))
        self.bt_Xoa.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../anh/Button-Delete-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_Xoa.setIcon(icon2)
        self.bt_Xoa.setIconSize(QtCore.QSize(25, 25))
        self.bt_Xoa.setObjectName("bt_Xoa")
        self.tableBienChiDan = QtWidgets.QTableWidget(self.centralwidget)
        self.tableBienChiDan.setGeometry(QtCore.QRect(10, 350, 961, 311))
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
        self.lb_tenBienCD_2 = QtWidgets.QLabel(self.centralwidget)
        self.lb_tenBienCD_2.setGeometry(QtCore.QRect(230, 170, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tenBienCD_2.setFont(font)
        self.lb_tenBienCD_2.setObjectName("lb_tenBienCD_2")
        self.txYNghia = QtWidgets.QTextEdit(self.centralwidget)
        self.txYNghia.setGeometry(QtCore.QRect(340, 170, 481, 35))
        self.txYNghia.setObjectName("txYNghia")
        self.widgetTieuDe = QtWidgets.QWidget(self.centralwidget)
        self.widgetTieuDe.setGeometry(QtCore.QRect(0, -1, 981, 101))
        self.widgetTieuDe.setAutoFillBackground(True)
        self.widgetTieuDe.setObjectName("widgetTieuDe")
        self.widgetTieuDe.setStyleSheet("background-color: #6ea0b0;")
        self.lbAnh = QtWidgets.QLabel(self.widgetTieuDe)
        self.lbAnh.setGeometry(QtCore.QRect(0, 0, 181, 101))
        self.lbAnh.setText("")
        self.lbAnh.setPixmap(QtGui.QPixmap("../anh/logoduongboVN.jpg"))
        self.lbAnh.setScaledContents(True)
        self.lbAnh.setAlignment(QtCore.Qt.AlignCenter)
        self.lbAnh.setObjectName("lbAnh")
        self.label = QtWidgets.QLabel(self.widgetTieuDe)
        self.label.setGeometry(QtCore.QRect(380, 20, 300, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(68)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel#label { color: yellow; }")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 981, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.hienThi()
        self.bt_layAnhCD.clicked.connect(self.chonAnh)
        self.bt_Them.clicked.connect(self.them)
        self.tableBienChiDan.itemClicked.connect(self.tableClick)
        self.bt_Sua.clicked.connect(self.sua)
        self.bt_Xoa.clicked.connect(self.xoa)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hệ thống quản lí biển báo giao thông"))
        self.lb_tenBienCD.setText(_translate("MainWindow", "Tên biển"))
        self.lb_AnhCD.setText(_translate("MainWindow", "Ảnh"))
        self.bt_layAnhCD.setText(_translate("MainWindow", "Chọn ảnh"))
        item = self.tableBienChiDan.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ảnh"))
        item = self.tableBienChiDan.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên biển"))
        item = self.tableBienChiDan.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ý nghĩa"))
        self.lb_tenBienCD_2.setText(_translate("MainWindow", "Ý nghĩa"))
        self.label.setText(_translate("MainWindow", " QUẢN LÍ BIỂN BÁO CẤM"))
    def hienThi(self):
        try:
            conn = mysql.connector.connect(user='root', password='123456789', host='localhost', database='doan_py')
            query = "SELECT * FROM bienbaocam"
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                tenBien,ynghia, imgPath = row
                bb = bienBao_DTO.bienbao(tenBien,ynghia, imgPath)
                self.dsBB.append(bb)
            if (len(self.dsBB) > 0):
                for row_index, bb in enumerate(self.dsBB):
                    self.tableBienChiDan.insertRow(row_index)

                    # Thiết lập ảnh
                    pixmap = QtGui.QPixmap("../anh/imgBienBao/" + bb.get_imgPath()).scaled(150, 150)
                    image_item = QTableWidgetItem()
                    image_item.setData(QtCore.Qt.DecorationRole, pixmap)
                    self.tableBienChiDan.setItem(row_index, 0, image_item)

                    # Thiết lập tên
                    name_item = QTableWidgetItem(bb.get_tenBien())
                    self.tableBienChiDan.setItem(row_index, 1, name_item)
                    self.tableBienChiDan.setItem(row_index,2,QTableWidgetItem(bb.get_yNghia()))
        except mysql.connector.Error as error:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Kết nối mysql thất bại {}".format(error))

    def chonAnh(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
        file_dialog.setViewMode(QFileDialog.Detail)
        if(file_dialog.exec_()):
            selected_files=file_dialog.selectedFiles()
            if selected_files:
                image_path=selected_files[0]
                self.imgPath=image_path
                pixmap=(QtGui.QPixmap(image_path)).scaled(490,140,151,111)
                self.lb_ChuaAnh.setPixmap(pixmap)
                self.lb_ChuaAnh.setScaledContents(True)
    def checkTenBien(self,ten):
        for bb in self.dsBB:
            if(bb.get_tenBien()==ten):
                return False
        return True
    def them(self):
        if(self.textEdit.toPlainText()==""):
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Vui lòng nhập tên biển báo")
            self.textEdit.setFocus()
        elif self.txYNghia.toPlainText()=="":
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Vui lòng nhập ý nghĩa của  biển báo bạn muốn thêm")
            self.txYNghia.setFocus()
        elif self.imgPath=="":
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Vui lòng chọn ảnh biển báo ")
        elif self.checkTenBien(self.textEdit.toPlainText())!=True:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi","Tên biển báo đã có trong hệ thống vui lòng kiểm tra lại")
            self.textEdit.setText("")
            self.textEdit.setFocus()
        else:
            img_name=os.path.basename(self.imgPath)
            self.imgPath=""
            bb=bienBao_DTO.bienbao(self.textEdit.toPlainText(),self.txYNghia.toPlainText(),img_name)
            self.dsBB.append(bb)
            soHang=self.tableBienChiDan.rowCount()
            self.tableBienChiDan.insertRow(soHang)
            #anh
            pixmap = QtGui.QPixmap("../anh/imgBienBao/" + bb.get_imgPath()).scaled(150, 150)
            image_item = QTableWidgetItem()
            image_item.setData(QtCore.Qt.DecorationRole, pixmap)
            self.tableBienChiDan.setItem(soHang, 0, image_item)
            # ten bien
            self.tableBienChiDan.setItem(soHang, 1, QTableWidgetItem(bb.get_tenBien()))
            # y nghia
            self.tableBienChiDan.setItem(soHang, 2, QTableWidgetItem(bb.get_yNghia()))
            try:
                conn=mysql.connector.connect(user='root', password='123456789', host='localhost', database='doan_py')
                cursor = conn.cursor()
                sql="INSERT INTO bienbaocam(Ten_BienBaoCam,Mieuta,HinhAnhBBC) VALUES (%s,%s,%s)"
                val=(bb.get_tenBien(),bb.get_yNghia(),bb.get_imgPath())
                cursor.execute(sql,val)
                conn.commit()
                self.textEdit.setText("")
                self.txYNghia.setText("")
                self.lb_ChuaAnh.setPixmap(QtGui.QPixmap())
                QtWidgets.QMessageBox.information(self.centralwidget, "Thành công", "Thêm phần tử mới thành công")
            except mysql.connector.Error as error:
                QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi","Lỗi khi thêm dữ liệu vào MySQL: {}".format(error))
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()
    def tableClick(self,item):
        row=item.row()
        if(row>=0 and row<len(self.dsBB)):
            tenbien=self.tableBienChiDan.item(row,1).text()
            self.textEdit.setText(tenbien)
            ynghia=self.tableBienChiDan.item(row,2).text()
            self.txYNghia.setText(ynghia)
            img_item=self.tableBienChiDan.item(row,0)
            if img_item is not None:
                pixmap=img_item.data(QtCore.Qt.DecorationRole)# Lấy pixmap từ dữ liệu của ô
                if not pixmap.isNull(): #kiem tra pixmap
                    scaled_pixmap = pixmap.scaled(490, 140, 151, 111)
                    self.lb_ChuaAnh.setPixmap(scaled_pixmap)
                    self.lb_ChuaAnh.setScaledContents(True)
    def sua(self):


        selected_row = self.tableBienChiDan.currentRow()

        if (selected_row >= 0 and selected_row < len(self.dsBB)):
            tenbiencu = self.dsBB[selected_row].get_tenBien()
            if self.textEdit.toPlainText() == "":
                QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Vui lòng nhập tên biển báo")
                self.textEdit.setFocus()
            elif self.txYNghia.toPlainText() == "":
                QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi","Vui lòng nhập ý nghĩa của  biển báo bạn muốn thêm")
                self.txYNghia.setFocus()
            elif tenbiencu!=self.textEdit.toPlainText() and self.checkTenBien(self.textEdit.toPlainText()) != True:
                QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi","Tên biển báo đã có trong hệ thống vui lòng kiểm tra lại")
                self.textEdit.setText("")
                self.textEdit.setFocus()
            else:
                tenbien=self.textEdit.toPlainText()
                ynghia=self.txYNghia.toPlainText()
                imgpath=self.dsBB[selected_row].get_imgPath()# lấy lại đường link ảnh cũ
                if(self.imgPath!=""):# có chọn ảnh mới k
                    imgpath=os.path.basename(self.imgPath)
                    self.imgPath=""
                #cap nhat bang
                self.tableBienChiDan.setItem(selected_row, 1, QTableWidgetItem(tenbien))
                self.tableBienChiDan.setItem(selected_row, 2, QTableWidgetItem(ynghia))
                pixmap = QtGui.QPixmap("../anh/imgBienBao/" + imgpath).scaled(150, 150)
                image_item = QTableWidgetItem()
                image_item.setData(QtCore.Qt.DecorationRole, pixmap)
                self.tableBienChiDan.setItem(selected_row, 0, image_item)
                #cap nhat mysql
                try:
                    conn = mysql.connector.connect(user='root', password='123456789', host='localhost',database='doan_py')
                    cursor = conn.cursor()
                    sql="UPDATE bienbaocam SET Ten_BienBaoCam= %s , Mieuta= %s , HinhAnhBBC= %s WHERE Ten_BienBaoCam= %s"
                    val=(tenbien,ynghia,imgpath,self.dsBB[selected_row].get_tenBien())
                    cursor.execute(sql, val)
                    conn.commit()
                    self.textEdit.setText("")
                    self.txYNghia.setText("")
                    self.lb_ChuaAnh.setPixmap(QtGui.QPixmap())
                    QtWidgets.QMessageBox.information(self.centralwidget, "Thành công", "Đã cập nhật thông tin thành công")
                except mysql.connector.Error as error:
                    QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Lỗi khi cập nhật dữ liệu trong MySQL: {}".format(error))
                finally:
                    if conn.is_connected():
                        cursor.close()
                        conn.close()
                #cap nhat trong ds
                self.dsBB[selected_row].set_imgPath(imgpath)
                self.dsBB[selected_row].set_tenBien(tenbien)
                self.dsBB[selected_row].set_yNghia(ynghia)
        else:QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Chọn hàng cần sửa")
    def xoa(self):
         selected_row = self.tableBienChiDan.currentRow()
         if (selected_row >= 0 and selected_row < len(self.dsBB)):
            #xoa bang
            self.tableBienChiDan.removeRow(selected_row)
            #xoa mysql
            try:
                conn = mysql.connector.connect(user='root', password='123456789', host='localhost', database='doan_py')
                cursor = conn.cursor()
                sql="DELETE FROM bienbaocam WHERE Ten_BienBaoCam = %s"
                val=(self.dsBB[selected_row].get_tenBien(),)
                cursor.execute(sql,val)
                conn.commit()
                QtWidgets.QMessageBox.information(self.centralwidget, "Thành công", "Đã xóa hàng thành công")
            except mysql.connector.Error as error:
                QtWidgets.QMessageBox.warning(self.centralwidget, "Lỗi", "Lỗi khi xóa dữ liệu trong MySQL: {}".format(error))

            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()
            #cap nhat ds
            del  self.dsBB[selected_row]
            self.textEdit.setText("")
            self.txYNghia.setText("")
            self.lb_ChuaAnh.setPixmap(QtGui.QPixmap())
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