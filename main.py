import files

"""Para la funcion Update"""
# try:
#     files.update("sample.txt", "Hola")

# except ValueError as error:
#     print("No se pudo modificar el archivo:", error)

"""Para la funcion read"""
content = files.read("sample.txt")
print(content)


print("Programa terminado con éxito")
