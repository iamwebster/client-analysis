import pandas as pd 
from pandas import DataFrame


class ClientAnalysis:
    def __init__(self, file_path: str) -> None:
        '''
        Инициализация ДатаФрейма.
        Загружает данные из CSV файла в в формате pandas DataFrame.
        '''
        try:
            self.df = pd.read_csv(file_path)
        except FileNotFoundError as e:
            print('Файл не найден:', e)

        return None

    def get_dataframe(self) -> DataFrame:
        '''Получение ДатаФрейма.'''
        return self.df
    
    def get_client_actions(self) -> DataFrame:
        '''Подсчет числа действий каждого клиента.'''
        self.df = self.df.groupby(['client_id', 'action']).count()
        return self.df
    
    def filter_client_data(self, client_id: int | None = None, 
                           action: str | None = None, timestamp: str | None = None) -> DataFrame:
        '''
        Фильтрация данных по определенным критериям:
        - Идентификатор клиента
        - Активность
        - Временная точка (в формате "YYYY-MM-DD HH:MM:SS")
        '''

        if client_id:
            self.df = self.df[self.df['client_id'] == client_id]
        if action:
            self.df = self.df[self.df['action'] == action]
        if timestamp:
            self.df = self.df[self.df['timestamp'] == timestamp]

        return self.df
    
    def analyze_client_behavior(self) -> DataFrame:
        '''Получение топ-5 клиентов с наибольшим числом действий.'''
        self.df = self.df[['client_id', 'action']].groupby('client_id').\
            count().sort_values(['action'], ascending=False)[:5].reset_index()
        return self.df
    
    def save_processed_data(self, file_name: str) -> bool:
        '''
        Сохранение обработанных данных после анализа в формате CSV.
        
        Возвращает True, если данные успешно сохранились. 
        Возвращает False, если произошла ошибка.
        '''
        try:
            self.df.to_csv(f'{file_name}.csv', encoding='utf-8')
            return True
        except IOError as e:
            print('Ошибка сохранения файла:', e)
            return False
        