import flet as ft
from flet import theme
from database import *

def MatchPage(page: ft.Page):
    page.title = "Flet Project"

    row_image_and_text = ft.Row(
        [
            ft.Image(src=f"./losgenericos/{getUserName(1)}.jpg", width=200, height=200, fit=ft.ImageFit.CONTAIN),
            ft.Text("MATCH", size=40, weight=ft.FontWeight.BOLD),
            ft.Image(src=f"./losgenericos/{getUserName(2)}.jpg", width=200, height=200, fit=ft.ImageFit.CONTAIN),
        ],
        alignment=ft.MainAxisAlignment.CENTER,    
    )


    hover_style = ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=10))
    btn_message=ft.FilledButton("Mensaje", on_click= lambda e: print("noseeeee"), on_hover=lambda e: (setattr(btn_message, "style", hover_style)))
    row_message = ft.Row(
        [
            btn_message
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    stack = ft.Stack(
            [
                ft.Container(height=100),
                ft.Image(
                    src=f"./imagenes/match.jpg",
                    width=page.window_width,
                    height=page.window_height,
                    fit=ft.ImageFit.COVER,
                ),     
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Text(
                                "| FaveFusion",
                                size=40,
                                weight=ft.FontWeight.BOLD,
                                text_align=ft.TextAlign.START,
                                width=page.window_width * 0.3,
                                color=ft.colors.GREEN_400
                            ),
                            margin=ft.margin.only(top=0, left=30, right=0, bottom=0)
                        ),
                        ft.Row(
                            [
                                ft.FilledButton("Home", on_click= lambda e: page.go("/home")),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                
                
                ft.Column(
                    [
                        row_image_and_text,
                        row_message
                    
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    height= 500
                )
            ]
        )
    return stack
