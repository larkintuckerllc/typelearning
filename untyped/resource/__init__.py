class MetadataItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Resource:
    def __init__(self, id, items):
        self.id = id
        self.metadata = {}
        for item in items:
            self.metadata[item.key] = item

    def read_metadata(self, items):
        metadata = {}
        for item in items:
            if item in self.metadata:
                metadata[item] = self.metadata[item]
        # if metadata == {}:
        #    return None
        return metadata
