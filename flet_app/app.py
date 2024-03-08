import flet as ft


def main(page):
    title = ft.Text(
        value="Hashzap!",
    )

    def send_message_tunnel(msg):
        msg_text = ft.Text(msg)
        chat.controls.append(msg_text)
        page.update()

    page.pubsub.subscribe(send_message_tunnel)

    def send_message(e):

        page.pubsub.send_all(f"{input_username.value}: {input_message.value}")
        page.update()

    chat = ft.Column([])
    input_message = ft.TextField(label="Message", on_submit=send_message)
    send_button = ft.ElevatedButton("Send", on_click=send_message)
    row_message = ft.Row([input_message, send_button])
    input_username = ft.TextField(label="Username")

    def enter_chat(e):
        popup.open = False
        page.remove(init_button)
        page.remove(title)
        page.add(chat)
        page.pubsub.send_all(f"{input_username.value}: has entered the chat")
        page.add(row_message)

        page.update()

    enter_button = ft.ElevatedButton("Enter Chat", on_click=enter_chat)

    popup = ft.AlertDialog(
        modal=True,
        open=False,
        title=ft.Text("Welcome to Hashzap!"),
        content=input_username,
        actions=[enter_button],
    )

    def show_popup(event):
        page.dialog = popup
        popup.open = True
        page.update()

    init_button = ft.ElevatedButton("Enter Chat", on_click=show_popup)

    page.add(title)
    page.add(init_button)


ft.app(target=main, view=ft.WEB_BROWSER)
