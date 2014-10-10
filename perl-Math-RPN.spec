%define upstream_name 	 Math-RPN
%define upstream_version 1.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.11
Release:	2

Summary:	Perl extension for Reverse Polish Math Expression Evaluation
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Math/Math-RPN-1.11.tar.gz

BuildRequires:	perl-devel
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
%setup -q -n  %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Math/RPN.pm
%{_mandir}/man?/*


%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.90.0-1mdv2010.0
+ Revision: 403858
- rebuild using %%perl_convert_version

* Wed May 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.09-1mdv2010.0
+ Revision: 372509
- forgot to update the source tarball
- update to 1.09
- making the url parsable

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.08-7mdv2009.0
+ Revision: 241747
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-5mdv2008.0
+ Revision: 86635
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-4mdv2007.0
- Rebuild

* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.08-3mdk
- Fix According to perl Policy
	- BuildRequires
	- Source URL
	- URL
- use mkrel

* Sat Jun 11 2005 Abel Cheung <deaddog@mandrivalinux.org> 1.08-2mdk
- Rebuild

* Sat Apr 24 2004 Abel Cheung <deaddog@deaddog.org> 1.08-1mdk
- First Mandrake Release


