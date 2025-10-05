from abc import ABC, abstractmethod


class FileBase(ABC):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def close(self):
        pass


class Json(FileBase):
    def __init__(self, new_file):
        self.new_file = new_file

    def open(self):
        return f'the {self.new_file} open in json method '

    def close(self):
        return f"the {self.new_file} close in json method"

    def edit(self):
        return f"the {self.new_file} edit in json method"


class Xml(FileBase):
    def __init__(self, new_file):
        self.new_file = new_file

    def open(self):
        return f'the {self.new_file} open in xml method '

    def close(self):
        return f"the {self.new_file} close in xml method"

    def edit(self):
        return f"the {self.new_file} edit in xml method"


class FileFactory():
    def __init__(self, file_type, file_name):
        self.file_type = file_type
        self.file_name = file_name

    def create_file(self):
        if self.file_type == "json":
            return Json(self.file_name)
        elif self.file_type == "xml":
            return Xml(self.file_name)
        raise ValueError(f"File type '{self.file_type}' not supported")


if __name__ == "__main__":
    f1=FileFactory("json","pouriaFile")
    print(f1.create_file().edit())
