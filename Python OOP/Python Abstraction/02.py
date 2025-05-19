# Payment Gateway System
# Abstract class: PaymentMethod
# Child classes: CreditCard, PayPal, GooglePay
# Abstract method: pay(amount)
# Task: Ask the user to choose a payment method, and each class should print how the payment is processed for that method.
from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"{amount} deducted from your credit card")
class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"{amount} deducted from your PayPal ID")
class GooglePlay(PaymentMethod):
    def pay(self, amount):
        print(f"{amount} deducted from your Google Play")
methods = {
    "creditcard": CreditCard(),
    "paypal": PayPal(),
    "googleplay": GooglePlay()
}
user_method = input("Enter your payment method (CreditCard / PayPal / GooglePlay): ").strip().lower().replace("-", "").replace(" ", "")
amount = int(input("Enter the amount you want to pay: "))
if user_method in methods:
    methods[user_method].pay(amount)
else:
    print("Invalid payment method. Please choose from CreditCard, PayPal, or GooglePlay.")
