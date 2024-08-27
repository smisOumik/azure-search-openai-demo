import csv
from io import StringIO
from typing import IO, AsyncGenerator, Dict, List

from .parser import Parser
from .page import Page

class CSVParser (Parser):
    async def parse (self, content: IO) -> AsyncGenerator [Page, None]:
        # Read the entire content into a string
        content_str = content.read ()
        if isinstance (content_str, bytes):
            content_str = content_str.decode ('utf-8')
        
        reader = csv.DictReader (StringIO (content_str))
        
        important_fields = [
            "No", "受付日時", "顧客会社名", "システム名", "発生箇所", 
            "受付概要", "受付詳細", "対応詳細", "原因"
        ]

        offset = 0
        for row_num, row in enumerate (reader):
            processed_row: Dict [str, str] = {field: row.get (field, "") for field in important_fields}
        
            processed_row ["combined_description"] = f"{processed_row ['受付概要']}{processed_row ['受付詳細']}"

            # Convert the processed row to a string
            page_text = "\n".join (f"{k}:{v}" for k, v in processed_row.items())

            yield Page (page_num = row_num, offset = offset, text = page_text)
            offset += len (page_text)