from openpyxl import Workbook

def exportar_para_excel(dados, caminho_arquivo):
    wb = Workbook()
    ws = wb.active
    ws.append(["Nome", "Status", "Telefone", "Data Nascimento"])

    for row in dados:
        ws.append(row)

    wb.save(caminho_arquivo)
