import flet as ft


def main(page: ft.Page):
    page.title = "Mi primer app en Flet Cloud"
    page.add(ft.Text("¡Hola DJ Fede desde Flet Cloud! 🚀", size=30, color="blue"))

ft.app(target=main, view=ft.AppView.WEB_BROWSER)

