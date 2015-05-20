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
my UserDB="/XML/users.xml";
my $source = XML::LibXML->load_xml(location => $UserDB);


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

# completare la parte del fail
if($fail) {
	CFUN::redir(/provains.cgi?$msg);
	}

#vado a gestire la parte XML
my $ptusers=$source->findnodes("/users/user");
my $father=$ptusers->get_node(1)->parentNode; #sono all'interno dell'albero, prendo il primo elemento user, e mi posiziono prima (alla radice)

#costruisco il template xml
if($type eq "") {
my struser="<user birth_date='$birthdate'>
		<username>$username</username>
		<password>$password</password>
		<e-mail>$mail</e-mail>
		<kind>
			<illustrator></illustrator>
			<writer></writer>
			<reader>1</reader>
		</kind>
	</user>";
}
elsif($type eq "1") {
my struser="<user birth_date='$birthdate'>
		<username>$username</username>
		<password>$password</password>
		<e-mail>$mail</e-mail>
		<kind>
			<illustrator>1</illustrator>
			<writer></writer>
			<reader>1</reader>
		</kind>
	</user>";
}
elsif($type eq "2"){
my struser="<user birth_date='$birthdate'>
		<username>$username</username>
		<password>$password</password>
		<e-mail>$mail</e-mail>
		<kind>
			<illustrator></illustrator>
			<writer>1</writer>
			<reader>1</reader>
		</kind>
	</user>";}
}
my $novopost=$xml->parse_balanced_chunk($struser,'UTF-8');
$father->appendchild($novopost);

open(OUT,">$userDB");
print OUT $source->toString;
close(OUT);

#ridirezionale l'utente


