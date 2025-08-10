from pathlib import Path
from functools import partial
import os


class FileOrganizer():
    def __init__(self, directory):
        self.directory = directory

    def verify_folders(self, folder_type, is_empty, item, directory):
        if is_empty:
            (directory / folder_type).mkdir(exist_ok=True)
        else:
            if item.stem != folder_type:
                (directory / folder_type).mkdir(exist_ok=True)

    def has_subdirectories(self, path):
        return any(os.path.isdir(os.path.join(path, item))
                   for item in os.listdir(path))

    def return_file_type(self, file):
        return file.suffix[1:]
    
    def create_category_folder(self):
        try:
            directory = Path(self.directory)
            folders = ["Images", "Videos", "Documents", "Spreadsheets",
                       "Presentations", "Compressed", "Executable", "Code",
                       "Database", "Vector Graphics", "Audios",
                       "Fonts", "3D Models", "Disk Images", "Others"]
            if self.has_subdirectories(directory):
                for item in directory.iterdir():
                    if item.is_dir():
                        verify_folder = partial(self.verify_folders,
                                                is_empty=False,
                                                item=item, directory=directory)
                        list(map(verify_folder, folders)) 
            else:
                verify_folder = partial(self.verify_folders, is_empty=True,
                                        item=None, directory=directory)
                list(map(verify_folder, folders))     
        except OSError as e:
            print(f"Error Processing {self.directory} : {e}")   

    def move_file(self, file, destination):     
        file.rename(destination / file.name)    

    def match_file(self, file, directory):
        """
        Matches file type and moves it to the appropriate subdirectory.
        Args:
            file: Path to the file (Path).
            directory: Base directory where subdirectories will be 
            created (Path).
        """
        file_type = self.return_file_type(file)    
        print(directory)
        match file_type:
            case 'png' | 'jpg' | 'jpeg' | 'gif' | 'bmp' | 'tiff' | 'tif' | 'svg' | 'webp':
                destination = directory / "Images"
                self.move_file(file, destination)
            case 'mp4' | 'avi' | 'mkv' | 'mov' | 'wmv' | 'flv' | 'mpeg' | 'mpg':
                destination = directory / "Videos"
                self.move_file(file, destination)
            case 'mp3' | 'wav' | 'aac' | 'ogg' | 'flac' | 'm4a':
                destination = directory / "Audios"
                self.move_file(file, destination)
            case 'doc' | 'docx' | 'pdf' | 'txt' | 'rtf' | 'odt':
                destination = directory / "Documents"
                self.move_file(file, destination)
            case 'xls' | 'xlsx' | 'csv' | 'ods':
                destination = directory / "Spreadsheets"
                self.move_file(file, destination)
            case 'ppt' | 'pptx' | 'odp':
                destination = directory / "Presentations"
                self.move_file(file, destination)
            case 'zip' | 'rar' | '7z' | 'tar' | 'gz':
                destination = directory / "Compressed"
                self.move_file(file, destination)
            case 'exe' | 'app' | 'apk' | 'bat' | 'sh':
                destination = directory / "Executable"
                self.move_file(file, destination)
            case 'py' | 'java' | 'cpp' | 'c' | 'html' | 'css' | 'js' | 'php':
                destination = directory / "Code"
                self.move_file(file, destination)
            case 'sql' | 'db' | 'sqlite' | 'mdb':
                destination = directory / "Database"
                self.move_file(file, destination)
            case 'ai' | 'psd' | 'eps' | 'indd':
                destination = directory / "Vector Graphics"
                self.move_file(file, destination)
            case 'ttf' | 'otf':
                destination = directory / "Fonts"
                self.move_file(file, destination)
            case 'obj' | 'fbx' | 'stl' | '3ds':
                destination = directory / "3D Models"
                self.move_file(file, destination)
            case 'iso' | 'dmg':
                destination = directory / "Disk Images"
                self.move_file(file, destination)
            case _:
                destination = directory / "Others"
                self.move_file(file, destination)    

    def place_file_in_folder(self):
        self.create_category_folder()
        try:
            directory = Path(self.directory)
            for item in directory.iterdir():
                if item.is_file():
                    self.match_file(item, directory)
        except OSError as e:
            print(f"Error processing {directory}: {e}")


def organize_files_into_folders(folder):
    organizer = FileOrganizer(folder)
    organizer.place_file_in_folder()
        


    
