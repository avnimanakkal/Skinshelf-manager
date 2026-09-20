# SkinShelf: Skincare Shelf Manager

## Problem Statement
People often buy many skincare products but forget when each one was opened, keep using products past their safe usage period, and mix products with clashing ingredients. There is no simple tool that keeps track of a personal skincare shelf and warns the user about these issues.

## Scope of the Project
**Included:**
- Adding, viewing, editing and deleting skincare products
- Tracking each product's open date and shelf life
- Flagging products as Fresh, Use Soon or Expired
- Detecting shared and clashing ingredients between products
- Showing total spending per product category
- Saving data to a file so it is available on the next run

**Not included:**
- Medical or dermatological advice (the clash rules are general guidelines only)
- Scanning products from photos
- Online shopping or product price comparison

## Target Users
- Students and young adults who use multiple skincare products
- Anyone who wants to avoid wasting money on expired products
- Beginners who are unsure which products can be used together

## High-Level Features
1. **Product Manager:** add, view, edit and delete products
2. **Expiry Tracker:** shows the status of every product based on open date and shelf life
3. **Ingredient Checker:** finds common and clashing ingredients using set operations
4. **Spending Report:** shows total spent per category
5. **Data Storage:** saves and loads products automatically
6. **Input Validation:** handles wrong inputs without crashing

## Technologies Used
- Python 3
- JSON file for storage
- Raptor / yEd for flowcharts
- Git and GitHub for version control
