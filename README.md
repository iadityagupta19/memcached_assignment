
# Key-Value Cache Cluster with Memcached
Initially I tried to do using Redis , but i was facing some issue which i was unable to resolve , so i did using Memcached

This project sets up a 3-node key-value cache cluster using Memcached  on your local machine and demonstrates basic CRUD (Create, Read, Update, Delete) operations.

## Prerequisites

- Python 3.x
- Memcached
- `pymemcache` library

## Setup

### Install Memcached

1. Install Memcached on your local machine if not already installed:

    ```sh
    sudo apt-get update
    sudo apt-get install memcached
    ```

2. Start multiple Memcached instances on different ports:

    ```sh
    memcached -p 11211 -d
    memcached -p 11212 -d
    memcached -p 11213 -d
    ```

### Install Python Dependencies

1. Create a virtual environment (optional but recommended):

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Install the `pymemcache` library:

    ```sh
    pip install pymemcache
    ```

## CRUD Application

### Code

The following Python script connects to the Memcached nodes and performs CRUD operations:

```python
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
```

### Running the Application

1. Ensure all three Memcached instances are running on ports `11211`, `11212`, and `11213`.

2. Execute the Python script:

    ```sh
    python solution.py
    ```


## Explanation

- **put(key, value):** Stores the key-value pair in the Memcached cluster.
- **get(key):** Retrieves the value associated with the key from the Memcached cluster.
- **delete(key):** Deletes the key-value pair from the Memcached cluster.

The example usage demonstrates adding a key-value pair, retrieving it, deleting it, and verifying the deletion.

## Conclusion

This setup allows you to experiment with a distributed key-value cache using Memcached. The provided script demonstrates basic CRUD operations that can be extended as needed for more complex applications.
