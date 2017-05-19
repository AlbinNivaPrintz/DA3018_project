cat Spruce_fingerprint_2017-03-10_16.48.olp.m4 | awk '{if ($4<0.99) print $4}' | wc -l
