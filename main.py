from tkinter import Button, Label, Toplevel, StringVar, Entry, END, Tk, messagebox
import json

root = Tk()
root.title("oder manager")
root.geometry("570x500")
root.resizable(False, False)
root.iconbitmap('img\\logo.ico')


# setting item price
pizza_price = 99
berger_price = 69
french_fries_price = 49
dosa_price = 99
momos_price = 49

Label(text="oder manager", font="a 15 bold", padx=220, bg='black', fg='white', height=3).grid(row=0, column=2, columnspan=5)


# writing in fill
def submit():
    total()
    name_info = name_var.get()
    phone_info = phone_var.get()
    pincode_info = pincode_var.get()
    state_info = state_var.get()
    city_info = city_var.get()
    if name_info == '' or phone_info == '' or pincode_info == '' or state_info == '' or city_info == '':
        messagebox.showinfo(title='Oops', message='please enter full address')
    else:
        building_info = building_var.get()
        write_fill = open('Document.txt', mode='a')
        fill_write1 = f"\n\nusername: {name_info} , phone no: {phone_info} , pincode: {pincode_info}\n"
        fill_write2 = f"state: {state_info}, city: {city_info} , building no: {building_info}\n"
        fill_write3 = f"total: {final_bill}"
        fill_writ_f = fill_write1 + fill_write2 + fill_write3
        write_fill.write(fill_writ_f)
        write_fill.close()
        sub_msg_lab.config(text='oder successfully submitted')
        print('oder submitted successfully')
        clear()


# total button
def total():
    global final_bill

    pizza_info = pizza_var.get()
    berger_info = berger_var.get()
    french_fries_info = french_fries_var.get()
    dosa_info = dosa_var.get()
    momos_info = momos_var.get()

    if pizza_info == '' and berger_info == '' and french_fries_info == '' and dosa_info == '' and momos_info == '':
        messagebox.showinfo(title='enter oder', message='     Order Info Could Not Be Blank     ')
    else:
        try:
            pizza_n = int(pizza_info)
        except:
            pizza_n = 0
        try:
            i2 = int(berger_info)
        except:
            i2 = 0
        try:
            i3 = int(french_fries_info)
        except:
            i3 = 0
        try:
            i4 = int(dosa_info)
        except:
            i4 = 0
        try:
            i5 = int(momos_info)
        except:
            i5 = 0

        # making final bill
        pizza_total = pizza_n * pizza_price
        berger_total = i2 * berger_price
        french_fries_total = i3 * french_fries_price
        dosa_total = i4 * dosa_price
        momos_total = i5 * momos_price

        final_bill = pizza_total + berger_total + french_fries_total + dosa_total + momos_total
        total_entry.delete(0, END)
        total_entry.insert(0, str(final_bill))


# menu top level
def menu():
    menu_window = Toplevel()
    menu_window.title("menu")
    menu_window.geometry("300x300")
    menu_window.iconbitmap('img\\logo.ico')
    menu_window.config(bg="green")
    menu_window.resizable(False, False)
    Label(menu_window, text="menu", padx=133, bg="green", font="asd 15 bold").grid(row=0, column=0)
    info_prise_text = "No.                       item name                        prise"
    Label(menu_window, bg="green", text=info_prise_text).grid(row=1, column=0)
    pizza_prise_text = f"1                             pizza                               {pizza_price}"
    Label(menu_window, bg="green", text=pizza_prise_text).grid(row=2, column=0)
    berger_prise_text = f"2                           berger                              {berger_price}"
    Label(menu_window, bg="green", text=berger_prise_text).grid(row=3, column=0)
    french_fries_prise_text = f"3                         french fries                        {french_fries_price}"
    Label(menu_window, bg="green", text=french_fries_prise_text).grid(row=4, column=0)
    dosa_prise_text = f"4                               dosa                             {dosa_price}"
    Label(menu_window, bg="green", text=dosa_prise_text).grid(row=5, column=0)
    item5_prise_text = f"5                            Momos                        {momos_price}"
    Label(menu_window, bg="green", text=item5_prise_text).grid(row=6, column=0)


# clear entry
def clear():

    # oder info delete
    pizza_entry.delete(0, END)
    berger_entry.delete(0, END)
    french_fries_entry.delete(0, END)
    dosa_entry.delete(0, END)
    momos_entry.delete(0, END)

    # personnel info delete
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    pincode_entry.delete(0, END)
    state_entry.delete(0, END)
    city_entry.delete(0, END)
    building_entry.delete(0, END)
    total_entry.delete(0, END)


