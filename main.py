import sys
import os
import re
from datetime import date
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                                QMessageBox, QLabel, QFileDialog, QTreeWidgetItem)

from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtGui import QPixmap, QIcon, QFont
from PySide6 import QtCore
from project_main_window import Ui_MainWindow
from project_widget_login import Ui_Login
from bases import DataBase
from xml_files import XmlReader
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from variables import ICON

class MyLogin(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(MyLogin, self).__init__()
        self.attempts = 0
        self.setupUi(self)
        self.setWindowTitle('KINGS - Login')
        icon = QIcon('files\\iconM.png')
        self.setWindowIcon(icon)

        self.button_login.clicked.connect(self.open_system)

        # Adiciona a imagem na tela de login
        self.label_image = QLabel(self)
        self.label_image.setGeometry(190, 100, 171, 161)
        pixmap = QPixmap('files\\login-user.png')
        self.label_image.setPixmap(pixmap)
        self.label_image.setScaledContents(True)

    def open_system(self):

        # Obtém o nome de usuário e a senha digitados
        username = self.input_user.text()
        password = self.input_password.text()

        # Autentica o usuário no banco de dados e obtém o perfil
        self.user_profile = self.authenticate_user(username, password)

        # Verifica se o perfil do usuário é válido e abre a janela principal se for
        if self.user_profile.lower() == 'admin' or self.user_profile.lower() == 'user':
            self.main_window = MyMainWindow(
                self.input_user.text(), self.user_profile.lower())
            self.main_window.show()
            self.close()
        else:
            if self.attempts < 3:
                msg = MyMessageBox()
                msg.setIcon(MyMessageBox.Warning)
                msg.setWindowTitle('KINGS - Error when accessing')
                msg.setText(f'incorrect username or password \n \n Attempt: {self.attempts +1} de 3')
                msg.exec()
                self.attempts += 1
            if self.attempts == 3:
                MyMessageBox.warning(self, "Login failed", "Authentication failure!")
                self.close()
                sys.exit(0)

    def authenticate_user(self, username, password):
        #Autentica o usuário no banco de dados e retorna o perfil
        db = DataBase()
        db.connect_()
        profile = db.check_user(username, password)
        db.close_connection()
        return profile


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, username, user) -> None:
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('KINGS - System Data Analysis')
        icon = QIcon('files\\iconM.png')
        self.setWindowIcon(icon)
        self.user = username
        self.path = ''

        if user.lower() == 'user':
            self.button_page_register.setVisible(False)

        # Connect signals to slots
        self.setup_button_connections()

        # filter
        self.line_filter.textChanged.connect(self.update_filter)

        # reset tables
        self.reset_table()

    def setup_button_connections(self):
        # Connect each button to its respective page
        self.button_home.clicked.connect(lambda: self.switch_page(self.page_home))
        self.button_importxml.clicked.connect(lambda: self.switch_page(self.page_importxml))
        self.button_tables.clicked.connect(lambda: self.switch_page(self.page_tables))
        self.button_about.clicked.connect(lambda: self.switch_page(self.page_about))
        self.button_contact.clicked.connect(lambda: self.switch_page(self.page_contact))
        self.button_page_register.clicked.connect(lambda: self.switch_page(self.page_register))
        self.button_signup.clicked.connect(self.register_user)

        # Arquivo XML
        self.button_open_import.clicked.connect(self.open_path)
        self.button_import_xml.clicked.connect(self.import_xml)

        # generate output e refund
        self.button_output.clicked.connect(self.generate_output)
        self.button_refund.clicked.connect(self.generate_refund)

        # generate excel and chart
        self.button_open_xlsx.clicked.connect(self.excel_file)
        self.button_open_chart.clicked.connect(self.graphic)


    def switch_page(self, page):
        # Set the current page widget
        self.Pages.setCurrentWidget(page)

    def register_user(self):

        try:
            if self.line_password.text() != self.line_password_2.text():
                msg = MyMessageBox()
                msg.setIcon(MyMessageBox.Warning)
                msg.setWindowTitle("KINGS - Passwords don't match")
                msg.setText('Passwords are not the same')
                msg.exec_()
                return None

            name = self.line_name.text()
            user = self.line_user.text()
            password = self.line_password.text()
            access = self.combo_box_profile.currentText()

            db = DataBase()
            db.connect_()
            db.insert_user(name, user, password, access)
            db.close_connection()

            msg = MyMessageBox()
            msg.setIcon(MyMessageBox.Information)
            msg.setWindowTitle('KINGS - User Registration')
            msg.setText('User registered successfully')
            msg.exec()

            self.line_name.setText('')
            self.line_user.setText('')
            self.line_password.setText('')
            self.line_password_2.setText('')
            

        except ValueError as e:
            print('Error:', e)

    def open_path(self):
        # Abre o diálogo para selecionar o diretório
        directory = QFileDialog.getExistingDirectory(
            self, "Open Directory", '/home', QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        
        # Verifica se o diretório selecionado não está vazio
        if directory:
            # Atualiza o campo de entrada na interface gráfica com o caminho selecionado
            self.line_import.setText(directory)

            # Exibe os arquivos encontrados no diretório selecionado para fins de depuração
            print("Arquivos encontrados no diretório selecionado:")
            for file_name in os.listdir(directory):
                print(os.path.join(directory, file_name))
        else:
            print("Nenhum diretório selecionado.")
            self.line_filter.setText(self.path)
    
    def import_xml(self):
        # Obter o caminho do diretório a partir do campo de entrada na interface gráfica
        directory = self.line_import.text()
        
        # Verificar se o diretório está vazio
        if not directory:
            msg = MyMessageBox()
            msg.setIcon(MyMessageBox.Warning)
            msg.setText("Please select a directory.")
            msg.setWindowTitle("KINGS - Directory Error")
            msg.exec()
            return

        # Criar uma instância do XmlReader
        xml = XmlReader(directory)

        # Obter todos os arquivos XML no diretório selecionado
        all_files = xml.all_files()

        # Definir o máximo da barra de progresso para o número de arquivos XML encontrados
        self.progressBar.setMaximum(len(all_files))

        # Conectar ao banco de dados
        db = DataBase()
        db.connect_()

        try:
            # Iterar sobre cada arquivo XML e importar os dados para o banco de dados
            for file_name in all_files:
                # Atualizar o valor da barra de progresso
                self.progressBar.setValue(self.progressBar.value() + 1)
                
                # Ler os dados do arquivo XML
                full_data_set = xml.nfe_data(file_name)

                # Inserir os dados no banco de dados
                db.insert_data(full_data_set)

            # Exibir uma mensagem de conclusão
            msg = MyMessageBox()
            msg.setIcon(MyMessageBox.Information)
            msg.setText("Import completed successfully.")
            msg.setWindowTitle("KINGS - XML Import")
            msg.exec()
        except Exception as e:
            # Exibir uma mensagem de erro em caso de falha na importação
            msg = MyMessageBox()
            msg.setIcon(MyMessageBox.Critical)
            msg.setText(f"An error occurred during XML import: {str(e)}")
            msg.setWindowTitle("KINGS - Import Error")
            msg.exec()
        finally:
            # Resetar o valor da barra de progresso
            self.progressBar.setValue(0)

        # Fechar a conexão com o banco de dados
        db.close_connection()

    def storage_table(self):
        """Atualiza a tabela de armazenamento."""
        self.table_storage.setStyleSheet(
            u' QHeaderView{color:black}; color:#fff; font-size: 15px;')

        cn = sqlite3.connect('System.db')
        result = pd.read_sql_query("SELECT * FROM Notas WHERE date_output = ''", cn)
        result = result.values.tolist()

        self.x = ''

        for i in result:
            # faz o check para identificar a mesma nota e adicionar um nivel
            if i[0] == self.x:
                QTreeWidgetItem(self.field, i)
            else:
                self.field = QTreeWidgetItem(self.table_storage, i)
                self.field.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

            self.x = i[0]

        self.table_storage.setSortingEnabled(True)
        
        for i in range(1, 15):
            self.table_storage.resizeColumnToContents(i)

    def input_table(self):
        """Atualiza a tabela de entrada."""
        self.table_input.setStyleSheet(
            u' QHeaderView{color:black}; color:#fff; font-size: 15px;')

        cn = sqlite3.connect('System.db')
        result = pd.read_sql_query("""SELECT nfe, serial, date_import, date_output, user FROM Notas WHERE date_output != ''""", cn)
        result = result.values.tolist()

        self.x = ''

        for i in result:
            # faz o check para identificar a mesma nota e adicionar um nivel
            if i[0] == self.x:
                QTreeWidgetItem(self.field, i)
            else:
                self.field = QTreeWidgetItem(self.table_input, i)
                self.field.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

            self.x = i[0]

        self.table_input.setSortingEnabled(True)
        
        for i in range(1, 15):
            self.table_input.resizeColumnToContents(i)

    def general_table(self):
        """Atualiza a tabela geral."""
        self.table_storage.setStyleSheet(
            u' QHeaderView{color:black}; color:#fff; font-size: 15px;')

        db = QSqlDatabase('QSQLITE')
        db.setDatabaseName('System.db')
        db.open()

        self.model = QSqlTableModel(db=db)
        self.table_general.setModel(self.model)
        self.model.setTable('Notas')
        self.model.select()

    def reset_table(self):
        """Redefine as tabelas."""
        self.table_storage.clear()
        self.table_input.clear()

        self.input_table()
        self.storage_table()
        self.general_table()

    def update_filter(self, s):
        """Atualiza o filtro."""
        s = re.sub('[\\W_]+', '', s)
        filter_str = 'nfe LIKE "%{}%"'.format(s)
        self.model.setFilter(filter_str)

    def generate_output(self):
        """Gera a saída."""
        # Inicializa a lista de itens selecionados como vazia
        self.checked_items_out = []

        # Função interna recursiva para percorrer os itens na árvore da tabela de armazenamento
        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                # Verifica se o item filho está marcado como selecionado
                if child.checkState(0) == QtCore.Qt.Checked:
                    # Adiciona o texto do item à lista de itens selecionados
                    self.checked_items_out.append(child.text(0))
                # Verifica se o item filho tem subitens e recursivamente chama a função para eles
                if child.childCount() > 0:
                    recurse(child)

        # Chama a função recursiva começando pelo item raiz da tabela de armazenamento
        recurse(self.table_storage.invisibleRootItem())

        # Verifica se há itens selecionados
        if self.checked_items_out:
            # Se houver itens selecionados, exibe uma mensagem de confirmação
            self.question('output')
        else:
            # Se não houver itens selecionados, exibe uma mensagem de aviso
            msg = MyMessageBox()
            msg.setIcon(MyMessageBox.Warning)
            msg.setText("Please select at least one item to output.")
            msg.setWindowTitle("KINGS - Output Error")
            msg.exec()

    # Método question e demais funcionalidades continuam aqui...

    
    def generate_refund(self):
        """Gera o reembolso."""
        self.checked_items = []

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                if child.checkState(0) == QtCore.Qt.Checked:
                    self.checked_items.append(child.text(0))

        recurse(self.table_input.invisibleRootItem())

        if not self.checked_items:
            msg = MyMessageBox()
            msg.setIcon(MyMessageBox.Warning)
            msg.setText("Please select at least one item to refund.")
            msg.setWindowTitle("KINGS - Refund Error")
            msg.exec()
        else:
            print(self.checked_items)  # Adicione esta linha para verificar se os itens estão sendo capturados corretamente
            self.question('refund')


    def question(self, table):
        """Pergunta para confirmação."""
        msg = MyMessageBox()

        if table == 'refund':
            msg.setText('Do you want to refund the selected notes?')
            msg.setInformativeText('The selected items will return to the stock.\
                                    Click on "Yes" to continue.')
            msg.setStandardButtons(MyMessageBox.Yes | MyMessageBox.No)
            msg.setDetailedText(f'Notas: {self.checked_items}')

            
        else:
            msg.setText('Do you want to generate the output of the selected notes?')
            msg.setInformativeText('The notes below will be deducted from the stock. '
                        'Click on "Yes" to continue.')
            msg.setStandardButtons(MyMessageBox.Yes | MyMessageBox.No)
            msg.setDetailedText(f'Notas: {self.checked_items_out}')


        msg.setIcon(MyMessageBox.Question)
        ret = msg.exec()

        if ret == MyMessageBox.Yes:
            if table == 'refund':
                self.db = DataBase()
                self.db.connect_()
                self.db.update_refund(self.checked_items)
                self.db.close_connection()
                self.reset_table()
            else:
                date_output = date.today()
                date_output = date_output.strftime('%d/%m/%Y')
                self.db = DataBase()
                self.db.connect_()
                self.db.update_storage(date_output, self.user, self.checked_items_out)
                self.db.close_connection()
                self.reset_table()

    def excel_file(self):
        """Cria um arquivo Excel."""
        cn = sqlite3.connect('System.db')

        result = pd.read_sql_query('SELECT * FROM Notas', cn)
        result.to_excel('Note summary.xlsx', sheet_name='Notas', index=False)

        msg = MyMessageBox()
        msg.setIcon(MyMessageBox.Information)
        msg.setWindowTitle('KINGS - Grade Report')
        msg.setText('Report generated successfully')
        msg.exec()

    def graphic(self):
        """Cria um gráfico."""
        cn = sqlite3.connect('System.db')  
        
        storage = pd.read_sql_query('SELECT * FROM Notas', cn)
        output = pd.read_sql_query(
            "SELECT * FROM Notas WHERE date_output != ''", cn)

        storage_count = len(storage)
        output_count = len(output)

        labels = 'Storage', 'Outputs'
        sizes = [storage_count, output_count]

        fig, ax1 = plt.subplots(1, 2, figsize=(10, 5))

        # Gráfico de pizza
        ax1[0].pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1[0].set_title('Storage vs Outputs')
        ax1[0].axis('equal')

        # Gráfico de barras (exemplo - você precisa adicionar seus próprios dados aqui)
        x = ['Category A', 'Category B', 'Category C']
        y = [20, 35, 30]
        ax1[1].bar(x, y)
        ax1[1].set_xlabel('Categories')
        ax1[1].set_ylabel('Values')
        ax1[1].set_title('Storage vs Outputs')

        plt.tight_layout()
        plt.show()

class MyMessageBox(QMessageBox):
    def __init__(self, parent=None):
        super(MyMessageBox, self).__init__(parent)
        
        self.setStyleSheet("QMessageBox { color: #fff; background-color: #385273; }"
                           "QPushButton { color: white; background-color: #323050; }"
                           "QPushButton:hover { color: black; background-color: #C9DFF2; }")
        
        self.setFont(QFont("Arial", 10))
        self.icon = QIcon(str(ICON))
        self.setWindowIcon(self.icon)
        self.setWindowTitle('KINGS')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = DataBase()
    db.connect_()
    db.create_table_users()  # Certifica-se de que a tabela de usuários esteja criada
    login = MyLogin()
    login.show()
    sys.exit(app.exec())
