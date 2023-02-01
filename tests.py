from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
#Балгодарю за предыдущее ревью! Желаю хорошего дня и прекрасного настроения! :)


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
        #Внес изменения, теперь проверяем что количество не изменилось
        #Нельзя добавить рейтинг книге, который нет в словаре
        assert collector.get_book_rating('LalaLend') == 1
        assert len(collector.get_books_rating()) == 1
        
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
    

        
        
    
        


        
    
