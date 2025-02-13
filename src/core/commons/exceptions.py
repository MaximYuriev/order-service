class ApplicationException(Exception):
    @property
    def message(self) -> str:
        return "Ошибка выполнения приложения!"
