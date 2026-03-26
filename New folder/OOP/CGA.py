# I'm not addicted, I can quit anytime I want I swear
import time
import random
ACTION_upgrade = ["?", "?u", "?up", "?upg", "?upgrade", "u", "up", "upg", "upgrade"]
ACTION_slot = ["!", "!s", "!slot", "!slotmachine", "slot", "slotmachine"]
ACTION_more = ["m", "more"]
ACTION_skip = ["skip", "end"]
ACTION_quit = ["q","quit", "exit"]

CHOICE_confirm = ["y", "yes", "!", "1"]
CHOICE_cancel = ["n", "no", "nope", "x", "?"]
QUITGAME = False

randomTip = [
    ["the slotmachine can be accessed with '!'", "the upgrade shop can be accessed with '?'",
     "check out upgrades daily", "some gamblers quit right before winning",
     "don't bid too much now", "remember, you have rent to pay and goal to reach",
     "", "",]
             ]

class Icon:
    def __init__(self, icon:str, value:int, multi:float, count:int):
        self.icon = icon
        self.value = value
        self.multi = multi
        self.count = count or 1

    def __str__(self):
        pass
iconList = []

class Stat:
    def __init__(self, money:int=0, aLv:int=0):
        self.day = 0
        self.maxDay = 21
        self.roll = 10
        self.money = money
        self.addictionLevel = aLv
        self.goal = [1, 0]
        self.upgrade = []
    
    def progressDay(self):
        self.day+=1
        if self.addictionLevel > 100:
            self.addictionLevel = 100
        elif self.addictionLevel < 0:
            return False

        if self.day > self.goal[0]:
            if self.money < self.goal[1] or self.day > self.maxDay:
                return False
            offset = 3
            if self.day%7 == 0:
                offset = 4
            self.goal = [self.goal[0]+offset, self.goal[1]+50]
        return True

upgradeList = []
class Upgrade:
    def __init__(self, rarity:int, cost:int, increment:int, maxLv:int):
        self.name = "PURCHASED"
        self.description = "(item purchased)"
        self.rarity = rarity
        self.cost = cost
        self.costIncrement = increment
        self.level = 0
        self.maxLv = maxLv

    def trigger(self):
        pass

    def __str__(self):
        return (f"[{self.name}] lv.{self.level+1}/{self.maxLv}: {int(self.cost*(self.costIncrement**self.level))}$\n{self.description}")

class UpgTempl(Upgrade):
    def __init__(self, rarity, cost, increment, maxLv):
        super().__init__(rarity, cost, increment, maxLv)
        self.name = ""
        self.description = ""
    
    def rollstart(self):
        pass

    def rollend(self):
        pass

    def onbuy(self):
        pass

class IconPowerup(Upgrade):
    def __init__(self, rarity, cost, increment, maxLv):
        super().__init__(rarity, cost, increment, maxLv)
        self.name = "Icon Power+"
        self.description = (f"Increase the value of all icons by 1 per level (up to {self.maxLv})")
        self.upgradedIcon = []
        
    def rollstart(self):
        for icon in iconList:
            if not icon in self.upgradedIcon:
                icon.value += self.level
                self.upgradedIcon.append(icon)

    def onbuy(self):
        for icon in iconList:
            icon.value += 1
            if not icon in self.upgradedIcon:
                self.upgradedIcon.append(icon)

class RollIncrease(Upgrade):
    def __init__(self, rarity, cost, increment, maxLv):
        super().__init__(rarity, cost, increment, maxLv)
        self.name = "Extra Roll"
        self.description = "Slotmachine roll limit by 1"
    
    def onbuy(self):
        player.roll += 1

iconPower = IconPowerup("common", 10, 1.5, 5)
rollInc = RollIncrease("common", 5, 1.6, 10)
upgradeList = [iconPower, rollInc]

