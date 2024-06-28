import memcache

# Connect to Memcached nodes
servers = ['127.0.0.1:11211', '127.0.0.1:11212', '127.0.0.1:11213']
client = memcache.Client(servers)

# CRUD Operations
def put(key, value):
    client.set(key, value)

def get(key):
    return client.get(key)

def delete(key):
    client.delete(key)

# Example usage
if __name__ == '__main__':
    key = 'doctor'
    value = 'Aditya'

    # Put operation
    put(key, value)
    print(f"Put {key}: {get(key)}")

    # Get operation
    retrieved_value = get(key)
    if retrieved_value:
        print(f"Get {key}: {retrieved_value}")
    else:
        print(f"{key} not found")

    # Delete operation
    delete(key)
    print(f"Deleted {key}")

    # Verify deletion
    print(f"Deleted {key}: {get(key)}")
