import flet as ft 
from complements.skills import idiomaring,skillpgb,locations,listcheck
class Sidebarheader(ft.UserControl):
    def build(self):
        return ft.Container(
            offset=ft.Offset(x=0,y=-0.1),
            content=ft.Column(
                spacing=2,
                controls=[
                    ft.Badge(
                        content=ft.Image(
                            src='my_foto.png',
                            border_radius=ft.border_radius.all(100),
                            width=80
                        ),
                        bgcolor=ft.colors.PRIMARY,
                        alignment=ft.alignment.bottom_right,
                        small_size=20,
                    ),
                    ft.Text(value='SHERLON MACHADO',theme_style=ft.TextThemeStyle.BODY_LARGE),
                    ft.Text(value='DESENVOLVEDOR FULLSTACK',theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                    
                ],horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),padding=ft.padding.symmetric(horizontal=40),
            alignment=ft.alignment.center
        )

class Sidebarcontent(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.expand=True
    def build(self):
        location=ft.Column(
            controls=[
               locations(title='NACINALIDADE',value='BRASIL'),
               locations(title='CIDADE',value='SALVADOR-BA'),
               locations(title='EMAIL',value='sherlonmachado20@gmail.com'),
            ]
        )
        idiomas=ft.Row(
            controls=[
                idiomaring(title='português',value=1.0),
                idiomaring(title='inglês',value=0.5),
                idiomaring(title='espanhol',value=0.5),
            ]
        )
        skills=ft.Column(
            controls=[
                skillpgb(title='python',value=1),
                skillpgb(title='java',value=0.8),
                skillpgb(title='sql',value=0.8),
                skillpgb(title='git',value=1),
                
            ]
        )
        tecnologies=ft.Container(
            content=ft.Column(
                controls=[
                    listcheck(valor='flet'),
                    listcheck(valor='django'),
                    listcheck(valor='sites e apps responsivos e multiplataforma'),
                    listcheck(valor='SQL relacionais e não relacionais'),
                    listcheck(valor='POO'),
                    listcheck(valor='versionamento com git'),
                    listcheck(valor='desenvolvimento full stack'),
                ],spacing=0,alignment=ft.MainAxisAlignment.START,scroll=ft.ScrollMode.AUTO
        ),height=200,expand=False
            )
        
        return ft.Container(
            bgcolor=ft.colors.BLACK12,
            padding=ft.padding.all(20),
            content=ft.Column(
                controls=[
                    location,
                    ft.Divider(height=30),
                    idiomas,
                    ft.Divider(height=30),
                    skills,
                    ft.Divider(height=30),
                    tecnologies,
                    ft.Divider(height=30),
                ],scroll=ft.ScrollMode.HIDDEN
            )
        )
    
class Sidebarfooter(ft.UserControl):
    def build(self):
        return ft.Container(
            padding=ft.padding.symmetric(vertical=10),
            content=ft.Row(
                controls=[
                ft.TextButton(
            text='download CV',
            style=ft.ButtonStyle(color=ft.colors.GREY),
            icon=ft.icons.DOWNLOAD,
            icon_color=ft.colors.WHITE,
            url='https://drive.google.com/uc?export=download&id=1Vru2eONvJDrtwXxxi_gEH839hGznQ-HK',),
                    ft.IconButton(
                        content=ft.Image(src='001-instagram.png',height=15,color='white'),
                        url='https://www.instagram.com/sherlon.py/',
                        bgcolor=ft.colors
                    ),
                    ft.IconButton(
                        content=ft.Image(src='002-linkedin.png',height=15,color='white'),
                        url='https://www.linkedin.com/in/sherlon-machado-980061245/',
                    ),
                    ft.IconButton(
                        content=ft.Image(src='003-github.png',height=15,color='white'),
                        url='https://github.com/SHERLON20',
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
class Sidebar(ft.UserControl):
    def build(self):
        return ft.Container(
            expand=True,
            content=ft.Column(
                controls=[
                    Sidebarheader(),
                    Sidebarcontent(),
                    Sidebarfooter(),
                    
                ]
            ),
            bgcolor=ft.colors.BACKGROUND,
        )