class Client:
    def __init__(self):
        self.__is_connected = False
        self.__last_response = None


    def connect(self):
        self.__is_connected = True
        print("Клиент подключен к серверу")
        return True


    def send_request(self, command, text=""):
        if not self.__is_connected:
            print("Клиент не подключен")
            return None

        print(f"Отправлен запрос: {command}")

        if command == 'Проверка связи с сервером':
            self.__last_response = f"Эхо: {text}"

        elif command == 'Текущее время на сервере':
            self.__last_response = "Текущее время: 12:00:00"

        elif command == 'Информация о сервере':
            self.__last_response = "Серверная система v1.0"

        elif command == 'Выход':
            self.__last_response = "До свидания!"

        else:
            self.__last_response = "Ошибка: неизвестная команда"

        print(f"Получен ответ: {self.__last_response}")
        return self.__last_response


    def disconnect(self):
        self.__is_connected = False
        print("Клиент отключен")