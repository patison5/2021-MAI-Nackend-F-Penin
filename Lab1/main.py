from LRUCache import LRUCache

if __name__ == '__main__':

    cache = LRUCache(10)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')
    print("вернёт 'James': ", cache.get('Jesse'))  # вернёт 'James'
    cache.rem('Walter')
    print("вернёт 'key not found!': ", cache.get('Walter'))  # вернёт 'key not found!'

    print("~ Элементы двусвязного списка:")
    cache.list_all_items()

    print('\n~ Мапа:')
    cache.list_all_map_items()