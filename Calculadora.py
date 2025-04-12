
# TITULO CALCULADORA GEARHEAD
# botão começar 
# quando clicar no botão:
    # dialog 
        #titulo: Calcular Cilindrada
        # Campo de texto:
            # Digite o valor do cilindro
            # Digite o valor do curso
            # Digite o valor do diâmetro
        # botão calcular
            # quando clicar no botão calcular:
                # calcular a cilindrada
                # mostrar o resultado em um dialog

# botão sair

# importar o flet 

import Flet as ft



#definir a função principal

def main(page):
    #definir elementos
    titulo = ft.Text("Calculadora Gearhead", size=30, color="blue", weight="bold")

    titulo_janela = ft.Text("Calcular Cilindrada")
    campo_cilindro = ft.TextField(label="Digite o valor do cilindro")
    campo_curso = ft.TextField(label="Digite o valor do curso")
    campo_diametro = ft.TextField(label="Digite o valor do diâmetro")
    botao_calcular = ft.ElevatedButton("Calcular")

    janela = ft.AlertDialog(
        title=titulo_janela,
        content=ft.Column([
            campo_cilindro,
            campo_curso,
            campo_diametro,
        ]),
        actions=[botao_calcular],
    )
    
    def abrir_dialog(evento):
        print("abrindo dialog")
        janela.open = True
        page.update()
        
    botao_comecar = ft.ElevatedButton("Começar", on_click= abrir_dialog)

  #adicionar dialog na pagina

    page.dialog = janela
  
  
    #colocar elementos na tela
    page.add(titulo)
    page.add(botao_comecar)


ft.app(main, view=ft.WEB_BROWSER)