def upgradeShop(reroll:bool=False):
    global itemForSale
    if reroll:
        newSale = []
        for _ in range(3):
            newSale.append(random.choice(upgradeList))
        itemForSale = list(newSale)
    else:
        BUYING = True
        while BUYING:
            print(f"You have {player.money}$")
            i = 0
            for item in itemForSale:
                i+= 1
                print(f"{i}>{item}\n")
            print("[1] [2] [3] [X]")
            while True:
                selection = input("->").lower().strip()
                try:
                    selection = int(selection)
                except:
                    pass
                if type(selection) == type(int(1)):
                    if selection-1 < len(itemForSale) and itemForSale[selection-1].name != "PURCHASED":
                            sItem = itemForSale[selection-1]
                            sPrice = sItem.cost * (sItem.costIncrement**sItem.level)
                            if player.money >= sPrice:
                                itemForSale[selection-1] = Upgrade("common", 0,0,0)
                                print("Purchased", sItem.name, "\n")
                                player.money -= sItem.cost * (sItem.costIncrement**sItem.level)
                                if not sItem in player.upgrade:
                                    player.upgrade.append(sItem)
                                sItem.level += 1
                                try:
                                    sItem.onbuy()
                                except:
                                    pass
                                break
                            else:
                                print("Insufficient money")
                    else:
                        print("invalid item")
                elif selection in ACTION_quit or selection == "x":
                    BUYING = False
                    break
    return

upgradeShop(True)

def getIcon(icon):
    for obj in iconList:
        if icon == obj.icon:
            return obj

"""=====THE SLOTMACHINE OF THE HOLY SPAGHETTI====="""
def rollSlotmachine(icons, y:int, x:int):
    for r in range(player.roll):
        player.addictionLevel += 5
        if r > 0:
            c = input(f"roll again? (you have {player.roll-r} roll & {player.money}$ left)\n (y/n) >")
            if c in CHOICE_cancel:
                if random.randint(1, 10) == 1:
                    print("💎💎🟫🟫🟫🟫🟫🟫🟫🟫\n💎💎🟫🟫🟫⛏️🏃\n💎💎🟫🟫🟫🟫🟫🟫🟫🟫\n💎💎🟫🧍\n💎💎🟫🟫🟫🟫🟫🟫🟫🟫")
                    time.sleep(4)
                break
        
        for upg in player.upgrade:
            try:
                upg.rollstart()
            except:
                pass

        player.money -= 1
        slot = []
        wins = []
        # slot list format = [Y][X]
        # roll the slot, + horizontal check
        slotIcon = []
        for icon in icons:
            for _ in range(icon.count):
                slotIcon.append(icon.icon)

        for _ in range(y):
            row = []
            streakH = 0
            for j in range(x):
                row.append(random.choice(slotIcon))
                # horizontal
                if row[j] == row[j-1] and j-1 >= 0:
                    streakH += 1
                else:
                    if streakH+1 >=3:
                        wins.append([streakH+1, row[j-1], "-"])
                    streakH = 0
            if streakH+1 >=3:
                wins.append([streakH+1, row[j-1], "-"])
            slot.append(row)
            print(row)
            time.sleep(.5)
        
        # checks
        for i in range(y-2):
            for j in range(x):
                # vertical
                streakV = 0
                while True:
                    if i+streakV+2 <= y and slot[i+streakV][j] == slot[i+streakV+1][j]:
                        streakV+=1
                    else:
                        if streakV+1 >=3:
                            wins.append([streakV+1, slot[i][j], "|"])
                        break

        for upg in player.upgrade:
            try:
                upg.rollend()
            except:
                pass
        
        profit = player.money + 1
        for w in wins:
            iconObj = getIcon(w[1])
            reward = int((iconObj.value*w[0]) * (iconObj.multi**w[0]))
            print(f"{w[2]}{w[0]}{w[2]}{w[1]} {reward}$")
            
            player.money += reward
            time.sleep(.4)

        profitState = "won"
        if player.money < profit:
            profitState = "lost"
        print(f"{profitState} {player.money-profit}$")
    

tempIconlist = ["🍊","🍒","🍀"]
# rollSlotmachine(tempIconlist, 3, 5)

