import flet as ft

def main(page: ft.Page):
     page.bgcolor = "#289cbf"
     mensagem= ft.Text("Escolha a opção correta!", color="#0f0c0c")
     resposta_correta = "Patrick" 

     def verificar_resposta(e):
        if e.control.content == resposta_correta:
             mensagem.value = "Parabéns"
        else:
            mensagem.value ="Resposta errada"
     page.update()
     
    #  page.add(ft.Text (e.control.content))
    
     page.title = "Game: Adivinhe o nome do melhor amigo do Bob Esponja"
     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
     page.vertical_alignment = ft.MainAxisAlignment.CENTER

     page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "Adivinhe quem é o melhor amigo do Bob Esponja",
                    size=24,
                    weight="bold",
                    color= "black"
                ),
                ft.Image(
                    src="images/bob esponja 2.webp",
                    height=200
                ),
               ft.Row(
                   controls=[
                       ft.Button(
                           content="Patrick",
                           on_click=verificar_resposta
                       ),
                       ft.Button(
                           content="Lula mulusco",
                           on_click=verificar_resposta
                       ),
                       ft.Button(
                           content="Plankton",
                           on_click=verificar_resposta
                       ),
                   ],
                   alignment=ft.MainAxisAlignment.CENTER
               ),
               mensagem
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.run(main)