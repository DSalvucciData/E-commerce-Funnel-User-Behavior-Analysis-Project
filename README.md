# E-commerce Funnel & User Behavior Analysis Project

## Overview
This project demonstrates a **sequential funnel analysis** on a simulated e-commerce dataset using **Python**.  
It tracks how users progress through **page views → product views → add to cart → checkout → purchase**, identifies drop-off points, and explores differences by **user type, device, and country**.  
Designed as a **learning exercise in Pandas and data visualization**.

## Dataset
- **Rows:** 2,944 | **Unique users:** 500  
- **Events:** page_view, product_view, add_to_cart, checkout, purchase  
- **Segments:** Countries (Italy, Germany, France, Spain), Devices (Desktop, Mobile), User Types (New, Returning)  
- **Origin:** Generated using [`data_generation.py`](src/data_generation.py) located in `src/data_generation.py` and saved as CSV

## Objectives
- Track user progression through the funnel.  
- Identify key drop-off points.  
- Explore behavioral differences across segments.  
- Highlight areas for potential improvements in user experience and conversion.

## Notebooks
- **EDA and Cleaning:** [`EDA_and_cleaning.ipynb`](notebooks/eda_and_cleaning.ipynb) – initial exploration and data cleaning  
- **Analysis:** [`Analysis.ipynb`](notebooks/Analysis.ipynb) – sequential funnel analysis, visualizations, and insights

