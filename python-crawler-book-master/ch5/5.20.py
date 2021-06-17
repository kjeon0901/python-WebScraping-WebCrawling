class namespace1:
    @staticmethod
    def s1():
        print('namespace1 s1스태틱 매소드')

    @staticmethod
    def s2():
        print('namespace1 s2스태틱 매소드')


class namespace2:
    @staticmethod
    def s1():
        print('namespace2 s1스태틱 매소드')

    @staticmethod
    def s2():
        print('namespace2 s2스태틱 매소드')

namespace1.s1()
namespace2.s2()
