# ROW MANIPULATION
import numpy as np
import argparse

parser = argparse.ArgumentParser(description= "Row Manipulation")
parser.add_argument('--N', type = int)
args = parser.parse_args()

identity_matrix = np.identity(args.N,dtype=float)
odd_matrix = identity_matrix[0::2]
even_matrix = identity_matrix[1::2]
permutation_matrix = np.concatenate((odd_matrix,even_matrix),axis=0)


def crop_array(arr_2d, offset_height, offset_width, target_height,target_width):
    
    return arr_2d[offset_height:offset_height + target_height +1,offset_width:offset_width + target_width +1]

offset_height = args.N //2 -1
offset_width = args.N //2 -1 
target_height = 1
target_width = 1
cropped_arr = crop_array(permutation_matrix, offset_height, offset_width, target_height, target_width)
padded_arr = np.pad(cropped_arr,pad_width=2,constant_values=0.5 )
replicated_arr = np.concatenate((padded_arr,padded_arr),axis=1)

print("Original array:",permutation_matrix,sep="\n")
print()
print("Cropped array:",cropped_arr,sep="\n")
print()
print("Padded array:",padded_arr,sep="\n")
print()
print("Concatenated array: shape=",replicated_arr.shape,sep="")
print(replicated_arr)




