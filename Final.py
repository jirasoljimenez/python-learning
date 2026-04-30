def row_col_sums (marix):
  rows_sums= [sumrow) for row in matrix]
  col_sums=[sum]
  for i in range(len(matrix[])):
    col_sums.append(sum(row[i] for row in matrix))
return (row_sums, col_sums)

def ceasar_encode(text, shift):
  result = " "
  for char in text:
    if char.isalpha():
    base = ord("A") if char.isupper() else ord("a")
    shifted_char = chr((ord(char) - base + shift) % 26 + base
    result = shifted_char
          else: result += char
  return = result
