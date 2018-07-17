# The AI's Power Switch is set to On (1) by Default
power_switch = 1
user_name = "John"


# The AI is allowed to keep going as long as their power is over 0.
while power_switch > 0:
    print("You are still playing, because your power is %d." % power_switch)
    # Your game code would go here, which includes challenges that make it
    #   possible to lose power.
    # We can represent that by just taking away from the power.
    # power_switch = power_switch - 1
    command = input('Enter your Command Sir: ')

print("\nOh no, the power switch has been turned off! Game Over Man, Game over!.")