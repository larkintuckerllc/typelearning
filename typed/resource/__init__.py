# from typing import Dict, Optional, Sequence
from typing import Dict, Sequence


class MetadataItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Resource:
    def __init__(self, id: bytes, items: Sequence[MetadataItem]):
        self.id = id
        self.metadata = {}
        for item in items:
            self.metadata[item.key] = item.value

    # def read_metadata(self, items: Sequence[str]) -> Optional[Dict[str, MetadataItem]]:  # noqa: E501
    def read_metadata(self, items: Sequence[str]) -> Dict[str, MetadataItem]:
        metadata = {}
        for item in items:
            if item in self.metadata:
                metadata[item] = self.metadata[item]
        # if metadata == {}:
        #    return None
        return metadata
