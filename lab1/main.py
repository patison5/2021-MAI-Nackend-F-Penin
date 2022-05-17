from LRUCache import LRUCache

if __name__ == '__main__':

    cache = LRUCache(10)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')

    print('\n~ Весь набор элементов::')
    cache.list_all_map_items()
    
    print("\nОбратимся по ключу 'Jesse', ожидаемый результат:  'James': ", cache.get('Jesse'))  # вернёт 'James'

    print("\nУдалим значение по ключу Walter")
    cache.rem('Walter')
    print("Обратимся по ключу Walter, ожидаемый результат 'key not found!': ", cache.get('Walter'))  # вернёт 'key not found!'

    print("\n~ Элементы двусвязного списка:")
    cache.list_all_items()

    print('\n~ Мапа:')
    cache.list_all_map_items()
