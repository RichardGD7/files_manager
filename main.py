import files

"""Para la funcion Update"""
# try:
#     files.update("sample.txt", "Hola")

# except ValueError as error:
#     print("No se pudo modificar el archivo:", error)

"""Para la funcion read"""
list1 = [{"username": "ricardo", "role": "developer"}]

# files.create("sample.json", list1)
files.update("sample.json", [{"username": "Alfredo", "role": "developer"}])

print(files.read("sample.json"))


print("Programa terminado con éxito")
