def repeat_word_in_rooms(word, rooms):
    word_length = len(word)
    repeat_times = rooms // word_length
    remainder = rooms % word_length

    repeated_word = word * repeat_times + word[:remainder]

    return repeated_word

word1 = "alta"
rooms1 = 10
print("Test Case 1:")
print("Word:", word1)
print("Rooms:", rooms1)
print("Output:", repeat_word_in_rooms(word1, rooms1))

word2 = "sepulsa"
rooms2 = 20
print("\nTest Case 2:")
print("Word:", word2)
print("Rooms:", rooms2)
print("Output:", repeat_word_in_rooms(word2, rooms2))
