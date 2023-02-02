import flet as ft
from flet import(Column)

def main(page:ft.page):
    page.title ="Bot activation movil"
    ft.Text(value= "LIBERTY")
    page.vertical_aligment=  ft.MainAxisAlignment.START
    page.horizonal_aligment= ft.CrossAxisAlignment.CENTER
    page.padding= 0
    page.bgcolor= "#28BCC9"
    titulo= ft.Text(value="BOT ACTIVATION MOVIL", font_family="Arial") 

    user_gac= ft.TextField(label="      user gac", width=320)

    password_gac= ft.TextField(label="      password_gac", width=320)

    password_udb= ft.TextField(label="      password_udb",  width=320)

    greetings = ft.column

    subtitulo= ft.Text(value="0  atentp RPA, ing. daniel rios ")

    c1 =ft.Container(
        ft.Text(f"flet", size=30, color= "blue",italic=True, weight="bold" ),
            
        width=1920,
        height=60,
        padding=0,
        alignment=ft.alignment.center_left,
        bgcolor="white",
        border_radius=0,

        animate_opacity=300,
    ) 

    def btn_click(e):
        titulo = ""
        user_gac = value = ""
        password_gac = value = ""
        password_udb = value = ""
        subtitulo = ""
        page.update ()

    def toggle_icon_button(e):
        e.control.selected = not e.control.selected
        e.control.Update()
   
    c2 =ft.Container(
        ft.Column(controls=[ 
           
            ft.Text(f"BOT ACTIVACION MOVIL ",size=14, color="black", font_family="ARIAL" ,weight="bold"),
            ft.Text(f"   ", size=8),
            ft.TextField(label="   USER GAC",prefix_icon=ft.icons.PERSON,width=320),
            ft.TextField(label=" PASSWORD GAC",width=320),
            ft.TextField(label="  PASSWORD BDA",width=320),

           ft.FilledButton(
           "   ingresar    ", on_click=btn_click,
           style=ft.ButtonStyle( 
               shape=ft.StadiumBorder(),            
            ),
        ),
              ft.Text(value=" 0                                              ATENTO RPA,  ING.DANIEL RIOS", weight="bold")
    ],              
    
    
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment="center"
                    
                   
                   ),               

        width=350,
        height=410,
        padding=0,
        alignment=ft.alignment.top_center,
        bgcolor="white",
        border_radius=15,
        animate_opacity=300,
        




    )
    


    page.add(
        c1,
        c2,
        
        
       
    ) 
        
        
ft.app(target=main) 
        

    


          
    

     



 
   

                


                

        
