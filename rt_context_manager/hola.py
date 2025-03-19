# hola.py
class HolaMundo:
    def __enter__(self):
        print("Entering context")
        return "¿Qué pasa?"

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_tb is not None:
            print("Exception occurred in context", exc_type, exc_value, exc_tb)
            return True

        print("Leaving context")
