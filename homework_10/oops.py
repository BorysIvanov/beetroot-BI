def oops():
    raise IndexError("Oops! An IndexError occurred.")

def catch_error():
    try:
        oops()
    except IndexError as e:
        print("Caught an IndexError:", e)


catch_error()

