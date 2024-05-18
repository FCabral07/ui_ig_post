import flet as ft

def main(page: ft.Page):
    def clicked(e):
        e.control.selected = not e.control.selected
        e.control.update()
    
    page.title= 'Post Instagram'
    
    # Configs
    page.bgcolor = ft.colors.BLACK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Container principal
    layout = ft.Container(
        bgcolor= ft.colors.WHITE,
        width= 500,
        height= 650,
        border_radius= 10,
        shadow= ft.BoxShadow(blur_radius= 20, color= ft.colors.TEAL),
        content= ft.Column(
            controls= [
                ft.ListTile(
                    title= ft.Text(value= 'flamengo', color= ft.colors.BLACK, weight= ft.FontWeight.BOLD),
                    subtitle= ft.Text('Estádio do Maracanã', color= ft.colors.BLACK),
                    leading= ft.Image(
                        src= 'https://pbs.twimg.com/profile_images/1757399549281247232/Cbf7FO8E_400x400.jpg',
                        fit= ft.ImageFit.CONTAIN,
                        border_radius= 25
                    ),
                    trailing= ft.Icon(name= ft.icons.MORE_HORIZ, color= ft.colors.BLACK)
                ),
                
                ft.Image(
                    src= 'https://pbs.twimg.com/media/GNtNExoXAAAAf_g?format=jpg&name=4096x4096',
                    
                ),
                ft.Container(
                    content= ft.Column(
                        controls=[
                            ft.ResponsiveRow(
                                columns= 12,
                                vertical_alignment= ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.IconButton(
                                        col= 1,
                                        icon= ft.icons.FAVORITE_BORDER,
                                        selected_icon= ft.icons.FAVORITE,
                                        selected= False,
                                        on_click= clicked,
                                        icon_color= ft.colors.BLACK,
                                        selected_icon_color= ft.colors.RED,
                                        icon_size= 30,
                                    ),
                                    ft.Icon(
                                        col= 1,
                                        name= ft.icons.CHAT_BUBBLE_OUTLINE,
                                        color= ft.colors.BLACK,
                                        size= 26
                                    ),
                                    ft.Icon(
                                        col= 0,
                                        name= ft.icons.SEND,
                                        color= ft.colors.BLACK,
                                        size= 24,
                                    ),
                                    ft.Container(col=8),
                                    ft.IconButton(
                                        col= 1,
                                        icon= ft.icons.BOOKMARK_BORDER,
                                        selected_icon= ft.icons.BOOKMARK_ROUNDED,
                                        selected= False,
                                        on_click= clicked,
                                        icon_color= ft.colors.BLACK,
                                        selected_icon_color= ft.colors.BLACK,
                                        icon_size= 30,
                                    )
                                ]
                            ),
                            ft.Container(
                                width= 500, height= 100, margin= ft.margin.only(top=0, left= 10, bottom=0, right=10), padding= ft.padding.all(0),
                                content= ft.Column(
                                    width= 500, height= 100,
                                    controls= [
                                        ft.Text(
                                            spans=[
                                                ft.TextSpan(text='Curtido por ', style=ft.TextStyle(color= ft.colors.BLACK, size= 15)),
                                                ft.TextSpan(text= 'FCabral07 ', style=ft.TextStyle(color= ft.colors.BLACK, size= 15, weight=ft.FontWeight.BOLD)),
                                                ft.TextSpan(text='e ', style=ft.TextStyle(color= ft.colors.BLACK, size= 15)),
                                                ft.TextSpan(text= 'outras pessoas', style=ft.TextStyle(color= ft.colors.BLACK, size= 15, weight=ft.FontWeight.BOLD)),
                                            ],
                                            offset= ft.Offset(x=0, y=-0.7)
                                        ),
                                        ft.Text(
                                            spans=[
                                                ft.TextSpan(text='flamengo ', style=ft.TextStyle(color= ft.colors.BLACK, size= 15)),
                                                ft.TextSpan(text= 'NA DIVIDIDA GANHA QUEM TEM UNIÃO!', style=ft.TextStyle(color= ft.colors.BLACK, italic= True, size= 15, weight=ft.FontWeight.BOLD)),
                                            ],
                                            offset= ft.Offset(x=0, y=-0.9)
                                        ),
                                        ft.Text(
                                            value='📸 Marcelo Cortes / CRF',
                                            style= ft.TextStyle(
                                                color= ft.colors.BLACK, size= 15
                                            ),
                                            offset= ft.Offset(x=0, y=-0.6)
                                        ),
                                        ft.Text(
                                            value='#VamosFlamengo #CRF',
                                            style= ft.TextStyle(
                                                color= ft.colors.BLUE, size= 15
                                            ),
                                            offset= ft.Offset(x=0, y=-1)
                                        ),
                                        ft.Text(
                                            value='Ver todos os 518 comentários',
                                            style= ft.TextStyle(
                                                color= ft.colors.GREY_700, size= 15
                                            ),
                                            offset= ft.Offset(x=0, y=-1.3)
                                        ),
                                        ft.Text(
                                            spans=[
                                                ft.TextSpan(text= 'Há 2 dias • ', style=ft.TextStyle(color= ft.colors.GREY_700, size= 14)),
                                                ft.TextSpan(text= 'Ver tradução', style=ft.TextStyle(color= ft.colors.BLACK87, size= 14, weight= ft.FontWeight.BOLD))
                                            ],
                                            offset= ft.Offset(x=0, y=-1.4)
                                        )
                                    ]
                                )
                            ),
                        ]
                    )
                )
            ]
        )
    )
    
    # Adicionando a página
    page.add(layout)
    
if __name__ == '__main__':
    ft.app(target= main)