# sing in button
def sing_in(name, phone, pincode, stat, city, building):
    new_user = {name: {"full_name": name, "Phone": phone, "pincode": pincode, "stat": stat, "city": city, "building": building}}

    try:
        # seeing if there is any old passwords data file
        with open("user_data.json", mode="r") as old_password_file:
            # reading old password data
            password_data = json.load(old_password_file)
    # if there is no file or if there is a file but no entries in it:
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        with open("user_data.json", mode="w") as new_password_file:
            json.dump(new_user, new_password_file, indent=4)
    # if there is old password data,
    else:
        #  New user entry json data will be updated to the old passwords data
        password_data.update(new_user)
        # Writing either the updated password data or the new user entry json data
        with open("user_data.json", mode="w") as old_password_file:
            json.dump(password_data, old_password_file, indent=4)


# sing in top level
def sing_in_top():
    def log():
        sing_in(name_log.get(), phone_log.get(), pin_log.get(), stat_log.get(), city_log.get(), building_log.get())
        user_name.delete(0, END)
    global user_name_var, password_var
    log_top = Toplevel()
    log_top.title('sing in')
    log_top.iconbitmap('img\\logo.ico')
    log_top.geometry('500x280')
    log_top.resizable(False, False)
    title_l = Label(log_top, text="sing in", font="a 15 bold", bg='black', fg='white', height=3, padx=220)
    title_l.grid(row=0, column=0, columnspan=5)
    Label(log_top, text='user name', fg='blue', font='serif 11 bold').grid(row=1, column=0)
    user_name_var = StringVar()
    Entry(log_top, bg='light pink', fg='blue', font='f 9', textvariable=user_name_var).grid(row=1, column=1)
    Label(log_top, text='password', fg='blue', font='serif 11 bold').grid(row=2, column=0)
    password_var = StringVar()
    Entry(log_top, bg='light pink', fg='blue', font='if 9', textvariable=password_var).grid(row=2, column=1)

    Label(log_top, text="full name", fg="blue", font='f 11 bold').grid(row=1, column=2)
    name_log = StringVar()
    user_name = Entry(log_top, textvariable=name_log, bg='light pink')
    user_name.grid(row=1, column=3)

    Label(log_top, text="phone no.", fg="blue", font='f 11 bold').grid(row=2, column=2)
    phone_log = StringVar()
    Entry(log_top, textvariable=phone_log, bg='light pink').grid(row=2, column=3)

    Label(log_top, text="pincode", fg="blue", font='f 11 bold').grid(row=3, column=2)
    pin_log = StringVar()
    Entry(log_top, textvariable=pin_log, bg='light pink').grid(row=3, column=3)

    Label(log_top, text="your state", fg="blue", font='f 11 bold').grid(row=4, column=2)
    stat_log = StringVar()
    Entry(log_top, textvariable=stat_log, bg='light pink').grid(row=4, column=3)

    Label(log_top, text="your city", fg="blue", font='f 11 bold').grid(row=5, column=2)
    city_log = StringVar()
    Entry(log_top, textvariable=city_log, bg='light pink').grid(row=5, column=3)

    Label(log_top, text="your building no.", fg="blue", font='f 11 bold').grid(row=6, column=2)
    building_log = StringVar()
    Entry(log_top, textvariable=building_log, bg='light pink').grid(row=6, column=3)

    Button(log_top, text='sing in', command=log).grid(row=3, column=1)


# auto fill
def auto_fill():
    global user_name_auto
    hello = user_name_auto.get()
    if name_var.get() == '':
        with open('user_data.json', 'r') as source:
            data = json.load(source)
            full_name = data[hello]['full_name']
            phone = data[hello]['Phone']
            pincode = data[hello]['pincode']
            stat = data[hello]['stat']
            city = data[hello]['city']
            building = data[hello]['building']

            if hello == full_name:
                name_entry.insert(0, full_name)
                phone_entry.insert(0, phone)
                pincode_entry.insert(0, pincode)
                state_entry.insert(0, stat)
                city_entry.insert(0, city)
                building_entry.insert(0, building)
            # else:
            #     print("hello")
            #     auto_fill_en.destroy()
            elif user_name_auto.get() == '':
                messagebox.showinfo(title='ada', message='user name field cannot be blank     ')
            else:
                messagebox.showinfo(title='ada', message='please enter right user name     ')
        # Button(auto_fill_top, text='auto fill', command=enter).grid(row=2, column=0)
    else:
        messagebox.showinfo(title='address already writen', message='     address already writen     ')


