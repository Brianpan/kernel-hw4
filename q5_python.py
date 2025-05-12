import math

# Generate 128 sample values for a sine wave
lut = []
for i in range(128):
    angle = (i / 128.0) * (2 * math.pi)
    lut.append(round(math.sin(angle) * 127))

# Append an extra value (0) to make interpolation easier, as in the C version.
lut.append(0)

# Print the lookup table values as a comma-separated string (without [ and ])
print(', '.join(map(str, lut)))
