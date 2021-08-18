class Question(dict):
    def __init__(self, type, name, message, choices=None):
        self.type = type
        self.name = name
        self.qmark = "[!]"
        self.message = message
        self.choices = choices or list()

    def __dict__(self):
        return {
            "type": self.type,
            "qmark": self.qmark,
            "message": self.message,
            "name": self.name,
            "choices": list(map(lambda x: {"name": x}, self.choices)),
        }

    def __setitem__(self, key, item):
        self.__dict__()[key] = item

    def __getitem__(self, key):
        return self.__dict__()[key]

    def __iter__(self):
        return iter(self.__dict__())
    
    def __contains__(self, item):
        return item in self.__dict__()
    
    def __len__(self):
        return len(self.__dict__())

    def __delitem__(self, key):
        del self.__dict__()[key]

    def has_key(self, k):
        return k in self.__dict__()

    def update(self, *args, **kwargs):
        return self.__dict__().update(*args, **kwargs)

    def keys(self):
        return self.__dict__().keys()

    def values(self):
        return self.__dict__().values()

    def items(self):
        return self.__dict__().items()

    def pop(self, *args):
        return self.__dict__().pop(*args)
    
    def copy(self):
        return self.__dict__().copy()


class CheckboxQuestion(Question):
    def __init__(self, name, choices=None):
        message = f"Select {name}"
        super().__init__("checkbox", name, message, choices=choices)


class ListQuestion(Question):
    def __init__(self, name, choices=None):
        message = f"Select {name}"
        super().__init__("list", name, message, choices=choices)
