# Caesar Cipher

A Python program that encrypts and decrypts messages using the Caesar cipher, a classic technique that shifts each letter in the alphabet by a fixed number of positions.

## What it does

- Lets the user choose to encrypt or decrypt a message
- Shifts each letter by the amount you enter
- Wraps around the alphabet using modulo (`Z` shifted by 1 becomes `A`)
- Preserves uppercase and lowercase letters
- Leaves spaces, numbers, and punctuation unchanged
- Handles invalid options with an error message

## How to run

```bash
python caesar_cipher.py
```

Choose `1` to encrypt or `2` to decrypt, then enter your message and a shift amount.

## Example

Encrypting:

```
===== Ceaser Cipher =====
1. encrypt
2. decrypt

Choose an option: 1
Enter your message: Hello, World!
Enter shift amount: 3

Result: Khoor, Zruog!
```

Decrypting the same message with the same shift:

```
Choose an option: 2
Enter your message: Khoor, Zruog!
Enter shift amount: 3

Result: Hello, World!
```

## How it works

Each letter is converted to its position in the alphabet (A = 0, B = 1, ... Z = 25) using `ord()`. The shift is added for encryption or subtracted for decryption, then `% 26` wraps the result back into the alphabet, and `chr()` converts it to a letter again. A single function, `encrypt_decrypt()`, handles both modes through a `direction` value of `1` or `-1`.

## Status

This is a small learning project exploring functions, string handling, and character codes.

Planned improvements:
- Input validation (handle a non-numeric shift amount)
- Let the user keep going without restarting the program
- Add a brute-force option that tries all 25 shifts

## Note

The Caesar cipher is a historical cipher and is very easy to break. It is a learning exercise and should not be used to protect real information.

## Author

Built while learning Python fundamentals: functions, loops, and the `ord()` and `chr()` functions.
