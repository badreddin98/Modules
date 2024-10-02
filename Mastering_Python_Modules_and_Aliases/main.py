import text_utils as tu
reversed_text = input("Enter text you want to reverse it! ")
capatilize_text = input("Enter text you want to make it capitalized! ")

reversed_text = tu.reverse_string(reversed_text)
print(f"Reversed String: {reversed_text}")

capitalized_text = tu.capitalize_string(capatilize_text)
print(f"capitalized String: {capitalized_text}")
