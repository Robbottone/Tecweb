#!/usr/bin/perl -w

use strict;
use warnings;
use utf8;
use XML::LibXSLT;
use XML::LibXML;
use CGI qw/:standard/;
use CGI::Session;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use Time::localtime;
use Email::Valid;

my $cgi=CGI->new();
my $xml = XML::LibXML->new();
my $xslt = XML::LibXSLT->new();
my $msg = "&&";
my $fail = 0;

my $username;
my $password;
my $birthday;
my $mail;
my $type;

#controllo sul campo username
if((!define $cgi->param('username')) && $cgi->param('username') eq "" ) 
	{
	$fail=1;
	$msg=$msg."msg1=username%20vuoto&&"; #alleggo tutti gli errori in un unica stringa di errore
	}
else
  {$username=$cgi->param('username');}
  
#controllo sul campo password
if((!define $cgi->param('password')) && $cgi->param('password') eq "" )
  {
  $fail=1;
  $msg=$msg."msg2=password%20vuoto&&";
  }
else {$password=$cgi->param('param');}

#controllo sul campo data nascita
if((!define $cgi->param('birthdate')) && $cgi->param('birthdate') eq "" )
  {
  $fail=1;
  $msg=$msg."msg3=campo%20data%20nascita%20vuoto&&";
  }
else {$birthdate=$cgi->param('birthdate');}

#controllo sul campo email
if((!define $cgi->param('mail')) && $cgi->param('mail') eq "" )
  {
  $fail=1;
  $msg=$msg."msg3=campo%20mail%20vuoto&&";
  }
else {$birthdate=$cgi->param('mail');}

#controllo sul campo email
if((!define $cgi->param('mail')) && $cgi->param('mail') eq "" )
  {
  $fail=1;
  $msg=$msg."msg3=campo%20mail%20vuoto&&";
  }
else {$birthdate=$cgi->param('mail');}

$type=$cgi->param('type');
