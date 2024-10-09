from typing import Any, List,Dict,Union
import flet as ft 
import math
class priceitem(ft.UserControl):
    def __init__(self,preco:int,url:str,intens_inclused:list[dict[str,Union[str,bool]]],**kwargs):
        super().__init__(**kwargs)
        self.preco=preco
        self.url=url
        self.item=intens_inclused
    def build(self):
        return ft.Container(
            bgcolor=ft.colors.ON_INVERSE_SURFACE,
            padding=ft.padding.symmetric(vertical=20,horizontal=50),
            content=ft.Column(
                controls=[
                ft.Text(value='pagamento por hora',theme_style=ft.TextThemeStyle.LABEL_LARGE,size=30),
                ft.Text(
                    spans=[
                        ft.TextSpan(text='R$',style=ft.TextStyle(color=ft.colors.WHITE)),
                        ft.TextSpan(text=f' {self.preco} ',style=ft.TextStyle(color=ft.colors.PRIMARY,weight=ft.FontWeight.BOLD,size=50)),
                        ft.TextSpan(text='/hora',style=ft.TextStyle(color=ft.colors.WHITE)),
                    ]
                ),
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Icon(
                                name=ft.icons.CHECK if item['is_included'] else ft.icons.CLOSE,
                                color=ft.colors.PRIMARY
                            ),
                                ft.Text(value=item['title'],theme_style=ft.TextThemeStyle.BODY_MEDIUM)
                            ],alignment=ft.MainAxisAlignment.CENTER
                            ) for item in self.item
                    ]
                ),
                ft.TextButton(
                    content=ft.Row(
                        controls=[
                            ft.Text(value='quero este',theme_style=ft.TextThemeStyle.BODY_LARGE,color=ft.colors.PRIMARY),
                            ft.Icon(name=ft.icons.ARROW_FORWARD_IOS,size=14,color=ft.colors.PRIMARY),
                            
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),url=self.url,
                )
           ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
        )

class itempopular(priceitem):
    def build(self):
        price_item=super().build()
        return ft.Stack(
            controls=[
                price_item,
                ft.Container(
                    bgcolor=ft.colors.PRIMARY,
                    content=ft.Text(value='popular',color=ft.colors.BLACK,weight=ft.FontWeight.BOLD),
                    padding=ft.padding.symmetric(vertical=5,horizontal=50),
                    right=-40,
                    top=15,
                    rotate=ft.Rotate(angle=math.radians(40)),
                )
            ]
        )

class projectitem(ft.UserControl):
    def __init__(self,title:str,description:str,url:str,**kwargs):
        super().__init__(**kwargs)
        self.title=title
        self.description=description
        self.url=url
            
    def build(self):
        return ft.Container(
            padding=ft.padding.all(30),
            bgcolor=ft.colors.ON_INVERSE_SURFACE,
            content=ft.Column(
                controls=[
                    ft.Text(value=self.title,theme_style=ft.TextThemeStyle.LABEL_LARGE),
                    ft.Text(value=self.description),
                    ft.TextButton(
                        content=ft.Row(
                            controls=[
                                ft.Text(value='ver ao vivo',theme_style=ft.TextThemeStyle.BODY_LARGE,color=ft.colors.PRIMARY,weight=ft.FontWeight.BOLD),
                                ft.Icon(name=ft.icons.ARROW_FORWARD_IOS,size=15,color=ft.colors.PRIMARY),
                            ],tight=True
                        ),url=self.url,
                    )
            ]
                )
        )
