# from typing import Dict, Optional, Sequence
from typing import Dict, Sequence


class MetadataItem:
    key: str
    value: str

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value


class Resource:
    metadata: Dict[str, MetadataItem]

    def __init__(self, id: bytes, items: Sequence[MetadataItem]):
        self.id = id
        self.metadata = {}
        for item in items:
            self.metadata[item.key] = item

    # def read_metadata(self, items: Sequence[str]) -> Optional[Dict[str, MetadataItem]]:  # noqa: E501
    def read_metadata(self, items: Sequence[str]) -> Dict[str, MetadataItem]:
        metadata: Dict[str, MetadataItem] = {}
        for item in items:
            if item in self.metadata:
                metadata[item] = self.metadata[item]
        # if metadata == {}:
        #    return None
        return metadata
