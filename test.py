from seq import Seq

if __name__ == '__main__':
    def f(x):
        print(x + 1)
        return x + 2


    Seq.of([1, 2, 3]).map(lambda x: f(x)).take(2).subscribe(print)
    # iter([1,2])
    print(Seq.of(1, 2, 3).join('a'))
    a0 = Seq.of(1, 2, 3)
    a = a0.take(3)
    b = a0.take(2)
    print(a.join(','))
    print(b.join(','))
    [1, "a"].__iter__()