def setupGame(diff):
    # the diff does nothing right now, literally illusion of freewill
    global player
    player = Stat(20, 0)

    orange = Icon("🍊", 5, 1, 10)
    cherry = Icon("🍒", 6, 1, 10)
    melon = Icon("🍉", 7, 1, 10)
    bell = Icon("🔔", 8, 1, 10)
    clover = Icon("🍀", 9, 1.2, 9)
    diamond = Icon("💎", 10, 1.4, 8)
    seven = Icon("7️⃣ ", 7, 1.7, 7)

    global iconList
    iconList = [orange, cherry, melon, bell, clover, diamond, seven]

setupGame(input("Select game difficulty (1-5): "))

print("💎💎🟫🟫🟫🟫🟫🟫🟫🟫\n💎💎🟫🟫🟫⛏️🏃\n💎💎🟫🟫🟫🟫🟫🟫🟫🟫\n💎💎🟫🧍\n💎💎🟫🟫🟫🟫🟫🟫🟫🟫")
while not QUITGAME :
    if not player.progressDay():
        QUITGAME = True
        break
    upgradeShop(True)
    dayprint = player.day
    if player.day < 10:
        dayprint = " " + str(dayprint)
    print(f"\n\n====================\n       DAY{dayprint}       ", end="\n ")
    for i in range(-2, 3):
        dayprint = player.day
        if dayprint+i < 0 or dayprint+i > player.maxDay:
            dayprint = "  "
        elif dayprint+i < 10:
            dayprint = " " + str(dayprint+i)
        else:
            dayprint += i
        print(dayprint, end="  ")

    print(f"\n          ^         \n====================")
    print(str(random.choice(randomTip[0]))+"\n")
    adisplay = ""
    for _ in range(int(player.addictionLevel/5)):
        adisplay += "▮"
    for _ in range(int(20 - (player.addictionLevel/5))):
        adisplay += "▯"
    print(f"Money: {player.money}\nAddiction[{adisplay} ]\n")

    print(f"Select action\n[?upgrade]  [!slotmachine]  [skip] or [more]")
    end_day = False
    while not end_day:
        action = input(">").lower().strip()
        if action in ACTION_upgrade:
            upgradeShop()
        elif action in ACTION_slot:
            if input("Use the slotmachine?\n (y/n) >").lower().strip() in CHOICE_confirm:
                rollSlotmachine(iconList, 3, 5)
                end_day = True
        elif action in ACTION_more:
            print("...[stats]  [goal]  [quit]")
        elif action == "stats" or action == "stat" or action == "s":
            print(f"stats: ")
        elif action == "goal" or action == "g":
            print(f"Reach {player.goal[1]}$ by day {player.goal[0]}")
        elif action in ACTION_skip:
            end_day = True
            if player.money >= player.goal[1]:
                if input("Skip to the next goal?\n (y/n) >").lower().strip() in CHOICE_confirm:
                    player.addictionLevel -= 4*(player.goal[0]-player.day)
                    player.day = player.goal[0]
        elif action == "quit" or action == "exit":
            if input("Exit the game?\n (y/n) >").lower().strip() in CHOICE_confirm:
                print("EXITING GAME...")
                QUITGAME = True
                break
        else:
            pass

# final day, money, upgrade, goal
final_state = "GAME OVER"
if player.day > player.maxDay:
    final_state = "YOU WIN"
print(f"\n\n▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯\n   {final_state}\n")
if player.day <= player.maxDay:
    print("final day:", player.day)
print(f"day{player.goal[0]} - {player.goal[1]}$")
adisplay = ""
for _ in range(int(player.addictionLevel/5)):
    adisplay += "▮"
for _ in range(int(20 - (player.addictionLevel/5))):
    adisplay += "▯"
print(f"money: {player.money}$\naddiction [{adisplay} ]")
for upg in player.upgrade:
    print(f"[{upg.name}] Lv:{upg.level}/{upg.maxLv}", end=", ")
if len(player.upgrade) > 0:
    print("")

print("               Thank You For Gambling!\n")