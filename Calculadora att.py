
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

import flet as ft

#definir a função principal

def main(page):
    #definir elementos
    titulo = ft.Text("Calculadora Gearhead", size=30, color="blue", weight="bold")

    def botao_calcular(evento):
       #fechar dialog, remover titulo e botao
        page.remove(titulo)
        page.remove(botao_comecar)
        page.close(janela)

        #pegar os valores dos campos
        curso = float(campo_curso.value)
        diametro = float(campo_diametro.value)

        #calcular a cilindrada
        cilindrada = (diametro**2) * 3.14 * (curso / 1000)

        #mostrar o resultado em um dialog
        resultado = ft.AlertDialog(
            title=ft.Text("Resultado"),
            content=ft.Text(f"A cilindrada é: {cilindrada:.2f}"),
            actions=[ft.TextButton("OK")],
        )
        page.open(resultado)

        
    botao_calcular = ft.ElevatedButton("Calcular", on_click=botao_calcular)


    titulo_janela = ft.Text("Calcular Cilindrada")
    campo_curso = ft.TextField(label="Digite o valor do curso do virabrequim (mm)")
    campo_diametro = ft.TextField(label="Digite o valor do diâmetro do pistão (mm)")
    

    janela = ft.AlertDialog(
        title=titulo_janela,
        content=ft.Column([
            campo_curso,
            campo_diametro,
        ]),
        actions=[botao_calcular],
    )


    
    def abrir_dialog(evento):
        print("abrindo dialog")
        page.open(janela)
        
    botao_comecar = ft.ElevatedButton("Começar", on_click=abrir_dialog)

    #colocar elementos na tela
    page.add(titulo)
    page.add(botao_comecar)


ft.app(main, view=ft.WEB_BROWSER)
