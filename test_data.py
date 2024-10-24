from data import data_stream

ds = data_stream()

# Test by printing the first 100 values from the stream

for _ in range(100):
    value = next(ds)
    print(f"Value {_}: {value}")
