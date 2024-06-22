import win32com.client

def get_folders_iterative(folder):
    folders_list = []
    stack = [folder]

    while stack:
        current_folder = stack.pop()
        folders_list.append((current_folder.Name, current_folder.EntryID))
        
        # Agregar subcarpetas a la pila
        for subfolder in current_folder.Folders:
            stack.append(subfolder)
    
    return folders_list

def main():
    # Crear una instancia de la aplicación Outlook
    outlook = win32com.client.Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")

    # Obtener la carpeta raíz del almacén predeterminado
    root_folder = namespace.Folders.Item(1)  # Puedes ajustar este índice según el almacén de correo
    #root_folder = namespace.GetDefaultFolder(5)  # Puedes ajustar este índice según el almacén de correo

    # Obtener todas las carpetas de manera iterativa
    folders_list = get_folders_iterative(root_folder)

    print(len(folders_list))
    # Imprimir todas las carpetas con sus EntryIDs
    for folder_name, folder_entry_id in folders_list:
        print(f"Folder Name: {folder_name}, EntryID: {folder_entry_id}")

if __name__ == "__main__":
    main()
