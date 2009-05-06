%define module 	Math-RPN
%define version 1.09
%define release %mkrel 1

Summary:	Perl extension for Reverse Polish Math Expression Evaluation
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License:	GPL or Artistic
URL:		http://search.cpan.org/dist/%{module}
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Math/%{module}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch

%description
Reverse Polish Notation is briefly a stack-based way of writing
mathematical expressions. This has the advantage of eliminating
the need for parenthesis and simplifying parsing for computers vs.
normal algebraic notation at a slight cost in the ability of humans
to easily comprehend the expressions.

Math::RPN will take a scalar or list of sclars which contain an RPN
expression as a set of comma delimited values and operators, and
return the result or stack, depending on context. If the function
is called in an array context, it will return the entire remaining stack.

%prep
%setup -q -n  %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Math/RPN.pm
%{_mandir}/man?/*

