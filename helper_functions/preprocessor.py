from typing import List, Optional, Union, Dict, Literal
from haystack.schema import Document
from haystack.nodes import PreProcessor
from .cleanup_blog_metadata import find_authors, find_publish_date, find_title, find_start, find_end

class CustomPreProcessor(PreProcessor):
    def process(
        self,
        documents: Union[dict, Document, List[Union[dict, Document]]],
        clean_whitespace: Optional[bool] = None,
        clean_header_footer: Optional[bool] = None,
        clean_empty_lines: Optional[bool] = None,
        remove_substrings: Optional[List[str]] = None,
        split_by: Optional[Literal["word", "sentence", "passage"]] = None,
        split_length: Optional[int] = None,
        split_overlap: Optional[int] = None,
        split_respect_sentence_boundary: Optional[bool] = None,
        id_hash_keys: Optional[List[str]] = None,
    ) -> List[Document]:
        if isinstance(documents, (Document, dict)):
            documents = self._cleanup_document(documents)
        elif isinstance(documents, list):
            documents = self._cleanup_documents(documents)
        else:
            raise Exception("documents provided to PreProcessor.prepreprocess() is not of type list nor Document")
        return super().process(
            documents=documents,
            clean_whitespace=clean_whitespace,
            clean_header_footer=clean_header_footer,
            clean_empty_lines=clean_empty_lines,
            remove_substrings=remove_substrings,
            split_by=split_by,
            split_length=split_length,
            split_overlap=split_overlap,
            split_respect_sentence_boundary=split_respect_sentence_boundary,
            id_hash_keys=id_hash_keys,
        )
        
    def _cleanup_document(self, document: Document) -> Document:
        prelim_start_article = document.content.index("Lesezeit")
        prelim_end_article = document.content.index("Hat dir der Beitrag gefallen?")
        prelim_article = document.content[:prelim_end_article]
        authors = find_authors(prelim_article)
        date = find_publish_date(prelim_article)
        title = find_title(prelim_article)
        start_article = find_start(prelim_article, title)
        end_article = find_end(prelim_article)
        article = prelim_article[start_article : end_article].strip()
        document.content = article
        document.meta["authors"] = authors
        document.meta["date"] = date
        document.meta["title"] = title
        return document
        
    def _cleanup_documents(self, documents: list[Document]) -> list[Document]:
        new_docs = []
        for d in documents:
            if '/blog/' in d.meta["url"] and '/blog/author/' not in d.meta["url"] and d.meta["url"] not in ["https://www.inovex.de/de/blog/", "https://www.inovex.de/de/blog/inovex-design/"]:
                print(f"Clean {d.meta['url']}")
                new_d = self._cleanup_document(d)
                new_docs.append(new_d)
            else:
                print(f"Ignore {d.meta['url']}")
        return new_docs
