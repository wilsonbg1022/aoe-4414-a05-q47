# =============================================================================
# conv_ops.py
# Written by Brett Wilson
# Virginia Tech Honor Code: I have neither given nor received unauthorized assistance on this work.
# 
# This script calculates the output shape and the number of operations (additions, multiplications, and divisions)
# for a convolutional layer given certain parameters.
# 
# Usage:
#     python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p
# 
# Arguments:
#     c_in   : Input channel count
#     h_in   : Input height count
#     w_in   : Input width count
#     n_filt : Number of filters in the convolution layer
#     h_filt : Filter height count
#     w_filt : Filter width count
#     s      : Stride of convolution filters
#     p      : Amount of padding on each of the four input map sides
# =============================================================================

import sys

def main():
    # Retrieve arguments
    c_in = int(sys.argv[1])
    h_in = int(sys.argv[2])
    w_in = int(sys.argv[3])
    n_filt = int(sys.argv[4])
    h_filt = int(sys.argv[5])
    w_filt = int(sys.argv[6])
    s = int(sys.argv[7])
    p = int(sys.argv[8])

    # Calculate output dimensions
    h_out = ((h_in - h_filt + 2 * p) // s) + 1
    w_out = ((w_in - w_filt + 2 * p) // s) + 1
    c_out = n_filt  # Output channels equal the number of filters

    # Calculate operation counts
    filter_ops = h_filt * w_filt * c_in  # Ops per filter application
    adds = filter_ops * h_out * w_out * n_filt - 1  # Adds exclude bias add
    muls = filter_ops * h_out * w_out * n_filt  # Multiplications for all filters
    divs = 0  # Divisions are not typically used in convolutional layers

    # Output results
    print(int(c_out))  # Output channel count
    print(int(h_out))  # Output height count
    print(int(w_out))  # Output width count
    print(int(adds))   # Number of additions performed
    print(int(muls))   # Number of multiplications performed
    print(int(divs))   # Number of divisions performed

if __name__ == "__main__":
    main()
