from Data_Cleaner import DataCleaner

cleaner = DataCleaner()
cleaner.load_data("raw_ebay.csv")
cleaner.remove_duplicates()
cleaner.remove_all_null_rows()
cleaner.restrict_ram_range()


# Optional: validate and coerce types
expected_types = {
    'Brand': str,
    'Product_Description': str,
    'Screen_Size': float,
    'RAM': int,
    'Processor': str,
    'GPU': str,
    'GPU_Type': str,
    'Resolution': str,
    'Condition': str,
    'Price': float
}
cleaner.validate_and_clean_types(expected_types)
cleaner.drop_rows_with_missing(required_columns=['Brand', 'Product_Description', 'Screen_Size', 'RAM', 'Processor', 'Price'])

# Optional: outlier removal
cleaner.remove_outliers_iqr('Price')
cleaner.remove_outliers_iqr('Screen_Size')

cleaner.save_data("cleaned_dataset.csv")
