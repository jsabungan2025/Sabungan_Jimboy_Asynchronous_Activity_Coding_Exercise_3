1. Conceptual Distinction
   1. What error occurred when trying to access atm.__pin directly? Why does Python behave this way?
      
     - When I tried to access atm.__pin directly, it gave me an AttributeError. This is because the PIN was created using two underscores, which means make it to a private attribute. And the python uses name mangling to make these attributes harder to access directly from outside the class. So I think this is useful for sensitive information like a PIN because it helps prevent it from being accidentally accessed, changed or leak to the other person.

   2. How did using @property allow you to change internal data structures or add validation without altering the public API for the caller?
      
    - I using @property made it easier to control how the balance is accessed and changed. I can only simply use account.balance without needing to know that the actual value is stored in balance. In the setter also lets me allowed to add a validation, such as preventing the balance from becoming negative. This means I can change how the balance works internally while the way I use it from outside the class stays the same.

   3. How did the ATM class demonstrate abstraction relative to the underlying BankAccount logic?
      
   - The ATM class demonstrated how flow by hiding the information in the BankAccount class. As a user, I don't have a power to directly change the balance or deal with the transaction list by the time that I want change it because it needs me to contact the personnel of the bank to change that what I want to change. I only can just use as user the methods like check_balance, perform_deposit, and perform_withdrawal. However, outside of it I don't power to change or edit a things because I'm only a user only.
