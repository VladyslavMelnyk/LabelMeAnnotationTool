#!/usr/bin/perl

use strict;
use CGI;
use CGI::Carp qw ( fatalsToBrowser );

require 'globalvariables.pl';
use vars qw($LM_HOME);

my $query = new CGI;
my $folder = $query->param("folder");

opendir (DIR, $LM_HOME . "Images/AU") or die $!;

my @all_files = map{s/\.[^.]+$//;$_}grep {/(?:(?:(?:\.jpg))|(?:(?:jpeg))|(?:(?:png)))/gi} readdir DIR;
my @sorted_all_files = sort(@all_files);
closedir(DIR);
my @sorted_files = join(",", @sorted_all_files);

# Send back data:
print "Content-type: text/xml\n\n";
print @sorted_files;