# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_graph(object):
    def setupUi(self, graph):
        graph.setObjectName("graph")
        graph.resize(470, 629)
        graph.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.display = QtWidgets.QLineEdit(graph)
        self.display.setGeometry(QtCore.QRect(10, 70, 451, 101))
        self.display.setObjectName("display")
        self.model = QtWidgets.QLabel(graph)
        self.model.setGeometry(QtCore.QRect(130, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.model.setFont(font)
        self.model.setAlignment(QtCore.Qt.AlignCenter)
        self.model.setObjectName("model")
        self.selectwindow = QtWidgets.QComboBox(graph)
        self.selectwindow.setGeometry(QtCore.QRect(10, 10, 121, 41))
        self.selectwindow.setObjectName("selectwindow")
        self.selectwindow.addItem("")
        self.selectwindow.addItem("")
        self.selectwindow.addItem("")
        self.selectwindow.addItem("")
        self.layoutWidget = QtWidgets.QWidget(graph)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 190, 451, 431))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.b7 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b7.sizePolicy().hasHeightForWidth())
        self.b7.setSizePolicy(sizePolicy)
        self.b7.setObjectName("b7")
        self.horizontalLayout_6.addWidget(self.b7)
        self.b8 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b8.sizePolicy().hasHeightForWidth())
        self.b8.setSizePolicy(sizePolicy)
        self.b8.setObjectName("b8")
        self.horizontalLayout_6.addWidget(self.b8)
        self.b9 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b9.sizePolicy().hasHeightForWidth())
        self.b9.setSizePolicy(sizePolicy)
        self.b9.setObjectName("b9")
        self.horizontalLayout_6.addWidget(self.b9)
        self.multiply = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.multiply.sizePolicy().hasHeightForWidth())
        self.multiply.setSizePolicy(sizePolicy)
        self.multiply.setObjectName("multiply")
        self.horizontalLayout_6.addWidget(self.multiply)
        self.equ = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equ.sizePolicy().hasHeightForWidth())
        self.equ.setSizePolicy(sizePolicy)
        self.equ.setObjectName("equ")
        self.horizontalLayout_6.addWidget(self.equ)
        self.sin1 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sin1.sizePolicy().hasHeightForWidth())
        self.sin1.setSizePolicy(sizePolicy)
        self.sin1.setObjectName("sin1")
        self.horizontalLayout_6.addWidget(self.sin1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.b4 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b4.sizePolicy().hasHeightForWidth())
        self.b4.setSizePolicy(sizePolicy)
        self.b4.setObjectName("b4")
        self.horizontalLayout_5.addWidget(self.b4)
        self.b5 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b5.sizePolicy().hasHeightForWidth())
        self.b5.setSizePolicy(sizePolicy)
        self.b5.setObjectName("b5")
        self.horizontalLayout_5.addWidget(self.b5)
        self.b6 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b6.sizePolicy().hasHeightForWidth())
        self.b6.setSizePolicy(sizePolicy)
        self.b6.setObjectName("b6")
        self.horizontalLayout_5.addWidget(self.b6)
        self.add = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
        self.add.setSizePolicy(sizePolicy)
        self.add.setObjectName("add")
        self.horizontalLayout_5.addWidget(self.add)
        self.back = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        self.back.setObjectName("back")
        self.horizontalLayout_5.addWidget(self.back)
        self.cos1 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cos1.sizePolicy().hasHeightForWidth())
        self.cos1.setSizePolicy(sizePolicy)
        self.cos1.setObjectName("cos1")
        self.horizontalLayout_5.addWidget(self.cos1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.b1 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b1.sizePolicy().hasHeightForWidth())
        self.b1.setSizePolicy(sizePolicy)
        self.b1.setObjectName("b1")
        self.horizontalLayout_4.addWidget(self.b1)
        self.b2 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b2.sizePolicy().hasHeightForWidth())
        self.b2.setSizePolicy(sizePolicy)
        self.b2.setObjectName("b2")
        self.horizontalLayout_4.addWidget(self.b2)
        self.b3 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b3.sizePolicy().hasHeightForWidth())
        self.b3.setSizePolicy(sizePolicy)
        self.b3.setObjectName("b3")
        self.horizontalLayout_4.addWidget(self.b3)
        self.substract = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.substract.sizePolicy().hasHeightForWidth())
        self.substract.setSizePolicy(sizePolicy)
        self.substract.setObjectName("substract")
        self.horizontalLayout_4.addWidget(self.substract)
        self.clear = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear.sizePolicy().hasHeightForWidth())
        self.clear.setSizePolicy(sizePolicy)
        self.clear.setObjectName("clear")
        self.horizontalLayout_4.addWidget(self.clear)
        self.tan1 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tan1.sizePolicy().hasHeightForWidth())
        self.tan1.setSizePolicy(sizePolicy)
        self.tan1.setObjectName("tan1")
        self.horizontalLayout_4.addWidget(self.tan1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.b0 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b0.sizePolicy().hasHeightForWidth())
        self.b0.setSizePolicy(sizePolicy)
        self.b0.setObjectName("b0")
        self.horizontalLayout_3.addWidget(self.b0)
        self.plus_minus = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plus_minus.sizePolicy().hasHeightForWidth())
        self.plus_minus.setSizePolicy(sizePolicy)
        self.plus_minus.setObjectName("plus_minus")
        self.horizontalLayout_3.addWidget(self.plus_minus)
        self.decimal = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decimal.sizePolicy().hasHeightForWidth())
        self.decimal.setSizePolicy(sizePolicy)
        self.decimal.setObjectName("decimal")
        self.horizontalLayout_3.addWidget(self.decimal)
        self.divide = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.divide.sizePolicy().hasHeightForWidth())
        self.divide.setSizePolicy(sizePolicy)
        self.divide.setObjectName("divide")
        self.horizontalLayout_3.addWidget(self.divide)
        self.equal = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equal.sizePolicy().hasHeightForWidth())
        self.equal.setSizePolicy(sizePolicy)
        self.equal.setObjectName("equal")
        self.horizontalLayout_3.addWidget(self.equal)
        self.x = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x.sizePolicy().hasHeightForWidth())
        self.x.setSizePolicy(sizePolicy)
        self.x.setObjectName("x")
        self.horizontalLayout_3.addWidget(self.x)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sin = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sin.sizePolicy().hasHeightForWidth())
        self.sin.setSizePolicy(sizePolicy)
        self.sin.setObjectName("sin")
        self.horizontalLayout_2.addWidget(self.sin)
        self.cos = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cos.sizePolicy().hasHeightForWidth())
        self.cos.setSizePolicy(sizePolicy)
        self.cos.setObjectName("cos")
        self.horizontalLayout_2.addWidget(self.cos)
        self.tan = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tan.sizePolicy().hasHeightForWidth())
        self.tan.setSizePolicy(sizePolicy)
        self.tan.setObjectName("tan")
        self.horizontalLayout_2.addWidget(self.tan)
        self.ln = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln.sizePolicy().hasHeightForWidth())
        self.ln.setSizePolicy(sizePolicy)
        self.ln.setObjectName("ln")
        self.horizontalLayout_2.addWidget(self.ln)
        self.log = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log.sizePolicy().hasHeightForWidth())
        self.log.setSizePolicy(sizePolicy)
        self.log.setObjectName("log")
        self.horizontalLayout_2.addWidget(self.log)
        self.sq_root = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sq_root.sizePolicy().hasHeightForWidth())
        self.sq_root.setSizePolicy(sizePolicy)
        self.sq_root.setObjectName("sq_root")
        self.horizontalLayout_2.addWidget(self.sq_root)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.b_open = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_open.sizePolicy().hasHeightForWidth())
        self.b_open.setSizePolicy(sizePolicy)
        self.b_open.setObjectName("b_open")
        self.horizontalLayout.addWidget(self.b_open)
        self.b_close = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_close.sizePolicy().hasHeightForWidth())
        self.b_close.setSizePolicy(sizePolicy)
        self.b_close.setObjectName("b_close")
        self.horizontalLayout.addWidget(self.b_close)
        self.power = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.power.sizePolicy().hasHeightForWidth())
        self.power.setSizePolicy(sizePolicy)
        self.power.setObjectName("power")
        self.horizontalLayout.addWidget(self.power)
        self.e = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.e.sizePolicy().hasHeightForWidth())
        self.e.setSizePolicy(sizePolicy)
        self.e.setObjectName("e")
        self.horizontalLayout.addWidget(self.e)
        self.pi = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pi.sizePolicy().hasHeightForWidth())
        self.pi.setSizePolicy(sizePolicy)
        self.pi.setObjectName("pi")
        self.horizontalLayout.addWidget(self.pi)
        self.plot = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot.sizePolicy().hasHeightForWidth())
        self.plot.setSizePolicy(sizePolicy)
        self.plot.setObjectName("plot")
        self.horizontalLayout.addWidget(self.plot)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(graph)
        QtCore.QMetaObject.connectSlotsByName(graph)

    def retranslateUi(self, graph):
        _translate = QtCore.QCoreApplication.translate
        graph.setWindowTitle(_translate("graph", "Widget"))
        self.model.setText(_translate("graph", "graph"))
        self.selectwindow.setItemText(0, _translate("graph", "standard"))
        self.selectwindow.setItemText(1, _translate("graph", "scientific"))
        self.selectwindow.setItemText(2, _translate("graph", "graph"))
        self.selectwindow.setItemText(3, _translate("graph", "time"))
        self.b7.setText(_translate("graph", "7"))
        self.b8.setText(_translate("graph", "8"))
        self.b9.setText(_translate("graph", "9"))
        self.multiply.setText(_translate("graph", "X"))
        self.equ.setText(_translate("graph", "Equation"))
        self.sin1.setText(_translate("graph", "sin-1"))
        self.b4.setText(_translate("graph", "4"))
        self.b5.setText(_translate("graph", "5"))
        self.b6.setText(_translate("graph", "6"))
        self.add.setText(_translate("graph", "+"))
        self.back.setText(_translate("graph", "Back"))
        self.cos1.setText(_translate("graph", "cos-1"))
        self.b1.setText(_translate("graph", "1"))
        self.b2.setText(_translate("graph", "2"))
        self.b3.setText(_translate("graph", "3"))
        self.substract.setText(_translate("graph", "-"))
        self.clear.setText(_translate("graph", "AC"))
        self.tan1.setText(_translate("graph", "tan-1"))
        self.b0.setText(_translate("graph", "0"))
        self.plus_minus.setText(_translate("graph", "+/-"))
        self.decimal.setText(_translate("graph", "."))
        self.divide.setText(_translate("graph", "/"))
        self.equal.setText(_translate("graph", "="))
        self.x.setText(_translate("graph", "x"))
        self.sin.setText(_translate("graph", "sin"))
        self.cos.setText(_translate("graph", "cos"))
        self.tan.setText(_translate("graph", "tan"))
        self.ln.setText(_translate("graph", "ln"))
        self.log.setText(_translate("graph", "log"))
        self.sq_root.setText(_translate("graph", "Sqrt"))
        self.b_open.setText(_translate("graph", "("))
        self.b_close.setText(_translate("graph", ")"))
        self.power.setText(_translate("graph", "^"))
        self.e.setText(_translate("graph", "e"))
        self.pi.setText(_translate("graph", "π"))
        self.plot.setText(_translate("graph", "plot"))