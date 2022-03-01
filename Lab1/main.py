from LRUCache import LRUCache

if __name__ == '__main__':

    print("Hello world")

    cache = LRUCache(100)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')
    cache.get('Jesse')  # вернёт 'James'
    cache.rem('Walter')
    cache.get('Walter')  # вернёт ''