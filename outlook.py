import win32com.client

def get_folders(folder, folders_list):
    """
    Función recursiva para obtener todas las carpetas y sus subcarpetas
    :param folder: La carpeta actual a procesar
    :param folders_list: Lista para almacenar la información de las carpetas
    """
    folders_list.append((folder.Name, folder.EntryID))
    for subfolder in folder.Folders:
        get_folders(subfolder, folders_list)

def main():
    # Crear una instancia de la aplicación Outlook
    outlook = win32com.client.Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")

    # Obtener la carpeta raíz del almacén predeterminado
    root_folder = namespace.Folders.Item(1)  # Puedes ajustar este índice según el almacén de correo

    # Lista para almacenar las carpetas
    folders_list = []

    # Obtener todas las carpetas
    get_folders(root_folder, folders_list)

    # Imprimir todas las carpetas con sus EntryIDs
    for folder_name, folder_entry_id in folders_list:
        print(f"Folder Name: {folder_name}, EntryID: {folder_entry_id}")

if __name__ == "__main__":
    main()