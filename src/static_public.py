import os, shutil

source = "static"
destination = "public"

def file_transfer():
    print("Deleting public directory files......")
    if not os.path.exists(destination):
        os.makedirs(destination)
    else:
        for file_name in os.listdir(destination):
            file_path = os.path.join(destination, file_name)

            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
            else:
                os.remove(file_path)
    print("Copying contents of static to public")
    for item in os.listdir(source):
        source_item = os.path.join(source, item)
        destination_item = os.path.join(destination, item)

        if os.path.isdir(source_item):
            shutil.copytree(source_item, destination_item)
        else:
            shutil.copy(source_item, destination_item)
 
