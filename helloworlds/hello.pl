#!/usr/bin/perl
use strict;
use warnings;
use List::Util qw( min max );



# Perl feels like brainfuck
# Syntax is hard
# Debug messages are worse
# Why does this language exists ! 


my $file = 'solutions/1/1/full.txt';

open my $info, $file or die "Could not open $file: $!";

print("File $file opened successfully!\n");

my $counter = 0;
my @numbers = (); 

while( my $line = <$info>)  {   
    #print("$line \n");
    $a = length($line);
    if ($a == 1) {
        
        push(@numbers, $counter);
        $counter = 0;
    }
    else {
        $counter += int($line);
    }

}

print "numbers are : @numbers\n";
my $max = max @numbers;
print("max is $max");

close(FH);
