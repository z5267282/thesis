def main():
    def real_main():
        a()

    def a():
        print("a")
    
    real_main()
