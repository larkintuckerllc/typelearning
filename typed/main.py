# from typing import Dict, Optional
from typing import Dict
from typed.resource import MetadataItem, Resource


# def has_name(metadata: Optional[Dict[str, MetadataItem]]) -> bool:
def has_name(metadata: Dict[str, MetadataItem]) -> bool:
    # if metadata is None:
    #     return False
    return 'name' in metadata


def run():
    resource = Resource(
        b'000',
        (
            MetadataItem('name', 'myname'),
        )
    )
    metadata = resource.read_metadata(('name',))
    # metadata = resource.read_metadata(('named',))
    print(has_name(metadata))
