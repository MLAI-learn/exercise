population={'china':143,
            'india':136,
            'usa':32,
            'pakistan':21}

def print_all():
    for country,p in population.items():
        print(f'{country}==>{p}')

def add():
    a=input('enter country to add')
    a=a.lower()
    if a in population:
        print(f'{a} already exists')
        return
    b=input(f'enter population of {a}')
    b=float(b)
    population[a]=b
    print_all()


def remove():
    r=input('enter country to remove')
    r=r.lower()
    if r not in population:
        print('country not in dict')
        return
    del population[r]
    print_all()


def query():
    q=input('enter country to query')
    q=q.lower()
    if q not in population:
        print('country not in dict')
        return
    print(f"population of {q} is : {population[q]} crores")

def main():
    op=input('enter the operation')
    op=op.lower()
    if op=='print':
        print_all()
    elif op=='add':
        add()
    elif op=='remove':
        remove()
    elif op=='query':
        query()

if __name__ == '__main__':
    main()
     



        
       

      