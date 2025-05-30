from abc import ABC, abstractmethod

class MixinLog(ABC):
    @abstractmethod
    def mostrar_log(self, mensagem: str):
        #Exibe uma mensagem de log no terminal.
        pass

class LogConsoleMixin(MixinLog):
    def mostrar_log(self, mensagem: str):
        print(f"[LOG] {mensagem}")