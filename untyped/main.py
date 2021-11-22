from untyped.resource import MetadataItem, Resource


def has_name(metadata):
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
    # metadata = resource.read_metadata(('funky',))
    print(has_name(metadata))
