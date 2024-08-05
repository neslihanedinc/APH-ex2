#2. Create a Python program that calculates the factorial of a given number.
def factorial(n):
    if n<0 :
        return "negatif sayiların faktoriyeli hesaplanmaz"
    result=1 #Faktöriyel sonucunu saklamak için kullanılan değişkendir. Bu kodda, başlangıçta genellikle result değişkeni 1 olarak ayarlanır.
    for i in range(1,n+1):
        result *=i
    return result
while True:
    user_input=input("Enter a number(or type exit to quit): ")
    if user_input.lower() == 'exit':
        break
    try:
        x=int(user_input)
        print(f"The factorial of {x} is {factorial(x)}.")
    except ValueError:
        print("Please enter a valid integer.")



