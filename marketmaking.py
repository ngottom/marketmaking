import random as r
import numpy as np
import matplotlib.pyplot as plt

#global vars
counter = 1
balance = 500
#Scatterplot of balance gets plotted at end
balance_array = []  
loss_rounds = {}
###generate a normal sample for the ask between 3 and 42
mean = 22.5  # Midpoint of the range (3 + 42) / 2
std_dev = 14  # Chosen standard deviation; adjust as necessary

# Function to generate a valid sample within the range [3, 42]
def generate_sample(mean, std_dev):
    while True:
        sample = np.random.normal(loc=mean, scale=std_dev)
        if 3 <= sample <= 41:
            return int(sample)

# Generate one valid sample
sample = generate_sample(mean, std_dev)

# Print the sample
print("Sample from normal distribution (3 to 41):", sample)
# if you want a uniformly distributed ask from 3 to 41
# ask = r.randrange(3,43)
ask = sample
def newCard():
    return r.randrange(2,15)

def newRound():
    global counter
    global balance
    global loss_rounds
    print(f'Starting balance:{balance}')
    ask = r.randrange(3,43)
    print(f'YOUR ASK:{ask}')
    card1 = newCard()
    print(f'CARD1:{card1}')
    card2 = 2
    print(f'CARD2:{card2}')
    card3 = 2
    print(f'CARD3:{card3}')
    card_total = card1 + card2 + card3
    print(f'cardtotal:{card_total}')

    
  
    #kellyCriterion():
        # p = probability of winning
    possible_total = r.randrange(card1+2,43)
    min_hand = card1 + 4
    max_hand = card1 + 28
    range_hand = max_hand - min_hand + 1
    if max_hand < ask:
        bet_percentage = 0
        print(f'bet percentage was 0')
    elif min_hand > ask:
        bet_percentage = 1
    else:
        p = (max_hand - ask)/ range_hand
        print(f'Probability of winning: {p}')
        q = 1-p
        b = 2
        bet_percentage = p - (q/b)
        if bet_percentage > 1:
            bet_percentage = 1
        if bet_percentage <= 0:
            bet_percentage = 0
        print(f'Bet percentage:{bet_percentage}')
        
    

    #bet
    
    if bet_percentage > 0:
        units_bought = (bet_percentage * balance) // ask
        print(f'units bought:{units_bought}')
        new_bet = units_bought * ask
        result = (card_total * units_bought ) - new_bet
        print(f'Net result:{result}')
        old_balance = balance
        balance += result
        print(f'NEW BALANCE:{balance}')
        if old_balance > balance:
            loss_rounds[counter] = 1-(balance / old_balance)  
            counter+=1   
            print(f'loss rounds:{loss_rounds}')
    else:
        print(f'Unchanged balance:{balance}')
    balance_array.append(balance)
    counter +=1
    
    # print(balance_array)
        
         
    


#starts simulation
def startGame():
    round = 1
    maxRounds = 100
    while balance > 0 and round <= maxRounds:
        newRound() 
        print(f'Round:{round}')
        round +=1
        print(f'==========New Round==========')

    
    
     


startGame()

### plot results 

time_points = list(range(len(balance_array)))  # Corresponding time points

# Create a scatter plot
plt.scatter(time_points, balance_array)

# Add title and labels
plt.title('Total Balance over Time')
plt.yscale('log')

plt.xlabel('Time')
plt.ylabel('Money')

# Display the plot
plt.show()


## plot the losses

x = list(loss_rounds.keys())
y = list(loss_rounds.values())

# Step 3: Create a scatter plot
plt.scatter(x, y)

# Step 4: Add titles and labels
plt.title('Lost Rounds and Percentage Loss')
plt.xlabel('Lost Rounds')
plt.ylabel('Loss Percentage')

# Step 5: Show the plot
print(loss_rounds)
plt.show()

#  Findings:
# Balance will follow almost linear progression towards infinity under a payout ratio of 1:1.
# An interesting result is when the payoff is increased considerably but the odds of a winning hand are rigged to be significantly reduced, as in the case of 
# setting card2 and card3 value to 0. In such a case, the kelly formula shows that there is no optimal strategy to win. A rigged odds is analogous to perhaps drawing 
# values from a rigged deck in a game of poker.