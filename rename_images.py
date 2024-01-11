import os

def rename_images(folder_path):
    # First phase: use a temporary
    temp_prefix = "temporary_"
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(('.png','.jpg', '.jpeg')) and f != '.DS_Store']
    for file in files:
        old_file_path = os.path.join(folder_path, file)
        temp_file_path = os.path.join(folder_path, temp_prefix + file)
        print(file)
        os.rename(old_file_path, temp_file_path)

    # Second phase: Remove the prefix and assign the progressive numbers
    temp_files = [f for f in os.listdir(folder_path) if f.startswith(temp_prefix)]
    temp_files.sort()
    for i, temp_file in enumerate(temp_files, start=0):
        new_filename = f"{i}.jpg"
        temp_file_path = os.path.join(folder_path, temp_file)
        new_file_path = os.path.join(folder_path, new_filename)
        print(i)
        os.rename(temp_file_path, new_file_path)

# put the root of the dataset
base_path = 'C:/Users/antos/Desktop/dataset_pulito/chest_xray'
# put the names of the class which were merged 
folders = ['Normal', 'Tuberculosis', 'Pneumonia']

for folder in folders:
    folder_path = os.path.join(base_path, folder)
    rename_images(folder_path)

print("Rename completed.")
