# SkinShelf: Skincare Shelf Manager

## Overview
SkinShelf is a Python command-line program that helps users manage their personal skincare shelf. It tracks when each product was opened, warns about products that are expiring or expired, detects clashing or overlapping key active ingredients between products, and shows a spending summary by category.

## Problem it Solves
People buy many skincare products but often forget when a product was opened, keep using products past their safe usage period, and unknowingly mix products with clashing active ingredients. SkinShelf keeps this information organized in one place.

## Features
- **Add, view, edit and delete products** with name, category, price, shelf life and open date
- **Expiry tracking:** every product is marked as Fresh, Use Soon or Expired based on its open date and shelf life
- **Ingredient checker:** uses set operations to detect shared active ingredients and known clashing combinations (e.g. retinol with vitamin C) between products
- **Spending report:** shows total spending per category and the category with the highest spend
- **Data persistence:** the shelf is saved to `data.json` and automatically reloaded the next time the program runs
- **Input validation:** invalid or empty inputs are rejected with a clear message instead of crashing the program

## Technologies Used
- Python 3
- `datetime` module for expiry calculations
- `json` module for data storage
- Git and GitHub for version control
- Raptor / yEd for flowcharts and diagrams

## Project Structure

## How to Install and Run
1. Install Python 3 from [python.org](https://www.python.org/downloads/) if not already installed.
2. Download or clone this repository.
3. Make sure all `.py` files are in the same folder.
4. Open `main.py` in IDLE (or any Python editor).
5. Run the file. A menu will appear in the console.

## How to Use
Choose an option from the menu by typing its number and pressing Enter:

## Testing Instructions
- **Add a product** with a real open date and check it appears under "View shelf"
- **Add two products** with clashing actives (e.g. retinol and vitamin C) and confirm "Ingredient check" flags them
- **Enter invalid input** (e.g. letters for price) and confirm the program asks again instead of crashing
- **Save and exit, then reopen** the program and confirm the shelf still shows the saved products

## Limitations and Future Enhancements
- Shelf life is calculated using 30 days per month, which is an approximation
- Ingredient clash rules are general guidelines only and not medical or dermatological advice
- Future versions could add barcode/photo scanning, a graphical interface, and reminders/notifications
