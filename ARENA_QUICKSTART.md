# Quick Start: Arena Mode

## TL;DR

Your bot now **automatically plays in arenas**. When it detects an arena game, it will:
- 🛑 Stop accepting challenges
- 🛑 Stop sending challenges  
- 🏆 Focus entirely on the arena
- ✅ Resume normal operations when done

**No setup needed!** It's automatic.

## Getting Started in 3 Steps

### 1. Deploy Your Bot

Same as before:

```bash
export LICHESS_TOKEN="your_token_here"
python3 LichessStockfishand-fairy-fish-1/run_scheduled.py
```

### 2. Join an Arena

Go to https://lichess.org/api/arena to find bot-allowed arenas, or create your own test arena.

### 3. Watch the Magic

Your bot will automatically:
- Join the arena when invited
- Detect it's an arena game
- Print: `🏆 ARENA DETECTED (Tournament ID: xxxxx)`
- Play the arena with all its power
- When done, print: `✅ Arena game ended - arena mode disabled`
- Resume normal challenge operations

## What You'll See in Logs

```
============================================================
Starting game: 12ab34cd5678
============================================================
🏆 ARENA DETECTED (Tournament ID: t4a2b3c4d5e6f7g8h)
🛑 Arena mode enabled - no challenges will be accepted or sent
Game started: YourBot vs OpponentBot
Variant: standard
Time control: 3s + 0s
Thinking (limit: 2.50s, depth: 45)... Move: e2e4 (score: +50)
[... game play ...]
  
Game finished: checkmate

✅ Arena game ended - arena mode disabled, resuming normal operations
```

## Configuration

### No Configuration Required!

Arena mode is **fully automatic**. The bot will:
- Detect arenas from the game data
- Enable arena mode automatically
- Disable arena mode when arena ends

### Manual Override (If Needed)

```python
# Disable arena mode manually (shouldn't be needed)
bot.arena_mode = False

# Check if currently in arena
print(bot.current_arena_id)  # Returns tournament ID or None
```

## Supported Arenas

The bot works with any Lichess arena that allows bots:
- ♟️ Standard chess
- ♞ Chess960  
- 🃏 All variants (if using Fairy Stockfish)
- All time controls
- Rated and casual

## Features During Arena

✅ Full Stockfish power  
✅ Opening books  
✅ Middlegame books  
✅ Endgame books  
✅ Optimal time management  
✅ All variants supported (with Fairy Stockfish)  

## Common Questions

### Q: Does it work with my existing bot?
**A:** Yes! Just update the code and redeploy. No other changes needed.

### Q: What if I don't want arena mode?
**A:** Delete the arena detection code from `handle_game()`. But you probably want this feature!

### Q: Does it affect challenge performance?
**A:** No! It only disables challenges during arenas (which is what you want anyway).

### Q: Can I turn off arena mode?
**A:** Set `bot.arena_mode = False` temporarily, but it will re-enable on next arena game.

### Q: What about wind-down mode?
**A:** Arena mode takes precedence. The bot will play the current arena game even during wind-down.

## Troubleshooting

**Problem:** Arena mode not activating
- **Solution:** Verify the arena is bot-allowed (check Lichess arena settings)

**Problem:** Bot stuck in arena mode after game
- **Solution:** Shouldn't happen. If it does, check logs for errors and restart bot.

**Problem:** Declined arena invites  
- **Solution:** Check if your bot account is allowed in that specific arena

**Problem:** Variant support error
- **Solution:** Use Fairy Stockfish for variant arenas: `bot.use_fairy_stockfish = True`

## Testing Arena Mode

### Local Test

1. Run your bot:
   ```bash
   export LICHESS_TOKEN="your_token"
   python3 LichessStockfishand-fairy-fish-1/run_scheduled.py
   ```

2. Create a test arena on Lichess (or join an existing one)

3. Manually challenge your bot to a game from within the arena

4. Watch for: `🏆 ARENA DETECTED` in the logs

### GitHub Actions Test

Push to main and wait for the scheduled run, or trigger manually:
1. Go to GitHub Actions tab
2. Click "Lichess Bot Scheduled Run"
3. Click "Run workflow"
4. Check logs for arena messages

## Next Steps

1. ✅ Test in a small arena first
2. ✅ Monitor bot logs (look for 🏆 messages)
3. ✅ Enjoy focused arena play
4. 📚 Read [ARENA_MODE_GUIDE.md](ARENA_MODE_GUIDE.md) for advanced details

---

**Happy arena play!** 🏆
