from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel
from PyQt5 import QtCore
import sys
import os
import functions
import classes_tasks
import datetime as dt
from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.insert(0, r"UI_py")
import buy_menu_UI
import dop_UI
import editing_homework_UI
import editing_ideas_UI
import editing_one_time_task_UI
import editing_permanent_task_UI
import editing_rules_UI
import history_UI
import homework_information_UI
import ideas_information_UI
import information_about_a_one_time_task_UI
import information_about_a_permanent_task_UI
import information_about_the_rules_UI
import managing_current_tasks_menu_UI
import managing_current_tasks_UI
import menu_UI
import new_homework_task_UI
import new_ideas_UI
import new_one_time_task_UI
import new_permanent_task_UI
import new_rules_UI
import new_task_UI
import savings_main_menu_UI
import saving_menu_UI
import shop_menu_UI
import statistics_UI
import sure_UI
import task_menu_UI


class Menu(QMainWindow, menu_UI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run1)
        self.pushButton_2.clicked.connect(self.run2)
        self.pushButton_3.clicked.connect(self.run3)
        self.pushButton_4.clicked.connect(self.run4)

    def run1(self):
        self.first_form = TaskMenu()
        self.first_form.show()
        self.close()

    def run2(self):
        self.first_form = SavingMainMenu()
        self.first_form.show()
        self.close()

    def run3(self):
        self.first_form = Statistics()
        self.first_form.show()
        self.close()

    def run4(self):
        self.first_form = Dop()
        self.first_form.show()
        self.close()


class TaskMenu(QMainWindow, task_menu_UI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run1)
        self.pushButton_2.clicked.connect(self.run2)
        self.pushButton_4.clicked.connect(self.run3)

    def run1(self):
        self.first_form = NewTask()
        self.first_form.show()
        self.close()

    def run2(self):
        self.first_form = ManagingCurrentTasks()
        self.first_form.show()
        self.close()

    def run3(self):
        self.first_form = Menu()
        self.first_form.show()
        self.close()


class SavingMainMenu(QMainWindow, savings_main_menu_UI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.run1)
        self.pushButton_3.clicked.connect(self.run2)
        self.pushButton_4.clicked.connect(self.run3)

    def run1(self):
        self.first_form = ShopMenu()
        self.first_form.show()
        self.close()

    def run2(self):
        self.first_form = SavingMenu()
        self.first_form.show()
        self.close()

    def run3(self):
        self.first_form = Menu()
        self.first_form.show()
        self.close()


class Statistics(QMainWindow, statistics_UI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run1)
        _translate = QtCore.QCoreApplication.translate
        vip, prs, nr = functions.read_sql_statistik()
        self.label_name_inf.setText(_translate("Form", str(prs)))
        self.label_frequency_inf.setText(_translate("Form", str(vip)))
        self.label_exp_inf.setText(_translate("Form", str(nr)))

    def run1(self):
        self.first_form = Menu()
        self.first_form.show()
        self.close()


class NewTask(QMainWindow, new_task_UI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run1)
        self.pushButton_2.clicked.connect(self.run2)
        self.pushButton_3.clicked.connect(self.run3)
        self.pushButton_4.clicked.connect(self.run4)
        self.pushButton_5.clicked.connect(self.run5)
        self.pushButton_6.clicked.connect(self.run6)

    def run1(self):
        self.first_form = NewPermanentTask()
        self.first_form.show()
        self.close()

    def run2(self):
        self.first_form = NewHomeworkTask()
        self.first_form.show()
        self.close()

    def run3(self):
        self.first_form = NewRules()
        self.first_form.show()
        self.close()

    def run4(self):
        self.first_form = NewOneTimeTask()
        self.first_form.show()
        self.close()

    def run5(self):
        self.first_form = NewIdeas()
        self.first_form.show()
        self.close()

    def run6(self):
        self.first_form = TaskMenu()
        self.first_form.show()
        self.close()


