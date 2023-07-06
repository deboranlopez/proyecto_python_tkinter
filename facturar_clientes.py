from tkinter import *
import sqlite3
from tkinter import ttk
import re
from tkinter import messagebox

# Modelo
## base de datos##


def crear_base():
    # se guarda en una variable la referencia de donde voy a guardar la base de datos
    con = sqlite3.connect("base_debora_lopez.db")
    return con


def crear_tabla():
    con = crear_base()
    cursor = con.cursor()
    sql = '''CREATE TABLE clientes
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre varchar(20) NOT NULL,
            apellido varchar(20) NOT NULL,
            Tipo_doc varchar(20) NOT NULL,
            documento INT,
            direccion varchar(20) NOT NULL,
            cant_sesiones real,
            total_facturar real,
            precio_sesion real)'''
    cursor.execute(sql)
    con.commit()


try:
    crear_base()
    crear_tabla()
except:
    print("Tabla ya creada")

global precio_sesion


def actualizar_precio_sesion(precio_nueva_sesion):
    if precio_nueva_sesion == 0:
        messagebox.showerror(
            message="Ingresar el valor correcto", title="Precio de la sesión")

    else:
        con = crear_base()
        cursor = con.cursor()
        global precio_sesion
        sql1 = "UPDATE clientes SET precio_sesion = ?"
        dato = (precio_nueva_sesion, )
        cursor.execute(sql1, dato)
        sql = "UPDATE clientes SET total_facturar = cant_sesiones*precio_sesion"
        cursor.execute(sql)
        con.commit()
        actualizar_treeview(tree)
        messagebox.showinfo(
            message="Se actualizó el nuevo valor", title="Precio de la sesión")
        return precio_sesion


global lista_documentos
lista_documentos = []


def documentos():
    con = crear_base()
    cursor = con.cursor()
    sql = "SELECT documento FROM clientes"
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in range(0, len(result)):
        global lista_documentos
        lista_documentos.append(result[i][0])
    print(lista_documentos)
    con.commit()
    return lista_documentos


def alta(
        nombre,
        apellido,
        Tipo_doc,
        documento,
        direccion,
        cant_sesiones,
        tree):

    global lista_documentos

    documentos()

    if documento == 0 or documento == None:
        messagebox.showerror(
            message="Ingresar el documento correcto", title="Alta de cliente")

    elif documento in lista_documentos:
        messagebox.showerror(
            message="Ya existe un cliente con el documento ingresado", title="Alta de cliente")

    else:
        print(nombre, apellido, Tipo_doc, documento, direccion, cant_sesiones)
        con = crear_base()
        cursor = con.cursor()
        precio_sesion = h_val.get()
        total_facturar = float(cant_sesiones) * float(precio_sesion)
        data = (nombre, apellido, Tipo_doc, documento,
                direccion, cant_sesiones, total_facturar)
        sql = "INSERT INTO clientes(nombre, apellido, Tipo_doc, documento, direccion, cant_sesiones, total_facturar) VALUES(?,?,?,?,?,?,?)"
        cursor.execute(sql, data)
        con.commit()
        messagebox.showinfo(
            message="Se agregó correctamente el nuevo cliente", title="Alta de cliente")
        actualizar_treeview(tree)


def eliminar(tree):
    try:
        valor = tree.selection()
        print(valor)
        item = tree.item(valor)
        print(item)
        print(item["text"])
        id = item["text"]

        con = crear_base()
        cursor = con.cursor()
        data = (id, )
        sql = "DELETE FROM clientes WHERE id = ?;"
        cursor.execute(sql, data)
        con.commit()
        tree.delete(valor)

        global lista_documentos
        lista_documentos = []

        messagebox.showinfo(
            message="Se elimino correctamente el cliente", title="Baja de cliente")

    except:
        messagebox.showerror(message="Seleccione el cliente",
                             title="Baja de cliente")


def consultar(tree):
    # Imprime los elementos del árbol.
    treeview_children = tree.get_children()
    print(treeview_children)
    con = crear_base()
    cursor = con.cursor()
    sql = "SELECT * FROM clientes ORDER BY id DESC;"
    datos = cursor.execute(sql)

    records = tree.get_children()
    for element in records:
        tree.delete(element)

    resultado = datos.fetchall()
    for fila in resultado:
        print(fila)
        tree.insert("", 0, text=fila[0],
                    values=(fila[1],
                            fila[2],
                            fila[3],
                            fila[4],
                            fila[5],
                            fila[6],
                            fila[7])
                    )


def seleccionar(documento):
    con = crear_base()
    cursor = con.cursor()
    documento = int(documento)
    data = (documento, )
    sql = "SELECT * FROM clientes WHERE documento=? ORDER BY id DESC;"

    records = tree.get_children()
    for element in records:
        tree.delete(element)

    datos = cursor.execute(sql, data)
    resultado = datos.fetchall()
    for fila in resultado:
        print(fila)
        tree.insert("", 0, text=fila[0],
                    values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7]))


