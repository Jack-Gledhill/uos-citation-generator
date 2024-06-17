from sources import *
from typing import Type


sources: dict[str, Type[Source]] = {
    "book": Book,
    "chapter": Chapter,
    "journal article": JournalArticle,
    "unpublished article": PreprintArticle,
    "online article": WebArticle,
    "webpage": Webpage,
    "conference paper": PublishedConferencePaper,
    "unpublished conference paper": UnpublishedConferencePaper
}

source = input("Source type: ").lower()
handler = sources[source]()
handler.ask()
print(handler.ieee)
