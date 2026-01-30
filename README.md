# ASCII Art Image Generator (Python)

This project converts a real image into an ASCII art portrait using only
core Python concepts such as loops, conditions, file handling, and
mathematical image processing.

No external image libraries (like OpenCV or Pillow) are used.

---

## Features
- Reads 24-bit BMP image in binary
- Converts RGB pixels to grayscale
- Enhances image using contrast stretching
- Applies gamma correction for better brightness
- Resizes image mathematically
- Maps pixel intensity to ASCII characters
- Prints a high-quality ASCII portrait

---

## Technologies Used
- Python 3
- File handling (binary read)
- Loops and conditional statements
- Mathematical image processing
- Coordinate scaling

---

## How It Works
1. Read BMP header to get width, height, and pixel offset.
2. Extract RGB pixel values.
3. Convert RGB to grayscale.
4. Normalize contrast and apply gamma correction.
5. Resize image using scaling formula.
6. Map grayscale values to ASCII characters.
7. Print ASCII art to console.

---

## ASCII Density Scale

