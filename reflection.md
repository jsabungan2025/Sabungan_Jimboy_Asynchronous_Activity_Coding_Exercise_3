1. Conceptual Distinction
   1. What error occurred when trying to access atm.__pin directly? Why does Python behave this way?
      
     - When I tried to access atm.__pin directly, it gave me an AttributeError. This is because the PIN was created using two underscores, which means make it to a private attribute. And the python uses name mangling to make these attributes harder to access directly from outside the class. So I think this is useful for sensitive information like a PIN because it helps prevent it from being accidentally accessed, changed or leak to the other person.

   2. How did using @property allow you to change internal data structures or add validation without altering the public API for the caller?
      
    - I using @property made it easier to control how the balance is accessed and changed. I can only simply use account.balance without needing to know that the actual value is stored in balance. In the setter also lets me allowed to add a validation, such as preventing the balance from becoming negative. This means I can change how the balance works internally while the way I use it from outside the class stays the same.

   3. How did the ATM class demonstrate abstraction relative to the underlying BankAccount logic?
      
   - The ATM class demonstrated how flow by hiding the information in the BankAccount class. As a user, I don't have a power to directly change the balance or deal with the transaction list by the time that I want change it because it needs me to contact the personnel of the bank to change that what I want to change. I only can just use as user the methods like check_balance, perform_deposit, and perform_withdrawal. However, outside of it I don't power to change or edit a things because I'm only a user only.
  
2. Final Reflection Questions
   1. What error occurred when trying to access atm.__pin directly? Why does Python behave this way?
      
   -When I tried to access atm.__pin directly, I got an AttributeError. This will happened because __pin is a private attribute in the ATM class. In the python uses name mangling for attributes that start with two underscores, which makes it harder to access them directly from outside the class. This helps us protect important data, like the PIN or data imformation of the user and from being accidentally changed, accessed or leaks of data information of the user.

   3. How did using @property allow you to change internal data structures or add validation without altering the public API for the caller?
      
   -Using @property allowed me to access the balance using account.balance instead of calling a separate getter method. Even though the actual balance is stored internally as _balance, the user does not need to know how it is stored.
It also allowed me to add validation when changing the balance. For example, I can prevent the balance from being set to a negative number through the setter. The way the caller uses account.balance stays the same even if the internal code or validation changes.

   4. How did the ATM class demonstrate abstraction relative to the underlying BankAccount logic?
      
   -The ATM class demonstrates how works by hiding the more complicated account operations from the user. Instead of directly accessing with _balance or _transactions, the user can only simply use methods like check_balance, perform_deposit, and perform_withdrawal. Other than method they are not have access to edit or change any information without the personnel of the bank.
