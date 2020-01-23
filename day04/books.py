#!/root/ysy/python/bin/python3
'''books
'''
class books:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return 'The book is %s,and it have %s pages.'% \
               (self.title,self.pages)

    def __call__(self, *args, **kwargs):
        print('%s is written by %s' % (self.title,self.author))

if __name__ == '__main__':
    pybook = books('三国志','ysy',50)
    print(pybook)
    pybook()