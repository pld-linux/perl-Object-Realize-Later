#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Object
%define	pnam	Realize-Later
Summary:	Object::Realize::Later - Delayed creation of objects
Summary(pl):	Object::Realize::Later - op�nione tworzenie obiekt�w
Name:		perl-Object-Realize-Later
Version:	0.14
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	880f6cdae5e07183b121a6758d7bc159
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{!?_without_tests:1}0
BuildRequires:	perl(Scalar::Util)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Object::Realize::Later class helps with implementing transparent
on demand realization of object data.  This is related to the tricks
on autoloading of data, the lesser known cousin of autoloading of
functionality.

%description -l pl
Klasa Object::Realize::Later pomaga w implementowaniu przezroczystego
realizowania danych obiektowych na ��danie. Jest to zwi�zane z trikami
przy automatycznym wczytywaniu danych, czyli mniej znan� pochodn�
funkcjonalno�ci automatycznego wczytywania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%dir %{perl_vendorlib}/Object
%dir %{perl_vendorlib}/Object/Realize
%{perl_vendorlib}/Object/Realize/*.pm
%{_mandir}/man3/*
