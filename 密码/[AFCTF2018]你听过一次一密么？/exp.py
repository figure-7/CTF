#!/usr/bin/python
## OTP - Recovering the private key from a set of messages that were encrypted w/ the same private key (Many time pad attack) - crypto100-many_time_secret @ alexctf 2017
# Original code by jwomers: https://github.com/Jwomers/many-time-pad-attack/blob/master/attack.py)

import string
import collections
import sets, sys

# 11 unknown ciphertexts (in hex format), all encrpyted with the same key

c1='25030206463d3d393131555f7f1d061d4052111a19544e2e5d'
c2='0f020606150f203f307f5c0a7f24070747130e16545000035d'
c3='1203075429152a7020365c167f390f1013170b1006481e1314'
c4='0f4610170e1e2235787f7853372c0f065752111b15454e0e09'
c5='081543000e1e6f3f3a3348533a270d064a02111a1b5f4e0a18'
c6='0909075412132e247436425332281a1c561f04071d520f0b11'
c7='4116111b101e2170203011113a69001b475206011552050219'
c8='041006064612297020375453342c17545a01451811411a470e'
c9='021311114a5b0335207f7c167f22001b44520c15544801125d'
c10='06140611460c26243c7f5c167f3d015446010053005907145d'
c11='0f05110d160f263f3a7f4210372c03111313090415481d49'
ciphers = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11]
# The target ciphertext we want to crack
#target_cipher = "0529242a631234122d2b36697f13272c207f2021283a6b0c7908"

# XORs two string
def strxor(a, b):     # xor two strings (trims the longer input)
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])

def target_fix(target_cipher):
    # To store the final key
    final_key = [None]*150
    # To store the positions we know are broken
    known_key_positions = set()

    # For each ciphertext
    for current_index, ciphertext in enumerate(ciphers):
        counter = collections.Counter()
        # for each other ciphertext
        for index, ciphertext2 in enumerate(ciphers):
            if current_index != index: # don't xor a ciphertext with itself
                for indexOfChar, char in enumerate(strxor(ciphertext.decode('hex'), ciphertext2.decode('hex'))): # Xor the two ciphertexts
                    # If a character in the xored result is a alphanumeric character, it means there was probably a space character in one of the plaintexts (we don't know which one)
                    if char in string.printable and char.isalpha(): counter[indexOfChar] += 1 # Increment the counter at this index
        knownSpaceIndexes = []

        # Loop through all positions where a space character was possible in the current_index cipher
        for ind, val in counter.items():
            # If a space was found at least 7 times at this index out of the 9 possible XORS, then the space character was likely from the current_index cipher!
            if val >= 7: knownSpaceIndexes.append(ind)
        #print knownSpaceIndexes # Shows all the positions where we now know the key!

        # Now Xor the current_index with spaces, and at the knownSpaceIndexes positions we get the key back!
        xor_with_spaces = strxor(ciphertext.decode('hex'),' '*150)
        for index in knownSpaceIndexes:
            # Store the key's value at the correct position
            final_key[index] = xor_with_spaces[index].encode('hex')
            # Record that we known the key at this position
            known_key_positions.add(index)

    # Construct a hex key from the currently known key, adding in '00' hex chars where we do not know (to make a complete hex string)
    final_key_hex = ''.join([val if val is not None else '00' for val in final_key])
    # Xor the currently known key with the target cipher
    output = strxor(target_cipher.decode('hex'),final_key_hex.decode('hex'))

    print "Fix this sentence:"
    print ''.join([char if index in known_key_positions else '*' for index, char in enumerate(output)])+"\n"

    # WAIT.. MANUAL STEP HERE 
    # This output are printing a * if that character is not known yet
    # fix the missing characters like this: "Let*M**k*ow if *o{*a" = "cure, Let Me know if you a"
    # if is too hard, change the target_cipher to another one and try again
    # and we have our key to fix the entire text!

    #sys.exit(0) #comment and continue if u got a good key

    target_plaintext = "cure, Let Me know if you a"
    print "Fixed:"
    print target_plaintext+"\n"

    key = strxor(target_cipher.decode('hex'),target_plaintext)

    print "Decrypted msg:"
    for cipher in ciphers:
        print strxor(cipher.decode('hex'),key)

    print "\nPrivate key recovered: "+key+"\n"
    
for i in ciphers:
    target_fix(i)
