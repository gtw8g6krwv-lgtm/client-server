class Server:
    def __init__(self):
        self.__requests = []
        self.__responses = []
        self.__is_running = False


    def start(self, request_empty_list_sign: int, first_request_list_index: int):
        self.__is_running = True
        print("Сервер запущен")

        while self.__is_running:
            if len(self.__requests) > request_empty_list_sign:
                request = self.__requests.pop(first_request_list_index)
                response = self.processing_request(request)
                self.__responses.append(response)


    def add_request(self, request):
        self.__requests.append(request)


    def get_response(self, response_empty_list_sign: int, first_response_list_index: int):
        if len(self.__responses) > response_empty_list_sign:
            return self.__responses.pop(first_response_list_index)
        return None


    def processing_request(self, request):
        command = request.get('command', '')

        if command == 'Проверка связи с сервером':
            return {'status': 'success', 'message': request.get('text', '')}

        elif command == 'Текущее время на сервере':
            return {'status': 'success', 'message': 'Время сервера: 12:00:00'}

        elif command == 'Информация о сервере':
            return {'status': 'success', 'message': 'Сервер работает'}

        elif command == 'Выход':
            return {'status': 'success', 'message': 'До свидания!'}

        else:
            return {'status': 'error', 'message': 'Неизвестная команда'}

    def stop(self):
        self.__is_running = False
        print("Сервер остановлен")