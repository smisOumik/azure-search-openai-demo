import csv
from io import StringIO
from typing import IO, AsyncGenerator, Dict, List

from .parser import Parser
from .page import Page

class CSVParser(Parser):
    async def parse(self, content: IO) -> AsyncGenerator[Page, None]:
        # Read the entire content as bytes
        content_bytes = content.read()
        
        # List of encodings to try
        encodings_to_try = ['utf-8', 'shift_jis', 'euc_jp', 'iso2022_jp']
        
        for encoding in encodings_to_try:
            try:
                content_str = content_bytes.decode(encoding)
                # Use tab as the delimiter and set quotechar to None to handle commas within fields
                reader = csv.DictReader(StringIO(content_str), delimiter='\t', quotechar=None)
                
                # Adjust important_fields based on your new CSV structure
                important_fields = reader.fieldnames if reader.fieldnames else []

                offset = 0
                for row_num, row in enumerate(reader):
                    processed_row: Dict[str, str] = {field: row.get(field, "").strip() for field in important_fields}
                
                    # Adjust this based on your new CSV structure
                    if "受付概要" in processed_row and "受付詳細" in processed_row:
                        processed_row["combined_description"] = f"{processed_row['受付概要']}{processed_row['受付詳細']}"

                    # Convert the processed row to a string
                    page_text = "\n".join(f"{k}:{v}" for k, v in processed_row.items())

                    yield Page(page_num=row_num, offset=offset, text=page_text)
                    offset += len(page_text)
                
                # If we successfully parsed the file, we can break the loop
                break
            except UnicodeDecodeError:
                # If this encoding didn't work, we'll try the next one
                continue
        else:
            # If we've tried all encodings and none worked, raise an error
            raise ValueError("Unable to decode the file with any of the attempted encodings")