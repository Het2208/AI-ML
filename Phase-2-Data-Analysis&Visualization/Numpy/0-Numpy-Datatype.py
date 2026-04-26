import numpy as np

### Integer
# int8	8-bit integer	-128 to 127
# int16	16-bit integer	-32,768 to 32,767
# int32	32-bit integer	-2,147,483,648 to 2,147,483,647
# int64	64-bit integer	-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807

# Default integer (platform dependent, usually int64)
arr = np.array([1, 2, 3, 4, 5])
print("Default Int:", arr.dtype)
print(arr.nbytes, "bytes")

# Explicit int8
arr_int8 = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print("\nint8:", arr_int8.dtype)
print(arr_int8.nbytes, "bytes")

# Explicit int16
arr_int16 = np.array([1, 2, 3, 4, 5], dtype=np.int16)
print("\nint16:", arr_int16.dtype)
print(arr_int16.nbytes, "bytes")

# Explicit int32
arr_int32 = np.array([1, 2, 3, 4, 5], dtype=np.int32)
print("\nint32:", arr_int32.dtype)
print(arr_int32.nbytes, "bytes")

# Explicit int64
arr_int64 = np.array([1, 2, 3, 4, 5], dtype=np.int64)
print("\nint64:", arr_int64.dtype)
print(arr_int64.nbytes, "bytes")


print("*" * 50)


### Unsigned Integer
# uint8	    Unsigned 8-bit integer	0 to 255
# uint16	Unsigned 16-bit integer	0 to 65,535
# uint32	Unsigned 32-bit integer	0 to 4,294,967,295
# uint64	Unsigned 64-bit integer	0 to 18,446,744,073,709,551,615

# uint8
arr_uint8 = np.array([1, 2, 3, 4, 5], dtype=np.uint8)
print("\nuint8:", arr_uint8.dtype)
print(arr_uint8.nbytes, "bytes")

# uint16
arr_uint16 = np.array([1, 2, 3, 4, 5], dtype=np.uint16)
print("\nuint16:", arr_uint16.dtype)
print(arr_uint16.nbytes, "bytes")

# uint32
arr_uint32 = np.array([1, 2, 3, 4, 5], dtype=np.uint32)
print("\nuint32:", arr_uint32.dtype)
print(arr_uint32.nbytes, "bytes")

# uint64
arr_uint64 = np.array([1, 2, 3, 4, 5], dtype=np.uint64)
print("\nuint64:", arr_uint64.dtype)
print(arr_uint64.nbytes, "bytes")

print("*" * 50)

### Floating-Point Types
# float16: Half precision float.
# float32: Single precision float.
# float64: 	Double-precision float (default)

# float16
arr_float16 = np.array([1.1, 2.2, 3.3], dtype=np.float16)
print("\nfloat16:", arr_float16.dtype)
print(arr_float16.nbytes, "bytes")

# float32
arr_float32 = np.array([1.1, 2.2, 3.3], dtype=np.float32)
print("\nfloat32:", arr_float32.dtype)
print(arr_float32.nbytes, "bytes")

# float64 (default)
arr_float64 = np.array([1.1, 2.2, 3.3])
print("\nfloat64:", arr_float64.dtype)
print(arr_float64.nbytes, "bytes")

print("*" * 50)

### Complex Number Types
# complex64: Complex number represented by two 32-bit floats.
# complex128 (or complex_): Complex number represented by two 64-bit floats, which is the default
# for Python's built-in complex type.

# complex64
arr_complex64 = np.array([1+2j, 3+4j], dtype=np.complex64)
print("\ncomplex64:", arr_complex64.dtype)
print(arr_complex64.nbytes, "bytes")

# complex128 (default)
arr_complex128 = np.array([1+2j, 3+4j])
print("\ncomplex128:", arr_complex128.dtype)
print(arr_complex128.nbytes, "bytes")

print("*" * 50)

### Other Types
# bool_: Boolean values (True or False) stored as a byte.
# str_ or unicode_: For handling string data.
# object_: For arbitrary Python objects, used when NumPy cannot determine a more specific type.

arr_bool = np.array([True, False, True], dtype=np.bool_)
print("\nbool_:", arr_bool.dtype)
print(arr_bool.nbytes, "bytes")

arr_str = np.array(["Het", "Preet", "Meet"], dtype=np.str_)
print("\nstr_:", arr_str.dtype)
print(arr_str.nbytes, "bytes")

arr_obj = np.array([1, "Hello", 3.14], dtype=np.object_)
print("\nobject_:", arr_obj.dtype)
print(arr_obj.nbytes, "bytes")
