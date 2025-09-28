import tkinter
import tkinter.ttk

from PIL import Image, ImageTk


window = tkinter.Tk()
window.title('90BMI')
window.geometry('470x580+700+200')
window.resizable(False, False)
window.config(bg='#f0f1f5')


# icon
icon_image = tkinter.PhotoImage(file='bin/icon.png')
window.iconphoto(False, icon_image)


#top
top_image = tkinter.PhotoImage(file='bin/top.png')
top = tkinter.Label(master=window, image=top_image)
top.place(x=-10, y=0)

#bottom
bottom_bg = tkinter.Label(
    master=window,
    bg='light sea green',
    width=72,
    height=18
)
bottom_bg.place(x=0, y=305)

# 2 boxes
boxes_image = tkinter.PhotoImage(file='bin/box.png')
tkinter.Label(master=window, image=boxes_image).place(x=20, y=100)
tkinter.Label(master=window, image=boxes_image).place(x=240, y=100)


# scales
scales_image = tkinter.PhotoImage(file='bin/scale.png')
tkinter.Label(master=window, image=scales_image, bg='light sea green',).place(x=20, y=310)


# Entry box
height_var = tkinter.StringVar()
height_entry = tkinter.Entry(
    master=window,
    textvariable=height_var,
    font=('arial',50, 'bold'),
    width=5,
    bd=0,
    bg='goldenrod',
    fg='gray0',
    justify='center'
)
height_entry.place(x=35, y=160)

weight_var = tkinter.StringVar()
weight_entry = tkinter.Entry(
    master=window,
    textvariable=weight_var,
    font=('arial',50, 'bold'),
    width=5,
    bd=0,
    bg='deep pink',
    fg='light yellow',
    justify='center'
)
weight_entry.place(x=255, y=160)

# 2 sliders

def slider_changed(value):
    value_h = round(float(current_height_value.get()))
    height_var.set(value_h)
    
    value_w = round(float(current_weight_value.get()))
    weight_var.set(value_w)

    person_image = Image.open('bin/man.png')
    person_image = person_image.resize([10 + int(value_w*0.8), 10 + value_h])
    
   
     
    person_image_tk = ImageTk.PhotoImage(person_image)
    man_image.config(image=person_image_tk)
    man_image.place(x=80, y=550 - value_h)
    man_image.image = person_image_tk
    

current_height_value = tkinter.DoubleVar()
style = tkinter.ttk.Style()
style.configure('TScale', background='white')

slider1 = tkinter.ttk.Scale(
    master=window,
    style='TScale',
    variable=current_height_value,
    command= slider_changed,
    from_=0,
    to=220
        
)
slider1.place(x=80, y=250)

def weight_changed(value):
    value = round(float(value))
    weight_var.set(value)


current_weight_value = tkinter.DoubleVar()
style = tkinter.ttk.Style()
style.configure('TScale', background='white')

slider2 = tkinter.ttk.Scale(
    master=window,
    style='TScale',
    variable=current_weight_value,
    command=slider_changed,
    from_=0,
    to=220
        
)
slider2.place(x=300, y=250)






# man image
man_image = tkinter.Label(master=window, bg="light sea green")
man_image.place(x=70, y=530)

# Result Button
def get_BMI():
    height, weight = float(height_var.get()), float(weight_var.get())
    print(height, weight)
    BMI_result = weight / (height / 100) **2
    print(BMI_result)
    bmi_result['text'] = f'{BMI_result:.0f}'







button_result = tkinter.Button(
    master=window,
    text='рассчитать',
    width=15,
    height=2,
    font=('arial', 12, 'bold'),
    bg='dark red',
    fg='white',
    command=get_BMI
  
)
button_result.place(x=280, y=340)

# result label


bmi_result = tkinter.Label(
    master=window,
    text='150',
    font=('arial', 50, 'bold'),
    bg='light sea green',
    fg='white'
)
bmi_result.place(x=300, y=400)






























































