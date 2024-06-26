import flet as ft
from flet import Page as page
from database import *


def LoginPage(page: ft.Page, changeName, data_user):

    title =  ft.Text("Sign Up",width=300,size=35,text_align="center",weight="w900")
    nombre = ft.TextField(width=300,height=60,hint_text="Username",border="underline",color="black",prefix_icon = ft.icons.PERSON)
    email = ft.TextField(width=300,height=60,hint_text="E-mail",border="underline",color="black",prefix_icon = ft.icons.EMAIL )
    password = ft.TextField(width=300,height=60,hint_text="Password",border="underline",color="black",prefix_icon = ft.icons.LOCK,password= True )
    age = ft.Dropdown(width=300,height=60,hint_text="Age",options=[ft.dropdown.Option("18"),ft.dropdown.Option("19"),ft.dropdown.Option("20"),ft.dropdown.Option("21"),ft.dropdown.Option("22"),ft.dropdown.Option("23"),],prefix_icon = ft.icons.CALENDAR_VIEW_DAY_ROUNDED)
    gender = ft.Dropdown(width=300,height=60,hint_text="Gender",options=[ft.dropdown.Option("Male"),ft.dropdown.Option("Female"),ft.dropdown.Option("Other"),],prefix_icon = ft.icons.PERSON_2_OUTLINED)
    checkTerms = ft.Checkbox(label="I accept the terms and conditions",check_color = "black")


    def button_clicked(e):
        changeName({
            "ID": "",
            "username": nombre.value,
            "email": email.value,
            "password": password.value,
            "age": age.value,
        })

        if not checkTerms.value:
            print("You have accepted the terms and conditions")
            return

        # print(data_user)
        ejecutorDeQueries.execute("INSERT INTO usuarios (id_usuario, nombre, apellido, edad, genero, telefono, correo, descripcion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", ('',nombre.value,'',age.value, gender.value, '', email.value, '' ))
        mycon.commit()
        ejecutorDeQueries.execute(f"SELECT id_usuario FROM usuarios WHERE nombre = '{nombre.value}' and edad = {age.value} and correo = '{email.value}'")
        id_usuario = ejecutorDeQueries.fetchall()
        data_user.setID(id_usuario[0][0])
        # Resetear los campos
        nombre.value = ""
        email.value = ""
        password.value = ""
        age.value = ""
        gender.value = ""
        page.update()
        page.go("/home")



    page.title = "Login"
    loginPage = ft.Stack(
            [
                ft.Image(
                  src="./imagenes/Login.jpg",
                  width=page.window_width,
                  height=page.window_height,
                  fit=ft.ImageFit.COVER
                ),
                ft.Container(
                  content=ft.Column(
                    [
                      title,
                      nombre,
                      age,
                      gender,
                      email,
                      password,
                      ft.ElevatedButton(text="Submit", on_click= button_clicked),
                      checkTerms
                    ]
                  ),
                  bgcolor=ft.colors.GREEN_500,
                  width=300,
                  height=530,
                  margin=ft.margin.only(top=10, left=50, right=0, bottom=0),
                  border_radius=20,
                  padding=ft.padding.all(20),
                )
            ]
        )

    return loginPage