# Item labels

# 1. oder info
Label(text="oder info", font=('relief', 14, 'bold')).grid(row=1, column=3)

Label(text="pizza", fg="blue", font='f 11 bold').grid(row=2, column=2)
pizza_var = StringVar()
pizza_entry = Entry(textvariable=pizza_var, bg='light pink')
pizza_entry.grid(row=2, column=3)

Label(text="berger", fg="blue", font='f 11 bold').grid(row=3, column=2)
berger_var = StringVar()
berger_entry = Entry(textvariable=berger_var, bg='light pink')
berger_entry.grid(row=3, column=3)

Label(text="french fries", fg="blue", font='f 11 bold').grid(row=4, column=2)
french_fries_var = StringVar()
french_fries_entry = Entry(textvariable=french_fries_var, bg='light pink')
french_fries_entry.grid(row=4, column=3)

Label(text="dosa", fg="blue", font='f 11 bold').grid(row=5, column=2)
dosa_var = StringVar()
dosa_entry = Entry(textvariable=dosa_var, bg='light pink')
dosa_entry.grid(row=5, column=3)

Label(text="Momos", fg="blue", font='f 11 bold').grid(row=6, column=2)
momos_var = StringVar()
momos_entry = Entry(textvariable=momos_var, bg='light pink')
momos_entry.grid(row=6, column=3)

Label(text="Total", fg="blue", font='f 11 bold').grid(row=7, column=2)
total_var = StringVar()
total_entry = Entry(textvariable=total_var, bg='light pink', highlightcolor='black')
total_entry.grid(row=7, column=3)

# 2. personnel info
Label(text="personnel info", font=('relief', 14, 'bold')).grid(row=1, column=5)

Label(text="Full Name", fg="blue", font='f 11 bold').grid(row=2, column=4)
name_var = StringVar()
name_entry = Entry(textvariable=name_var, bg='light pink')
name_entry.grid(row=2, column=5)

Label(text="Phone No.", fg="blue", font='f 11 bold').grid(row=3, column=4)
phone_var = StringVar()
phone_entry = Entry(textvariable=phone_var, bg='light pink')
phone_entry.grid(row=3, column=5)

Label(text="Pincode", fg="blue", font='f 11 bold').grid(row=4, column=4)
pincode_var = StringVar()
pincode_entry = Entry(textvariable=pincode_var, bg='light pink')
pincode_entry.grid(row=4, column=5)

Label(text="State", fg="blue", font='f 11 bold').grid(row=5, column=4)
state_var = StringVar()
state_entry = Entry(textvariable=state_var, bg='light pink')
state_entry.grid(row=5, column=5)

Label(text="City", fg="blue", font='f 11 bold').grid(row=6, column=4)
city_var = StringVar()
city_entry = Entry(textvariable=city_var, bg='light pink')
city_entry.grid(row=6, column=5)

Label(text="Building No.", fg="blue", font='f 11 bold').grid(row=7, column=4)
building_var = StringVar()
building_entry = Entry(textvariable=building_var, bg='light pink')
building_entry.grid(row=7, column=5)

# menu button
Button(text="Menu", command=menu).grid(row=8, column=2)

# clear button
Button(text=" Clear ", command=clear).grid(row=8, column=3)

# total button
Button(text=" Total ", command=total).grid(row=8, column=4)

# submit button
submit_btn = Button(text=" Submit ", command=submit)
submit_btn.grid(row=8, column=5, pady=5)

sub_msg_lab = Label(text='', fg='green', font='aa 15 bold', bg='black', width=47)
sub_msg_lab.grid(row=10, column=0, columnspan=6, pady=15)

Label(text="User Name", fg="blue", font='f 11 bold').grid(row=11, column=2)
user_name_auto = StringVar()

auto_fill_en = Entry(textvariable=user_name_auto, bg='light pink')
auto_fill_en.grid(row=11, column=3)

Button(text='Auto fill', command=auto_fill).grid(row=11, column=4)

Button(text='Sing in', command=sing_in_top).grid(row=11, column=5)

thank_lab = Label(text='Thank You For Visiting My Software', fg='green', font='aa 15 bold', bg='black', padx=115)
thank_lab.grid(row=12, column=0, columnspan=6, pady=48)

root.mainloop()