def actualizar_treeview(mitreview):
    # Pueden obtenerse todos los elementos hijos dentro del árbol
    # retorna una lista,recorre y borra

    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)

    sql = "SELECT * FROM clientes ORDER BY id DESC"
    con = crear_base()
    cursor = con.cursor()
    datos = cursor.execute(sql)

    # toma los datos que vienen en formato que no podemos mostrar
    # los vuelve una lista para poder recorrerla con el bucle for

    resultado = datos.fetchall()
    for fila in resultado:
        print(fila)
        mitreview.insert("", 0, text=fila[0],
                         values=(fila[1],
                                 fila[2],
                                 fila[3],
                                 fila[4],
                                 fila[5],
                                 fila[6],
                                 fila[7])
                         )


## vista ######
root = Tk()
root.title("Clientes para facturar")

titulo = Label(root, text="Ingrese los datos del cliente", bg="turquoise1",
               fg="black", height=1, width=80)
titulo.grid(row=0, column=0, columnspan=7, padx=1, pady=1, sticky=W+E)

nombre = Label(root, text="Nombre")
nombre.grid(row=1, column=0, sticky=W)
apellido = Label(root, text="Apellido")
apellido.grid(row=1, column=2, sticky=W)
tipo_documento = Label(root, text="Tipo de documento")
tipo_documento.grid(row=2, column=0, sticky=W)
documento = Label(root, text="Documento")
documento.grid(row=2, column=2, sticky=W)
direccion = Label(root, text="Direccion")
direccion.grid(row=3, column=0, sticky=W)
cant_sesiones = Label(root, text="Cantidad de sesiones")
cant_sesiones.grid(row=4, column=0, sticky=W)
precio_sesion = Label(root, text="Ingresar precio de la sesion:")
precio_sesion.grid(row=6, column=0, sticky=W)

# Defino variables para tomar valores de campos de entrada
a_val, b_val, c_val, d_val, e_val, f_val, h_val = StringVar(
), StringVar(), StringVar(), IntVar(), StringVar(), IntVar(), DoubleVar()
w_ancho = 70

entrada1 = Entry(root, textvariable=a_val, width=w_ancho)
entrada1.grid(row=1, column=1)
entrada2 = Entry(root, textvariable=b_val, width=w_ancho)
entrada2.grid(row=1, column=3)
entrada3 = Entry(root, textvariable=c_val, width=w_ancho)
entrada3.grid(row=2, column=1)
entrada4 = Entry(root, textvariable=d_val, width=w_ancho)
entrada4.grid(row=2, column=3)
entrada5 = Entry(root, textvariable=e_val, width=w_ancho)
entrada5.grid(row=3, column=1)
entrada6 = Entry(root, textvariable=f_val, width=w_ancho)
entrada6.grid(row=4, column=1)

entrada8 = Entry(root, textvariable=h_val, width=w_ancho)
entrada8.grid(row=7, column=1)

titulo2 = Label(root, text="Ingrese primero el precio de la sesion", bg="turquoise1",
                fg="black", height=1, width=70)
titulo2.grid(row=8, column=1, columnspan=1, padx=1, pady=1, sticky=W+E)

# ----------------------------
# TREEVIEW
# ----------------------------

tree = ttk.Treeview(root)
tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6", "col7")
tree.column("#0", width=90, minwidth=50, anchor=W)
tree.column("col1", width=200, minwidth=80)
tree.column("col2", width=200, minwidth=80)
tree.column("col3", width=200, minwidth=80)
tree.column("col4", width=200, minwidth=80)
tree.column("col5", width=200, minwidth=80)
tree.column("col6", width=200, minwidth=80)
tree.column("col7", width=200, minwidth=80)
tree.heading("#0", text="ID")
tree.heading("col1", text="Nombre")
tree.heading("col2", text="Apellido")
tree.heading("col3", text="Tipo de documento")
tree.heading("col4", text="Documento")
tree.heading("col5", text="Dirección")
tree.heading("col6", text="Cantidad de Sesiones")
tree.heading("col7", text="Total a Facturar")
tree.grid(row=12, column=0, columnspan=8)

boton_alta = Button(root, text="Agragar cliente", command=lambda: alta(
    a_val.get(), b_val.get(), c_val.get(), d_val.get(), e_val.get(), f_val.get(), tree))
boton_alta.grid(row=4, column=3)

boton_consulta = Button(root, text="Consultar todo",
                        command=lambda: consultar(tree))
boton_consulta.grid(row=5, column=3)

boton_consulta = Button(root, text="Consultar por doc",
                        command=lambda: seleccionar(d_val.get()))
boton_consulta.grid(row=6, column=3)

boton_borrar = Button(root, text="Eliminar cliente",
                      command=lambda: eliminar(tree))
boton_borrar.grid(row=7, column=3)

boton_editar_sesion = Button(
    root, text="Precio por sesión", command=lambda: actualizar_precio_sesion(h_val.get()))
boton_editar_sesion.grid(row=8, column=0)

root.mainloop()
