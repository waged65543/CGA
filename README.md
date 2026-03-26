# 💎 Casino Gambling Adventure (CGA)

A Python-based slot machine gambling game with a 21-day progression system. Manage your addiction, buy upgrades, and try to reach your financial goals before time runs out!

---

## 🎮 Features

- **Slot Machine Gameplay**: Spin and match icons to win money (🍊, 🍒, 🍉, 🔔, 🍀, 💎, 7️⃣)
- **Upgrade Shop**: Purchase upgrades to increase icon values and roll limits
- **Addiction System**: Your addiction level increases with each spin and decreases as you progress
- **Dynamic Goals**: Goals increase in difficulty as you progress (higher money needed by specific days)
- **Day-Based Progression**: Survive 21 days while meeting financial milestones
- **Multiple Icon Rarity**: Different icons have different values and multiplier effects

---

## 📋 Requirements

- **Python 3.6+**
- No external dependencies (uses only standard library: `time` and `random`)

---

## 🚀 How to Run

### Windows
1. Open Command Prompt or PowerShell
2. Navigate to the game directory:
   ```
   cd CGA\New folder\OOP\
   ```
3. Run the game:
   ```
   python CGA.py
   ```

### macOS / Linux
1. Open Terminal
2. Navigate to the game directory:
   ```
   cd CGA/"New folder"/OOP/
   ```
3. Run the game:
   ```
   python3 CGA.py
   ```

---

## 🎯 How to Play

### Starting the Game
When you launch the game, you'll be prompted to select a difficulty (1-5). Choose your difficulty level to begin!

### Game Actions

**Press `?` (or `upgrade`, `u`, `upg`) to:**
- Open the upgrade shop
- Purchase upgrades to boost your stats

**Press `!` (or `slot`, `slotmachine`) to:**
- Spin the slot machine
- Match 3 or more icons in a row (horizontal or vertical) to win money
- Each spin costs $1

**Press `skip` (or `end`) to:**
- End your current day

**Press `more` (or `m`) to:**
- View additional options like stats and goals

**Press `q`, `quit`, or `exit` to:**
- Exit the game

---

## 💰 Game Mechanics

### Starting Resources
- **Money**: $20
- **Rolls**: 10 (spins per day)
- **Addiction Level**: 0

### Slot Machine Rules
- Each spin costs **$1**
- Match 3+ identical icons horizontally or vertically to win
- Icon rewards depend on:
  - **Icon Value** (base payout): 5-10 coins depending on rarity
  - **Match Count**: More matches = higher multiplier
  - **Icon Multiplier**: Some icons have built-in multipliers (up to 1.7x)
- Example: A 3-match diamond (💎) = `(10 * 3) * (1.4^3)` = $590

### Icon Reference
| Icon | Base Value | Multiplier | Frequency |
|------|-----------|-----------|-----------|
| 🍊 Orange | 5 | 1.0x | High (10x) |
| 🍒 Cherry | 6 | 1.0x | High (10x) |
| 🍉 Melon | 7 | 1.0x | High (10x) |
| 🔔 Bell | 8 | 1.0x | Medium (10x) |
| 🍀 Clover | 9 | 1.2x | Medium (9x) |
| 💎 Diamond | 10 | 1.4x | Low (8x) |
| 7️⃣ Seven | 7 | 1.7x | Rarest (7x) |

### Addiction System
- **Increases by 5** with each spin
- **Decreases by 4** for each day you skip (per day skipped)
- **Maximum**: 100
- **Minimum**: 0 (game over if negative)

### Daily Goals
Goals increase as you progress:
- **Day 1**: Reach $50
- Subsequent goals increase every 3-4 days (every 7 days: +4 days buffer, +50$)

---

## 🏆 Win/Lose Conditions

### 🎉 WIN
- Reach Day 21+ and maintain money above goal thresholds

### 💀 LOSE
- Run out of money before reaching a goal deadline
- Addiction level drops below 0
- Reach Day 21 without saving enough money

---

## 🛒 Upgrades

### Icon Power+
- **Cost**: $10 (increases by 1.5x per level)
- **Max Level**: 5
- **Effect**: Increases all icon base values by 1 per level

### Extra Roll
- **Cost**: $5 (increases by 1.6x per level)
- **Max Level**: 10
- **Effect**: Adds 1 additional spin roll per level

---

## 💡 Tips

- Don't spend all your money early; keep a buffer for upcoming goals
- Check upgrades daily for random shop refreshes
- Icon Power+ is more efficient early game
- The "skip" feature reduces addiction (useful for penalty management)
- 7️⃣ diamonds are rare but worth it for big wins!
- Some gamblers quit right before winning... don't be that person!

---

## 🐛 Troubleshooting

**Game won't run:**
- Ensure you have Python 3.6+ installed
- Check your file path contains no special characters
- Try running with `python` or `python3` depending on your setup

**Emojis not displaying:**
- This is a terminal/console encoding issue
- The game will still function normally
- Try running in a different terminal or updating your console

---

## 📝 Notes

- This is an educational project demonstrating OOP concepts in Python
- Game balance can be adjusted by modifying upgrade costs and icon values
- Each playthrough is randomized based on slot machine rolls and upgrade shop offerings

---

**Good luck! Remember, you can quit anytime you want... I swear.** 💎
