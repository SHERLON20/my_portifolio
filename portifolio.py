import flet as ft 
from partions.sidebar import Sidebar
from partions.content import maincontent
class apptheme:
    theme=ft.Theme(
        color_scheme=ft.ColorScheme(
            background='#20202a',
            on_background='#2d2d3a',
            primary=ft.colors.AMBER,
            on_inverse_surface='#2d2d3a'
        ),
        text_theme=ft.TextTheme(
            body_large=ft.TextStyle(
                weight=ft.FontWeight.BOLD,
                color=ft.colors.WHITE,
                size=14,
            ),
            body_medium=ft.TextStyle(
                weight=ft.FontWeight.NORMAL,
                color=ft.colors.GREY,
                size=14
            ),
            headline_large=ft.TextStyle(
                weight=ft.FontWeight.W_900,
                color=ft.colors.WHITE,
                size=50
            ),
            label_large=ft.TextStyle(
                weight=ft.FontWeight.W_700,
                color=ft.colors.WHITE,
                size=16
            ),
            headline_medium=ft.TextStyle(
                weight=ft.FontWeight.W_700,
                color=ft.colors.WHITE,
                size=30
            )
        ),#abaixo tem o codigo para deixar o scroll transparente nas versões web e desktop
        scrollbar_theme=ft.ScrollbarTheme(
            track_visibility=False,
            thumb_visibility=False,
            track_color={ft.MaterialState.DEFAULT: ft.colors.TRANSPARENT},
            thumb_color={ft.MaterialState.HOVERED:ft.colors.TRANSPARENT,ft.MaterialState.DEFAULT:ft.colors.TRANSPARENT}
        )
    )

class app:
    def __init__(self,page:ft.Page) -> None:
        self.page=page
        self.page.theme=apptheme.theme
        self.page.on_resize=self.show_app_bar
        self.page.theme_mode=ft.ThemeMode.DARK
        self.main()
        self.show_app_bar()
    def togle_sidebar(self,e):
        self.sidebar.col['xs']=12 if self.sidebar.col['xs']==0 else 0    
        self.content.col['xs']=0 if self.content.col['xs']==12 else 12
        self.page.update()    
    def show_app_bar(self,e=None):
        if self.page.width<768:
            self.page.appbar=ft.AppBar(
                leading=ft.IconButton(
                    icon=ft.icons.MENU,
                    icon_color=ft.colors.WHITE,
                    on_click=self.togle_sidebar
                ),bgcolor=ft.colors.BACKGROUND
            )
        else:
            self.page.appbar=None
        self.page.update()
    def main(self):
        self.sidebar=Sidebar(col={'xs':0,'md':5,'lg':4,'xxl':3})
        self.content=maincontent(col={'xs':12,'md':7,'lg':8,'xxl':9})
        layout=ft.ResponsiveRow(
            columns=12,
            controls=[
                self.sidebar,
                self.content
            ],expand=True,
        )
        self.page.add(layout)
ft.app(target=app,assets_dir="assets")