#!/usr/bin/perl

use strict;
use CGI;
use CGI::Carp qw(fatalsToBrowser);

require 'globalvariables.pl';
use vars qw($LM_HOME);

my $query = new CGI;
my $folder = $query->param("folder");
my $image = $query->param("image");

my $im_dir;
my $im_file;

opendir(DIR, $LM_HOME . "Images/$folder") || die("Cannot read folder $LM_HOME/Images/$folder");
my @all_images = readdir(DIR);
closedir(DIR);

my $i = 0;
# Get location of image in array:
for (my $j = 0; $j < scalar(@all_images); $j++) {
    if ($all_images[$j] =~ m/$image/) {
        $i = $j;
        last;
    }
}

$im_dir = $folder;
$im_file = $all_images[$i];


# Send back data:
print "Content-type: text/xml\n\n";
print "<out><dir>$im_dir</dir><file>$im_file</file></out>";
