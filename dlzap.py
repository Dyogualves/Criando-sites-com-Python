# Frontend -> Usuari vê/INTERAGE
# Backend -> logica por traz do site 

# Titulo DLzap
# Botão de iniciar o chat 
    # Pop-up
        # Bem vindo ao DLzap
        # escreva seu nome
        # Entrar no chat

# chat
    # Dyogu entrou no chat
    # Mensagem do usuario
# Campo para enviar mensagem 
# Botão para enviar
import flet as ft 


def main(pagina):
    Titulo = ft.Text("DLZAP")
    
    nome_usuario = ft .TextField(label="Escreva seu nome")
    
    chat = ft.Column()
    
    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_mensagem(evento):
        # colocar o nome do usuario que enviou mensagem 
        texto_campo_mensagem = f"usuario: {nome_usuario.value}: {campo_mensagem.value}"
        pagina.pubsub.send_all(texto_campo_mensagem)
        #limpar campo de mensagem 
        campo_mensagem.value =""
        pagina.update()
        
    campo_mensagem = ft.TextField(label = "Escreva sua mensagem aqui", 
                                  on_submit= enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click= enviar_mensagem)
    

    def Entrar_chat(evento):
        # feche o popup
        popup.open =False
        # tire o botão "iniciar chat" da tela 
        pagina.remove(botao_iniciar)
        # adicionar nosso chat 
        pagina.add(chat)
        # criar o campo de enviar mensagem 
        linha_mensagem = ft.Row(
            [campo_mensagem, botao_enviar]
        )

        pagina.add(linha_mensagem)
        # botão de enviar mensagem 
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)
        pagina.update()


    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao DLZAP"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=Entrar_chat)]
        )

        

    def iniciar_chat(evento):
        pagina.dialog = popup  # Flet chama os popup de dialog
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("iniciar chat", on_click=iniciar_chat)

    pagina.add(Titulo)
    pagina.add(botao_iniciar)

#ft.app(main)
ft.app(main, view= ft.WEB_BROWSER)

