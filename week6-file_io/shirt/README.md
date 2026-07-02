# 👕 CS50P – Shirt

Overlay a transparent shirt image onto any input photo using Python and Pillow.

This project is my solution to the **Shirt** problem from Harvard's **CS50's Introduction to Programming with Python**.

## Features

* Validates command-line arguments
* Accepts only `.jpg`, `.jpeg`, and `.png` files
* Ensures input and output files have matching extensions
* Detects missing input files
* Automatically resizes and crops the input image to match the shirt template
* Preserves transparency using the PNG alpha channel as a mask
* Saves the processed image to the specified output file

## Technologies

* Python 3
* Pillow (PIL)

## Usage

```bash
python shirt.py input.jpg output.jpg
```

or

```bash
python shirt.py input.png output.png
```

## Example

## Example

| Before | After |
|---------|--------|
| ![](https://github.com/rominva/Harvard-CS50P-Portfolio/blob/main/week6-file_io/shirt/before1.jpg) | ![](https://github.com/rominva/Harvard-CS50P-Portfolio/blob/main/week6-file_io/shirt/after1.jpg) |

## What I Learned

While building this project, I practiced:

* Working with third-party Python libraries
* Reading and understanding library documentation
* Image processing with Pillow
* Resizing and cropping images using `ImageOps.fit()`
* Overlaying transparent PNG images using alpha masks
* File validation and command-line argument handling
* Exception handling with `try` / `except`

## Project Structure

```
shirt.py
shirt.png
before1.jpg
after1.jpg
README.md
```

---

This project was completed as part of Harvard's **CS50P** course.
