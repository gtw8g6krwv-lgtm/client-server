from server import Server
from client import Client


class Application:
    def __init__(self):
        self.__running = True
        self.__server = None
        self.__client = None


    def run(self):
        print("Клиент-серверная система")
        first_menu_point = "1"
        second_menu_point = "2"
        third_menu_point = "3"
        run_server = "Запустить сервер"
        run_client = "Запустить клиент"
        exit = "Выход"


        while self.__running:
            print("\nВыберите режим работы:")
            print(f"{first_menu_point}. {run_server}")
            print(f"{second_menu_point}. {run_client}")
            print(f"{third_menu_point}. {exit}")

            user_choice = input(f"\nВаш выбор ({first_menu_point}-{third_menu_point}): ").strip()

            if user_choice == first_menu_point:
                self.__run_server_mode()

            elif user_choice == second_menu_point:
                self.__run_client_mode()

            elif user_choice == third_menu_point:
                self.__running = False
                print("До свидания!")
            else:
                print("Неверный выбор")


    def __run_server_mode(self):
        self.__server = Server()
        self.__server.start()
        stop_server = "стоп"
        check_status = "статус"

        server_active = True

        while server_active:
            user_command = input("\nСервер > ").strip()

            if user_command == stop_server:
                self.__server.stop()
                server_active = False

            elif user_command == check_status:
                print("Сервер работает")
            else:
                print("Доступные команды: стоп, статус")


    def __run_client_mode(self):
        self.__client = Client()
        self.__client.connect()
        self.__show_help()

        session_active = True

        while session_active:
            user_input = input("\nКлиент > ").strip()






