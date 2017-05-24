#!/usr/bin/env bash
cat ../../resources/Spruce_fingerprint_2017-03-10_16.48.olp.m4 | awk '$4>0.99 {print}' > ../../resources/Spruce_fingerprint_weak
