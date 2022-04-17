import psycopg2
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter import OptionMenu, Scrollbar, StringVar, messagebox
from datetime import date

background = '#ffe4e1'
foreground = '#79a1e0'

def main_screen():
    window = tk.Tk(className="Reportes")
    Font = tkFont.Font(family="@MS UI Gothic", size=12, weight="bold" )
    logoCanvas = tk.Canvas(window, width = 150, height = 150, highlightthickness=0, bg=background)
    window.configure(bg=background)
    window.geometry("900x500")
    window.resizable(False,False)
    
    
    button_top10_genre = tk.Button(window, bg=foreground, width=30, height=4, text="top10_genre", font=Font, command=lambda: top10_genre())
    button_top10_genre.place(relx=0.1, rely=0.2, anchor="w")
    
    button_reproduction_amount = tk.Button(window, bg=foreground, width=30, height=4, text="reproduction_amount", font=Font, command=lambda: reproduction_amount())
    button_reproduction_amount.place(relx=0.9, rely=0.2, anchor="e")
    
    button_top10_staff = tk.Button(window, bg=foreground, width=30, height=4, text="top10_staff", font=Font, command=lambda: top10_staff())
    button_top10_staff.place(relx=0.1, rely=0.5, anchor="w")
    
    button_premium_accounts = tk.Button(window, bg=foreground, width=30, height=4, text="premium_accounts", font=Font, command=lambda: premium_accounts())
    button_premium_accounts.place(relx=0.9, rely=0.5, anchor="e")
    
    button_peak_hour = tk.Button(window, bg=foreground, width=30, height=4, text="peak_hour", font=Font, command=lambda: peak_hour())
    button_peak_hour.place(relx=0.5, rely=0.8, anchor="center")
    
    window.mainloop()

def create_screenUI(tittle):
    window = tk.Tk(className= tittle)
    Font = tkFont.Font(family="@MS UI Gothic", size=12, weight="bold" )
    logoCanvas = tk.Canvas(window, width = 150, height = 150, highlightthickness=0, bg=background)
    window.configure(bg=background)
    window.geometry("900x500")
    window.resizable(False,False)

    return window, Font
  

def top10_genre():
    window, Font = create_screenUI("top10_genre")
    
    initialCal = Calendar(window, setmode ='day', date_pattern = 'yy/m/d')
    initialCal.place(relx=0.3, rely=0.4, anchor="e")
    
    endCal = Calendar(window, setmode ='day', date_pattern = 'yy/m/d')
    endCal.place(relx=0.45, rely=0.4, anchor="center")


    button_select = tk.Button(window, bg=foreground, width=20, height=2, text="Generar Reporte", font=Font, command=lambda: top10_genre_report(initialCal, endCal,entryarea, Font))
    button_select.place(relx=0.2, rely=0.7, anchor="w")
    
    entryarea = tk.Canvas(window, width=300, height=400, bg=foreground)
    entryarea.place(relx=0.95, rely=0.5, anchor="e")
    
    
def top10_genre_report(initial, final, report_area, Font):
    initial_date = initial.get_date()
    final_date = final.get_date()
    
    userText = Label(report_area, text = initial_date, bg = foreground, font = Font)
    userText.place(relx=0.1, rely=0.2, anchor="w")
    
    userText2 = Label(report_area, text = final_date, bg = foreground, font = Font)
    userText2.place(relx=0.1, rely=0.4, anchor="w")    

  

def reproduction_amount():
    window, Font = create_screenUI("reproduction_amount")
    
    initialCal = Calendar(window, setmode ='day', date_pattern = 'yy/m/d')
    initialCal.place(relx=0.3, rely=0.4, anchor="e")
    
    endCal = Calendar(window, setmode ='day', date_pattern = 'yy/m/d')
    endCal.place(relx=0.45, rely=0.4, anchor="center")


    button_select = tk.Button(window, bg=foreground, width=20, height=2, text="Generar Reporte", font=Font, command=lambda: reproduction_amount_report(initialCal, endCal,entryarea, Font))
    button_select.place(relx=0.2, rely=0.7, anchor="w")
    
    entryarea = tk.Canvas(window, width=300, height=400, bg=foreground)
    entryarea.place(relx=0.95, rely=0.5, anchor="e")
    
def reproduction_amount_report(initial, final, report_area, Font):
    initial_date = initial.get_date()
    final_date = final.get_date()
    
    userText = Label(report_area, text = initial_date, bg = foreground, font = Font)
    userText.place(relx=0.1, rely=0.2, anchor="w")
    
    userText2 = Label(report_area, text = final_date, bg = foreground, font = Font)
    userText2.place(relx=0.1, rely=0.4, anchor="w")    
    
    
    
