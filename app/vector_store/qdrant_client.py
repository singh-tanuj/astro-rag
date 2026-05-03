from qdrant_client import QdrantClient


def get_qdrant_client():
    return QdrantClient(path="data/qdrant_storage")


if __name__ == "__main__":
    client = get_qdrant_client()
    print(client.get_collections())
    client.close()