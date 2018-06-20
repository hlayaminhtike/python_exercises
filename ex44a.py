class Parent(object):
    def implicit(itself):
        print("PARENT implicit()")
class Child(Parent):
    pass
dad=Parent()
son=Child()

dad.implicit()
son.implicit()

