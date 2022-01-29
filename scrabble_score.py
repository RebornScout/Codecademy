letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letter: point for letter, point in zip(letters, points)}
letter_to_points[" "] = 0

def score_word(word):
  """Take word and calculate the score"""
  point_total = 0
  for letter in word:
    try:
      point_total += letter_to_points[letter.upper()]
    except KeyError:
      point_total += 0
  return point_total

player_to_words = {"player1": ["blue", "tennis", "exit"], "wordNerd": ["earth", "eyes", "machine"], "Lexi Con": ["eraser", "belly", "husky"], "Prof Reader": ["zap", "coma", "period"]}
player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

print(player_to_points)

# play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played
# update_point_totals() — turn your nested loops into a function that you can call any time a word is played
