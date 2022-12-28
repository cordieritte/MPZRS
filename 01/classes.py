"""Computer and service sketch"""
import datetime
import urllib.request


class FileSystem:
    """The file system stub"""

    def __init__(self):
        self._files = ["file1.txt", "file2.txt"]
        self._space = 12345

    def files(self):
        """Return the list of files"""
        return self._files

    def space(self):
        """Return the free space in storage"""
        return self._space


class Computer:
    """Computer"""

    def __init__(self):
        self._handlers = {}
        self._file_sys = FileSystem()

    def send_request(self, destination, name, command, *args):
        """Send to destination (dst) some (name) request with command
        and optional args"""
        answer = destination._handlers[name](command, *args)
        print(answer)

    def add_service(self, srv):
        """Add service to computer"""
        self._handlers[srv.name()] = srv.handle_request

    def file_system(self):
        """Give access to the file system"""
        return self._file_sys


class Files:
    """The service providing the work with files"""

    @staticmethod
    def name():
        return "files"

    def __init__(self, comp):
        self._comp = comp

    def handle_request(self, command, *args):
        """Handle request"""
        if command == "list":
            return self.list_of_files()

        if command == "space":
            return self.free_space()

        if command == "reduce space":
            return self.reduce_space(*args)

        if command == "add files":
            return self.transfer_files(*args)

        return "Wrong args or command"

    def list_of_files(self):
        """Return the list of files"""
        return self._comp.file_system().files()

    def free_space(self):
        """Return the free space in storage"""
        return self._comp.file_system().space()

    def transfer_files(self, file):
        """Add file (file) to computer file system"""
        self._comp.file_system()._files.append(file)
        return self.list_of_files()

    def reduce_space(self, space):
        """Reduce space of the computer file system"""
        self._comp.file_system()._space = self._comp.file_system()._space - space
        return self.free_space()


class Clock:
    """Time service"""
    
    
    @staticmethod
    def name():
        return "clock"

    def handle_request(self, command, *args):
        """Handle request"""
        if command == "now":
            if args[0] == "local":
                return "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())

            if args[0] == "utc":
                return "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.utcnow())

            return "Wrong args"

        return "Unknown command"


class Network:
    """Network service"""
    
    
    @staticmethod
    def name():
        return "network"

    def handle_request(self, command, *args):
        """Handle request"""
        if command == "check":
            host = "http://google.com"
            try:
                urllib.request.urlopen(host)
                return True
            except:
                return False

        return "Unknown command"