class ManagingCurrentTasks(QMainWindow, managing_current_tasks_UI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        _translate = QtCore.QCoreApplication.translate
        self.lst_obj = functions.full_read()
        for i in range(len(self.lst_obj)):
            self.comboBox.addItem("")
            self.comboBox.setItemText(i, _translate("Form", f"{self.lst_obj[i].name}"))
        self.pushButton.clicked.connect(self.run1)
        self.pushButton_2.clicked.connect(self.run2)

    def run1(self):
        self.first_form = TaskMenu()
        self.first_form.show()
        self.close()

    def run2(self):
        self.first_form = ManagingCurrentTasksMenu(self.lst_obj[self.comboBox.currentIndex()])
        self.first_form.show()
        self.close()


class ShopMenu(QMainWindow, shop_menu_UI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.run1)
        self.pushButton_3.clicked.connect(self.run2)
        self.pushButton_4.clicked.connect(self.run3)

    def run1(self):
        self.first_form = BuyMenu()
        self.first_form.show()
        self.close()

    def run2(self):
        self.first_form = History()
        self.first_form.show()
        self.close()

    def run3(self):
        self.first_form = SavingMainMenu()
        self.first_form.show()
        self.close()


class SavingMenu(QMainWindow, saving_menu_UI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run1)
        _translate = QtCore.QCoreApplication.translate
        money, exp = functions.read_saving()
        self.label_name_inf.setText(_translate("Form", money))
        self.label_frequency_inf.setText(_translate("Form", exp))

    def run1(self):
        self.first_form = SavingMainMenu()
        self.first_form.show()
        self.close()


class NewPermanentTask(QMainWindow, new_permanent_task_UI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run1)
        self.pushButton_2.clicked.connect(self.run2)

    def run1(self):
        self.first_form = NewTask()
        self.first_form.show()
        self.close()

    def run2(self):
        try:
            functions.save(
                classes_tasks.PermanentTasks(self.lineEdit.text(), self.lineEdit_2.text(),
                                             self.comboBox_2.currentIndex(),
                                             int(self.lineEdit_3.text()), int(self.lineEdit_4.text()),
                                             self.lineEdit_5.text()))
            self.first_form = Menu()
            self.first_form.show()
            self.close()
        except BaseException:
            pass


class NewOneTimeTask(QMainWindow, new_one_time_task_UI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run1)
        self.pushButton_2.clicked.connect(self.run2)

    def run1(self):
        self.first_form = NewTask()
        self.first_form.show()
        self.close()

    def run2(self):
        try:
            functions.save(
                classes_tasks.OneTimeTasks(self.lineEdit.text(), int(self.lineEdit_3.text()),
                                           int(self.lineEdit_4.text()),
                                           dt.datetime(dt.datetime.now().year, self.comboBox_2.currentIndex() + 1,
                                                       self.comboBox_2.currentIndex() + 1).date(),
                                           self.lineEdit_5.text()))
            self.first_form = Menu()
            self.first_form.show()
            self.close()
        except:
            pass


class NewHomeworkTask(QMainWindow, new_homework_task_UI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run1)
        self.pushButton_2.clicked.connect(self.run2)

    def run1(self):
        self.first_form = NewTask()
        self.first_form.show()
        self.close()

    def run2(self):
        try:
            functions.save(
                classes_tasks.Homework(self.lineEdit.text(), int(self.lineEdit_3.text()), int(self.lineEdit_4.text()),
                                       str(self.comboBox_2.currentIndex() + 1) + '.' + str(
                                           self.comboBox_3.currentIndex() + 1),
                                       self.lineEdit_5.text(), self.lineEdit_6.text()))
            self.first_form = Menu()
            self.first_form.show()
            self.close()
        except BaseException:
            self.first_form = NewHomeworkTask()
            self.first_form.show()
            self.close()


class NewIdeas(QMainWindow, new_ideas_UI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run1)
        self.pushButton_2.clicked.connect(self.run2)

    def run1(self):
        self.first_form = NewTask()
        self.first_form.show()
        self.close()

    def run2(self):
        try:
            functions.save(
                classes_tasks.Ideas(self.lineEdit.text(), int(self.lineEdit_3.text()), int(self.lineEdit_4.text()),
                                    self.lineEdit_5.text()))
            self.first_form = Menu()
            self.first_form.show()
            self.close()
        except BaseException:
            self.first_form = NewIdeas()
            self.first_form.show()
            self.close()


class NewRules(QMainWindow, new_rules_UI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run1)
        self.pushButton_2.clicked.connect(self.run2)

    def run1(self):
        self.first_form = NewTask()
        self.first_form.show()
        self.close()

    def run2(self):
        try:
            functions.save(
                classes_tasks.Rules(self.lineEdit.text(), int(self.lineEdit_3.text()), int(self.lineEdit_4.text()),
                                    self.lineEdit_5.text()))
            self.first_form = Menu()
            self.first_form.show()
            self.close()
        except BaseException:
            self.first_form = NewRules()
            self.first_form.show()
            self.close()


class ManagingCurrentTasksMenu(QMainWindow, managing_current_tasks_menu_UI.Ui_Form):
    def __init__(self, obj):
        super().__init__()
        self.setupUi(self)
        self.obj = obj
        self.pushButton.clicked.connect(self.run1)
        self.pushButton_2.clicked.connect(self.run2)
        self.pushButton_3.clicked.connect(self.run3)
        self.pushButton_4.clicked.connect(self.run4)
        self.pushButton_5.clicked.connect(self.run5)

    def run1(self):
        self.first_form = functions.information_panel_UI(self.obj)
        self.first_form.show()
        self.close()

    def run2(self):
        functions.wr_inf(-(self.obj.virtual_coins), -(self.obj.exp))
        self.first_form = Menu()
        self.first_form.show()
        self.close()

    def run3(self):
        functions.delete(self.obj)
        self.first_form = Menu()
        self.first_form.show()
        self.close()

    def run4(self):
        functions.wr_inf((self.obj.virtual_coins), (self.obj.exp))
        self.first_form = Menu()
        self.first_form.show()
        self.close()

    def run5(self):
        self.first_form = ManagingCurrentTasks()
        self.first_form.show()
        self.close()


class InformationAboutAPermanentTask(QMainWindow, information_about_a_permanent_task_UI.Ui_Form):
    def __init__(self, obj):
        super().__init__()
        _translate = QtCore.QCoreApplication.translate
        self.obj = obj
        self.setupUi(self)
        self.obj = obj
        self.label_name_inf.setText(_translate("Form", f"{obj.name}"))
        self.label_frequency_inf.setText(
            _translate("Form", f"{obj.quantity} {['в день', 'в неделю', 'в месяц', 'в год'][obj.frequency]}"))
        self.label_exp_inf.setText(_translate("Form", f"{obj.exp}"))
        self.label_virtual_coins_inf.setText(_translate("Form", f"{obj.virtual_coins}"))
        self.label_described_inf.setText(_translate("Form", f"{obj.described}"))
        self.pushButton.clicked.connect(self.run1)

    def run1(self):
        self.first_form = ManagingCurrentTasksMenu(self.obj)
        self.first_form.show()
        self.close()


class InformationAboutAOneTimeTask(QMainWindow, information_about_a_one_time_task_UI.Ui_Form):
    def __init__(self, obj):
        super().__init__()
        _translate = QtCore.QCoreApplication.translate
        self.obj = obj
        self.setupUi(self)
        self.obj = obj
        self.label_name_inf.setText(_translate("Form", f"{obj.name}"))
        self.label_term_inf.setText(_translate("Form", f"{obj.term}"))
        self.label_exp_inf.setText(_translate("Form", f"{obj.exp}"))
        self.label_virtual_coins_inf.setText(_translate("Form", f"{obj.virtual_coins}"))
        self.label_described_inf.setText(_translate("Form", f"{obj.described}"))
        self.pushButton.clicked.connect(self.run1)

    def run1(self):
        self.first_form = ManagingCurrentTasksMenu(self.obj)
        self.first_form.show()
        self.close()


class HomeworkInformation(QMainWindow, homework_information_UI.Ui_Form):
    def __init__(self, obj):
        super().__init__()
        _translate = QtCore.QCoreApplication.translate
        self.obj = obj
        self.setupUi(self)
        self.obj = obj
        self.label_name_inf.setText(_translate("Form", f"{obj.name}"))
        self.label_term_inf.setText(_translate("Form", f"{obj.term}"))
        self.label_exp_inf.setText(_translate("Form", f"{obj.exp}"))
        self.label_virtual_coins_inf.setText(_translate("Form", f"{obj.virtual_coins}"))
        self.label_lesson_inf.setText(_translate("Form", f"{obj.lesson}"))
        self.label_described_inf_2.setText(_translate("Form", f"{obj.task}"))
        self.pushButton.clicked.connect(self.run1)

    def run1(self):
        self.first_form = ManagingCurrentTasksMenu(self.obj)
        self.first_form.show()
        self.close()


class IdeasInformation(QMainWindow, ideas_information_UI.Ui_Form):
    def __init__(self, obj):
        super().__init__()
        _translate = QtCore.QCoreApplication.translate
        self.obj = obj
        self.setupUi(self)
        self.obj = obj
        self.label_name_inf.setText(_translate("Form", f"{obj.name}"))
        self.label_exp_inf.setText(_translate("Form", f"{obj.exp}"))
        self.label_virtual_coins_inf.setText(_translate("Form", f"{obj.virtual_coins}"))
        self.label_described_inf.setText(_translate("Form", f"{obj.described}"))
        self.pushButton.clicked.connect(self.run1)

    def run1(self):
        self.first_form = ManagingCurrentTasksMenu(self.obj)
        self.first_form.show()
        self.close()


class InformationAboutTheRules(QMainWindow, information_about_the_rules_UI.Ui_Form):
    def __init__(self, obj):
        super().__init__()
        _translate = QtCore.QCoreApplication.translate
        self.obj = obj
        self.setupUi(self)
        self.obj = obj
        self.label_name_inf.setText(_translate("Form", f"{obj.name}"))
        self.label_exp_inf.setText(_translate("Form", f"{obj.exp}"))
        self.label_virtual_coins_inf.setText(_translate("Form", f"{obj.virtual_coins}"))
        self.label_described_inf.setText(_translate("Form", f"{obj.described}"))
        self.label_violated_inf.setText(_translate("Form", f"{obj.violated}"))
        self.pushButton.clicked.connect(self.run1)

    def run1(self):
        self.first_form = ManagingCurrentTasksMenu(self.obj)
        self.first_form.show()
        self.close()


class BuyMenu(QMainWindow, buy_menu_UI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run1)
        self.pushButton_2.clicked.connect(self.run2)

    def run1(self):
        self.first_form = ShopMenu()
        self.first_form.show()
        self.close()

    def run2(self):
        try:
            functions.write_history(self.lineEdit.text(), int(self.lineEdit_2.text()))
            functions.wr_inf(-int(self.lineEdit_2.text()), 0)
            self.first_form = Menu()
            self.first_form.show()
            self.close()
        except BaseException:
            pass


class History(QMainWindow, history_UI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run1)
        _translate = QtCore.QCoreApplication.translate
        self.lst = functions.read_history()
        for i in range(len(self.lst)):
            self.comboBox.addItem("")
            self.comboBox.setItemText(i, _translate("Form", f"{self.lst[i]}"))

    def run1(self):
        self.first_form = ShopMenu()
        self.first_form.show()
        self.close()


class Dop(QMainWindow, dop_UI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run1)
        self.pushButton_2.clicked.connect(self.run2)
        self.pushButton_3.clicked.connect(self.run3)
        self.pushButton_4.clicked.connect(self.run4)

    def run1(self):
        _translate = QtCore.QCoreApplication.translate
        firstDayText = '{}-01-01'.format(self.dateEdit.dateTime().toString('yyyy'))
        firstDay = QtCore.QDateTime.fromString(firstDayText, "yyyy-MM-dd").toString("yyyy-MM-dd")
        d = list(map(int, firstDay.split('-')))
        dd = dt.datetime(*d)
        self.label.setText(_translate("Form", f"{dd.weekday()}"))

    def run2(self):
        functions.del_sql_statistik()
        self.first_form = Menu()
        self.first_form.show()
        self.close()

    def run3(self):
        self.first_form = Menu()
        self.first_form.show()
        self.close()

    def run4(self):
        self.first_form = Dial()
        self.first_form.show()
        self.close()


class Dial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Отображение картинки')

        ## Изображение
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.pixmap = QPixmap(fname)
        # Если картинки нет, то QPixmap будет пустым,
        # а исключения не будет
        self.image = QLabel(self)
        self.image.move(80, 60)
        self.image.resize(250, 250)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(0, 330, 401, 71))
        self.pushButton.setObjectName("pushButton")
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Form", "Назад"))
        self.pushButton.clicked.connect(self.run1)

    def run1(self):
        self.first_form = Dop()
        self.first_form.show()
        self.close()
