import os 
from analysis import ClientAnalysis

file_name = 'test.csv'
file_path = os.path.join(os.getcwd(), file_name)


if __name__ == '__main__':
    # Инициализация экземпляра класса с переданным путем к файлу
    client = ClientAnalysis(file_path=file_path)

    # Получение ДатаФрейма
    client.get_dataframe()
