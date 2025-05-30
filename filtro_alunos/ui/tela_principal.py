# ui/tela_principal.py
import os
from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QDateEdit, QTableWidget, QTableWidgetItem, QFileDialog, QMessageBox
)
from PyQt6.QtCore import QDate
from db.consulta import buscar_alunos_bloqueados
from export.exportar_excel import exportar_para_excel

class TelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Filtro de Alunos Bloqueados")
        self.setGeometry(100, 100, 800, 500)

        # Campos de data
        self.data_inicio = QDateEdit()
        self.data_inicio.setCalendarPopup(True)
        self.data_inicio.setDate(QDate.currentDate().addMonths(-1))

        self.data_fim = QDateEdit()
        self.data_fim.setCalendarPopup(True)
        self.data_fim.setDate(QDate.currentDate())

        # Botões
        self.botao_buscar = QPushButton("Buscar Bloqueados")
        self.botao_exportar = QPushButton("Exportar para Excel")
        self.botao_exportar.setEnabled(False)  # só libera após buscar dados

        # Tabela para mostrar resultados
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(4)
        self.tabela.setHorizontalHeaderLabels(["Nome", "Status", "Telefone", "Data Nascimento"])

        # Layout dos filtros
        layout_filtros = QHBoxLayout()
        layout_filtros.addWidget(QLabel("Data Início:"))
        layout_filtros.addWidget(self.data_inicio)
        layout_filtros.addWidget(QLabel("Data Fim:"))
        layout_filtros.addWidget(self.data_fim)
        layout_filtros.addWidget(self.botao_buscar)
        layout_filtros.addWidget(self.botao_exportar)

        # Layout principal
        layout_principal = QVBoxLayout()
        layout_principal.addLayout(layout_filtros)
        layout_principal.addWidget(self.tabela)

        self.setLayout(layout_principal)

        # Conexões dos botões
        self.botao_buscar.clicked.connect(self.buscar)
        self.botao_exportar.clicked.connect(self.exportar)

        # Dados atuais buscados
        self.dados_atual = []

    def buscar(self):
        data_ini = self.data_inicio.date().toString("yyyy-MM-dd")
        data_fim = self.data_fim.date().toString("yyyy-MM-dd")

        try:
            resultados = buscar_alunos_bloqueados(data_ini, data_fim)
            self.dados_atual = resultados

            self.tabela.setRowCount(len(resultados))
            for i, row in enumerate(resultados):
                for j, valor in enumerate(row):
                    self.tabela.setItem(i, j, QTableWidgetItem(str(valor)))

            self.botao_exportar.setEnabled(len(resultados) > 0)

            if len(resultados) == 0:
                QMessageBox.information(self, "Nenhum resultado", "Nenhum aluno bloqueado encontrado neste período.")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao buscar dados:\n{str(e)}")

    def exportar(self):
        if not self.dados_atual:
            QMessageBox.warning(self, "Aviso", "Nenhum dado para exportar. Busque os dados primeiro.")
            return

        caminho, _ = QFileDialog.getSaveFileName(self, "Salvar arquivo", os.path.expanduser("~"),
                                                 "Excel Files (*.xlsx)")
        if caminho:
            try:
                exportar_para_excel(self.dados_atual, caminho)
                QMessageBox.information(self, "Sucesso", f"Arquivo salvo em:\n{caminho}")
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao exportar para Excel:\n{str(e)}")


