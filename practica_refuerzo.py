class producto:
    def __init__(self, nombre,precio,cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    def valor_total(self):
        return self.precio * self.cantidad
    def mostrar_info(self):
        return f"Producto: {self.nombre} | Precio: {self.precio} | Cantidad: {self.cantidad} | Valor total: {self.valor_total()}"
    
import sqlite3
conexion = sqlite3.connect("inventario.db")
cursor = conexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS productos (nombre text, precio real, cantidad integer)")

nom = input("Ingrese el nombre del producto: ")
pre = float(input("ingrese el precio del producto: "))
cant = int(input("ingrese la cantidad del producto: "))

nuevo_producto = producto(nom, pre, cant)
cursor.execute("INSERT INTO productos VALUES (?, ?, ?)", (nuevo_producto.nombre, nuevo_producto.precio, nuevo_producto.cantidad))
print(nuevo_producto.mostrar_info())

conexion.commit()
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
print("Productos en la base de datos:")
for producto in productos:
    print(f"Producto: {producto[0]} | Precio: {producto[1]} | Cantidad: {producto[2]}")
conexion.close()