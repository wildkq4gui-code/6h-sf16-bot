# Arena Mode Guide

## Overview

Your bot now supports **automatic arena participation**! When your bot joins a Lichess arena (tournament), it will automatically:

1. ✅ Detect that it's playing in an arena
2. 🛑 **STOP accepting challenges** from others
3. 🛑 **STOP sending challenges** to others  
4. 🏆 **FOCUS entirely on the arena**
5. ✅ Resume normal challenge operations when the arena ends

## How It Works

### Automatic Detection

The bot monitors incoming games and automatically detects if a game is part of an arena/tournament by checking the game metadata. When an arena game is detected:

```
🏆 ARENA DETECTED (Tournament ID: xxxxx)
🛑 Arena mode enabled - no challenges will be accepted or sent
```

### Challenge Management During Arena

During an arena:
- The bot **WILL NOT** accept incoming challenges
- The bot **WILL NOT** send new challenges  
- The bot **WILL** focus on playing arena games
- All incoming challenges are automatically declined

### After Arena Ends

Once the arena game finishes:
```
✅ Arena game ended - arena mode disabled, resuming normal operations
```

The bot returns to normal operations and can:
- Accept manual challenges
- Send challenges to other bots
- Auto-challenge random bots (if configured)

## Implementation Details

### What Changed

1. **New field added to track arenas:**
   - `self.current_arena_id` - Stores the tournament ID when in an arena

2. **New method to detect arenas:**
   - `is_arena_game(game_event)` - Returns tuple `(is_arena, tournament_id)`

3. **Modified game handler:**
   - Detects arena status when game starts
   - Sets `arena_mode = True` automatically
   - Resets `arena_mode = False` when arena ends

4. **Existing challenge controls now work:**
   - `challenge_user()` - Checks `arena_mode` and refuses challenges
   - `challenge_random_bot()` - Checks `arena_mode` and refuses challenges
   - `accept_challenge()` - Checks `arena_mode` and declines incoming challenges

## Configuration

### No Configuration Needed

The arena detection is **completely automatic**. Once deployed, your bot will:
- Join arenas when invited
- Automatically disable challenges
- Play optimally during the arena
- Resume normal operations afterward

### Optional Manual Control

If needed, you can manually control arena mode:

```python
# Manually disable arena mode (if stuck for some reason)
bot.arena_mode = False
bot.current_arena_id = None

# Get current arena status
if bot.arena_mode:
    print(f"Currently in arena: {bot.current_arena_id}")
```

## Supported Arena Types

The bot works with any Lichess arena that accepts bot accounts, including:
- ♟️ Standard chess arenas
- ♞ Chess960 arenas
- 🃏 Variant arenas (if Fairy Stockfish is enabled)
- Rated and casual arenas
- Any time control

## Bot Account Requirement

Your bot account must:
- ✅ Be upgraded to a **BOT account** on Lichess
- ✅ Have the **bot:play** API scope
- ✅ Be **eligible to play in arenas** (no restrictions)

**Important:** Some arenas on Lichess may have restrictions. Check the arena settings to ensure bots are allowed.

## Troubleshooting

### Arena mode not disabling after game?
- This should NOT happen, but if it does, the bot will auto-disable on the next check
- You can also manually disable it via the configuration

### Bot rejecting arena invites?
- Ensure your bot account is allowed to play in that specific arena
- Check if the variant is supported (may need Fairy Stockfish for variants)
- Verify the time control isn't blocked by your settings

### Want to disable arena support?
- Set `bot.arena_mode = True` manually to act like you're always in an arena
- Or remove the arena detection logic from `handle_game()`

## Best Practices

1. **Let the bot join arenas naturally** - Don't manually manage arena mode
2. **Keep challenge settings enabled** - The bot will auto-manage during arenas
3. **Use appropriate time controls** - Configure manual time limits for your preferred arena speed
4. **Monitor bot logs** - Look for `🏆 ARENA DETECTED` messages to verify operation

## Example Output

When your bot plays in an arena, you'll see:

```
============================================================
Starting game: 12ab34cd5678
============================================================
🏆 ARENA DETECTED (Tournament ID: t4a2b3c4d5e6f7g8h)
🛑 Arena mode enabled - no challenges will be accepted or sent
Game started: YourBot vs OpponentBot
Variant: standard
Time control: 3s + 0s
[... game play ...]
Game finished: checkmate

✅ Arena game ended - arena mode disabled, resuming normal operations
```

## Technical Details

### Event Detection

The bot checks the `gameFull` event for the presence of a `tournament` field:

```python
tournament_id = game_event.get('tournament')
if tournament_id:
    # Arena detected!
    arena_mode = True
```

### State Management

- **Arena Start:** `arena_mode` is set to `True` when arena game starts
- **Arena Active:** All challenge functions respect `arena_mode` flag
- **Arena End:** `arena_mode` is set to `False` when game ends

### Supported Features During Arena

✅ All engine features (Stockfish, Fairy Stockfish, variants)  
✅ Opening books  
✅ Middlegame books  
✅ Endgame books  
✅ Time management optimization  
✅ Chat messages  
✅ Manual speed settings  

## Questions or Issues?

If you encounter any issues:
1. Check bot logs for `ARENA DETECTED` messages
2. Verify your bot account is allowed in the specific arena
3. Ensure your API token has bot:play scope
4. Check that the variant is supported (if not standard)

---

**Happy arena play!** 🏆