def top10_staff():
    window, Font = create_screenUI("top10_staff")
    
    #Crear lado de cuentas normales
    normal_txt = Label(window, text = "Cuentas Normales", bg = background, font = Font)
    normal_txt.place(relx=0.3, rely=0.05, anchor="center")
    normalArea = tk.Canvas(window, width=350, height=400, bg=foreground)
    normalArea.place(relx=0.1, rely=0.5, anchor="w")
    normalArea.create_line(0,200,360,200, fill= "white", width =1)
    normal_director_txt = Label(normalArea, text = "Actores", bg = foreground, font = Font)
    normal_director_txt.place(relx=0.5, rely=0.05, anchor="n")
    normal_actor_txt = Label(normalArea, text = "Directores", bg = foreground, font = Font)
    normal_actor_txt.place(relx=0.5, rely=0.55, anchor="center")
    
    #Creat lado de cuentas premium
    premium_text = Label(window, text = "Cuentas Premium", bg = background, font = Font)
    premium_text.place(relx=0.75, rely=0.05, anchor="center")
    premiumArea = tk.Canvas(window, width=350, height=400, bg=foreground)
    premiumArea.place(relx=0.95, rely=0.5, anchor="e")
    premiumArea.create_line(0,200,360,200, fill= "white", width =1)
    normal_director_txt = Label(premiumArea, text = "Actores", bg = foreground, font = Font)
    normal_director_txt.place(relx=0.5, rely=0.05, anchor="n")
    normal_actor_txt = Label(premiumArea, text = "Directores", bg = foreground, font = Font)
    normal_actor_txt.place(relx=0.5, rely=0.55, anchor="center")
    


def premium_accounts():
    window, Font = create_screenUI("premium_accounts")
    number_font = tkFont.Font(family="@MS UI Gothic", size=30, weight="bold" )
    
    label_txt = Label(window, text = "Cantidad de cuentas premium en los ultimos 6 meses", bg = background, font = Font)
    label_txt.place(relx=0.5, rely=0.15, anchor="center")
    entryarea = tk.Canvas(window, width=600, height=300, bg=foreground)
    entryarea.place(relx=0.5, rely=0.5, anchor="center")
    
    number_txt = Label(entryarea, text = "69", bg = foreground, font = number_font)
    number_txt.place(relx=0.5, rely=0.15, anchor="center")
    
    fecha = date.today()
    today_year = int(fecha.strftime("%Y"))
    today_month = fecha.strftime("%m")
    today_day = fecha.strftime("%d")

    
    if (today_month == "01"):
        today_year = today_year - 1 
        print("year: ", today_year)
        print("month: 7")
        
        today_year = str(today_year)
        whole_date = today_year + "-" + "07" + "-" + today_day

        
    elif (today_month =="02"):
        today_year = today_year - 1 
        print("year: ", today_year)
        print("month: 8")
        
        today_year = str(today_year)
        whole_date = today_year + "-" + "08" + "-" + today_day
        
    elif (today_month =="03"):
        today_year = today_year - 1 
        print("year: ", today_year)
        print("month: 9")
        
        today_year = str(today_year)
        whole_date = today_year + "-" + "09" + "-" + today_day
        
    elif (today_month =="04"):
        today_year = today_year - 1 
        print("year: ", today_year)
        print("month: 10")
        
        today_year = str(today_year)
        whole_date = today_year + "-" + "10" + "-" + today_day
        
    elif (today_month =="05"):
        today_year = today_year - 1 
        print("year: ", today_year)
        print("month: 11")
        
        today_year = str(today_year)
        whole_date = today_year + "-" + "11" + "-" + today_day
        
    elif (today_month =="06"):
        today_year = today_year - 1 
        print("year: ", today_year)
        print("month: 12")
        
        today_year = str(today_year)
        whole_date = today_year + "-" + "12" + "-" + today_day
        
    elif (today_month =="07"):
        print("year: ", today_year)
        print("month: 1")
        
        today_year = str(today_year)
        whole_date = today_year + "-" + "01" + "-" + today_day
        
    elif (today_month =="08"):
        print("year: ", today_year)
        print("month: 2")
        
        today_year = str(today_year)
        whole_date = today_year + "-" + "02" + "-" + today_day
        
    elif (today_month =="09"):
        print("year: ", today_year)
        print("month: 3")
        
        today_year = str(today_year)
        whole_date = today_year + "-" + "03" + "-" + today_day
        
    elif (today_month =="10"):
        print("year: ", today_year)
        print("month: 4")
        
        today_year = str(today_year)
        whole_date = today_year + "-" + "04" + "-" + today_day
        
    elif (today_month =="11"):
        print("year: ", today_year)
        print("month: 5")
        
        today_year = str(today_year)
        whole_date = today_year + "-" + "05" + "-" + today_day
        
    elif (today_month =="12"):
        print("year: ", today_year)
        print("month: 6")
        
        today_year = str(today_year)
        whole_date = today_year + "-" + "06" + "-" + today_day
    



def peak_hour():
    window, Font = create_screenUI("peak_hour")
    
    myCal = Calendar(window, setmode ='day', date_pattern = 'yy/m/d')
    myCal.place(relx=0.35, rely=0.4, anchor="e")
    
    button_select = tk.Button(window, bg=foreground, width=20, height=2, text="Generar Reporte", font=Font, command=lambda: peak_hour_report(myCal, entryarea, Font))
    button_select.place(relx=0.125, rely=0.7, anchor="w")
    
    entryarea = tk.Canvas(window, width=450, height=400, bg=foreground)
    entryarea.place(relx=0.95, rely=0.5, anchor="e")
    
def peak_hour_report(date, report_area, Font):
    given_date = date.get_date()
    
    
    userText = Label(report_area, text = given_date, bg = foreground, font = Font)
    userText.place(relx=0.1, rely=0.2, anchor="w")


main_screen()