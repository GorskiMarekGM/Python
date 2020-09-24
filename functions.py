def announce(f):
    def wrapper():
        print("About to run function")
        f()
        print("Done with function")
        return wrapper
#decorator function adds additional features to the function

@announce
def hello():
    print("Hello world!")


# Shark article

def announcer2(f):
    def decorate_me():
        print("Shark in the ocean")
        f()
        print("Author: Tim")
        return decorate_me

@announcer2
def post():
    print("This is text of the first post, about sharks")
