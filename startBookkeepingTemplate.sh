#!/bin/sh
if [ $# == 1 ]; then
    touch $1.xls
    echo "1\n,借方,,貸方" >> $1.xls
    open $1.xls
else
    echo "Invalid Number of Argument"
fi
