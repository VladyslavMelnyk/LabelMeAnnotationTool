#!/usr/bin/perl

use strict;
use CGI;
use CGI::Carp qw ( fatalsToBrowser );

require 'globalvariables.pl';
use vars qw($LM_HOME);

my $query = new CGI;
my $mode = $query->param("mode");
my $collection = $query->param("collection");
my $folder = $query->param("folder");

if($mode eq "c") {
    my $fname = $LM_HOME . "annotationCache/DirLists/$collection.txt";

    if(!open(FP,$fname)) {
	print "Status: 404\n\n";
	return;
    }

    open(NUMLINES,"wc -l $fname |");
    my $numlines = <NUMLINES>;
    ($numlines,my $bar) = split(" DirLists",$numlines);
    close(NUMLINES);

    my @all_images=(); # initialise empty array
    my @all_folders=(); # initialise empty
    for(my $i = 0; $i < int($numlines); $i++) {
        my $fileinfo = readline(FP);
        (my $temp_dir,my $temp_file) = split(",",$fileinfo);
        $temp_file =~ tr/"\n"//d; # remove trailing newline
        $all_images[$i]=$temp_file; #append images
        $all_folders[$i]=$temp_dir;
    }
    my @sorted_files = join(",", @all_images);
    # Send back data:
    print "Content-type: text/xml\n\n";
    print @sorted_files;
}
elsif($mode eq "f") {
    opendir (DIR, $LM_HOME . "Images/$folder") or die $!;

    my @all_files = map{s/\.[^.]+$//;$_}grep {/(?:(?:(?:\.jpg))|(?:(?:jpeg))|(?:(?:png)))/gi} readdir DIR;
    closedir(DIR);
    my @sorted_files = join(",", @all_files);
    # Send back data:
    print "Content-type: text/xml\n\n";
    print @sorted_files;
}
