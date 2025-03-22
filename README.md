# Caesar_Cipher
This is an Encryption - Decryption techinique.

This repository contains a simple implementation of a **Caesar Cipher**, a type of substitution cipher where each letter in the text is shifted by a fixed number of positions (shift key) in the alphabet. The program provides both encryption and decryption functionalities using this cipher.

#### Features
- **Encryption**: Converts plain text into a ciphered text by shifting letters forward in the alphabet.
- **Decryption**: Reverses the process, converting ciphered text back into plain text by shifting letters backward.
- Handles spaces in the input text gracefully by preserving them in the output.

#### Code Workflow
1. The program defines an alphabet array (`alpha`) to map letters to indices.
2. Users can choose between encryption (`e`) and decryption (`d`).
3. For both operations:
   - Input text is taken from the user.
   - A shift key (an integer) is provided by the user.
   - Each letter of the text is shifted according to the key. Spaces are preserved as they are.
4. The process loops until the user decides to exit.

#### Example Usage
1. Choose the desired operation:
   - Enter `e` for encryption.
   - Enter `d` for decryption.
2. Input your text and shift key.
3. The result (encrypted or decrypted text) is displayed.
4. Optionally, rerun the program or exit.

This program is a great way to learn about basic cryptographic concepts and explore Python's string manipulation capabilities! Feel free to enhance it or adapt it for your own projects. 😊