class maincontent(ft.UserControl):
    def __init__(self,**kawargs):
        super().__init__(**kawargs)
        self.expand=True
    def build(self):
        banner=ft.Container(
            image_src='bg.jpg',
            image_fit=ft.ImageFit.COVER,
            image_repeat=ft.ImageRepeat.NO_REPEAT,
            image_opacity=0.5,
            bgcolor=ft.colors.BACKGROUND,
            margin=ft.margin.only(top=30),
            shadow=ft.BoxShadow(color=ft.colors.ON_BACKGROUND,offset=ft.Offset(x=0,y=-60),spread_radius=-30),
            content=ft.ResponsiveRow(
                columns=12,
                vertical_alignment=ft.CrossAxisAlignment.END,
                controls=[
                    ft.Container(
                        col={'md':12,'lg':8,'xs':12},
                        padding=ft.padding.all(50),
                        content=ft.Column(
                            controls=[
                                ft.Text(value='descubra meu incrivel portifólio',theme_style=ft.TextThemeStyle.HEADLINE_LARGE),
                                ft.Text(
                                    spans=[
                                        ft.TextSpan(text='<'),
                                        ft.TextSpan(text='code',style=ft.TextStyle(color=ft.colors.PRIMARY)),
                                        ft.TextSpan(text='> '),
                                        
                                        ft.TextSpan(text='Eu Desenvolvo aplicativos IOS e ANDROID, softwares para MaCOS, windows e linux, alem de web sites responsivéis',style=ft.TextStyle(color=ft.colors.WHITE)),
                                        
                                        ft.TextSpan(text=' </'),
                                        ft.TextSpan(text='code',style=ft.TextStyle(color=ft.colors.PRIMARY)),
                                        ft.TextSpan(text='> '),
                                    ],theme_style=ft.TextThemeStyle.BODY_MEDIUM
                                ),
                                ft.ElevatedButton(
                                    bgcolor=ft.colors.PRIMARY,
                                    content=ft.Text(value='Explore Agora',color=ft.colors.BLACK,weight=ft.FontWeight.BOLD),
                                    url='https://github.com/SHERLON20?tab=repositories',
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),
                                )
                            ],spacing=20,alignment=ft.MainAxisAlignment.CENTER
                        )
                    ),
                    ft.Container(
                        col={'md':12,'lg':4,'xs':12},
                        content=ft.Image(
                            src='foto_1.png',
                        )
                    )
                ]
            )
        )
        experiencia=ft.Container(
            padding=ft.padding.symmetric(vertical=20),
            content=ft.ResponsiveRow(
                columns=12,
                controls=[
                    ft.Text(
                        col={'xs':6,'md':3},
                        spans=[
                            ft.TextSpan(text='3+ ',style=ft.TextStyle(color=ft.colors.PRIMARY,weight=ft.FontWeight.W_900,size=20)),
                            ft.TextSpan(text='anos de experiência',style=ft.TextStyle(color=ft.colors.WHITE,size=20)),
                        ]
                    ),
                    ft.Text(
                        col={'xs':6,'md':3},
                        spans=[
                            ft.TextSpan(text='50+ ',style=ft.TextStyle(color=ft.colors.PRIMARY,weight=ft.FontWeight.W_900,size=20)),
                            ft.TextSpan(text='projetos concluídos',style=ft.TextStyle(color=ft.colors.WHITE,size=20)),
                        ]
                    ),
                    ft.Text(
                        col={'xs':6,'md':3},
                        spans=[
                            ft.TextSpan(text='50+ ',style=ft.TextStyle(color=ft.colors.PRIMARY,weight=ft.FontWeight.W_900,size=20)),
                            ft.TextSpan(text='clientes satisfeitos',style=ft.TextStyle(color=ft.colors.WHITE,size=20)),
                        ]
                    ),
                    ft.Text(
                        col={'xs':6,'md':3},
                        spans=[
                            ft.TextSpan(text='3+ ',style=ft.TextStyle(color=ft.colors.PRIMARY,weight=ft.FontWeight.W_900,size=20)),
                            ft.TextSpan(text='linguaguens de domínio',style=ft.TextStyle(color=ft.colors.WHITE,size=20)),
                        ]
                    ),
                ]
            )
        )
        projetos=ft.ResponsiveRow(
            columns=12,
            controls=[
                projectitem(title='app de listas de compras/afazeres',
                            description='um aplicativo para organizar as compras no dia a dia\nou organizar a rotina de caminha e etc...',
                            url='https://todo-app-by35.onrender.com',
                            col={'xs':12,'md':6,'lg':4}
                            ),
                projectitem(title='gerador de senhas ',
                            description='um sistema que vai te entregar uma senha ao seu gosto\ne ainda tem a funcionalidade de copiar a senha',
                            url='https://gerador-de-senhas-442e.onrender.com',
                            col={'xs':12,'md':6,'lg':4}
                            ),
                projectitem(title='card do clash of clans',
                            description='uma copia de um card de jogos do clash of clans.',
                            url='https://clash-of-clans-card-1.onrender.com',
                            col={'xs':12,'md':6,'lg':4}
                            ),
                projectitem(title='jogo da forca',
                            description='um app de jogo da forca bem intuitivo na versão web',
                            url='https://jogo-da-forca-github-io.onrender.com/',
                            col={'xs':12,'md':6,'lg':4}
                            ),
                projectitem(title='card de vendas online',
                            description='um card autêntico de qualquer site de vendas online de hoje em dia.',
                            url='https://card-de-vendas-online.onrender.com',
                            col={'xs':12,'md':6,'lg':4}
                            ),
                projectitem(title='calculadora',
                            description='um app que simula uma calculadora do iphone',
                            url='https://calculadora-kfvm.onrender.com',
                            col={'xs':12,'md':6,'lg':4},
                ),
                projectitem(title='hábito app',
                            description='um app pra auxiliar na maratona de manter seus habitos/hobby bem organizado.',
                            url='https://habito-app.onrender.com',
                            col={'xs':12,'md':6,'lg':4},
                            ),
                projectitem(title='chat de conversas',
                            description='um chat desenvolvido para conversas com pessoas distantes ',
                            url='https://chat-k5nj.onrender.com',
                            col={'xs':12,'md':6,'lg':4},
                            )
                
            ],
            spacing=30,
            run_spacing=30,
        )
        precos=ft.ResponsiveRow(
            columns=12,
            spacing=30,
            run_spacing=30,
            controls=[
                priceitem(preco=20,
                          url='mailto:sherlonmachado20@gmail.com',
                          intens_inclused=[{'title':'prototipagem',"is_included":True},
                                           {'title':'desenvolvimento web',"is_included":True},
                                           {'title':'aplicativo multiplataforma',"is_included":False},
                                           {'title':'manutenção por 12 horas',"is_included":False},
                                           ],
                          col={'xs':12,'md':6,'lg':6,'xxl':4}
                          ),
                itempopular(preco=100,
                          url='mailto:sherlonmachado20@gmail.com',
                          intens_inclused=[{'title':'prototipagem',"is_included":True},
                                           {'title':'desenvolvimento web',"is_included":True},
                                           {'title':'aplicativo multiplataforma',"is_included":True},
                                           {'title':'manutenção por 12 horas',"is_included":False},
                                           ],
                          col={'xs':12,'md':6,'lg':6,'xxl':4}
                          ),
                priceitem(preco=200,
                          url='mailto:sherlonmachado20@gmail.com',
                          intens_inclused=[{'title':'prototipagem',"is_included":True},
                                           {'title':'desenvolvimento web',"is_included":True},
                                           {'title':'aplicativo multiplataforma',"is_included":True},
                                           {'title':'manutenção por 12 horas',"is_included":True},
                                           ],
                          col={'xs':12,'md':6,'lg':6,'xxl':4}
                          ),
            ]
        )
        logos=ft.Container(
            padding=ft.padding.all(30),
            opacity=0.6,
            content=ft.ResponsiveRow(
                columns=12,
                controls=[
                    ft.Image(
                        src='brand-1-464x512.png',
                        col={'xs':6,'lg':3,'xl':3,'md':3}
                    ),
                    ft.Image(
                        src='brand-2-458x512.png',
                        col={'xs':6,'lg':3,'xl':3,'md':3}
                ),
                    ft.Image(
                        src='brand-3-456x512.png',
                        col={'xs':6,'lg':3,'xl':3,'md':3}
                ),
                    ft.Image(
                        src='brand-1-464x512.png',
                        col={'xs':6,'lg':3,'xl':3,'md':3}
                ),
                ]
            )
        )
        footer=ft.Container(
            bgcolor=ft.colors.ON_INVERSE_SURFACE,
            padding=ft.padding.all(30),
            content=ft.ResponsiveRow(
                columns=12,
                controls=[
                    ft.Text(
                        col={'xs':12,'md':6},
                        value='₢ 2024 todos os direitos reservados',
                        theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                        
                    ),
                    ft.Text(
                        col={'xs':12,'md':6},
                        spans=[
                            ft.TextSpan(text='E-MAIL: ',style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                            ft.TextSpan(
                                text='sherlonmachado20@gmail.com',
                                url='mailto:sherlonmachado20@gmail.com'
                            )
                        ],
                        theme_style=ft.TextThemeStyle.BODY_MEDIUM
                    )
                ]
            )
        )
        def titulo(titulo:str):
            return ft.Container(
                padding=ft.padding.symmetric(vertical=20),
                content=ft.Text(value=titulo,theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)
            )
        return ft.Container(
            content=ft.Column(
                controls=[
                    banner,
                    experiencia,
                    titulo(titulo='projetos'),
                    projetos,
                    titulo(titulo='preços'),
                    precos,
                    #testemunhos,
                    logos,
                    footer
                ],scroll=ft.ScrollMode.ADAPTIVE
            ),bgcolor=ft.colors.BACKGROUND,padding=ft.padding.all(30)
        )
        