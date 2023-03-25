Brief for Design Project. 

Replicating an RPG shop. 

Classes: 
Loot
Items
Store
Adventurer

MVP: 

> Adventurers will be able to sell their loot at the store. 
> The store will appraise their Loot and convert this to Items. 
> The adventurer will be able to sell Items and buy Items. 
> The adventurer will have an inventory display. 
> The shop will display it’s most expensive items from its stock in the front of the store (the home page) 

C.R.U.D

> The store will be able to C.R.U.D  to its stock. 
> the store will be able to C.R.U.D to its appraisal book. 

Extensions:

> it’d be nice also if the shop will resell items from the adventurers with a percentage markup. (i.e. add bought items to the stock dict)
> add attributes to the adventurer class for equipped Items.

Advanced: 

> The user could negotiate the price for all their loot

Behaviours: 

Adventurer: 

storeItems(): store items into their Inventory
buyItems() : adventurer will be able to buy items from the store into their inventory. 

Store: 

appraisal() - The store will take in Loot and convert this to an Item using a dictionary lookup and charge the adventurer

buyLoot() - Adventurers can choose to sell their loot without appraisal.

buyItems() - Can buy Items. 

resell() - The store resells Items bought. If they are a Loot object, it is appraised first.  
