# gg23026-main
from add import add_numbers
from mult import multiply_numbers

def main():
    print("Main programma")

    a, b = 5, 3
    print(f"Summa skaitļiem {a} un {b} ir {add_numbers(a, b)}.")

    x, y = 4, 7
    print(f"Reizinājums starp skaitļiem {x} un {y} ir {multiply_numbers(x, y)}.")

if __name__ == "__main__":
    main()