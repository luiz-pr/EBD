from PyQt5 import  uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user = 'root',
    password = '',
    database = 'EBD'
)

def funcao_principal():
    nome = formulario.lineEdit.text()
    departamento = formulario.lineEdit_2.text()
    trazer = ""
    categoria = ""

    print('-------------------------------------------------------------')
    print('Nome: ', nome)
    print('Departamento: ', departamento)
    if formulario.checkBox.isChecked():
        print('Trouxe Revista: Sim')
        trazer = "Revista"

    elif formulario.checkBox_2.isChecked():
        print('Trouxe Bíblia: Sim')
        trazer = "Bíblia"

    elif formulario.checkBox_3.isChecked():
        print('Trouxe Visitante: Sim')
        trazer = "Visitante"



    if formulario.radioButton_4.isChecked():
        print('Classe Ester')
        categoria = "Ester"

    elif formulario.radioButton_5.isChecked():
        print('Classe Débora')
        categoria = "Ester"

    elif formulario.radioButton_6.isChecked():
        print('Classe Varões')
        categoria = "Varões"

    elif formulario.radioButton_7.isChecked():
        print('Classe Mocidade')
        categoria = "Mocidade"

    elif formulario.radioButton_8.isChecked():
        print('Classe Mensageiros da Fé')
        categoria = "Mensageiros"

    elif formulario.radioButton_9.isChecked():
        print('Classe Primários')
        categoria = "Primários"

    elif formulario.radioButton_10.isChecked():
        print('Classe Juniôres')
        categoria = "Juniores"

    elif formulario.radioButton_11.isChecked():
        print('Classe Ovelinhas de Cristo')
        categoria = "Ovelinhas"

    cursor = banco.cursor()
    comando_SQL = "insert into cadastro (nome, departamento, trazer, categoria) values (%s, %s, %s, %s)"
    dados = (str(nome), str(departamento), trazer, categoria)
    cursor.execute(comando_SQL, dados)
    banco.commit()

print('-------------------------------------------------------------')


app = QtWidgets.QApplication([])
formulario = uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

valores = formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()

print('-------------------------------------------------------------')
