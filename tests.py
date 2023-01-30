from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    


    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        # создаем экземпляр (объект) класса BooksCollector
        

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2
        
    #тестирование добавления двух книг
    def test_add_new_book_add_two_books_clone(self):
        collector = BooksCollector()
        collector.add_new_book('Nemo')
        collector.add_new_book('Nemo')

        assert len(collector.get_books_rating()) == 1
        assert collector.get_book_rating('Nemo') == 1

    #тестирование добавления рейтинга книге
    def test_set_book_rating_Papirus_result_6(self):
        collectior = BooksCollector()
        collectior.add_new_book('Papirus')
        collectior.set_book_rating('Papirus',6)

        assert collectior.get_book_rating('Papirus') == 6

    #дбавление рейтинга книги, которой нет в словаре
    def test_set_book_rating_is_not_in_map(self):
        collector = BooksCollector()
        collector.add_new_book('Ris')
        collector.set_book_rating('Grecha',5)

        assert collector.get_book_rating('Grecha') != 5
        assert len(collector.get_books_rating()) == 1
        
    #тестирование невозможности добавления рейтинга ниже 1
    def test_set_book_rating_cannot_be_min_1(self):
        collector = BooksCollector()
        collector.add_new_book('Avatar')
        collector.set_book_rating('Avatar',9)
        collector.set_book_rating('Avatar', -1)

        assert collector.get_book_rating('Avatar') != 1
        assert collector.get_book_rating('Avatar') == 9
        
    #тестирование добаления рейтинга выше 10 (ошибка)
    def test_set_book_rating_cannot_be_moremax_10(self):
        collector = BooksCollector()
        collector.add_new_book('Milf')
        collector.set_book_rating('Milf',10)
        collector.set_book_rating('Milf',11)
        
        assert collector.get_book_rating('Milf') == 10
        assert collector.get_book_rating('Milf') != 11
        
    #
    def test_not_add_book_havnt_rating(self):
        collector = BooksCollector()
        collector.add_new_book('LalaLend')
        collector.set_book_rating('Piro',5)
        
        #Нельзя добавить рейтинг книге, который нет в словаре
        assert collector.get_book_rating('LalaLend') == 1
        assert collector.get_book_rating('Piro') != 5
        assert collector.get_book_rating('Piro') != 1
        
    #тестирование добавления книги в избранное
    def test_add_book_in_favorite_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Snikers')
        collector.add_book_in_favorites('Snikers')
        
        assert len(collector.get_list_of_favorites_books()) == 1
        
    #тестирования не добавления в избранное если книги нет в словаре
    def test_add_book_in_favorite_book_if_not_in_rating(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Stalker')
        
        assert len(collector.get_list_of_favorites_books()) != 1
        
    #тестирования удаления книги из избранного
    def test_deleted_book_in_favorites_book_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Machin')
        collector.add_book_in_favorites('Machin')
        
        assert len(collector.get_list_of_favorites_books()) == 1
        
        collector.delete_book_from_favorites('Machin')
        
        assert len(collector.get_list_of_favorites_books()) == 0
    
    
#далее идет вторая версия кода, я создал тест с глобальной переменной работающей в рамках тестового класса для упрощения кода

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollectorr:
    collector = BooksCollector()
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):

        # создаем экземпляр (объект) класса BooksCollector
        #collector = BooksCollector()

        # добавляем две книги
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(self.collector.get_books_rating()) == 2
            
    #тест добавление одинаковых книг
    def test_add_new_book_add_two_copy_books(self):

        self.collector.add_new_book('Pop')
        self.collector.add_new_book('Pop')
        #проверка количества одинаковых книг
        assert len(self.collector.get_books_rating()) == 3
        assert self.collector.get_book_rating('Pop') == 1
        
    def test_set_book_rating_Papirus_result_6(self):
        
        self.collector.set_book_rating('Pop',6)
        #проверка что рейтинг книги равен 6
        assert self.collector.get_book_rating('Pop') == 6
        
    #дбавление рейтинга книги, которой нет в словаре
    def test_set_book_rating_is_not_in_map(self):
        # выставление рейтинга книги, которой нет в словаре
        self.collector.set_book_rating('Grecha',5)
        #проверка что у гречи не появился рейтинг и она не появилась в словаре
        assert self.collector.get_book_rating('Grecha') != 5
        assert len(self.collector.get_books_rating()) == 3
    #тестирование невозможности добавления ретинга ниже 1
    def test_set_book_rating_cannot_be_min_1(self):
    
        self.collector.set_book_rating('Pop',-1)
        #проверка что рейтинг не ставится отрицательный и должен остаться рейтинг 6, который бы в словаре
        assert self.collector.get_book_rating('Pop') != -1
        assert self.collector.get_book_rating('Pop') == 6
    #тест невозможности добавления рейтинга больше 10
    def test_set_book_rating_cannot_be_max_10(self):
        
        self.collector.set_book_rating('Pop', 11)
        #проверяем что рейтинг книги не изменился
        assert self.collector.get_book_rating('Pop') != 11
        assert self.collector.get_book_rating('Pop') == 6
    #тест невозможности добавить рейтинг книги,которой нет в маппе
    def test_add_new_book_havnt_rating(self):
        
        self.collector.set_book_rating('Piro',5)
        #Проверяем что рейтинг не выставлен и кол-во книг не изменилось
        assert self.collector.get_book_rating('Piro') != 5
        assert len(self.collector.get_books_rating()) == 3
    #Проверка добавления книги в избранное
    def test_add_book_in_favorites_book_added(self):
    
        self.collector.add_book_in_favorites('Pop')
        #Проверяем что в избранном появлиась одна книга
        assert len(self.collector.get_list_of_favorites_books()) == 1
    #Проверка невозможности добавить в избранное книгу, которой нет в маппе
    def test_add_book_in_favorites_if_book_not_in_mappa(self):
    
        self.collector.add_book_in_favorites('Rango')
        #Проверка что кол-во книг в избранном не изменилось
        assert len(self.collector.get_list_of_favorites_books()) == 1
    #Проверка удаления книги из избранного
    def test_deleted_book_in_favorite_book_deleted(self):
        #Проверяем что книг в избранном одна
        assert len(self.collector.get_list_of_favorites_books()) == 1
        #Удаляем книгу из избранного
        self.collector.delete_book_from_favorites('Pop')
        #Проверяем что после удаления книг осталось 0
        assert len(self.collector.get_list_of_favorites_books()) == 0
        
    
        
        
        
        
    
        


        
    
